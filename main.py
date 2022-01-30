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


def main():
    amount_user = int(input('введите количество игроков:\n'))
    questions = modules.questions
    used_questions = []
    used_indexes = []
    users = []
    for i in range(amount_user):
        index_list = index_questions(amount_user, questions, used_indexes)
        user_question = give_questions(index_list, questions, used_questions)
        users.append(modules.User(i+1, user_question))


if __name__ == '__main__':
    main()
