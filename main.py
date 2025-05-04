from File_Manager import FileManager, Word
from Word_Node_Player import Player
from Game_Engine import GameEngine
from menu import display_menu

class Main:
    def __init__(self):
        self.word_list = FileManager.load_words('words.txt')
        self.leaderboard = FileManager.load_leaderboard('leaderboard.txt')

    def start(self):
        while True:
            display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.start_game()
            elif choice == '2':
                self.view_leaderboard()
            elif choice == '3':
                self.manage_word_list()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1-4.")

    def start_game(self):
        name = input("Enter your name: ").strip()
        if not name:
            name = "Anonymous"
        player = Player(name)
        print("\nSelect Difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        diff_choice = input("Choice: ").strip()
        difficulty = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}.get(diff_choice, 'Easy')
        game = GameEngine(player, self.word_list, difficulty)
        game.start_game()

    def view_leaderboard(self):
        print("\n===== LEADERBOARD =====")
        leaderboard = FileManager.load_leaderboard('leaderboard.txt')
        for i, (name, score) in enumerate(leaderboard[:5], 1):
            print(f"{i}. {name} - {score}")

    def manage_word_list(self):
        print("\nAdmin Mode: Manage Word List")
        print("1. Add Word")
        print("2. Delete Word")
        print("3. Search Word")
        print("4. Back")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            word = input("Enter word: ").strip()
            difficulty = input("Difficulty (Easy/Medium/Hard): ").strip().capitalize()
            if difficulty not in ['Easy', 'Medium', 'Hard']:
                difficulty = 'Easy'
            hint = input("Enter hint (definition for Easy/Hard, scrambled for Medium): ").strip()
            if not self.word_list.search_word(word):
                self.word_list.add_word(Word(word, difficulty, hint))
                FileManager.save_words('words.txt', self.word_list)
                print("Word added.")
            else:
                print("Word already exists.")
        elif choice == '2':
            word = input("Enter word to delete: ").strip()
            if self.word_list.delete_word(word):
                FileManager.save_words('words.txt', self.word_list)
                print("Word deleted.")
            else:
                print("Word not found.")
        elif choice == '3':
            word = input("Enter word to search: ").strip()
            if self.word_list.search_word(word):
                print("Word exists.")
            else:
                print("Word not found.")
        elif choice == '4':
            return
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main = Main()
    main.start()