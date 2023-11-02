# Game based off of the British gameshow, Countdown.
# With inspiration coming from the '8 out of 10 cats' variation.

# **** Rules ****
# see: https://wiki.apterous.org/Main_Page

# **** Gameplay ****
# Two Letter Rounds, Two Numbers Rounds, One final Conundrum

# Ask if player wants to play a full round, just numbers or just Letters

if (full):
    score =+ letters()
    score =+ numbers()
    score =+ letters()
    score =+ numbers()
    # score =+ conundrum()

    # Display their final score

if (numbers):
    score = numbers()

if (letters):
    score = letters()

# **** Global Variables ****
score = 0

# **** Numbers Round ****
# Choose 6 numbers to include a max of 4 large and a randomized target
# Large: one each of 25, 50, 75 100
# Small: two each of 1, 2, 3 ,4, 5, 6, 7, 8, 9
# Target: Random between 100 and 1000 (my guess - actual rule?)
# Any Contenstant / Team with the valid answer gets points (how many?)
# In live Gameplay the smalls are randomized in 3 rows, 2 with 7 and 1 with 6

# Ask user for quantity of large. Must be between 0 & 4
# Large numbers cannot be repeated


# Randomly choose the remaining from small for a total of 6 Numbers
# No small can be repeated more than twice


# Generate a random number between 100 & 1000 and display it to the user
goal_num = random(100,1000)

# Start a 30 second timer


# Ask user what number they got & determine their score
# If playing against another player the closest would get the points
# This is just a custom adaptation to make this enjoyable
player_num = 0 #ask player
if (player_num = goal_num):
    return 10
if (player_num < goal_num and player_num > (goal_num * .9)):
    return 5
return 0

# Have user show how they got there one line at a time
# This is a future add. It will need structure or validation


# **** Letters Round ****
# Choose 9 letters to include at least 3 vowels and 4 consonents
# Possible combinations: 3v 6c, 4v 5c, 5v 4c
# Contenstant / Team with the longest word gets 1 point per letter
# Nine letters words are worth double points, or 18

# Choose a random between 1 and 3 for the number of vowels

# Choose and Display the 9 letters to the player

# Ask user what their longest word is

# Validate it against a chosen dictionary

# Assign them points based on validity of the word
if (valid_word):
    #return length of word
return 0

# **** Conundrum Round ****
# 2 or 3 words with a total of 9 letters and a valid anagram
# Generally 10 points to the solving team, although variations exist

# Future add. Takes more logic
# Define a set of anagrams that can be broken down into smaller words
# Dispay the smaller words to the player
# Start a timer
# Compare their answer with the correct and assign points
