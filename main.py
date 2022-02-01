import datetime
import random
from typing import List, Any

import modules


def get_questions(quantity_user, list_questions, used):
    len_question = len(list_questions)
    amount_questions = len_question // quantity_user
    user_questions = []
    while len(user_questions) != amount_questions:
        choice = random.choice(list_questions)
        if choice in used:
            continue
        else:
            user_questions.append(choice)
            used.append(choice)
    return user_questions


def ask_user(list_questions, username):
    for questions in list_questions:
        for question in questions:
            print(f'{question.text}\n')
            list_answers = question.answers
            for i, answer in enumerate(list_answers):
                print(f'{i+1}:{answer}')
            choice = input('ваш вариант:\n')
            try:
                choice = int(choice)
            except:
                print('введите вариант от 1 до 4')
                return 'no'
            if choice <= 0:
                print('введите правильное значение!')
                break
            try:
                choice -= 1
                if list_answers[choice].key:
                    print('right <3\n')
                    username.amount_right_answers += 1
                else:
                    print('wrong :(\n')
            except IndexError:
                print('введите правильное значение!')


def create_result(list_user, list_result):
    for user in list_user:
        print(f'вопросы для {user.id_} игрока:\n')
        start = datetime.datetime.now()
        is_working = ask_user(user.questions, user)
        if is_working == 'no':
            return
        difference = datetime.datetime.now() - start
        difference_sec = difference.total_seconds()
        days = divmod(difference_sec, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        seconds = divmod(minutes[1], 1)
        res_time = f'{int(minutes[0]):02d}:{int(seconds[0]):02d}'
        user.time = res_time
        list_result.append(modules.Result(user.id_, user.time, user.amount_right_answers))


def who_winner(list_results):
    list_rights = []
    list_time = []
    for res in list_results:
        list_rights.append(res.amount)
        list_time.append(res.time)

    max_points = max(list_rights)
    list_time.sort()
    for res in list_results:
        if res.amount == max_points:
            for time in list_time:
                if res.time == time:
                    return res


def main():
    try:
        amount_user = int(input('введите количество игроков:\n'))
    except:
        print('введите правильное значение в числах')
        return
    questions = modules.questions
    if amount_user > len(questions):
        print('вас слишком много, максимум 16')
        return
    users = []
    results = []
    used_questions = []
    for i in range(amount_user):
        user_question = get_questions(amount_user, questions, used_questions)
        users.append(modules.User(i+1, user_question))

    create_result(users, results)
    winner = who_winner(results)
    print(f'победитель игрок {winner.number} время: {winner.time}'
          f' количество правильных ответов:{winner.amount}')

#test
if __name__ == '__main__':
    main()
