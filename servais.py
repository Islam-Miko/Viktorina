from modls import questions


def quest(number):
    totall = len(questions) // number

    list_ = []
    for i in range(number):
        list_player = []
        for j in range(totall):
            question = questions.pop()
            list_player.append(question)
        list_.append(list_player)

    return list_


def qwe(list_user):
    records = []
    for i in list_user:
        total_total = i.winner_coef()
        records.append(total_total)

    win_corf =  max(records)
    for user in list_user:
        if user.total/user.time == win_corf:
            return user
def winner(list_user):
    winner = max(list_user, key=lambda x: x.coef())
    return winner

