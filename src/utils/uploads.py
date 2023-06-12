from src.constants import QUESTIONS, QuestionType
from src.models import Question, QuestionChoice


def upload_questions() -> list[Question]:
    questions = []
    for question in QUESTIONS:
        init_kwargs = {
            'text': question.get('text'),
            'type': question.get('question_type'),
        }
        if question.get('question_type') == QuestionType.choices:
            choices = []
            for choice in question.get('choices'):
                choices.append(
                    QuestionChoice(text=choice)
                )
            init_kwargs['choices'] = choices
        instance = Question(
            **init_kwargs,
        )
        questions.append(instance)
    return questions
