from models.User import User
from models.Category import Category
from models.Question import Question
from rich.console import Console

console = Console()



def menu():
    console.print("Please select an option:", style="bold blue")
    print("0. Exit the program")
    print("1. Play a game")
    print("2. Reset game")

    choice = input("> ").strip()

    if choice == "0":
        exit_program()
    elif choice == "1":
        find_or_create_player()
    elif choice == "2":
        reset_game()
    elif choice == "3":

def exit_program():
    console.print("Goodbye!", style="bold red")
    exit()
    
def reset_game():
    console.print("Game has been reset", style="bold green")


def find_or_create_player():

    player = User.find_name(name)

    if player is None:
        new_player = User.create(name)
        console.print(f"Welcome, {new_player.name}!", style="bold green")
        select_category(new_player)
    else:
        console.print(f"Welcome back, {player.name}!", style="bold green")
        select_category(player)

def delete_user():
    name = input("Enter your name to delete your account: ").strip()

    if name.lower() in EXIT_WORDS:
        exit_program()

    player = User.find_name(name)

    if player:
        confirm = input(f"Are you sure you want to delete the user '{name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            User.delete(player.id)  
            console.print(f"The user '{name}' has been deleted.", style="bold red")
        else:
            console.print("User deletion canceled.", style="bold yellow")
    else:
        console.print(f"Could not find user with name '{name}'.", style="bold red")


def select_category(player):
    console.print("Select a category:", style="bold blue")
    print("1. Pop Culture")
    print("2. Sports")
    print("3. Food")
    print("4. Science")

    choice = input("> ").strip()

    if choice in EXIT_WORDS:
        exit_program()

    categories = { '1': 'Pop Culture', '2': 'Sports', '3': 'Food', '4': 'Science' }

    if choice not in categories:
        console.print("Invalid category. Please try again.", style="bold red")
        select_category(player)
    else:
        player.selected_category = categories[choice]
        console.print(f"Category '{player.selected_category}' selected. Let's begin!", style="bold green")

def next_question(player):
    category = Category.find_by_name(player.selected_category)
    if category is None:
        console.print(f"Sorry, we couldn't find the category '{player.selected_category}'.", style="bold red")
        return

    if player.current_question_index < len(questions):
        selected_question = questions[player.current_question_index]
        console.print(f"Question: {selected_question.question_text}", style="bold green")
        user_answer = input("Answer (choose number): ").strip()

        if user_answer.lower() in EXIT_WORDS:
            exit_program()

        check_answer(selected_question, user_answer, player)
    else:
        end_game(player)

def check_answer(selected_question, user_answer, player):
    correct_answer = selected_question.get_correct_answer().strip().lower()

    answer_mapping = {
        "1": selected_question.question_text.split('%')[0].split('.')[1].strip(),
        "2": selected_question.question_text.split('%')[1].split('.')[1].strip(),
        "3": selected_question.question_text.split('%')[2].split('.')[1].strip(),
        "4": selected_question.question_text.split('%')[3].split('.')[1].strip()
    }

    user_answer_text = answer_mapping.get(user_answer.strip(), "").lower()

    if user_answer_text == correct_answer:
        console.print("Correct!", style="bold green")
    else:
        console.print(f"Incorrect! The correct answer was: {correct_answer}", style="bold red")
    
    player.increment_questions_answered()
    player.current_question_index += 1  

    next_question(player)

def end_game(player):
    console.print("Congratulations! You've answered all 5 questions.", style="bold blue")
    print("Would you like to:")
    print("1. Play again")
    print("2. Return to the main menu")
    
    choice = input("> ").strip()

    if choice == "1":
      
    else:
        print("Invalid choice, returning to the main menu.")
        menu()