from random import randint


def play():

    with open('assets/question', 'r') as file:
        questions = [list(line.split(';')) for line in file.readlines()]
    while True:

        try:
            nb_players = int(input("Choose the number of players (1-10):\n"))
            if 1 <= nb_players <= 10:
                break
            else:
                print('Incorrect input. Try again\n\n')
        except TypeError:
            print('Incorrect input. Try again\n\n')

    while True:

        try:
            game_mode = int(input("Choose a game mode: 1-Last to stand (elimination) 2-First to n points:\n"))
            if 1 <= game_mode <= 2:
                break
            else:
                print('Incorrect input. Try again\n\n')
        except TypeError:
            print('Incorrect input. Try again\n\n')

    if game_mode == 2:
        while True:

            try:
                points_to_win = int(input("Choose the score to win (2-30) :\n"))
                if 2 <= points_to_win <= 30:
                    break
                else:
                    print('Incorrect input. Try again\n\n')
            except TypeError:
                print('Incorrect input. Try again\n\n')
        players = [0] * nb_players
        outer_break = 0
        while True:
            for i in range(nb_players):
                num_question = randint(0, len(questions)-1)
                question = questions[num_question][0]
                answer = questions[num_question][1]
                player_answer = input(f'\n{question}\nIt\'s the turn of player {i+1}\nType in your answer: ')
                if player_answer.lower().strip() == answer.lower().strip():
                    players[i] += 1
                    print("\nThis is the correct answer!\n")
                    if players[i] == points_to_win:
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\nThe player {i+1} has just won with {points_to_win} points!")
                        outer_break = 1
                        break
                    else:
                        print(f'The player {i+1} now has {players[i]} points')
                else:
                    print(f'\nThis is not the correct answer, the correct answer was: {answer}')
                    print(f'the player {i+1} still has {players[i]} points')
            if outer_break:
                break
        try:
            a = int(input(f'\n\nDo you want to replay? 0-No 1-Yes'))
            if a == 1:
                print('\n\n\n\n')
                play()

        except TypeError:
            pass
    if game_mode == 1:
        players = [1] * nb_players
        while players.count(1) > 1:
            for i in range(len(players)):
                if players[i] == 1:
                    num_question = randint(0, len(questions) - 1)
                    question = questions[num_question][0]
                    answer = questions[num_question][1]
                    player_answer = input(f'\n{question}\nIt\'s the turn of player {i + 1}\nType in your answer: ')
                    if player_answer.lower().strip() == answer.lower().strip():
                        print(f'the player {i+1} got the answer right, he stands in the game')
                    else:
                        players[i] = 0
                        print(f"the player {i + 1} is eliminated. The right answer was {answer}")
                        if players.count(1) == 1:
                            break
        for i, player in enumerate(players):
            if player == 1:
                print(f'\n\n\n\n\n\n\n\n\n\n\n\n\nthe player {i+1} just won the game!!')
        try:
            a = int(input(f'\n\nDo you want to replay? 0-No 1-Yes'))
            if a == 1:
                print('\n\n\n\n')
                play()
        except TypeError:
            print('get the fuck outta here bro')
