import csv
from datetime import datetime

from pydantic import BaseModel

from src.constants import QuestionType


class Answer(BaseModel):
    text: str


class QuestionChoice(BaseModel):
    text: str


class Question(BaseModel):
    text: str
    type: QuestionType
    choices: list[QuestionChoice] | None = None
    answer: Answer | None = None

    def __str__(self) -> str:
        if self.type == QuestionType.choices:
            text = f'{self.text}\n\n'
            for number, choice in enumerate(self.choices, start=1):
                text += f'{number}. {choice.text}\n'
            text += '\nВыберите согласно нумерации.\n'
        else:
            text = f'{self.text}\n\nНажмите на стрелку клавиатуры -> для продолжения.\n'
        return text


class Stimulus(BaseModel):
    target: str
    left: str
    right: str
    answer: str
    time_to_answer: str
    is_correct: str


class ExperimentData(BaseModel):
    questions: list[Question] | None = None
    stimulus: list[Stimulus] | None = None

    def to_csv(self, participant):
        fieldnames = [
                         'Целевые стимулы', 'Левые стимулы', 'Правые стимулы', 'Ответ участника', 'Правильный ответ',
                         'Время ответа'
                     ] + [
                         question.text for question in self.questions
                     ]
        today = datetime.now()
        file_name = f'output_data/{participant}-{today.strftime("%Y-%m-%d-%H.%M.%S")}.csv'
        with open(file_name, 'w', encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for stimulus in self.stimulus:
                almost_row = {
                    'Целевые стимулы': stimulus.target,
                    'Левые стимулы': stimulus.left,
                    'Правые стимулы': stimulus.right,
                    'Ответ участника': stimulus.answer,
                    'Правильный ответ': stimulus.is_correct,
                    'Время ответа': stimulus.time_to_answer,
                    **{
                        question.text: question.answer.text for question in self.questions
                    },
                }
                writer.writerow(almost_row)
