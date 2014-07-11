# PyPoker

PyPoker is a single player poker game written in Python. It is based of simple five-hand poker.

DISCLAIMER: I, Nicholas Gauthier, do not endorse physical gambling in ANY way. This has been put on Github purely for educational reasons. If you feel the need to gamble real currency, please stop playing the game.

WARNING: This game is completely WIP. It doesn't work properly and it's impossible to win! This has been put on Github purely for educational reasons.

## Installing

Windows and Mac users will need to have installed Python.

Windows users can run the "start.bat" file to begin playing.
Mac users will need to somehow run the file. (TODO: Update instructions. Sorry, don't own a Mac)

## Playing the game

PyPoker is played with the keyboard. It will give you a series of text prompts, and you submit your answer via a number. If your number isn't and option, your game could behave unexpectedly.

## Accounts

There is a account system in this game, but the accounts are local. You cannot switch computers without moving the "players.json" file if you want to keep your progress.

As I mentioned, the accounts are stored in "players.json". Accounts are stored in a key-value pair, with the key being the username, and the value being the amount of coins you have.

WARNING: Do not treat these accounts like personal property. If someone play PyPoker under your account, it's your fault! Even though these accounts don't have passwords, you can still revert how many coins you had last in the save file.