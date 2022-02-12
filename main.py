import datetime
import random
from database import *
import modules
from typing import List
import re


def get_questions(quantity_user: int,
                  list_questions: List[modules.Question],
                  len_question) -> List[modules.Question]:
    """gets questions for user"""
    amount_questions = len_question // quantity_user
    user_questions = []
    while len(user_questions) != amount_questions:
        choice = random.choice(list_questions)
        user_questions.append(choice)
        list_questions.remove(choice)
    return user_questions


def ask_user(list_questions, username):
    for questions in list_questions:
        print(f'{questions.text}\n')
        list_answers = questions.answers
        for i, answer in enumerate(list_answers):
            print(f'{i+1}:{answer}')
        choice = input('ваш вариант:\n')
        try:
            choice = int(choice)
        except Exception as e:
            print(e)
            print('введите вариант от 1 до 4')
            return 'no'
        if choice <= 0:
            print('введите правильное значение от 1 до 4')
            return 'no'
        try:
            choice -= 1
            if list_answers[choice].key:
                print('правильно\n')
                username.amount_right_answers += 1
            else:
                print('неправильно\n'
                      'правильный вариант:')
                print(questions.correct_answer[0].text)
        except IndexError:
            print('введите правильное значение от 1 до 4')
            return 'no'


def create_result(list_user: List[modules.User], list_result):
    for user in list_user:
        name = input('введите ваше имя:\n')
        print(f'вопросы для {user.id_} игрока:\n')
        start = datetime.datetime.now()
        is_working = ask_user(user.questions, user)
        if is_working == 'no':
            return
        user.time = datetime.datetime.now() - start
        list_result.append(modules.Result(user.id_, user.time, user.amount_right_answers, name))


def who_winner(list_results):
    winner = max(list_results, key=lambda x: x.coeff)
    return winner


def validator(login, password):
    pattern_password = re.compile(r"[a-zA-Z0-9@#$%^&+=]{8,}")
    pattern_login = re.compile(r"[a-zA-z0-9]{6,}")
    if re.fullmatch(pattern_login, login) and re.fullmatch(pattern_password, password):
        return True
    else:
        return False


def quiz(login):
    choice = int(input('выберите:\n'
                       '1: начать викторину\n'
                       '2: посмотреть статистику\n'))
    if choice == 1:
        try:
            amount_user = int(input('введите количество игроков:\n'))
        except Exception as e:
            print(e)
            print('введите правильное значение в числах')
            return
        questions = modules.questions
        if amount_user > len(questions):
            print('вас слишком много, максимум 16')
            return
        users = []
        results = []
        len_questions = len(questions)
        for i in range(amount_user):
            user_question = get_questions(amount_user, questions, len_questions)
            users.append(modules.User(i + 1, user_question))

        create_result(users, results)
        winner = who_winner(results)
        print(f'победитель игрок {winner.number} время: {winner.time}'
              f' количество правильных ответов:{winner.amount}')

        create_table()
        points = winner.amount / winner.time.seconds
        today = datetime.datetime.today()
        if points != 0:
            insert_in_table(login, winner.name, points, today)

    elif choice == 2:
        get_from_db(login)

    else:
        print('введите 1 или 2')
        return


def main():
    register = int(input('выберите:\n'
                         '1: регистрация\n'
                         '2: войти\n'))
    create_table_registered()
    if register == 1:
        try:
            while True:
                login = input('придумайте логин: ')
                password = input('придумайте пароль: ')
                result = validator(login, password)
                if result:
                    break
                else:
                    print('логин должен состоят из английских букв и цифр длиною не менеее 6\n'
                          'пароль должен состоят из букв, цифр и спец. символов и длиною не менее 8')

        except Exception as e:
            print(e)
            return

        data_players = get_users_from_table()
        if data_players:
            for row in data_players:
                if row.username == login:
                    print('вы уже зарегистрированы')
                    return
            registration(login, password)
            print('вы зарегистированы\n')
        else:
            registration(login, password)
            print('вы зарегистированы\n')
    elif register == 2:
        data_players = get_users_from_table()
        authorized_login = input('введите ваш логин: ')
        authorized_password = input('введите ваш пароль: ')
        for row in data_players:
            if row.username == authorized_login and row.password == authorized_password:
                print('вы вошли в свой аккаунт\n'
                      'приятной игры ^_^\n')
                quiz(authorized_login)
                return
        print('неправильный логин или пароль')

    else:
        print('введите 1 или 2')
        return


if __name__ == '__main__':
    main()
