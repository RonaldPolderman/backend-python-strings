# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from gettext import find

# PART 1
# Name the 2 players who scored in Euro 1988 final
scorer_name = "Ruud Gullit"
scorer_name1 = "Marco van Basten"
# The minutes where the  scores where
goal_0 = 32
goal_1 = 54
# create a string of the names and the minute they scored in
scorers = scorer_name + ' '+str(goal_0) + ', '+scorer_name1 + ' ' + str(goal_1)
# use an F-string with additional text and seperated on a new text line
report = f'{scorer_name} scored in the {goal_0}nd minute\n{scorer_name1} scored in the {goal_1}th minute'
print(report)

# PART 2
# choose another player in the 1988 match
player = "Ronald Koeman"
# use slice and find method to isolate the player's 1st name
space = player.find(" ")
first_name = player[:space]
print(first_name)
# use find, slice and len to isolate and store the lenght of the last name(without the space counting so result should be 6 not 7 )
last_name = player[space:]
print(last_name)
last_name_len = len(last_name[:-1])
print(last_name_len)
# isolate the players name in this: R. Koeman format (dus het moet er uitzien als R. Koeman)
name_short = f"{player[:1]}." f"{player[space: ]}"
print(name_short)
# chant when a player is about to score.
# their first name plus an exclamationmark(!)
# chant their name as often the lenght of their first name is (Ronald is 6 letters so chant 6 times)
# make sure the last character in the string isn't a space?
# chant = (player[:6]+"! ") * len(player[:6])
# chant = f" {first_name}!" * 6
# chant = f" {first_name}!" * len(first_name)
# chant = (" "+first_name+"!") * len(first_name)
# chant = f"{pre_chant}" * len(first_name)
times_chant = len(first_name)
pre_chant = ((first_name + "! ") * times_chant)
chant = pre_chant[:-1]
# good_chant make sure the last character of chant isnt a space by using inequality operator(!=)
# this variable needs to be a boolean not a string. you can create the value for this variable by comapring the last character of chant with a space character
# try this REPL for example: print(2 != 3). and also try: print(2 != 2)
good_chant = chant[-1] != " "
print(good_chant)
