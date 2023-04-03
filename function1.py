def get_menu_option():
  print("\nLet's play TIC TAC TOE")
  print("\nGame options:\n1. Human vs Human\n2. Random AI vs Random AI\n3. Human vs Random AI\n4. Human vs Unbeatable AI")
  while True:
    opt_input = input("\nSelect game mode: ")
    try:
      opt_input = int(opt_input)
      if opt_input < 5 and opt_input > 0:
        return opt_input
      else:
        print("\nInvalid input. Try Again.")
    except ValueError:
      print("\nThats not a number. Please enter a number from 1-4.")


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option) # if the user selected 1, it should print 1