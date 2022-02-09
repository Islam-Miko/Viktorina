from modules import questions


def ques(num):
    total = len(questions) // num
    listt = []
    for i in range(num):
        list_player = []
        for k in range(total):
            question = questions.pop()
            list_player.append(question)
        listt.append(list_player)

    return listt
