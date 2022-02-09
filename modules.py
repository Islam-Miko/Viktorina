class Question:
    def __init__(self, text, *ans):
        self.text = text
        self.answers = [an for an in ans]

    def __str__(self):
        return f'df"{self.text}'


class Result:
    def __init__(self, number, time, amount):
        self.number = number
        self.time = time
        self.amount = amount

    def __str__(self):
        return f'id:{self.number} time:{self.time} amount:{self.amount}'


class User:
    def __init__(self, id_, *questions):
        self.id_ = id_
        self.questions = questions
        self.amount_right_answers = 0
        self.time = None


class Answers:
    def __init__(self, text: str, key: bool):
        self.text = text
        self.key = key

    def __str__(self):
        return f'{self.text}'


questions = [
    Question('Кто самый богатый человек в мире?',
             Answers('1. Илон Маск', True),
             Answers('2. Билл Гейтс', False),
             Answers('3. Марк Цукерберг', False),
             Answers('4. Ларри Эллисон', False)
             ),
    Question('Какой язык программирования занимает первое место в мире?',
             Answers('1. C#', False),
             Answers('2. Java', False),
             Answers('3. JavaScript', False),
             Answers('4. Python', True)
             ),
    Question('Из какой страны родом Джастин Бибер?',
             Answers('1. США', False),
             Answers('2. Канада', True),
             Answers('3. Франция', False),
             Answers('4. Англия', True)
             ),
    Question('Что является национальным животным Шотландии?',
             Answers('1. Лошадь', False),
             Answers('2. Единорог', True),
             Answers('3. Волк', False),
             Answers('4. Корова', False)
             ),
    Question('Какая страна производит больше всего кофе в мире?',
             Answers('1. Колумбия', False),
             Answers('2. Индонезия', False),
             Answers('3. Бразилия', True),
             Answers('4. Вьетнам', False)
             ),
    Question('Какой безалкогольный напиток первым был взят в космос?',
             Answers('1. Пепси', False),
             Answers('2. Фанта', False),
             Answers('3. Кока-Кола', True),
             Answers('4. Снапл', False)
             ),
    Question('Как называется маленький пластмассовый кусочек на конце шнурка?',
             Answers('1. Строка', False),
             Answers('2. Чехол', False),
             Answers('3. Кружево', False),
             Answers('4. Аглет', True)
             )
]


