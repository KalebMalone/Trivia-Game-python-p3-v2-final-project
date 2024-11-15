from models import CONN
from models.Question import Question

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @classmethod
    def create_table(cls):
        cursor = CONN.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE CHECK(name <> '')
            )
        ''')

    @classmethod
    def create(cls, name):
        new_category = cls(name)
        new_category.save()
        return new_category

    def save(self):
        cursor = CONN.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (self.name, self.id))
        CONN.commit()

    @classmethod
    def get_all(cls):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories')
        rows = cursor.fetchall()
        return [cls(row[1], row[0]) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE LOWER(name) = LOWER(?)', (name,))
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None

    def category_questions(self):
        return [question for question in Question.get_all() if question.category_id == self.id]