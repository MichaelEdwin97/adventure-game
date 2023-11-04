import time
import random

def display_message(message, delay=2):
    print(message)
    time.sleep(delay)

def make_choice():
    return input("Please enter 1 or 2: ")

def play_game(choice):
    outcome = random.choice(["win", "lose"])
    return outcome

def main():
    display_message("You find yourself standing in an open field, filled with grass and yellow wildflowers")
    display_message("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village...")
    display_message("There is a house close by. You can walk quickly to the door and knock, hoping someone opens up, and it's not the wicked fairie, or you can enter the cave to find solace.")
    display_message("You are faced with two options:")
    display_message("Enter 1 to knock on the door of the house")
    display_message("Enter 2 to peer into the cave")
    display_message("What would you like to do?")
    
    option = make_choice()

    if option == "1":
        outcome = play_game(option)
        if outcome == "win":
            display_message("The door creaks open, and you are welcomed inside by a friendly villager. You are safe. You win!")
        else:
            display_message("As you knock, the wicked fairie answers the door and casts a spell on you. You lose!")
    else:
        outcome = play_game(option)
        if outcome == "win":
            display_message("You find a hidden stash of treasure inside the cave. Congratulations, you win!")
        else:
            display_message("You encounter a swarm of bats and are forced to flee. You lose!")

if __name__ == "__main__":
    main()
