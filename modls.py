class Question:
    def __init__(self, text, *ans):
        self.text = text
        self.answers = [an for an in ans]

class Answers:
    def __init__(self, text: str, key: bool):
        self.text = text
        self.key = key

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
             Answers('6', False),
             Answers('5', True)
             ),
    Question('1+3=?',
             Answers('3', False),
             Answers('1', False),
             Answers('5', False),
             Answers('4', True)
             ),
    Question('1+5=?',
             Answers('3', False),
             Answers('1', False),
             Answers('5', False),
             Answers('6', True)
             ),

]

class User:
    def __init__(self, id):
        self.id = id
        self.total = 0
        self.time = None

    def __str__(self):
        return f'id: {self.id}, right ans:{self.total}'

    def coef(self):
        return self.total/self.time.seconds

