import random
import os           #same as to clear() to clear screen
from art import logo

def deal_card():
    '''prints out a random card from our card list'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    '''if we have sum of 21 and length of two cards return 0 for blackjack'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    '''if we have and ace card(11) and our sum is over 21 then we remove the 11 card and replace with 1 by appending'''
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "You lost, opponent got blackjack!!"
    elif user_score == 0:
        return "You won, you got blackjack!!"
    elif user_score > 21:
        return "You lose, you went over 21!!"
    elif computer_score > 21:
        return "You win, opponent went over 21!!"
    elif user_score > computer_score:
        return "You win, your score is higher!!"
    else:
        return "You lose, opponent score is higher"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for x in range(2):
        '''deals 2 cards to user and computer'''
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards} and your score is {user_score}")
        print(f"Computers first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input('Would you like to draw another card? Type "yes" or "no": ')
            if another_card == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    '''if computer score is < 17 or if computer isnt blackjack(0)they have to keep drawing'''
    while computer_score !=0 and computer_score < 17: 
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is {user_cards} scoring {user_score}, The computers final hand is {computer_cards} scoring {computer_score}")
    print(compare(user_score, computer_score))

while input('Do you want to play a game of blackjack? y or n: ').lower() == 'y':
    os.system('cls')
    play_game()