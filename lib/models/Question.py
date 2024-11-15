from models import CONN

class Question:
    def __init__(self, question_text, answer, category_id, id=None):
        self.id = id
        self.question_text = question_text
        self.answer = answer
        self.category_id = category_id

    def get_correct_answer(self):
        return self.answer

    @classmethod
    def create_table(cls):
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
        CONN.commit()

    @classmethod
    def drop_table(cls):
        cursor = CONN.cursor()
        cursor.execute('DROP TABLE IF EXISTS questions')
        CONN.commit()

    @classmethod
    def create(cls, question_text, answer, category_id):
        new_question = cls(question_text, answer, category_id)
        new_question.save()
        return new_question

    def save(self):
        cursor = CONN.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO questions (question_text, answer, category_id) VALUES (?, ?, ?)', 

        CONN.commit()

    @classmethod
    def get_all(cls):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM questions')
        rows = cursor.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]