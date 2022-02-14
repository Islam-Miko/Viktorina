class Question:
    def __init__(self, text, *ans):
        self.text = text
        self.answers = [an for an in ans]

class Answers:
    def __init__(self, text: str, key: bool):
        self.text = text
        self.key = key


class User:
    def __init__(self, id):
        self.id = id
        self.total = 0
        self.time = None

    def __str__(self):
        return f'Игрок № id: {self.id+1}, right ans:{self.total}'

    def coef(self):
        return self.total/self.time.seconds



questions = [
    Question('Что напечатает следующий код print((1 ,2, 3)<(1, 2, 4))',
             Answers('None', False),
             Answers('True', True),
             Answers('False', False),
             Answers('Ошибка', False)
             ),
    Question('Что делает следующий код: def a(b, c, d): pass',
             Answers('Определяет список и инициализирует его', False),
             Answers('Определяет функцию, которая ничего не делает', True),
             Answers('Определяет функцию, которая передает параметры', False),
             Answers('Определяет пустой класс', False)
             ),
    Question('Что выведет следующий код в Python 3.x? print(type(1 / 2))',
             Answers("class 'tuple'", False),
             Answers("class 'int'", False),
             Answers("class 'number'", False),
             Answers('class float', True)
             ),
    Question('Какая из функций вернет итерируемый объект?',
             Answers('len()', False),
             Answers('xrange()', False),
             Answers('range()', True),
             Answers('ord()', False)
             ),
    Question("Какого типа будет результат следующего выражения: (' ',)",
             Answers('str(строка)', False),
             Answers('tuple(кортеж)', True),
             Answers('возникнет синтаксическая ошибка', False),
             Answers('unicode строка', False)
             ),

]
