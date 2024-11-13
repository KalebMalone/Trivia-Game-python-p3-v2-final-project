from models.category import Category
from lib.models.Question import Question

def drop_tables():
    Question.drop_table()
    Category.drop_table()
    
def create_tables():
    Category.create_table()
    Question.create_table()
    
def seed_trivia_game(): #create categories
    pop_culture = Category.create("Pop Culture")
    sports = Category.create("Sports")
    food = Category.create("Food")
    science = Category.create("Science")
    
pop_q1 = Question.create_question(
    
)