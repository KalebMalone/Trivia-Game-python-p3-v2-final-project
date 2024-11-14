from helpers import (
    menu,
    exit_program,
    find_or_create_player,
    delete_user
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            find_or_create_player()
        elif choice == "5":
            delete_user()
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    main()