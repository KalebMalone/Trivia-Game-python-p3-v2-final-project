from models.Category import Category
from models.Question import Question
from models.User import User
from helpers import console 

def drop_tables():
    Question.drop_table()
    Category.drop_table()
    User.drop_table()
def create_tables():
    Category.create_table()
    Question.create_table()
    User.create_table()
    
def seed_trivia_game(): #create categories
    pop_culture = Category.create("Pop Culture")
    sports = Category.create("Sports")
    food = Category.create("Food")
    science = Category.create("Science")
    
    return (pop_culture, sports, food, science)

if __name__ == "__main__":
    drop_tables()
    create_tables()
    (pop_culture, sports, food, science) = seed_trivia_game()  
