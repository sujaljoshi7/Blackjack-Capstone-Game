import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck"""
    return random.choice(cards)


def calculate_score(all_cards_list):
    if sum(all_cards_list) == 21 and len(all_cards_list) == 2:
        return 0
    if sum(all_cards_list) > 21 and 11 in all_cards_list:
        all_cards_list.remove(11)
        all_cards_list.append(1)

    return sum(all_cards_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "Lose, you went over 😭"
    elif computer_score > 21:
        return "Win, opponent went over 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            break

        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
            user_cards.append(deal_card())
        else:
            break

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()
