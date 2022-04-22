#Scrabble Project
#In this project, I process some data from a group of players playing scrabble. I utilise lists, dictionaries amd list comprehensions to organize players, words, and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Creating dictionary to assoicate letters with their points.
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[" "] = 0
print(letters_to_points)

#Converts the word to upper case and calculates its points
def score_word(word):
  point_total = 0
  for each_letter in word:
    upper_case = each_letter.upper()
    if upper_case in letters:
      value = letter_to_points.get(upper_case)
      point_total += value
    else:
      point_total += 0
  return point_total

def score_word(word):
  points_total = 0
  for letter in word:
    points_total += letters_to_points.get(letter,0)
  return points_total

# Testing the fucntion.
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Creating a dictionary of players and the words they already have
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# A dictionary acting as a total results table when called
player_to_points = {}
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

update_point_totals()
print(player_to_points)

#Function to allow a play to use a word
def play_word(player, word):
    player_to_words[player].append(word)
    update_point_totals()

#Test runs
play_word("player1", "CODE")
play_word("player1", "lower")
print(player_to_points)



