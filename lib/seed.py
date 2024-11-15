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
    
    pop_q1 = Question.create("Who is the best singer of all time? 1. Beyonce % 2. Celine Dion % 3. Whitney Houston % 4. Mariah Carey %", "Mariah Carey", pop_culture.id)

    pop_q2 = Question.create("What is the name of the fictional kingdom in 'Black Panther'? 1. Narnia % 2. Wakanda % 3. Ginovia % 4. Candy Land %", "Wakanda", pop_culture.id)

    pop_q3 = Question.create("In the TV show 'Friends', what is the name of Ross and Monica's mother? 1. Judy Geller % 2. Jody Geller % 3. Francine Geller % 4. Martha Geller %", "Judy Geller", pop_culture.id)

    pop_q4 = Question.create("Who won the first season of American Idol in 2002? 1. Adam Levine % 2. Kelly Clarkson % 3. Carrie Underwood % 4. Jordan Sparks %", "Kelly Clarkson", pop_culture.id)

    pop_q5 = Question.create("Who famously interrupted Taylor Swift's acceptance speech at the 2009 MTV Video Music Awards, sparking controversy and backlash? 1. Chris Martin % 2. Kanye West % 3. Kendrick Lamar % 4. Drake %", "Kanye West", pop_culture.id)


#sports

    sports_q1 = Question.create("What year is officially recognized as the beginning of the modern Olympic Games? 1. 1886 % 2. 1896 % 3. 1906 % 4. 1916 %", "1896", sports.id)

    sports_q2 = Question.create("What distance do marathon participants run? 1. 10 kilometres % 2. 21 kilometres % 3. 42,195 kilometres % 4. 100 kilometres %", "42,195 kilometres", sports.id)

    sports_q3 = Question.create("Which athlete won the largest number of gold medals at the Olympic Games? 1. Michael Phelps % 2. Usain Bolt % 3. Maria Sharapova % 4. Yusuf Bolt %", "Michael Phelps", sports.id)

    sports_q4 = Question.create("In what year were the first modern Winter Olympic games held? 1. 1924 % 2. 1932 % 3. 1948 % 4. 1956 %", "1924", sports.id)

    sports_q5 = Question.create("In what year was the International Football Federation (FIFA) founded? 1. 1904 % 2. 1923 % 3. 1948 % 4. 1960 %", "1904", sports.id)

#food

    food_q1 = Question.create("Which country did the french fries originate from? 1. France % 2. USA % 3. UK % 4. Belgium %", "Belgium", food.id)

    food_q2 = Question.create("Which food never rots and does not require preservatives to keep fresh? 1. Tea % 2. Honey % 3. Peanuts % 4. Oats %", "Honey", food.id)

    food_q3 = Question.create("Which food contains the most calories per gram? 1. Chocolate % 2. Chia seeds % 3. Avocado % 4. Pistachio %", "Avocado", food.id)

    food_q4 = Question.create("Which was the first fast-food restaurant to open an outlet in China? 1. Jollibee % 2. Subway % 3. KFC % 4. McDonald's %", "KFC", food.id)

    food_q5 = Question.create("Among the numerous pizza toppings, which is the most commonly used? 1. Extra cheese % 2. Mushrooms % 3. Pepperoni % 4. Pineapple %", "Pepperoni", food.id)


#science

    science_q1 = Question.create("What is the chemical symbol for water? 1. H2 % 2. O2 % 3. CO2 % 4. H20 %", "H2O", science.id)

    science_q2 = Question.create("What planet is known as the 'Red Planet'? 1. Venus % 2. Jupiter % 3. Mars % 4. Saturn %", "Mars", science.id)

    science_q3 = Question.create("What is the powerhouse of the cell? 1. Nucleus % 2. Mitochondria % 3. Ribosome % 4. Golgi apparatus %", "Mitochondria", science.id)
    
    science_q4 = Question.create("What gas do plants absorb from the atmosphere? 1. Oxygen % 2. Carbon Dioxide % 3. Nitrogen % 4. Helium %", "Carbon Dioxide", science.id)
    
    science_q5 = Question.create("What force keeps planets in orbit around the sun? 1. Electromagnetism % 2. Friction % 3. Gravity % 4. Tension %", "Gravity", science.id)