""" 
    Name: code_guru_wk12.py
    Author: Savannah Baird
    Created: 11/06/25
    Purpose: A fun Mad Lib game
"""
from rich.console import Console
from rich.panel import Panel 

# TODO: Define the main function
def main():
    # Use Rich to print a title
    console = Console()
    console.print(
        Panel.fit(
         "     Mad Libs    ",
         style = "bright_green",
         subtitle = "Pick your story"
         )
   )
    # Show the story options
    print("1. Pirate Surprise \n2. Secret Adventure \n3. The Best Sport Story")
    
    # call the choose function
    choice()


# TODO: Define the pirate story function
def pirate():
    # Create an empty list
    answers = []
    # Use .append to add user input to the list
    answers.append(input("Enter an Adjective: "))
    answers.append(input("Enter a Name: "))
    answers.append(input("Enter a noun: "))
    answers.append(input("Enter an exclamation: "))
    answers.append(input("Enter a place: "))
    answers.append(input("Enter an animal [plural]: "))
    answers.append(input("Enter a food [plural]: "))
    answers.append(input("Enter a verb: "))
    # Return the story with the user input from the list
    return(f"One {answers[0]} morning, Captain {answers[1]} woke up to find a {answers[2]} stuck to their forehead. “{answers[3]}!” they shouted, realizing it was a treasure map leading straight to {answers[4]}. With a crew of {answers[5]} and a sack full of {answers[6]}, they set sail, ready to {answers[7]} their way into a legend.")
    
# TODO: Define the adventure story function
def adventure():
    # Create an empty list
    choice = []
    # use .append to add user input to the list
    choice.append(input("Enter a Name: "))
    choice.append(input("Enter an Adjactive: "))
    choice.append(input("Enter a creature [plural]: "))
    choice.append(input("Enter a Magical object: "))
    choice.append(input("Enter a Verb ending in -ing: "))
    choice.append(input("Enter a Place: "))
    choice.append(input("Enter an Exclamation: "))
    choice.append(input("Enter a Verb: "))
    choice.append(input("Enter a Noun: "))
    # Return the story with the user input throughout
    return(f"{choice[0]} was a {choice[1]} adventurer known for outsmarting {choice[2]} and collecting rare treasures. One foggy morning, they discovered a glowing {choice[3]} while {choice[4]} near {choice[5]}. “{choice[6]}!” they shouted, as the ground trembled beneath their feet. With no time to lose, they had to {choice[7]} past a wall of enchanted vines to reach the ancient {choice[8]} before sunset.")

# TODO: Define the sport function
def sport():
    # Create an empty list
    pick = []
    # Use .append to add the user input to the list 
    pick.append(input("Enter a Sport: "))
    pick.append(input("Enter an Athlete: "))
    pick.append(input("Enter an Adjective: "))
    pick.append(input("Enter a snack [plural]: "))
    pick.append(input("Enter a Verb ending in -ing: "))
    pick.append(input("Enter an Exclamation: "))
    pick.append(input("Enter an Object: "))
    pick.append(input("Enter a Verb: "))
    # Return the story with the user input throughout the story
    return(f"It was the final match of the {pick[0]} season, and the crowd roared as {pick[1]} stepped onto the field wearing a {pick[2]} jersey and juggling {pick[3]}. Just as the whistle blew, they started {pick[4]} and shouted, “{pick[5]}!” The ball bounced off a {pick[6]}, and somehow they managed to {pick[7]} it straight into the record books.")

# TODO: Define choice function
def choice():
    # Have the user input their choice
    choose = input("Which story would you like? [x to exit] ")
    # Use a while loop to allow you to keep playing
    while choose != "x":
        # Use if/else to show the users choice of stories 
        if choose == "1":
            print("Great Choice!")
            console = Console()
            console.print("[blue]Pirate Surprise")
            print(pirate())
            choose = input("Which story would you like? [x to exit] ")
        elif choose == "2":
            print("Great Choice!")
            console = Console()
            console.print("[red]Secret Adventure")
            print(adventure())
            choose = input("Which story would you like? [x to exit] ")
        elif choose == "3": 
            print("Great Choice!")
            console = Console()
            console.print("[yellow]The Best Sport Story")
            print(sport())
            choose = input("Which story would you like? [x to exit] ")
        else: 
            print("Play again later.")
            break
    print("Thanks for playing")
# Define the main function
main()