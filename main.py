import datetime

from services import quest, winners
from models import User, questions
from database import data, read_db

def main():

    all_user = []
    people = int(input('enter count: '))
    if people > len(questions):
        print('Больше игроков, чем вопросов')
        return
    start = quest(people)                                           # СПИСОК ВОПРОСОВ
    print(start)

    for i in range(people):                                         # ВОПРОСЫ ДЛЯ 1ГО ИГРОКА
        print(f'Отвечает игрок под номером {i+1}')
        user = User(i)
        start_time = datetime.datetime.now()
        run = start[i]
        for j in run:                                               # 1Й ВОПРОС
            print('Вопрос:')
            print(j.text, end=' ')
            print('\nВарианты ответов:')
            n = 1
            for k in j.answers:                                     # ВАРИАНТЫ ОТВЕТОВ
                print(str(n)+')', k.text, end='; ')
                n += 1
            print('\n')
            choice = int(input('Мой ответ: ')) - 1
            x = j.answers[choice]
            if x.key:
                user.total += 1
        end = datetime.datetime.now()
        user.time = end - start_time
        all_user.append(user)


    print(all_user)
    print('----------'*5)
    user_winner = winners(all_user)
    print(user_winner)
    if user_winner.total == 0:
        print("нет победителя")
    else:
        data(user_winner)

    read_db()


main()
