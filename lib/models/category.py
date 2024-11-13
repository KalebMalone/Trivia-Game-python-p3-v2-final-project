from models.__init__ import CONN

class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("Name must be a string.")
        elif len(value_to_validate) < 1:
            raise ValueError("Name must be at least 1 character long.")
        elif hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed after initialization.")
        self._name = value_to_validate

    @staticmethod
    def create_table():
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            ''')

    @classmethod
    def drop_table(cls):
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DROP TABLE IF EXISTS categories')

    @classmethod
    def create(cls, name):
        new_category = cls(name)
        new_category.save()
        return new_category

    def save(self):
        with CONN:
            cursor = CONN.cursor()
            if self.id is None:
                cursor.execute('INSERT INTO categories (name) VALUES (?)', (self.name,))
                self.id = cursor.lastrowid
            else:
                cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (self.name, self.id))

    @classmethod
    def get_all(cls):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories')
        rows = cursor.fetchall()
        return [cls(row[1], row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, category_id):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE id = ?', (category_id,))
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None

    @classmethod
    def find_by_name(cls, name):
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE name = ?', (name,))
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None

    @staticmethod
    def delete(category_id):
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DELETE FROM categories WHERE id = ?', (category_id,))

    def category_questions(self):
        from models.Question import Question
        return [question for question in Question.get_all() if question.category_id == self.id]


if __name__ == "__main__":
    Category.create_table()

    new_category = Category.create('Science')

    all_categories = Category.get_all()
    print(all_categories)

    category = Category.find_by_id(1)
    print(category)

    category = Category.find_by_name('Science')
    print(category)

    category_to_update = Category('Mathematics', id=1)
    category_to_update.save()

    Category.delete(1)