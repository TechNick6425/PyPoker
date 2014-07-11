import array
import random

cards = []

def format(card):
	suit = card // 13
	number = card % 13

	ssuit = 'error'
	if suit == 0:
		ssuit = 'Hearts'
	elif suit == 1:
		ssuit = 'Diamonds'
	elif suit == 2:
		ssuit = 'Clubs'
	elif suit == 3:
		ssuit = 'Spades'

	snumber = 'error'
	if number == 0:
		snumber = 'Ace'
	elif number == 10:
		snumber = 'Jack'
	elif number == 11:
		snumber = 'Queen'
	elif number == 12:
		snumber == 'King'
	else:
		snumber = number + 1
	
	formatted = str(snumber) + ' of ' + str(ssuit)
	return formatted

def randomCard():
	card = 0
	while True:
		card = random.randrange(51)

		#Check if the card is already in play.
		try:
			index = cards.index(card)
		except ValueError:
			break

	cards.append(card)
	return card

def resetRandomizer():
	cards = []