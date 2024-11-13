from __init__ import CONN #import package
import sqlite3
class Question:
    """Represents a trivia question in the database."""
    
    def __init__(self, question_text, answer, category_id, id=None):
        """
        Initialize a new question instance.
        
        Parameters:
        - question_text (str): The text of the trivia question.
        - answer (str): The answer to the trivia question.
        - category_id (int): The ID of the category this question belongs to.
        - id (int, optional): The unique identifier for the question in the database (default is None).
        """
        self.id = id
        self.question_text = question_text
        self.answer = answer
        self.category_id = category_id

    @classmethod
    def create_table(cls):
        """Create the 'questions' table in the database if it does not exist."""
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question_text TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories (id)
                )
            ''')
            # defines columns with data types:
            # - id: auto-incremented primary key(uniquely identifies each record in a table)
            # - question_text: required text for the question
            # - answer: required text for the answer
            # - category_id, referencing 'categories' table

    @classmethod
    def drop_table(cls):
        """Drop the 'questions' table from the database, if it exists."""
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DROP TABLE IF EXISTS questions')

    @classmethod
    def create(cls, question_text, answer, category_id):
        """
        Create a new question instance and save it to the database.
        
        Parameters:
        - question_text (str): The text of the question.
        - answer (str): The answer to the question.
        - category_id (int): The ID of the category this question belongs to.
        
        Returns:
        - Question: The newly created question instance.
        """
        new_question = cls(question_text, answer, category_id)
        new_question.save()
        return new_question

    def save(self):
        """
        Save the current question instance to the database.
        If the question has no ID, it is inserted as a new row.
        Otherwise, the existing row is updated.
        """
        with CONN:
            cursor = CONN.cursor()
            if self.id is None:
                # Insert a new question and get the auto-generated ID
                cursor.execute('INSERT INTO questions (question_text, answer, category_id) VALUES (?, ?, ?)',
                            (self.question_text, self.answer, self.category_id))
                self.id = cursor.lastrowid  # Stores the ID assigned by the database
            else:
                # Update existing question with the given ID
                cursor.execute('UPDATE questions SET question_text = ?, answer = ?, category_id = ? WHERE id = ?',
                            (self.question_text, self.answer, self.category_id, self.id))

    @classmethod
    def get_all(cls):
        """
        Retrieve all questions from the database.
        
        Returns:
        - list[Question]: A list of Question instances for each question in the table.
        """
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM questions')
        rows = cursor.fetchall()
        # Create and return Question instances for each row in the table
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def get_by_category(cls, category_id):
        """
        Retrieve all questions for a specific category.
        
        Parameters:
        - category_id (int): The ID of the category to filter questions by.
        
        Returns:
        - list[Question]: A list of Question instances for questions in the specified category.
        """
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM questions WHERE category_id = ?', (category_id,))
        rows = cursor.fetchall()
        # Create and return Question instances for each question in the specified category
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]
