import sys
import game
import json

# Get the players

f = open('players.json')
players = json.load(f)

# Setup some player data

player = ''

coins = 0

#Startup prompt

print 'Welcome to PyPoker!'
print 'Please make a choice an press enter!\n'

print '1. Login to an existing account'
print '2. Create a new acount'
print '3. Quit\n'

choice = input('>')

if choice == 1:
	while True:
		print '\nPlease enter your account ID.'
		print 'P.S. Please put it in "double paranthases" like this.'
		aid = input('>')
		if aid in players:
			player = aid
			coins = players[player]
			print 'Welcome back, ' + player + '!'
			print 'You have ' + str(coins) + ' coins in your account.'
			break
		else:
			print 'That account doesn\'t exist!'
elif choice == 2:
	# Account creation
	while True:
		print '\nPlease enter a unique account ID for yourself.'
		print 'P.S. Please put it in "double paranthases" like this.'
		aid = input('>')
		if not aid in players:
			player = aid
			players[player] = 100
			coins = players[player]
			print 'Welcome, ' + player + '!'
			print 'You have been given 100 complementary coins.'
			break
		else:
			print 'That account already exists!'
else:
	print 'Goodbye!'
	sys.exit(0)

while True:
	print '\nWhat would you like to do?'
	print '1. Play a round'
	print '2. Leave'
	
	choice = input('>')
	
	if choice == 1:
		# Play the game!
		coins = game.play(coins)
	else:
		print 'We hope you enjoyed your stay!'
		
		# Save player data
		players[player] = coins
		f = open('players.json', 'w')
		json.dump(players, f)
		print 'Goodbye!'
		sys.exit(0)