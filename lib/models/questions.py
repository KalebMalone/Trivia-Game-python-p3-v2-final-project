from models.__init__ import CONN #import package


class Question:
    """Represents a trivia question in the database."""

    def __init__(self, question_text, answer, category_id, id=None):
        """Initialize a new question."""
        self.id = id
        self.question_text = question_text
        self.answer = answer
        self.category_id = category_id

    @classmethod
    def create_table(cls):
        """Create the questions table in the database."""
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
        """Drop the questions table."""
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DROP TABLE IF EXISTS questions')

    @classmethod
    def create(cls, question_text, answer, category_id):
        """Create a new question and save it to the database."""
        new_question = cls(question_text, answer, category_id)
        new_question.save()
        return new_question

    def save(self):
        """Save the current question instance to the database."""
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
        """Get all questions from the database."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM questions')
        rows = cursor.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def get_by_category(cls, category_id):
        """Get all questions for a specific category."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM questions WHERE category_id = ?', (category_id,))
        rows = cursor.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]
