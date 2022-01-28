import viktorina
import random

user_used = []

def play():
    chek = 0

    while True:
        chek += 1
        for question in random.choices(viktorina.questions):
            try:
                if question in user_used:
                    continue
                print(question.text)
                for answer in question.answers:
                    print(answer.text)
                player_response = int(input('enter your choice\n'
                                   'options - 1,2,3,4:\n'))
                player_response -= 1
                if player_response < 0:
                    print('False')
                elif question.answers[player_response].key:
                    print('True')
                else:
                    print('False')

            except Exception:
                print('False')
            user_used.append(question)

        if chek >= 6:
            break

play()

# надо доделать
