import datetime
import random
from database import create_table, insert_in_table, get_from_db
import modules


def get_questions(quantity_user, list_questions):
    len_question = len(list_questions)
    amount_questions = len_question // quantity_user
    user_questions = []
    while len(user_questions) != amount_questions:
        choice = random.choice(list_questions)
        list_questions.remove(choice)
        user_questions.append(choice)

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
                    print(question.correct_answer[0].text)
            except IndexError:
                print('введите правильное значение от 1 до 4')
                return 'no'


def create_result(list_user, list_result):
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


def main():
    choice = int(input('выберите:\n'
                       '1: начать викторину\n'
                       '2: посмотреть статистику\n'))
    if choice == 1:
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
        for i in range(amount_user):
            user_question = get_questions(amount_user, questions)
            users.append(modules.User(i+1, user_question))

        create_result(users, results)
        winner = who_winner(results)
        print(f'победитель игрок {winner.number} время: {winner.time}'
              f' количество правильных ответов:{winner.amount}')

        create_table()
        points = winner.amount / winner.time.seconds
        today = datetime.datetime.today()
        if points != 0:
            insert_in_table(winner.name, points, today)

    elif choice == 2:
        get_from_db()

    else:
        print('введите 1 или 2')
        return


if __name__ == '__main__':
    main()
