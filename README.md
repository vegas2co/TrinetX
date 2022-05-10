# Poker with TrinetX
Uploading Poker functionality

This program consist of multiple functions working together.

The new_deck variable is passed into the get_deck() function to get a fresh set of cards to pass out to the player and computer.

The pass_cards() function passes 5 random cards to the computer and the player.

The determine_rank() function is the brains of the program. This function examines the symbols and digits of the cards to determine the ranking categories.
The ranking categories are [one pair, two pait, three of a kind, straight, flush, full house, four of a kind, straight flush].

Lastly, the winner() function determine the winner of the game by determining who has the higher rank.

This file doesn't use jokers so No [Five of a kind]. Also no High card logic, we treated high card as one pair. 

If Player wins - The terminal prints the players ranking, the computers ranking and that the player won the game.

If the Computer wins - The terminal prints the players ranking and the computers ranking twice, then prints that the computer won the game.

If it's a Tie - The terminal prints the players ranking and the computers ranking twice, then prints that the game is a Tie.
