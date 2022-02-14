import datetime
#aziza
from servais import quest, qwe
from modls import User, questions
from database import data, read_db


def main():
    while True:
        all_user = []
        puopl = int(input('enter count: '))
        if puopl > len(questions):
            print('больше игроков чем вопросов')
            continue
        start = quest(puopl)
        print(start)

        for i in range(puopl):
            print(f'Отвечает игрок под номером {i}')
            user = User(i)
            start_time = datetime.datetime.now()
            run = start[i]
            for j in run:
                n = 1
                print(j.text)
                for k in j.answers:
                    print(f'{n}. {k.text}')
                    n += 1
                choice = int(input('enter: ')) - 1
                x = j.answers[choice]
                if x.key:
                    user.total += 1
            end = datetime.datetime.now()
            user.time = end - start_time
            all_user.append(user)

        print('-----' * 5)
        user_winner = qwe(all_user)
        print(user_winner)
        if user_winner.total == 0:
            print('нету подебителя')
        else:
            data(user_winner)

        read_db()


if __name__ == '__main__':
    main()