import random
import time


def print_p(word):
    """Prints a message and waits for 2 seconds."""
    print(word)
    time.sleep(2)


def valid_input(prompt, *options):
    """Prompts the user for input until they
    provide one of the valid options."""
    options = [option.lower() for option in options]
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print_p("Sorry, I don't understand. Please choose a valid option.")


def intro():
    """Displays the introduction to the adventure game."""
    print_p("You are Laila.")
    print_p("You want to visit your grandma in the deep forest"
            " to deliver her the medicine.")
    print_p("Section 1: The Deep Forest Adventure")
    print_p("Your journey begins in The Deep Forest.")
    print_p("You start going deeper into the forest"
            " until you reach the river.")


def left_road():
    """Handles the choices when taking the left road."""
    print_p("You find a wooden boat.")
    choice = valid_input(
        "Press 1 to keep walking beside the river.\n"
        "Press 2 to take the boat into the river.\n", "1", "2")
    if choice == "2":
        print_p("The boat starts moving in the river"
                " but the current is too strong,"
                " leading you into a water slope. You fall and drown.")
        end_game()
    else:
        print_p("You proceed carefully along the river and encounter a tiger.")
        print_p("You remember you have some food in your bag.")
        print_p("You feed the tiger,"
                " and it becomes your friend and follows you.")
        choices_section2()


def right_road():
    """Handles the choices when taking the right road."""
    print_p("You encounter a tiger.")
    choice = valid_input(
        "Press 1 to tame the tiger.\nPress 2 to fight the tiger.\n",
        "1", "2"
    )
    if choice == "1":
        print_p("The tiger becomes your companion. You proceed to Section 2.")
        choices_section2()
    else:
        weapons = ["Food", "Fork"]
        print_p("Wait! There's a chest behind you.")
        print_p("Open it; it might have a weapon.")
        weapon = random.choice(weapons)
        print_p(f"You got a {weapon} from the chest.")
        if weapon == "Fork":
            print_p("The tiger attacks you with the fork."
                    " You won't proceed to Section 2.")
            end_game()
        else:
            print_p("You feed the tiger, and it becomes your friend."
                    " You proceed to Section 2.")
            choices_section2()


def choices_section1():
    """Handles the choices in Section 1 of the adventure."""
    road = valid_input(
        "Press 1 to take the left side.\nPress 2 to take the right side.\n",
        "1", "2"
    )
    if road == "1":
        left_road()
    else:
        right_road()


def quicksand():
    """Handles the choices when facing quicksand."""
    print_p("You walk into the quicksand.")
    choice = valid_input(
        "Press 1 to move slowly.\nPress 2 to move quickly.\n",
        "1", "2"
    )
    if choice == "1":
        print_p("You move slowly and manage to cross it safely."
                " You proceed to the Final Section.")
        choices_final()
    else:
        print_p("You move quickly and start sinking."
                " It swallows you; you die.")
        end_game()


def climbing():
    """Handles the choices when encountering thorny trees."""
    print_p("You find thorny trees.")
    choice = valid_input(
        "Press 1 to climb carefully.\nPress 2 to find another way.\n",
        "1", "2"
    )
    if choice == "1":
        print_p("You climb carefully, get some wounds but"
                " survive and make it to the other side.")
        print_p("You proceed to the Final Section.")
        choices_final()
    else:
        print_p("You find a narrow road but you can fit in hardly."
                " You proceed to the Final Section.")
        choices_final()


def choices_section2():
    """Handles the choices in Section 2 of the adventure."""
    print_p("Section 2: The Quicksand")
    choice = valid_input(
        "Press 1 to face your fears and cross the quicksand.\n"
        "Press 2 to reach the thorny trees.\n", "1", "2")
    if choice == "1":
        quicksand()
    else:
        climbing()


def choices_final():
    """Handles the choices in the Final Section of the adventure."""
    print_p("Final Section: Grandma's House")
    print_p("You get closer to Grandma's house but"
            " notice a wolf around the door.")
    choice = valid_input(
        "Press 1 to call the tiger to fight the wolf.\n"
        "Press 2 to sneak around the wolf.\n", "1", "2")
    if choice == "1":
        print_p("The fight begins."
                "The tiger is stronger than the wolf and defeats it."
                " You deliver the medicine to your grandma!")
        print_p("Hooray, you win!")
        end_game()
    else:
        print_p("You are caught, and the wolf eats you. You lose.")
        end_game()


def end_game():
    """Handles the end of the game."""
    if valid_input("Play again? yes or no\n", "yes", "no") == "yes":
        adventure_game()
    else:
        print_p("OK, Goodbye")


def adventure_game():
    """Starts the adventure game."""
    intro()
    choices_section1()


def main():
    """Main function to start the game."""
    adventure_game()


if __name__ == "__main__":
    main()
