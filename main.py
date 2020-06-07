import random
print("########################################################")
print("           Welcome to Rock Paper Scissor Game           ")
print("########################################################")
wrt = open("history.txt", "w")
count = 0
options = ["rock", "paper", "scissor"]
try:
    while True:
        print("Enter Your choice or write \"done\" to exit")
        user_choice = input(">> ")
        user_choice = user_choice.strip()
        count = count + 1
        wrt.write(str(count) + "\n")
        wrt.write("User Choice: " + user_choice + "\n")
        computer_choice = random.choice(options)
        wrt.write("Computer Choice: " + computer_choice + "\n")
        # Rock
        if user_choice.lower() == "rock":
            if computer_choice == "scissor":
                print("Excellent! You Won :)")
                print("Computer has chosen " + computer_choice)

            elif computer_choice == "paper":
                print("Sorry you lost :(")
                print("Computer has chosen " + computer_choice)
            else:
                print("Draw")
                print("Looks like you and computer has same taste.xD")
        # Paper
        elif user_choice.lower() == "paper":
            if computer_choice == "rock":
                print("Excellent! You Won :)")
                print("Computer has chosen " + computer_choice)
            elif computer_choice == "scissor":
                print("Sorry you lost :(")
                print("Computer has chosen " + computer_choice)
            else:
                print("Draw")
                print("Looks like you and computer has same taste.xD")
        # Scissor
        elif user_choice.lower() == "scissor":
            if computer_choice == "paper":
                print("Excellent! You Won :)")
                print("Computer has chosen " + computer_choice)
            elif computer_choice == "rock":
                print("Sorry you lost :(")
                print("Computer has chosen " + computer_choice)
            else:
                print("Draw")
                print("Looks like you and computer has same taste.xD")

        elif user_choice.lower() == "done":
            print("Exited from the game")
            break
        # I could have used "else" but I tried to experiment with "elif" and "not in" condition
        # elif user_choice.lower() not in options:      # commenting because if this condition exist then there is no \n
            # print("Wrong INPUT. Try again")           # need of except condition
        print("--------------------------------------------------------")
    wrt.close()
except:
    print("Something Went Wrong")

