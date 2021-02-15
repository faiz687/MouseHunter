def Restart():
  """Function To Restart The Game Again.The entire script is in this 
  function."""
  import pickle
  from random import randint
  def random_mouse(extent):
    """Function to get 2 random integers as the mouse row and column.
    It takes an input which extends its range upon the size of the grid"""   
    mouses_row = randint(1,extent)
    mouses_coloumn =  randint(1,extent)
    #print(mouses_row)
    #print(mouses_coloumn)
    return [mouses_row,mouses_coloumn]
  
  def developing_lists(column_rows):
    """"Function to develop lists, this function takes an input of the size
    of the board(int) and develops lists accordingly"""
    rows = column_rows 
    columns = column_rows 
    lists = [0] * rows
    for i in range(columns):
       lists[i] = [0] * rows
    return lists
  
  def print_board(board_size,lists,guess_row,guess_coloumn,steps,acquired_level):
    """"Function to print the board.When this function is executed it
    prints the lists in the form of a board. It takes an input the board size(int) 
    lists , guess_row(int) , guess_coloumn(int) , steps(int) , acquired_level(int)which the user has selected"""
    
    column_rows =  board_size
    a = developing_lists(column_rows)
    for column_heading in range(board_size + 1):
      print(column_heading , end = "  ")
    print(" ")
    if acquired_level == 5 :
      for i in range(board_size):
        print((i+1),*lists[i] , sep = "  ")
        

    if lists[guess_row - 1][guess_coloumn - 1] == steps or lists[guess_row -1 ][guess_coloumn - 1] == "X":
      for i in range(board_size):
        print((i+1),*lists[i] , sep = "  ")
    else: 
      a[guess_row - 1][guess_coloumn - 1]  != steps or a[guess_row - 1][guess_coloumn - 1] != "X"
      for i in range(board_size):
        print((i+1),*a[i] , sep = "  ")    
    
  def actual_steps(asked_row,asked_coloumn,mouse_rows,mouses_coloumns):
    """Function to calculate the steps away from the mouse. It takes four 
    inputs(int) and Returns the number of steps or the shortest distance."""  
    if asked_row >= mouse_rows and asked_coloumn >= mouses_coloumns:
      spaces = (asked_row - mouse_rows) + (asked_coloumn - mouses_coloumns)
      return spaces
    elif mouse_rows >= asked_row and mouses_coloumns >= asked_coloumn:
      spaces = (mouse_rows - asked_row) + (mouses_coloumns - asked_coloumn)
      return spaces
    elif asked_row >= mouse_rows and mouses_coloumns >= asked_coloumn:
      spaces = (asked_row - mouse_rows) + (mouses_coloumns - asked_coloumn)
      return spaces
    else : 
      mouse_rows >= asked_row and asked_coloumn >= mouses_coloumns
      spaces = (mouse_rows - asked_row) + (asked_coloumn - mouses_coloumns)
      return spaces
  
  def save_score(points,selectedlevel):
      """Function to save your score.This function saves the points in a 
      file to view later. It takes two inputs points(int) and selectedlevel(int)
      and saves it to a file."""
      if selectedlevel == 1:
        selectedlevel = "EASY"
      elif selectedlevel == 2:
        selectedlevel = "MEDIUM"
      elif selectedlevel == 3:
        selectedlevel = "HARD"
      savescores = input("Would you like to save your score ? (Y/N)")
      permitted = ["y","Y","n","N"]
      if savescores not in permitted:
        print("YOU CAN ONLY PRESS Y OR N")
        save_score(points,selectedlevel)
      if savescores == "y" or savescores == "Y":
        f = open("Mouse_hunter_scores.txt","a")
        a = f.write(input("Enter your name :") + " : " + str(points) + " : " 
                     + (selectedlevel) + "\n")
        f.close
        return a
      elif savescores == "n" or savescores == "N":
        return ""
  
  def points_scored(guess_es,selectedlevel):
    """Function to calculate the points user has scored. It takes inputs 
     the number of guesses(int) , selectedlevel(int) and outputs the points scored(int)."""
    points = 1100
    for i in range(1,guess_es+1):
      points = points - 100
    print("you have scored " + str(points) + " points ")
    save_score(points,selectedlevel)
  
    
  def user_move(selected_level):
    """ Function to ask the users to guess the row and column and display
    if the mouse is on that row and column  It takes an input the selected 
    level(int) and displays the board size and guesses accordingly. """
    try:
      acquired_level = selected_level
      steps = 0
      if acquired_level == 5:
        save_game_file = open("Mouse_hunter_save.txt", "rb")
        saved_game_list = lists = pickle.load(save_game_file)
        mouses_row  =  pickle.load(save_game_file)
        mouses_coloumn = pickle.load(save_game_file)
        guesses = pickle.load(save_game_file)
        selected_level = pickle.load(save_game_file)
        steps = pickle.load(save_game_file)
        board_size =pickle.load(save_game_file)
        chances_and_boardsize = {1:[8,5],2:[5,7],3:[4,9],4:[4,5],5:[]}
        chances_and_boardsize[5] = [guesses,board_size]
      permitted = [1,2,3,4]
      if acquired_level in  permitted:
        chances_and_boardsize = {1:[8,5],2:[5,7],3:[4,9],4:[4,5]}  
      for i in chances_and_boardsize:
        if i == acquired_level:
          given_chances = chances_and_boardsize[i][0]          
          board_size = chances_and_boardsize[i][1]
          lists = developing_lists(board_size)
          guess = 1
          if acquired_level == 5:
            print_board(board_size,saved_game_list,mouses_row,mouses_coloumn,steps,acquired_level)
          if acquired_level in permitted:
            print_board(board_size,lists,guess,guess,steps,acquired_level)
      if selected_level == 4:
        mouses_row = int(input("select a row to hide  ? : "))
        mouses_coloumn = int(input("select a column to hide ? : "))
      allowed =  [1,2,3]                        
      if acquired_level in allowed:
        t = random_mouse(board_size)
        mouses_row = t[0]
        mouses_coloumn = t[1]
      guesses = 1
      print ("you will get " +(str(given_chances))+ " guesses to find the mouse(X)")
      while guesses <= given_chances:
        permitted = [1,2,3]
        print("guess..." + str(guesses))
        if selected_level not in permitted:
          guess_row = randint(1,5)
          guess_coloumn = randint(1,5)
        if selected_level in permitted:
          if guesses >= 2:
            save_game = input("Save Game : ? (Y/N)")
            if save_game == "y" or save_game == "Y":
              save_game_file = open("Mouse_hunter_save.txt","wb")
              pickle.dump(lists,save_game_file)
              pickle.dump(mouses_row,save_game_file)
              pickle.dump(mouses_coloumn,save_game_file)
              pickle.dump(guesses,save_game_file)
              pickle.dump(selected_level,save_game_file)
              pickle.dump(steps,save_game_file)
              pickle.dump(board_size,save_game_file)
              save_game_file.close
              break
          guess_row = int(input("guess the row : "))
          guess_coloumn = int(input("guess the coloumn : "))
        if guess_row > board_size or guess_coloumn > board_size:
          print("SELECTED ROW OR COLUMN OUT OF RANGE !!")
          user_move(selected_level)
        if guess_row == 0 or guess_coloumn == 0:
          print("SELECTED ROW OR COLUMN OUT OF RANGE !!")
          user_move(selected_level)
        if guess_row == mouses_row and guess_coloumn == mouses_coloumn:
          lists[mouses_row - 1] .pop(mouses_coloumn - 1)
          lists[mouses_row - 1].insert(mouses_coloumn - 1,"X")
          print_board(board_size,lists,guess_row,guess_coloumn,steps,acquired_level)
          print("congratulations you caught the mouse in " +str(guesses)+" guess")
          if selected_level != 4:
            points_scored(guesses,selected_level)
          play_again = input("would you like to restart ? (Y/N)")
          if play_again == "Y" or play_again == "y":
            Restart()
          if play_again == "N" or play_again == "n":
            break
          break
        elif guess_row !=  mouses_row or guess_coloumn != mouses_coloumn:
          if guess_row <= board_size or guess_coloumn <= board_size:
            lists[guess_row - 1].pop(guess_coloumn - 1)
            steps = actual_steps(guess_row,guess_coloumn,mouses_row,mouses_coloumn)
            lists[guess_row - 1].insert(guess_coloumn - 1,steps)
            guesses = guesses + 1
            print_board(board_size,lists,guess_row,guess_coloumn,steps,acquired_level)
      else :
        points = 0 
        lists[mouses_row - 1] .pop(mouses_coloumn - 1)
        lists[mouses_row - 1].insert(mouses_coloumn - 1,"X")
        print_board(board_size,lists,guess_row,guess_coloumn,steps,acquired_level)
        print("YOU RAN OUT OF GUESSES => GAME OVER")
        print("you have scored " + str(points) + " points ")
        if selected_level != 4:
          save_score(points,selected_level)
        play_again = input("would you like to restart ? (Y/N)")
        if play_again == "Y" or play_again == "y":
          Restart()
    except ValueError:
          print("YOU CAN ONLY ENTER A NUMBER !!")
          user_move(selected_level)

  def welcome_screen():
    """ Function to print the welcome screen for the game """
    print(" "*18 , "*"*40)
    print(" "*18, "|      (\___/)           MOUSE-HUNTERZ |")
    print(" "*18, "|       |O O\                          |")
    print(" "*18, "|      / \./ \            CREATED BY   |")
    print(" "*18, "|     /       \            :FAIZAAN:   |")
    print(" "*18, "|     }  ' '   }      /                |")
    print(" "*18, "|     |       / \____/                 |")
    print(" "*18, "|    _\_______\_/                      |")
    print(" "*18,"*"*40)
    print(" "*27,"PRESS S TO START GAME \n"," "*25,"PRESS R TO SEE RANKINGS \n"," "*25,"PRESS I FOR INSTRUCTIONS \n"," "*18,"*"*40)
    start_options = input()
    permitted = ["s","S","R","r","i","I"]
    if start_options not in permitted:
      print("YOU CAN ONLY SELECT THE GIVEN OPTIONS")
      welcome_screen()
    if start_options == "S" or start_options == "s":
      print("SELECT A LEVEL => :::(1)EASY (2)MEDIUM (3)HARD (4)AI (5)LOAD GAME:::")
      select_level = int(input())
      if select_level <= 5 and select_level > 0:
        user_move(select_level)
      if select_level > 5:
        print("YOU CAN ONLY ENTER THE GIVEN NUMBERS")
        welcome_screen()
    elif start_options == "r" or start_options == "R":
      with open("Mouse_hunter_scores.txt","r+") as ranks_file:
        ranks_file = ranks_file.readlines()
        for rankings in ranks_file:
          print(rankings)
        welcome_screen()
    if start_options == "i" or start_options == "I":
      print(" "*16 , "STARTING OF THE GAME,THE MOUSE WILL BE RANDOMLY \n PLACED ON THE GRID. YOU HAVE TO FIND THE MOUSE BE SELECTING THE ROW AND COLUMN. YOU CAN ALSO CHOOSE ON WHICH LEVEL YOU WOULD LIKE TO PLAY WHICH WOULD CHANGE THE NUMBER OF LIVES AND SIZE OF THE GRID. SELECTING (AI) GIVES YOU THE ABILITY TO HIDE THE MOUSE AND THE COMPUTER TO FIND IT. AFTER EACH GUESS YOU CAN SAVE YOUR PROGRESS AND PLAY LATER. ")
      welcome_screen()
  welcome_screen()
Restart()