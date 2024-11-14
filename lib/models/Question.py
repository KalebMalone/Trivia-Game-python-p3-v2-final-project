from __init__ import CONN #import package

class Question:
    def __init__(self, question_text, answer, category_id, id=None):
        self.id = id
        self.question_text = question_text
        self.answer = answer
        self.category_id = category_id

    @classmethod
    def create_table(cls):
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

    @classmethod
    def drop_table(cls):
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DROP TABLE IF EXISTS questions')

    @classmethod
    def create(cls, question_text, answer, category_id):
        new_question = cls(question_text, answer, category_id)
        new_question.save()
        return new_question

    def save(self):
        with CONN:
            cursor = CONN.cursor()
            if self.id is None:
                cursor.execute('INSERT INTO questions (question_text, answer, category_id) VALUES (?, ?, ?)',
                            (self.question_text, self.answer, self.category_id))
                self.id = cursor.lastrowid
            else:
                cursor.execute('UPDATE questions SET question_text = ?, answer = ?, category_id = ? WHERE id = ?',
                            (self.question_text, self.answer, self.category_id, self.id))

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