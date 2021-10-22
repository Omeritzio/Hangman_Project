import random

shortWords = [ "ankle", "apple", "birds", "aunts", "blood", "bones", "forty", "glitz", "gnome", "goats", "fairy", "gator", "glass", "kneel", "laces", "party", "zones"]

longWords = [ "jackrabbit", "maximizers", "abnormally", "adrenaline", "california", "basketball", "friendship", "renovation", "skateboard", "understand", "leadership", "restaurant", "generation", "girlfriend", "vegetables", "protection", "trampoline"]

# *** תחילת משחק ***
# פוקציה אשר מבקשת מהמשתמש לבחור דרגת קושי - קלה או קשה
def challenge():
  print ("Choose your difficulty level - for easy click 'E' for hard click 'H' : \n")
  Level = input("E/H: ? \n")
  difficult = Level.lower()

  while difficult != "e" and difficult != "h": 
    print ("Error - Choose your difficulty level again:\n")
    Level = input("E/H: ? \n")
    difficult = Level.lower()
    
  if difficult == "e":
    random_easy = random.choice(shortWords)
    print ("You chose the 'easy' level. Good luck!\n")
    return random_easy
    
  elif difficult == "h":
    random_hard = random.choice(longWords)
    print ("You chose the 'hard' level. Good luck!\n")
    return random_hard


# פונקציה אשר מכניסה את האותיות בסדר הנכון ע"פ הקווים
def lines(correct_position_letters):
  line = ""
  for i in correct_position_letters:
    if i != 0:
      line += i
    else:
      line += ("_ ")
  return line

# פונקציית האיש התלוי
def hangman_graphic(lose):
  gallows = ["_______\n|     |\n|\n|\n|\n|\n|\n=======",
  "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
  "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
  "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
  "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
  "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
  "_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n======="]
  print (gallows[lose])

easy = []
hard = []

# הפוקציה המרכזית - מפעילה את המשחק
def play(game_word):
  correct_position_letters = []
  list_letters = []
  wrong_letter= []


  tries = 6
  lose = 0
  win = 0
  
  # פוקנציה אשר מכניסה אפסים ע"פ סדר האותיות
  for i in range (len(game_word)):
    correct_position_letters.append(0)

  while tries > 0:
    upORlow = input("Please guess a letter:\n")
    guess_letter = upORlow.lower()

    # tried
    # אותיות שהמשתמש כבר בחר
    if guess_letter in list_letters or guess_letter in wrong_letter:
      print ("You have tried this letter\n")

    # wrong letter
    elif guess_letter not in game_word:
      tries -= 1
      lose += 1
      hangman_graphic(lose)
      print (f"Wrong letter. You have more {tries} tries\n")
      wrong_letter.append(guess_letter)

      # lost game
      if tries == 0:
        print ("You lost the game - The man is dead :/\n")
        if len(game_word) > 5:
          hard.append("lose")
        elif len(game_word) <= 5:
          easy.append("lose")
        print("To play again click 'Y'. To finish the game click 'N':\n")
        again = input("Y/N: ? \n")
        play_again = again.lower()
        

        while play_again != "y" and play_again != "n":
          print ("Error - You chose wrong letter:\n")
          again = input("Y/N: ? \n")
          play_again = again.lower()
        if play_again == "y":
          print ("Lets play again:\n")
          game_word = challenge()
          play(game_word)
        elif play_again == "n":
          easy_win = easy.count("win")
          easy_lose = easy.count("lose")
          print (f"Your score in 'easy' difficulty - 'win' : {easy_win} and 'lost' : {easy_lose}\n")
          hard_win = hard.count("win")
          hard_lose = hard.count("lose")
          print (f"Your score in 'hard' difficulty - 'win' : {hard_win} and 'lost' : {hard_lose}\n")
          print ("Thanks for playing. Bye for now :)\n")

    # true letter
    elif guess_letter in game_word:
      win += 1
      hangman_graphic(lose)
      print ("This is one of letter")
      list_letters.append(guess_letter)
      for i in range (len(game_word)):
        if game_word[i] == guess_letter:
          correct_position_letters[i] = game_word[i]
      print (lines(correct_position_letters))

    # win game
      if lines(correct_position_letters) == game_word:
        tries = 0
        if len(game_word) > 5:
          hard.append("win")
        elif len(game_word) <= 5:
          easy.append("win")
        display = [win],[lose]
        print (f"Right letter\Wrong letter : {display}\n")
        print ("Good Job! You guessed the right word! :)\n")
        print("For play again click 'Y'. For finish click 'N':\n")
        again = input("Y/N: ? \n")
        play_again = again.lower()
        while play_again != "y" and play_again != "n":
          print ("Error - For play again click 'Y'. For finish click 'N':\n")
          again = input("Y/N: ? \n")
          play_again = again.lower()
        if play_again == "y":
          print ("Lets play again:\n")
          game_word = challenge()
          play(game_word)
        elif play_again == "n":
          easy_win = easy.count("win")
          easy_lose = easy.count("lose")
          print (f"Your score in 'easy' difficulty - 'win' : {easy_win} and 'lost' : {easy_lose}\n")
          hard_win = hard.count("win")
          hard_lose = hard.count("lose")
          print (f"Your score in 'hard' difficulty - 'win' : {hard_win} and 'lost' : {hard_lose}\n")
          print ("Thanks for playing. Bye for now :)\n")