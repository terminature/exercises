while True:
    Player_1 = input("Player 1 Enter Rock, Paper or Scissor:").lower().strip()
    Player_2 = input("Player 2 Enter Rock, Paper or Scissor:").lower().strip()

    def compare(name1,name2):
        if name1==name2:
            print ("Its a tie")
            pass

        elif name1=="rock" and name2 == "paper" or name1=="paper" and name2=="scissor" or name1 == 'scissor' and name2 == "rock":
            print ("Player1 wins")
            pass
        elif name2=="rock" and name1 == "paper" or name2=="paper" and name1 =="scissor" or name2 == 'scissor' and name1 == "rock":
            print ("Player2 wins")
            pass
        else:
            print("better luck next time")

    compare(Player_1, Player_2)

    x = input (" would you like to try again (yes/no)").lower().strip()
    if x == 'yes':
        continue
    else:
        break

