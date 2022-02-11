from models import questions

def quest(number):

    total = len(questions)//number
    list_p = []
    for i in range(number):
        list_player = []
        for j in range(total):
            question = questions.pop()
            list_player.append(question)
        list_p.append(list_player)
    return list_p

def winners(list_user):

    winner = max(list_user, key=lambda x: x.coef())
    return winner

    # records = []
    # for i in list_user:
    #     total = i.total
    #     time = i.time
    #     total_total = total/time
    #     records.append(total_total)
    # win_coef = max(records)
    # for user in
    # return max(records)







