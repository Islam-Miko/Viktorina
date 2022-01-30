import datetime
import random
import modules


def index_questions(amount_user, list_questions, used):
    len_question = len(list_questions)
    amount_questions = len_question // amount_user
    index_of_questions = set()
    while len(index_of_questions) != amount_questions:
        index = random.randint(0, len_question-1)
        if index not in used:
            index_of_questions.add(index)
            used.append(index)

    return index_of_questions


def give_questions(indexes, list_of_questions, used):
    user_questions = []
    for i in indexes:
        if list_of_questions[i] not in used:
            user_questions.append(list_of_questions[i])
            used.append(list_of_questions[i])

    return user_questions


def ask_user(list_questions, username):
    for questions in list_questions:
        for question in questions:
            print(f'{question.text}\n')
            list_answers = question.answers
            for answer in list_answers:
                print(f'{answer}')
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
        is_working = ask_user(user.user_questions, user)
        if is_working == 'no':
            return
        difference = datetime.datetime.now() - start
        difference_sec = difference.total_seconds()
        days = divmod(difference_sec, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        seconds = divmod(minutes[1], 1)
        res_time = f'{minutes[0]}:{seconds[0]}'
        user.time = res_time
        list_result.append(modules.Result(user.id_, user.time, user.amount_right_answers))


def main():
    try:
        amount_user = int(input('введите количество игроков:\n'))
    except:
        print('введите правильное значение в числах')
        return
    questions = modules.questions
    used_questions = []
    used_indexes = []
    users = []
    results = []
    for i in range(amount_user):
        index_list = index_questions(amount_user, questions, used_indexes)
        user_question = give_questions(index_list, questions, used_questions)
        users.append(modules.User(i+1, user_question))

    create_result(users, results)


if __name__ == '__main__':
    main()
