class Question:
    def __init__(self, text, *ans):
        self.text = text
        self.answers = [an for an in ans]
        self.choice = 1


class Answers:
    def __init__(self, text: str, key: bool):
        self.text = text
        self.key = key
        self.number = 99


class Result:
    def __init__(self, number, time, amount):
        self.number = number
        self.time = time
        self.amount = amount


questions = [
    Question('1+1=?',
             Answers('3', False),
             Answers('1', False),
             Answers('5', False),
             Answers('2', True)
             ),
    Question('1+4=?',
             Answers('3', False),
             Answers('1', False),
             Answers('5', False),
             Answers('2', True)
             ),
    Question('1+3=?',
             Answers('3', False),
             Answers('1', False),
             Answers('5', False),
             Answers('2', True)
             ),
    Question('1+5=?',
             Answers('3', False),
             Answers('1', False),
             Answers('5', False),
             Answers('2', True)
             ),

]


class Question:
    def __init__(self, text, *answers):
        self.text = text
        self.answers = [ans for ans in answers]


class Answer:
    def __init__(self, text: str, key: bool):
        self.text = text
        self.key = key


questions = [
    Question(
        '1+1=?',
        Answer('1', False),
        Answer('7', False),
        Answer('3', False),
        Answer('2', True)
    )
]

for question in questions:
    print(question.text)
    for answer in question.answers:
        print(answer.text)
    choice = int(input('enter your choice:\n'))
    if choice <= 0:
        print('enter valid variant!')
        break
    try:
        choice -= 1
        if question.answers[choice].key:
            print('right <3')
        else:
            print('wrong :(')
    except IndexError:
        print('enter valid variant!')


