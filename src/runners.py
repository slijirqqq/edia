import abc
import logging

from psychopy import core
from psychopy.visual import Window

from src.components import (AnswerQuestionComponent, ChoiceQuestionComponent,
                            ImageComponent, InstructionComponent,
                            LeftImageComponent, MainWindow,
                            RightImageComponent, TextQuestionComponent,
                            XImageComponent)
from src.constants import RIGHT, QuestionType
from src.handlers import ExperimentHandler, FirstStageTrial, ThirdStageTrial
from src.keyboards import (DefaultKeyboard, ImageChoiceKeyboard,
                           InstructionStepKeyboard, QuestionKeyboard)
from src.models import Answer, ExperimentData, Question, Stimulus
from src.utils.mixins import RunnerInstructionMixin
from src.utils.uploads import upload_questions

logger = logging.getLogger(__name__)


class DefaultRunner(abc.ABC):

    def __init__(self, timer: core.CountdownTimer, clock: core.Clock):
        self._experiment: ExperimentHandler = ExperimentHandler.get_handler()
        self._window: Window = MainWindow()
        self._timer: core.CountdownTimer = timer
        self._global_clock: core.Clock = clock
        self._clock = core.Clock()
        self._keyboard = InstructionStepKeyboard()
        self._default_keyboard = DefaultKeyboard()
        self._timer.reset()
        self._continue = True

    def run(self):
        self._reset_time()
        self.run_steps()

    @abc.abstractmethod
    def run_steps(self):
        pass

    def flip(self):
        if self._continue:
            self._window.flip()

    def check(self, component, *args) -> bool:
        if component is None:
            return self._continue
        return component.check(
            self._time,
            self._frame,
            self._this_flip,
            self._global_flip,
            *args,
        )

    @staticmethod
    def _disable_auto_draw(*components):
        for component in components:
            if component is not None:
                component.auto_draw(False)

    def _update_time(self):
        self._time = self._clock.getTime()
        self._this_flip = self._window.getFutureFlipTime(clock=self._clock)
        self._global_flip = self._window.getFutureFlipTime(clock=None)
        self._frame += 1

    def _reset_time(self):
        self._time = 0.
        self._frame = -1
        self._clock.reset(
            -self._window.getFutureFlipTime(clock='now')
        )

    def _reset_after_step(self):
        self._timer.reset()
        self._continue: bool = True
        self._time: float = 0.
        self._frame: int = -1


