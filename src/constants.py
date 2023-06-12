from enum import Enum

ESCAPE = 'escape'
SPACE_BAR = 'space'
RIGHT = 'right'
LEFT = 'left'

FRAME_TOLERANCE = 0.001


class TrialMethod(Enum):
    sequential = 'sequential'
    random = 'random'


class QuestionType(Enum):
    text = 'text'
    choices = 'choices'


QUESTIONS = [
    {
        'text': 'Ваш пол',
        'question_type': QuestionType.choices,
        'choices': [
            'Мужской',
            'Женский',
        ],
    },
    {
        'text': 'Ваш возраст',
        'question_type': QuestionType.text,
    },
    {
        'text': 'Ваше место жительства',
        'question_type': QuestionType.text,
    },
    {
        'text': 'Ваш родной язык',
        'question_type': QuestionType.text,
    },
    {
        'text': 'Ваш уровень образования',
        'question_type': QuestionType.choices,
        'choices': [
            'Неполное среднее',
            'Среднее',
            'Среднее специальное',
            'Незаконченное высшее',
            'Высшее',
            'Ученая степень',
        ]

    },
    {
        'text': 'Ваша профессия',
        'question_type': QuestionType.text,
    },
    {
        'text': 'Тип Вашей деятельности',
        'question_type': QuestionType.choices,
        'choices': [
            'С людьми',
            'Без людей',
            'Сложно ответить',
        ]
    },
    {
        'text': 'Как вы думаете, какая память у вас лучше развита?',
        'question_type': QuestionType.choices,
        'choices': [
            'Зрительная',
            'Слуховая',
            'Моторная',
            'Вкусовая',
        ]
    },
    {
        'text': 'Как бы вы оценили свою способность запоминать лица?',
        'question_type': QuestionType.choices,
        'choices': [
            'Легко и быстро',
            'Не вызывает явных проблем',
            'С трудностями',
            'Невозможно',
        ]
    },
    {
        'text':
            'Если вы встретили знакомого человека через несколько лет после последней встречи, '
            'вы бы узнали его?'
        ,
        'question_type': QuestionType.choices,
        'choices': [
            'Да',
            'Скорее да, чем нет',
            'Скорее нет, чем да',
            'Нет',
        ],
    },
    *({
        'text': text,
        'question_type': QuestionType.choices,
        'choices': [
            'Левая',
            'Правая',
        ],
    } for text in (
        'При письме указывайте доминирующую руку',
        'Укажите доминирующую руку при рисовании',
        'Укажите доминирующую руку при чистке зубов',
        'Укажите доминирующую руку при броске',
        'Укажите доминирующую руку при резке',
        'Укажите доминирующую руку при использовании столовых приборов',
    )
    )
]
