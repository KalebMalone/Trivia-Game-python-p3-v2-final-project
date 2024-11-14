from models.User import User
from models.category import Category
from models.Question import Question
from rich.console import Console
from rich.console import Theme
from rich.table import Table
import random
from threading import Timer
import ipdb

theme = Theme({
    "heading": "bold blue",
    "subhead": "bold blue",
    "table_head": "bold blue on blue1",
    "tile": "bold blue on blue1",
    "table": "on blue1",
})

console = Console(theme=theme)
timer_expired_flag = False

EXIT_WORDS = ["0", "exit", "quit"]

def menu():
    console.print("Please select an option:", style="subhead")
    print("0. Exit the program")
    print("1. Play a game")
    print("4. Reset game")
    print("5. Delete User")

def exit_program():
    console.print("Goodbye!", style="subhead")
    exit()

def find_or_create_player():
    name = input("Enter your name: ").strip()

    if name.lower() in EXIT_WORDS:
        exit_program()

    player = User.find_name(name)

    if player is None:
        new_player = User.create(name)
        console.print(f"Welcome, {new_player.name}!", style="subhead")
        play_game(new_player)
    else:
        console.print(f"Welcome back, {player.name}!", style="subhead")
        play_game(player)

def delete_user():
    name = input("Enter your name: ").strip()

    if name.lower() in EXIT_WORDS:
        exit_program()

    player = User.find_name(name)
    if player:
        player.delete()
    else:
        console.print(f"Could not find {name}.", style="subhead")

def play_game(player):
    select_category(player)

def add_points(selected_question, player, doubleJeopardy):
    if doubleJeopardy:
        player.score += selected_question.point_value * 2
    else:
        player.score += selected_question.point_value
    
    player.update()
    
def subtract_points(selected_question, player, doubleJeopardy):
    if doubleJeopardy:
        player.score -= selected_question.point_value * 2
    else:
        player.score -= selected_question.point_value
        
    player.update()
    
def end_game(player):
    console.print(f"Congratulations! Your final score is {player.score}!", style="subhead")
    menu()

def check_answer(selected_question, answer, player, doubleJeopardy):
    global timer_expired_flag
    timer_expired_flag = False

    if selected_question.answer == answer:
        add_points(selected_question, player, doubleJeopardy)
        
        console.print(f"Great job! You won {selected_question.point_value} points!", style="subhead")
        console.print(f"Your current score is {player.score}.")
        
    else:
        subtract_points(selected_question, player, doubleJeopardy)
        
        console.print(f"Sorry, the answer was {selected_question.answer}, you lost {selected_question.point_value} points.", style="subhead")
        console.print(f"Your current score is {player.score}.")
        
        
    selected_question.point_value = ""
    selected_question.save()

    if player.questions_answered() < 30:
        play_game(player)
    else:
        end_game(player)

def select_category(player):
    console.print("Select a category: ", style="subhead")
    
    selected_category = input("Type a category name (Pop Culture, Sports, Food, Science): ").strip().lower()

    if selected_category in EXIT_WORDS:
        exit_program()
    
    valid_categories = ['pop culture', 'sports', 'food', 'science']
    
    if selected_category not in valid_categories:
        console.print('Invalid category selection!', style="subhead")
        return select_category(player)

    selected_points = input("Type a question amount: $").strip()
    
    try:
        if selected_points in EXIT_WORDS:
            exit_program()

        points = int(selected_points)
    
    except ValueError:
        console.print('You must input a valid number!', style="subhead")
        return select_category(player)
        
    category = Category.find_by_name(selected_category)
    
    if points not in [question.point_value for question in category.category_questions() if question.point_value]:
        console.print('Invalid question amount!', style="subhead")
        return select_category(player)
    