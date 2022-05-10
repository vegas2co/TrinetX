'''
Poker Game Logic using Terminal
By Khallid Williams
For: TrinetX
Date May 10th, 2022
'''

import requests
import json
from collections import Counter

new_deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
draw_cards = requests.get("https://deckofcardsapi.com/api/deck/sqz9i7wg2lxi/draw/?count=10")
cards = ['2','3','4','5','6','7','8','9','0','J','Q','K','A']
straight = ["".join(cards[i:i+5]) for i in range(0,len(cards),1)] #returns 5 cards in order.

def get_deck(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

def pass_cards():
    me = []
    computer = []
    passed_out_cards = []
    cards_to_read = []
    for i in draw_cards.json()['cards']: #pass 5 cards to me
        #print(i['suit'] + ' ' + i['value']) #read cards dealed
        cards = i['code'] #add cards to stack
        output = i['value'] + ' ' + i['suit']
        passed_out_cards.append(cards)
        cards_to_read.append(output)
        me = passed_out_cards[:5] #pass first 5  cards
        computer = passed_out_cards[5:]
    print('My cards ' + str(cards_to_read[:5]))
    print('Computer cards ' + str(cards_to_read[5:]))
    return me, computer

my_cards, computer_cards = pass_cards()

def determine_rank(userCards):
    symbols = [] #symbols list
    values = [] #digit list
    v_pairs = 0 #count how many pairs
    s_pairs = 0 #count how many pairs
    v_counter = 0 #value counter 
    s_counter = 0 #symbol counter
    score = ''
    score_1 = ''

    for i in userCards: #loop thru list to grab each value
        values.append(i[-2:-1])
        symbols.append(i[-1:])

    v = Counter(values) #count the duplicates 
    s = Counter(symbols) #count the duplicates 

    get_value_count = v.values()
    get_symbol_count = s.values()
    get_card_digits = v.keys()

    for i in get_value_count: #get card logic for values e.g. 2-king
        if i > 1:
            v_counter = 1
            score = 'One Pair'
            v_pairs += 1
            if v_pairs == 2:
                v_counter = 2
                score = 'Two Pair'
            if i == 3:
                if (2 in get_value_count):
                    s_counter = 6
                    v_counter = 6
                    score = 'Full House'
                    score_1 = 'Full House'
                else:
                    v_counter = 3
                    score_1 = 'Three of a kind'
            if i == 4:
                v_counter = 7
                score = 'Four of a kind'
            if i == 5:
                v_counter = 5
                score = 'Flush'
        if i == 0:
            score == 'High Card'

    #print('symbol ' + str(get_symbol_count))
    #print('values ' + str(get_value_count))
    #print('symbol ' + str(s))
    #print('values ' + str(v))

    for i in get_symbol_count: #get card logic for symbols e.g. D,S,C,H
        if i > 1:
            s_counter = 1
            score_1 = 'One Pair'
            s_pairs += 1
            if s_pairs == 2:
                s_counter = 2
                score_1 = 'Two Pair'
            if i == 3:
                if (2 in get_symbol_count):
                    s_counter = 6
                    v_counter = 6
                    score = 'Full House'
                    score_1 = 'Full House'
                else:
                    s_counter = 3
                    score_1 = 'Three of a kind'
            if i == 4:
                s_counter = 7
                score_1 = 'Four of a kind'
            if i == 5:
                s_counter = 5
                score_1 = 'Flush'
            if (get_card_digits in straight):
                s_counter = 8
                v_counter = 8
                score = 'Straight'
                score_1 = 'Straight'
                print('Straight')
        if i == 0:
            score_1 == 'High Card'


    if s_counter > v_counter: #higher count determines winner
        if score > score_1:
            print(score)
        else:
            print(score_1)
        return s_counter
    else:
        if score > score_1:
            print(score)
        else:
            print(score_1)
        return v_counter

def winner():
    if determine_rank(my_cards) > determine_rank(computer_cards):
        print('I won')
    elif determine_rank(my_cards) < determine_rank(computer_cards):
        print('Computer won')
    else :
        print('Tie game')


if __name__ == "__main__":
    get_deck(new_deck.json())
    winner()