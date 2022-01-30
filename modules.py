class Question:
    def __init__(self, text, *ans):
        self.text = text
        self.answers = [an for an in ans]
        self.choice = 1

    def __str__(self):
        return f'{self.text}'


class Answers:
    def __init__(self, text: str, key: bool):
        self.text = text
        self.key = key

    def __str__(self):
        return f'{self.text}'


class Result:
    def __init__(self, number, time, amount):
        self.number = number
        self.time = time
        self.amount = amount

    def __str__(self):
        return f'id:{self.name} time:{self.time} amount:{self.amount}'


class User:
    def __init__(self, id_, *user_questions):
        self.id_ = id_
        self.user_questions = user_questions
        self.amount_right_answers = 0
        self.time = None

    def __str__(self):
        return f'id:{self.id_}\t'


questions = [
    Question(' Где правильно создана переменная?',
             Answers('var num = 2', False),
             Answers('num = float(2)', True),
             Answers('нет подходящего варианта', False),
             Answers('$num = 2', False)
             ),
    Question('Как получить данные от пользователя?',
             Answers('Использовать метод get()', False),
             Answers('Использовать метод readLine()', False),
             Answers('Использовать метод input() ', True),
             Answers('Использовать метод read()', False)
             ),
    Question('Какая библиотека отвечает за время?',
             Answers('Time', False),
             Answers('localtime', False),
             Answers('time', True),
             Answers('clock', False)
             ),
    Question('Сколько библиотек можно импортировать в один проект?',
             Answers('Неограниченное количество', True),
             Answers('Не более 23', False),
             Answers('Не более 5', False),
             Answers('Не более 3', False)
             ),
    Question('Выберите верные утверждения про списки:',
             Answers('списки могут содержать элементы различных типов', True),
             Answers('списки неизменяемые', False),
             Answers('у списков нету методов', False),
             Answers('списки нельзя передавать как аргумент', False)
             ),
    Question('Сколько параметров может принимать функция?',
             Answers('Нисколько, функция не принимает значения, только возвращает', False),
             Answers('1', False),
             Answers('2', False),
             Answers('бесконечно много', True)
             ),
    Question('В каком случае правильно создана анонимная функция?',
             Answers('lambda x+1: x', False),
             Answers('x + 1 = lambda x', False),
             Answers('lambda x: x + 1', True),
             Answers('def lambda():', False)
             ),
    Question('Имеется кортеж вида T = (4, 2, 3).'
             ' Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?',
             Answers('T[0] = 1', False),
             Answers('T = (1) + T[1:]', False),
             Answers('T = (1,) + T[1:]', True),
             Answers('T.startswith(1)', False)
             ),
    Question('Для чего в Python используется встроенная функция enumerate()?',
             Answers('Для определения количества элементов последовательности.', False),
             Answers('Для одновременного итерирования по самим элементам и их индексам.', True),
             Answers('Для сортировки элементов по значениям id.', False)
             ),
    Question('Необходимо собрать и вывести все уникальные слова из строки рекламного текста.'
             ' Какой из перечисленных типов данных Python подходит лучше всего?',
             Answers('кортеж (tuple)', False),
             Answers('список (list)', False),
             Answers('множество (set)', True),
             Answers('словарь (dict)', False)
             ),
    Question('Как вывести список методов и атрибутов объекта x?',
             Answers('help(x)', False),
             Answers('info(x)', False),
             Answers('?x', False),
             Answers('dir(x)', True)
             ),
    Question('Какая из перечисленных инструкций выполнится быстрее всего, если n = 10**6?',
             Answers('a = list(i for i in range(n))', False),
             Answers('a = [i for i in range(n)]', False),
             Answers('a = (i for i in range(n))', True),
             Answers('a = {i for i in range(n)}', False)
             ),
    Question(' С помощью Python нужно записать данные в файл, но только в том случае, если файла ещё нет.'
             ' Какой режим указать в инструкции open()?',
             Answers("'x'", True),
             Answers("'w'", False),
             Answers("'r'", False),
             Answers("'d'", False)
             ),
    Question('Для чего в пакетах модулей python в файле __init__.py служит список __all__?',
             Answers('Для конструкторов классов, как и всё, что связано с __init__', False),
             Answers('Список определяет, что экспортировать, когда происходит импорт с помощью from *', True),
             Answers('Для перечисления переменных, которые будут скрыты для импортирования.', False)
             ),
    Question('При объявлении класса с помощью оператора class что пишется в круглых скобках после имени класса?',
             Answers('Имена аргументов, принимаемых методом __init__.', False),
             Answers('Имена принимаемых классом аргументов.', False),
             Answers('Имена суперклассов, если класс наследуется от одного или нескольких классов.', True),
             Answers('Имена классов, порождаемых данным классом.', False)
             ),
    Question('Какую роль в описании метода класса выполняет декоратор @property?',
             Answers('Декорированный метод становится статическим, экземпляр не передаётся.', False),
             Answers('Декорированный метод становится методом класса: метод получает класс, а не экземпляр.',False),
             Answers('Значение, возвращаемое декорированным методом, вычисляется при извлечении.'
                     ' Можно обратиться к методу экземпляра, как к атрибуту.', True)
             )
]
