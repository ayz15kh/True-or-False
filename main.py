import random

# Инициализация игры
joker = 2
ace = 6
king = 6
queen = 6

user1_deck = []
user2_deck = []
# Количество очков у игроков
user1_score = 0
user2_score = 0

# Определяем текущий стол
def current_table():
    global storage
    table_choice = random.randint(1, 3)
    if table_choice == 1:
        storage = 'ace table'
    elif table_choice == 2:
        storage = 'king table'
    else:
        storage = 'queen table'
    print(f"Current table: {storage}")

# Раздача карт двум игрокам
def card_dealing():
    global king, queen, ace, joker
    for user in range(1, 3):
        a = 0
        while a < 4:
            jjj = random.randint(1, 4)
            if jjj == 1 and ace > 0:
                (user1_deck if user == 1 else user2_deck).append("ace")
                ace -= 1
                a += 1
            elif jjj == 2 and king > 0:
                (user1_deck if user == 1 else user2_deck).append("king")
                king -= 1
                a += 1
            elif jjj == 3 and queen > 0:
                (user1_deck if user == 1 else user2_deck).append("queen")
                queen -= 1
                a += 1
            elif jjj == 4 and joker > 0:
                (user1_deck if user == 1 else user2_deck).append("joker")
                joker -= 1
                a += 1

def get_player_claim():
    if storage == 'ace table':
        return 'ace'
    elif storage == 'king table':
        return 'king'
    else:
        return 'queen'

def player_turn(player_num):
    global user1_score, user2_score
    current_deck = user1_deck if player_num == 1 else user2_deck

    print(f"Player {player_num}, your current deck: {current_deck}")
    num_cards = int(input(f"Player {player_num}, how many cards do you want to throw (1-3)? "))
    while num_cards < 1 or num_cards > 3:
        num_cards = int(input(f"Invalid number! Player {player_num}, how many cards do you want to throw (1-3)? "))

    thrown_cards = []
    for i in range(num_cards):
        card = input(f"Player {player_num}, enter the card you want to throw ({current_deck}): ")
        while card not in current_deck:
            card = input(f"Invalid card! Please enter a card from your deck: ")
        current_deck.remove(card)
        thrown_cards.append(card)

    print(f"Player {player_num} threw cards.")

    if 'joker' in thrown_cards:
        claim = storage
    else:
        claim = get_player_claim()
    print(f'Player {player_num} claims: This is a {claim}')

    action_choice = input(f"Player {3 - player_num}, do you want to (1) throw cards or (2) True/False? ")

    if action_choice == '1':
        current_deck_opponent = user1_deck if player_num == 2 else user2_deck
        print(f"Player {3 - player_num}, your current deck: {current_deck_opponent}")

        num_cards_opponent = int(input(f"Player {3 - player_num}, how many cards do you want to throw (1-3)? "))
        while num_cards_opponent < 1 or num_cards_opponent > 3:
            num_cards_opponent = int(input(f"Invalid number! Player {3 - player_num}, how many cards do you want to throw (1-3)? "))

        for i in range(num_cards_opponent):
            card = input(f"Player {3 - player_num}, enter the card you want to throw ({current_deck_opponent}): ")
            while card not in current_deck_opponent:
                card = input(f"Invalid card! Please enter a card from your deck: ")
            current_deck_opponent.remove(card)

        print(f"Player {3 - player_num} threw cards.")

    challenge = input(f"Player {3 - player_num}, do you think Player {player_num} threw only '{get_player_claim()}' cards? (True/False): ")

    correct_guess = False

    if challenge.lower() == 'true':
        all_match = True
        for card in thrown_cards:
            if card == 'joker':
                continue
            if card != get_player_claim():
                all_match = False
                break
        if all_match:
            correct_guess = True


    elif challenge.lower() == 'false':
        match = False
        for card in thrown_cards:
            if card == 'joker':
                continue
            if card != get_player_claim():
                match = True
                break

        if match:
            correct_guess = True

    if correct_guess:
        print(f"Player {3 - player_num} guessed correctly!")
        if player_num == 1:
            user2_score += 1
        else:
            user1_score += 1
    else:
        print(f"Player {3 - player_num} guessed incorrectly!")
        if player_num == 1:
            user1_score += 1
        else:
            user2_score += 1

def new_cards():
    global user1_deck, user2_deck,ace,king,queen,joker
    while len(user1_deck) < 4:
        jjj = random.randint(1, 4)
        if jjj == 1 and ace > 0:
            user1_deck.append("ace")
            ace -= 1
        elif jjj == 2 and king > 0:
            user1_deck.append("king")
            king -= 1
        elif jjj == 3 and queen > 0:
            user1_deck.append("queen")
            queen -= 1
        elif jjj == 4 and joker > 0:
            user1_deck.append("joker")
            joker -= 1
    while len(user2_deck) < 4:
        jjj = random.randint(1, 4)
        if jjj == 1 and ace > 0:
            user2_deck.append("ace")
            ace -= 1
        elif jjj == 2 and king > 0:
            user2_deck.append("king")
            king -= 1
        elif jjj == 3 and queen > 0:
            user2_deck.append("queen")
            queen -= 1
        elif jjj == 4 and joker > 0:
            user2_deck.append("joker")
            joker -= 1
def game_cycle():
    while True:
        player_turn(1)
        player_turn(2)
        print(f"Scores: Player 1: {user1_score}, Player 2: {user2_score}")
        print('The cards are dealt!')
        new_cards()
        if user1_score >= 5 or user2_score >= 5:
            break
    print('Game over!')
    print('Final scores:')
    print(f'Player 1: {user1_score}, Player 2: {user2_score}')
    if user1_score > user2_score:
        print('Player 1 won!')
    else:
        print('Player 2 won!')

def main():
    print("Hello, this is the beginning of the game.")
    current_table()
    card_dealing()
    print("Each player was dealt 4 cards")
    get_player_claim()
    game_cycle()
main()