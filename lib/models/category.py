# Import the sqlite3 library to work with an SQLite database.
import sqlite3

# Establish a connection to the SQLite database named 'database.db'.
# If the file doesn't exist, it will be created.
CONN = sqlite3.connect('database.db')

# Create a cursor object to interact with the database.
CURSOR = CONN.cursor()

# Define a class to represent the 'Categories' table in the database.
class Category:
    # Store all category instances in a class-level dictionary.
    all = {}

    # Initialize a new category instance with a name and optional ID.
    def __init__(self, name, id=None):
        self.id = id  # The ID of the category, if it exists in the database.
        self.name = name  # The name of the category.
        
    @classmethod
    def create_table(cls):
        """Create the categories table if it doesn't exist."""
        try:
            with CONN:
                # Execute SQL to create the 'categories' table with an 'id' and 'name'.
                # 'id' is the primary key and auto-increments.
                # 'name' is unique and must not be null.
                CURSOR.execute('''
                    CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE
                    );
                ''')
        except Exception as e:
            # Print any errors that occur when creating the table.
            print(f"Error creating table: {e}")

    @classmethod
    def drop_table(cls):
        """Drop the categories table if it exists."""
        try:
            with CONN:
                # Execute SQL to drop the 'categories' table if it exists.
                CURSOR.execute('DROP TABLE IF EXISTS categories')
        except Exception as e:
            # Print any errors that occur when dropping the table.
            print(f"Error dropping table: {e}")

    @classmethod
    def create(cls, name):
        """Create a new category in the database."""
        # Create a new category instance.
        new_category = cls(name)
        # Save the instance to the database.
        new_category.save()
        return new_category

    def save(self):
        """Save the current instance to the database."""
        try:
            with CONN:
                if self.id is None:
                    # If the category doesn't have an ID, insert it into the database.
                    CURSOR.execute('INSERT INTO categories (name) VALUES (?)', (self.name,))
                    # Set the instance's ID to the last inserted row's ID.
                    self.id = CURSOR.lastrowid
                else:
                    # If the category already has an ID, update the existing record.
                    CURSOR.execute('UPDATE categories SET name = ? WHERE id = ?', (self.name, self.id))
        except Exception as e:
            # Print any errors that occur when saving the category.
            print(f"Error saving category: {e}")
    
polictics = Categories("politics")