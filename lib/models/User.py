from models import CONN, CURSOR
from models.Question import Question

class User:
    def __init__(self, name, id=None):
        self._name = name
        self.id = id
        self.questions_answered = 0

    def __str__(self):
        return f"Player {self._name}: {self.id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._validate_name(new_name)
        self._name = new_name

    def _validate_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if len(new_name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if not new_name.isalpha():
            raise ValueError("Name must only contain alphabetic characters")

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS players
        """)
        CONN.commit()

    @classmethod
    def create(cls, name):
        new_player = cls(name)
        new_player.save()
        return new_player

    def save(self):
        with CONN:
            if self.id is None:
                CURSOR.execute('INSERT INTO players (name) VALUES (?)', (self.name,))
                self.id = CURSOR.lastrowid
            else:
                CURSOR.execute('UPDATE players SET name = ? WHERE id = ?', (self.name, self.id))

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM players")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[0]) for row in rows]

    @classmethod
    def find_name(cls, name):
        CURSOR.execute("SELECT * FROM players WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

    @classmethod
    def find_by_id(cls, user_id):
        CURSOR.execute("SELECT * FROM players WHERE id = ?", (user_id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

    @classmethod
    def delete(cls, user_id):
        with CONN:
            CURSOR.execute("DELETE FROM players WHERE id = ?", (user_id,))

    def increment_questions_answered(self):
        self.questions_answered += 1