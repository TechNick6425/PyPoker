def value(card1, card2, card3, card4, card5):
	#Order the cards
	cards = sorted([card1, card2, card3, card4, card5])
	card1 = cards[0]
	card2 = cards[1]
	card3 = cards[2]
	card4 = cards[3]
	card5 = cards[4]

	# Get some card data
	card1suit = card1 // 13
	card1card = card1 % 13

	card2suit = card2 // 13
	card2card = card2 % 13

	card3suit = card3 // 13
	card3card = card3 % 13

	card4suit = card4 // 13
	card4card = card4 % 13

	card5suit = card5 // 13
	card5card = card5 % 13
	
	if card1suit == card2suit and card2suit == card3suit and card3suit == card4suit and card4suit == card5suit:
		if card1card == 0:
			if card2card == 9:
				if card3card == 10:
					if card4card == 11:
						if card5card == 12:
							return 'royalflush'
						else:
							return 'flush'
					else:
						return 'flush'
				else:
					return 'flush'
			else:
				return 'flush'
		else:
			if card1card == card2card - 1:
				if card2card == card3card - 1:
					if card3card == card4card - 1:
						if card4card == card5card - 1:
							return 'straightflush'
						else:
							return 'flush'
					else:
						return 'flush'
				else:
					return 'flush'
			else:
				return 'flush'
	else:
		if card1card == card2card:
			if card2card == card3card and card3card == card4card:
				return '4ofakind'
			else:
				if card2card == card3card:
					return '3ofakind'
				else:
					if card3card == card4card:
						if card4card == card5card:
							return 'fullhouse'
						else:
							return '2pair'
					else:
						if card4card == card5card:
							return '2pair'
						else:
							return 'pair'
		else:
			if card2card == card3card and card3card == card4card and card4card == card5card:
				return '4ofakind'
			else:
				if card2card == card3card:
					if card3card == card4card:
						return '3ofakind'
					else:
						if card4card == card5card:
							return '2pair'
						else:
							return 'pair'
				else:
					if card3card == card4card:
						if card4card == card5card:
							return '3ofakind'
						else:
							if card1card == card2card - 1:
								if card2card == card3card - 1:
									if card3card == card4card - 1:
										if card4card == card5card - 1:
											return 'straight'
										else:
											return 'junk'
									else:
										return 'junk'
								else:
									return 'junk'
							else:
								return 'junk'

def convert(rank):
	if rank == 'junk':
		return 0
	elif rank == 'pair':
		return 1
	elif rank == '2pair':
		return 2
	elif rank == '3ofakind':
		return 3
	elif rank == 'flush':
		return 4
	elif rank == 'straight':
		return 5
	elif rank == 'fullhouse':
		return 6
	elif rank == '4ofakind':
		return 7
	elif rank == 'straightflush':
		return 8
	elif rank == 'royalflush':
		return 9
	else:
		return -1