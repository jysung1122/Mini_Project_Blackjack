import random
from replit import clear
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    score = sum(card_list)

    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)

    if score == 21 and len(card_list) == 2:
        return 0  # Blackjack

    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Computer wins with a Blackjack!"
    elif user_score == 0:
        return "User wins with a Blackjack!"
    elif user_score > 21:
        return "User busts. Computer wins!"
    elif computer_score > 21:
        return "Computer busts. User wins!"
    elif user_score > computer_score:
        return "User wins!"
    else:
        return "Computer wins!"


def play_game():
    print(art.logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        should_continue = False
    else:
        should_continue = True

    while should_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ").lower(
        ) == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            if user_score > 21:
                should_continue = False
        else:
            should_continue = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final cards: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': "
            ).lower() == 'y':
    clear()
    play_game()