class FirstStageRunner(DefaultRunner, RunnerInstructionMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instruction = InstructionComponent(
            text='Этап 1.\n\n'
                 'Сейчас перед Вами будут появляться фотографии, внимательно рассмотртите их.\n\n'
                 'Для продолжения нажмите "пробел"',
        )
        self._image = ImageComponent()
        self._trials = FirstStageTrial()

    def run_steps(self):
        self._instruction_step()
        self._disable_auto_draw(self._instruction)
        self._reset_after_step()
        self._experiment.addLoop(self._trials)
        self._trial_step()

    def _trial_step(self):
        while self._continue:
            self._timer.addTime(5.)
            self._reset_time()
            try:
                image: dict = self._trials.next()
                self._image.setImage(image.get('imagefile'))
                while self._timer.getTime() > 0.:
                    self._update_time()
                    self._continue = self.check(self._image)
                    self._continue = self.check(self._default_keyboard)
                    self.flip()
                self._image.disable()
                self._timer.addTime(15.)
                while self._timer.getTime() > 0.:
                    self._update_time()
                    self._continue = self.check(self._default_keyboard)
                    self.flip()
            except StopIteration:
                self._continue = False


class SecondStageRunner(DefaultRunner, RunnerInstructionMixin):
    def __init__(self, data: ExperimentData, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._clock = core.Clock()
        self._keyboard = InstructionStepKeyboard()
        self._default_keyboard = DefaultKeyboard()
        self._question_keyboard = QuestionKeyboard()
        self._instruction = InstructionComponent(
            text='Этап 2.\n\n'
                 'Вам будет предъявлен ряд вопросов о Вас.\n\n'
                 'Вопросы с вариантами ответов предполагают выбор одного из пунктов. '
                 'Открытые вопросы –– самостоятельный ввод ответа.\n\n'
                 'Ваша задача будет заключаться в том, чтобы дать ответы на все вопросы.\n\n'
                 'Для продолжения нажмите "пробел"',
        )
        self._questions: list[Question] = upload_questions()
        self._data = data

    def run_steps(self):
        self._instruction_step()
        self._disable_auto_draw(self._instruction)
        self._reset_after_step()
        self._question_step()

    def _question_step(self):
        for question in self._questions:
            self._reset_time()
            self._question_keyboard.disable()
            self._continue = True
            if question.type == QuestionType.choices:
                question_component = ChoiceQuestionComponent(
                    text=str(question),
                    choices=question.choices,
                )
                answer_component = None
                keys = list(map(str, range(1, len(question.choices) + 1)))
            else:
                question_component = TextQuestionComponent(
                    text=str(question),
                )
                answer_component = AnswerQuestionComponent()
                keys = [RIGHT]
            while self._continue:
                self._update_time()
                self._continue = self.check(question_component)
                self._continue = self.check(answer_component)
                self._continue = self.check(self._question_keyboard, keys)
                self.flip()
            self._disable_auto_draw(question_component, answer_component)
            self._accept_answers(question, answer_component)
        self._data.questions = self._questions

    def _accept_answers(self, question: Question, answer: AnswerQuestionComponent | None):
        result: str
        if answer is None:
            answer_mapping = {
                str(_id): choice.text for _id, choice in enumerate(question.choices, start=1)
            }
            result = answer_mapping[self._question_keyboard.keys]
        else:
            result = answer.text
        question.answer = Answer(text=result)


class ThirdStageRunner(DefaultRunner, RunnerInstructionMixin):

    def __init__(self, data: ExperimentData, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._clock = core.Clock()
        self._keyboard = InstructionStepKeyboard()
        self._default_keyboard = DefaultKeyboard()
        self._choice_keyboard = ImageChoiceKeyboard()
        self._instruction = InstructionComponent(
            text='Этап 3.\n\n'
                 'Сначала на короткое время вам будет предложено посмотреть лицо.\n'
                 'Далее вам надо будет выбрать одни из двух вариантов, соответсвующий этому лицу или его части.\n\n'
                 'Для выбора используйте стрелочки "влево" и "вправо"\n\n'
                 'Для продолжения нажмите "пробел"',
        )
        self._x_image = XImageComponent()
        self._image = ImageComponent()
        self._left_image = LeftImageComponent()
        self._right_image = RightImageComponent()
        self._trials = ThirdStageTrial()
        self._data = data

    def run_steps(self):
        self._instruction_step()
        self._disable_auto_draw(self._instruction)
        self._reset_after_step()
        self._experiment.addLoop(self._trials)
        self._trial_step()

    def _trial_step(self):
        answers = []
        while self._continue:
            self._reset_time()
            self._timer.reset()
            try:
                image: dict = self._trials.next()
                self._simple_image_flow(self._x_image, 1.)
                self._image.setImage(image.get('imagetest'))
                self._simple_image_flow(self._image, 1.)
                self._simple_image_flow(self._x_image, 0.2)
                self._left_image.setImage(image.get('imageleft'))
                self._right_image.setImage(image.get('imageright'))
                correct_answers = image.get('corans')
                self._choice_image_flow(self._left_image, self._right_image, correct_answers)
                self._disable_auto_draw(self._image, self._x_image, self._left_image, self._right_image)
                answers.append(
                    self._accept_answers(image)
                )
            except StopIteration:
                self._continue = False
        self._data.stimulus = answers

    def _simple_image_flow(self, image, time: float):
        self._timer.addTime(time)
        while self._timer.getTime() > 0.:
            self._update_time()
            self._continue = self.check(image)
            self._continue = self.check(self._default_keyboard)
            self.flip()
        image.disable()
        self._reset_time()
        self._timer.reset()

    def _choice_image_flow(self, left, right, correct_answers):
        while self._continue:
            self._update_time()
            self.check(left)
            self.check(right)
            self._continue = self.check(self._choice_keyboard, correct_answers)
            self.flip()
        self._continue = True
        left.disable()
        right.disable()
        self._choice_keyboard.disable()
        self._reset_time()

    def _accept_answers(self, image):
        return Stimulus(
            target=image.get('imagetest'),
            left=image.get('imageleft'),
            right=image.get('imageright'),
            answer=self._choice_keyboard.keys,
            time_to_answer='{:.4} секунд'.format(self._choice_keyboard.rt),
            is_correct='Правильно' if self._choice_keyboard.corr else 'Неправильно',
        )


class EndStageRunner(DefaultRunner, RunnerInstructionMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instruction = InstructionComponent(
            text='Спасибо за уделенное время!\n\n'
                 'Для завершения нажмите "пробел"',
        )

    def run_steps(self):
        self._instruction_step()
        self._disable_auto_draw(self._instruction)
        self._reset_after_step()
