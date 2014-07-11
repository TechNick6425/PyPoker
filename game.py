pcoins = 0
pcard1 = 0
pcard2 = 0
pcard3 = 0
pcard4 = 0
pcard5 = 0

c1coins = 0
c1card1 = 0
c1card2 = 0
c1card3 = 0
c1card4 = 0
c1card5 = 0

c2coins = 0
c2card1 = 0
c2card2 = 0
c2card3 = 0
c2card4 = 0
c2card5 = 0

c3coins = 0
c3card1 = 0
c3card2 = 0
c3card3 = 0
c3card4 = 0
c3card5 = 0

def play(coins):
	import card as cardLib
	import random
	import ai

	cardLib.resetRandomizer()

	pcoins = coins
	pcard1 = cardLib.randomCard()
	pcard2 = cardLib.randomCard()
	pcard3 = cardLib.randomCard()
	pcard4 = cardLib.randomCard()
	pcard5 = cardLib.randomCard()

	c1card1 = cardLib.randomCard()
	c1card2 = cardLib.randomCard()
	c1card3 = cardLib.randomCard()
	c1card4 = cardLib.randomCard()
	c1card5 = cardLib.randomCard()

	c2card1 = cardLib.randomCard()
	c2card2 = cardLib.randomCard()
	c2card3 = cardLib.randomCard()
	c2card4 = cardLib.randomCard()
	c2card5 = cardLib.randomCard()

	c3card1 = cardLib.randomCard()
	c3card2 = cardLib.randomCard()
	c3card3 = cardLib.randomCard()
	c3card4 = cardLib.randomCard()
	c3card5 = cardLib.randomCard()

	pcoins = pcoins - 1
	print 'You ante one coin.'
	print 'You are dealt five cards. They are'
	print '1. ' + cardLib.format(pcard1)
	print '2. ' + cardLib.format(pcard2)
	print '3. ' + cardLib.format(pcard3)
	print '4. ' + cardLib.format(pcard4)
	print '5. ' + cardLib.format(pcard5)

	print 'How many cards would you like to trade?'

	cards = input('>')

	if cards == 0:
		print 'You keep all of your cards.'
	elif cards == 5:
		print 'You trade in your entire hand.'
		pcard1 = cardLib.randomCard()
		pcard2 = cardLib.randomCard()
		pcard3 = cardLib.randomCard()
		pcard4 = cardLib.randomCard()
		pcard5 = cardLib.randomCard()
	else:
		print 'Which cards will you trade in?'
		print 'EX: 245 trades in cards 2, 4, and 5'
		trades = input('>')
		for card in str(trades):
			if card == '1':
				pcard1 = cardLib.randomCard()
			elif card == '2':
				pcard2 = cardLib.randomCard()
			elif card == '3':
				pcard3 = cardLib.randomCard()
			elif card == '4':
				pcard4 = cardLib.randomCard()
			elif card == '5':
				pcard5 = cardLib.randomCard()
	
	print 'You new hand is'
	print '1. ' + cardLib.format(pcard1)
	print '2. ' + cardLib.format(pcard2)
	print '3. ' + cardLib.format(pcard3)
	print '4. ' + cardLib.format(pcard4)
	print '5. ' + cardLib.format(pcard5)

	print '\nYou have ' + str(pcoins) + ' coins.'
	print 'It is your turn to bet.'
	print 'What do you do?'

	c1rank = ai.convert(ai.value(c1card1, c1card2, c1card3, c1card4, c1card5))
	c2rank = ai.convert(ai.value(c2card1, c2card2, c2card3, c2card4, c2card5))
	c3rank = ai.convert(ai.value(c3card1, c3card2, c3card3, c3card4, c3card5))

	pot = 4
	currentBet = 0

	print '1. Call'
	print '2. Fold'
	print '3. Bet'
	choice = input('>')

	com1fold = False
	com2fold = False
	com3fold = False

	p1call = False
	c1call = False
	c2call = False
	c3call = False

	if choice == 1:
		# Next turn
		print 'You call, and play moves to the left.'
		p1call = True
	elif choice == 2:
		print 'You fold. You now have ' + str(pcoins) + ' coins.'
		return pcoins
	elif choice == 3:
		print '\nHow much?'
		bet = input('>')

		print '\nYou bet ' + str(bet) + ' coins.'
		pcoins -= bet
		currentBet = bet
		pot += bet

	while True:

		if not com1fold:
			print '\nIt is COM1\'s turn to bet.'
			if c1rank > (currentBet // 10):
				c1bet = (c1rank - 1) * 2
				if c1bet == 0:
					c1bet = 1
				currentBet += c1bet
				print 'COM1 ups the bet by ' + str(c1bet) + ' coins.'
				pot += currentBet + c1bet
			elif c1rank == (currentBet // 10):
				print 'COM1 matches and calls.'
				pot += currentBet
				c1call = True
			else:
				print 'COM1 folds.'
				com1fold = True

		if not com2fold:
			print '\nIt is COM2\'s turn to bet.'

			if c2rank > (currentBet // 10):
				c2bet = (c2rank - 1) * 2
				if c2bet == 0:
					c2bet = 1
				currentBet += c2bet
				print 'COM2 ups the bet by ' + str(c2bet) + ' coins.'
				pot += currentBet + c2bet
			elif c2rank == (currentBet // 10):
				print 'COM2 matches and calls.'
				pot += currentBet
				c2call = True
			else:
				print 'COM2 folds.'
				com2fold = True

		if not com3fold:
			print '\nIt is COM3\'s turn to bet.'

			if c3rank > (currentBet // 10):
				c3bet = (c3rank - 1) * 2
				if c3bet == 0:
					c3bet = 1
				currentBet = c3bet
				c3bet = c3bet - currentBet
				pot += currentBet + c3bet
				print 'COM3 ups the bet by ' + str(c3bet) + ' coins.'
			elif c3rank == (currentBet // 10):
				print 'COM3 matches and calls.'
				pot += currentBet
				c3call = True
			else:
				print 'COM3 folds.'
				com3fold = True

		print '\nIt\'s your turn to bet.'
		print 'The current bet is ' + str(currentBet)

		print '\n1. Match and Call'
		print '2. Up'
		print '3. Fold'

		choice = input('>')

		if choice == 1:
			print '\nYou match the bet at ' + str(currentBet) + ' coins.'
			pot += currentBet
			p1call = True
		elif choice == 2:
			print 'By how much?'
			up = input('>')
			pot += currentBet + up
			pcoins -= up
			currentBet += up
			print '\nYou up the current bet to ' + str(currentBet) + ' coins.'
		elif choice == 3:
			print '\nYou fold. You now have ' + str(pcoins) + ' coins.'
			return pcoins

		if p1call:
			if c1call or com1fold:
				if c2call or com2fold:
					if c3call or com3fold:
						break
	
	print 'The betting has finished.'
	print 'The pot contains ' + str(pot) + ' coins.'
	print 'Your hand contains'
	print '1. ' + cardLib.format(pcard1)
	print '2. ' + cardLib.format(pcard2)
	print '3. ' + cardLib.format(pcard3)
	print '4. ' + cardLib.format(pcard4)
	print '5. ' + cardLib.format(pcard5)

	p1value = ai.convert(ai.value(pcard1, pcard2, pcard3, pcard4, pcard5))

	if p1value == 0:
		print 'You show junk.'
	elif p1value == 1:
		print 'You show a pair.'
	elif p1value == 2:
		print 'You show two pair.'
	elif p1value == 3:
		print 'You show three of a kind.'
	elif p1value == 4:
		print 'You show a flush.'
	elif p1value == 5:
		print 'You show a straight.'
	elif p1value == 6:
		print 'You show a full house.'
	elif p1value == 7:
		print 'You show four of a kind.'
	elif p1value == 8:
		print 'You show a straight flush.'
	elif p1value == 9:
		print 'You show a royal flush.'
	else:
		print 'You show ' + str(ai.value(pcard1, pcard2, pcard3, pcard4, pcard5))

	if not com1fold:
		if c1rank == 0:
			print 'COM1 shows junk.'
		elif c1rank == 1:
			print 'COM1 shows a pair.'
		elif c1rank == 2:
			print 'COM1 shows two pair.'
		elif c1rank == 3:
			print 'COM1 shows three of a kind.'
		elif c1rank == 4:
			print 'COM1 shows a flush.'
		elif c1rank == 5:
			print 'COM1 shows a straight.'
		elif c1rank == 6:
			print 'COM1 shows a full house.'
		elif c1rank == 7:
			print 'COM1 shows four of a kind.'
		elif c1rank == 8:
			print 'COM1 shows a straight flush.'
		elif c1rank == 9:
			print 'COM1 shows a royal flush.'
		else:
			print 'COM1 shows ' + str(c1rank)

	if not com2fold:
		if c2rank == 0:
			print 'COM2 shows junk.'
		elif c2rank == 1:
			print 'COM2 shows a pair.'
		elif c2rank == 2:
			print 'COM2 shows two pair.'
		elif c2rank == 3:
			print 'COM2 shows three of a kind.'
		elif c2rank == 4:
			print 'COM2 shows a flush.'
		elif c2rank == 5:
			print 'COM2 shows a straight.'
		elif c2rank == 6:
			print 'COM2 shows a full house.'
		elif c2rank == 7:
			print 'COM2 shows four of a kind.'
		elif c2rank == 8:
			print 'COM2 shows a straight flush.'
		elif c2rank == 9:
			print 'COM2 shows a royal flush.'
		else:
			print 'COM2 shows ' + str(c2rank)

	if not com3fold:
		if c3rank == 0:
			print 'COM3 shows junk.'
		elif c3rank == 1:
			print 'COM3 shows a pair.'
		elif c3rank == 2:
			print 'COM3 shows two pair.'
		elif c3rank == 3:
			print 'COM3 shows three of a kind.'
		elif c3rank == 4:
			print 'COM3 shows a flush.'
		elif c3rank == 5:
			print 'COM3 shows a straight.'
		elif c3rank == 6:
			print 'COM3 shows a full house.'
		elif c3rank == 7:
			print 'COM3 shows four of a kind.'
		elif c3rank == 8:
			print 'COM3 shows a straight flush.'
		elif c3rank == 9:
			print 'COM3 shows a royal flush.'
		else:
			print 'COM3 shows ' + str(c3rank)

	if p1value > c1rank and p1value > c2rank and p1value > c3rank:
		print 'You win!'
		print 'You won ' + str(pot) + ' coins.'
		pcoins += pot
		return pcoins
	elif c1rank > p1value and c1rank > c2rank and c1rank > c3rank:
		if com1fold:
			if p1value > c2rank and p1value > c3rank:
				print 'You win!'
				print 'You won ' + str(pot) + ' coins.'
				pcoins += pot
				return pcoins
			elif c2rank > p1value and c2rank > c3rank:
				if com2fold:
					if p1value > c3rank:
						print 'You win!'
						print 'You won ' + str(pot) + ' coins.'
						pcoins += pot
						return pcoins
					else:
						if com3fold:
							print 'You win!'
							print 'You won ' + str(pot) + ' coins.'
							pcoins += pot
							return pcoins
						else:
							print 'COM3 wins!'
							print 'You leave with ' + str(pcoins) + ' coins.'
							return pcoins
				else:
					print 'COM2 wins!'
					print 'You leave with ' + str(pcoins) + ' coins.'
					return pcoins
			elif c3rank > p1value and c3rank > c2rank:
				print 'COM3 wins!'
				print 'You leave with ' + str(pcoins) + ' coins.'
				return pcoins
		else:
			print 'COM1 wins!'
			print 'You leave with ' + str(pcoins) + ' coins.'
			return pcoins
	elif c2rank > p1value and c2rank > c1rank and c2rank > c3rank:
		if com2fold:
			if p1value > c1rank and p1value > c3rank:
				print 'You win!'
				print 'You won ' + str(pot) + ' coins.'
				pcoins += pot
				return pcoins
			elif c1rank > p1value and c1rank > c3rank:
				if com1fold:
					if p1value > c3rank:
						print 'You win!'
						print 'You won ' + str(pot) + ' coins.'
						pcoins += pot
						return pcoins
					else:
						if com3fold:
							print 'You win!'
							print 'You won ' + str(pot) + ' coins.'
							pcoins += pot
							return pcoins
						else:
							print 'COM3 wins!'
							print 'You leave with ' + str(pcoins) + ' coins.'
							return pcoins
			elif c3rank > p1value and c3rank > c1rank:
				if com3fold:
					if p1value > c1rank:
						print 'You win!'
						print 'You won ' + str(pot) + ' coins.'
						pcoins += pot
						return pcoins
					else:
						if com1fold:
							print 'You win!'
							print 'You won ' + str(pot) + ' coins.'
							pcoins += pot
							return pcoins
						else:
							print 'COM1 wins!'
							print 'You leave with ' + str(pcoins) + ' coins.'
							return pcoins
				else:
					print 'COM3 wins!'
					print 'You leave with ' + str(pcoins) + ' coins.'
					return pcoins
		else:
			print 'COM2 wins!'
			print 'You leave with ' + str(pcoins) + ' coins.'
			return pcoins
	elif c3rank > p1value and c3rank > c1rank and c3rank > c2rank:
		if c3fold:
			if p1value > c1rank and p1value > c2rank:
				print 'You win!'
				print 'You won ' + str(pot) + ' coins.'
				pcoins += pot
				return pcoins
			elif c1rank > p1value and c1rank > c2rank:
				if com1fold:
					if p1value > c2rank:
						print 'You win!'
						print 'You won ' + str(pot) + ' coins.'
						pcoins += pot
						return pcoins
					elif c2rank > p1value:
						if com2fold:
							print 'You win!'
							print 'You won ' + str(pot) + ' coins.'
							pcoins += pot
							return pcoins
						else:
							print 'COM2 wins!'
							print 'You leave with ' + str(pcoins) + ' coins.'
							return pcoins
				else:
					print 'COM1 wins!'
					print 'You leave with ' + str(pcoins) + ' coins.'
					return pcoins
		else:
			print 'COM3 wins!'
			print 'You leave with ' + str(pcoins) + ' coins.'
			return pcoins


	print 'Nobody wins!'
	print 'You leave with ' + str(pcoins) + ' coins.'
	return pcoins