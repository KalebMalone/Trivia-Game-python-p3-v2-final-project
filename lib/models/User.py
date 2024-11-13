from __init__ import CONN, CURSOR
from Question import Question

class User:
    def __init__(self, name, id=None):
        self._name = name
        self.id = id

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
            raise ValueError("Name must be 3 characters")
        if not new_name.isalpha():
            raise ValueError("Name must only contain alphabetic characters")

    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                );
            """
        )
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
        """
            DROP TABLE IF EXISTS players
        """
        )
        CONN.commit()

    @classmethod
    def create(cls, name):
        new_player = cls(name)
        new_player.save()
        return new_player
    
    @classmethod
    def get_all(cls):
        CURSOR.execute(
        """
            SELECT * from players;
        """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[0]) for row in rows]
    
    @classmethod
    def find_name(cls, name):
        CURSOR.execute(
        """
            SELECT * FROM players
            WHERE name = ?;
        """
        (name,) 
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[0] if row else None)