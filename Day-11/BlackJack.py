from random import *
from os import system, name
from art import logo

players_cards = []
computers_cards = []


def deal_card():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    c_choice = choice(cards)
    return c_choice

def calculate_score(cards):
    """Take a list of cards and returns it's sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(players_score, computers_score):
    if players_score == computers_score:
        return "Draw"
    elif players_score == 0:
        return 'Win, You won with a Blackjack'
    elif computers_score == 0:
        return "Lose, Opponent has Blackjack"
    elif players_score > 21:
        return "You went over 21, You lose"
    elif computers_score > 21:
        return "You win, opponent went over"
    elif players_score > computers_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    is_game_over = False
    print(logo)
    while len(players_cards) < 2:
        players_cards.append(deal_card())
        computers_cards.append(deal_card())
    while not is_game_over:
        players_score = calculate_score(players_cards)
        computers_score = calculate_score(computers_cards)
        print(f"Your cards: {players_cards}, current score: {players_score}")
        print(f"Computers first card: {computers_cards[0]}")

        if players_score == 0 or computers_score == 0 or players_score > 21:
            is_game_over = True
        else:
            players_option = input("Type 'y' to choose a card or 'n' to pass: ").lower()
            if players_option == 'y':
                players_cards.append(deal_card())
            else:
                is_game_over = True
                
    while 0 < computers_score <= 17:
        computers_cards.append(deal_card())
        computers_score = calculate_score(computers_cards)
    print(f"Your final hand: {players_cards} Your final score: {players_score}")
    print(f"Computer's final hand: {computers_cards} Computer's final score: {computers_score}")
    print(compare(players_score, computers_score))
    players_cards.clear()
    computers_cards.clear()
   
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    play_game()
    