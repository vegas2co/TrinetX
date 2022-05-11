'''
Poker Game Logic using Terminal
By Khallid Williams
For: TrinetX
Date May 10th, 2022
'''

import requests
import json
from collections import Counter
import unittest

new_deck = requests.get("https://deckofcardsapi.com/api/deck/new/?deck_count=1")
draw_cards = requests.get("https://deckofcardsapi.com/api/deck/sqz9i7wg2lxi/draw/?count=10")
resuffle = requests.get("https://deckofcardsapi.com/api/deck/sqz9i7wg2lxi/shuffle/")
cards = ['2','3','4','5','6','7','8','9','0','J','Q','K','A']
ranking = ['One Pair', 'Two Pair', 'Three of a kind', 'Straight', 'Flush', 'Full House', 'Four of a kind', 'Straight Flush']
straight = ["".join(cards[i:i+5]) for i in range(0,len(cards),1)] #returns 5 cards in order e.g 6,7,8,9,0.
winning_list = ['I Won', 'Computer won', 'Tie game']

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

  for i in get_value_count: #get card logic for values e.g. 2 - king
    if i > 1:
      v_counter = 1
      score = ranking[0]
      v_pairs += 1
      if v_pairs == 2:
        v_counter = 2
        score = ranking[1]
      if i == 3:
        if (2 in get_value_count):
          v_counter = 6
          score = ranking[5]
        else:
          v_counter = 3
          score = ranking[2]
      if i == 4:
        v_counter = 7
        score = ranking[6]
      if i == 5:
        if (get_card_digits in straight):
          v_counter = 8
          score = ranking[7]
          score_1 = ranking[7]
        else:
          s_counter = 5
          score = ranking[4]
      if (get_card_digits in straight):
          v_counter = 4
          score = ranking[3]

  for i in get_symbol_count: #get card logic for symbols e.g. D,S,C,H
    if i > 1:
      s_counter = 1
      score_1 = ranking[0]
      s_pairs += 1
      if s_pairs == 2:
        s_counter = 2
        score_1 = ranking[1]
      if i == 3:
        if (2 in get_symbol_count):
          s_counter = 6
          score_1 = ranking[5]
        else:
          s_counter = 3
          score_1 = ranking[2]
      if i == 4:
        s_counter = 7
        score_1 = ranking[6]
      if i == 5:
        if (get_card_digits in straight):
            s_counter = 8
            score = ranking[7]
            score_1 = ranking[7]
        else:
            s_counter = 5
            score_1 = ranking[4]

  if s_counter > v_counter: #higher count determines winner
    if score > score_1:
      print(score)
    else:
      print(score_1)
    return s_counter
  if v_counter > s_counter:
    if score > score_1:
      print(score)
    else:
      print(score_1)
    return v_counter

me = determine_rank(my_cards)
opp = determine_rank(computer_cards)

def winner():
  if me > opp:
    print(winning_list[0])
    return winning_list[0]
  elif me < opp:
    print(winning_list[1])
    return winning_list[1]
  else:
    print(winning_list[2])
    return winning_list[2]

class PokerTest(unittest.TestCase):
  def test_card_amount(self):
    card_count = 52
    self.assertEqual(card_count, int(get_deck(new_deck.json()["remaining"])))   

  def test_winner(self):
    who_won = winner()
    self.assertIn(who_won, winning_list)
    
  def test_how_many_cards_received(self):
    cards_received = 5
    self.assertEqual(cards_received, len(my_cards))
    self.assertEqual(cards_received, len(computer_cards))
    
  def test_highest_scoring_hand(self):
    if me > opp:
      self.assertGreater(me,opp)
    elif opp > me:
      self.assertGreater(opp,me) 
    else:
      self.assertEqual(me,opp)
      
if __name__ == "__main__":
  unittest.main()
  resuffle
  get_deck(new_deck.json())
  winner()