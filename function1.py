def get_menu_option():
  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  print("Game options:\n1. Human vs Human\n2. Random AI vs Random AI\n3. Human vs Random AI\n4. Human vs Unbeatable AI")
  while True:
    opt_input = int(input("Select game mode: "))
    if opt_input < 5 and opt_input > 0:
      return opt_input
    else:
      print("Invalid input. Try Again.")
  
  
  


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option) # if the user selected 1, it should print 1