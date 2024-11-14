import sqlite3
from __init__ import CONN  # Assuming CONN is properly defined in models

class Question:
    def __init__(self, question_text, answer, category_id, id=None):
        self.id = id
        self.question_text = question_text
        self.answer = answer
        self.category_id = category_id

    @classmethod
    def create_table(cls):
        try:
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
        except Exception as e:
            return e

    @classmethod
    def drop_table(cls):
        try:
            cursor = CONN.cursor()
            cursor.execute('DROP TABLE IF EXISTS questions')
        except Exception as e: 
            return e

    @classmethod
    def create(cls, question_text, answer, category_id):
        new_question = cls(question_text, answer, category_id)
        new_question.save()
        return new_question

    def save(self):
        try:
            cursor = CONN.cursor()
            if self.id is None:
                cursor.execute('INSERT INTO questions (question_text, answer, category_id) VALUES (?, ?, ?)',
                            (self.question_text, self.answer, self.category_id))
                self.id = cursor.lastrowid
            else:
                cursor.execute('UPDATE questions SET question_text = ?, answer = ?, category_id = ? WHERE id = ?',
                            (self.question_text, self.answer, self.category_id, self.id))
            CONN.commit()  # commit after changes
        except Exception as e: 
            CONN.rollback()
            return e

    @classmethod
    def get_all(cls):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM questions')
        rows = cursor.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def get_by_category(cls, category_id):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM questions WHERE category_id = ?', (category_id,))
        rows = cursor.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

if __name__ == "__main__":
    import ipdb; ipdb.set_trace()  # Start debugging from here

