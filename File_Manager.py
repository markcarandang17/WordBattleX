from Wordlist import WordList
from Word_Node_Player import Word

class FileManager:
    def load_words(filename):
        word_list = WordList()
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(',', 2)
                        if len(parts) == 3:
                            word, difficulty, hint = parts
                            word_list.add_word(Word(word, difficulty, hint))
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Starting with empty word list.")
        return word_list

    def save_words(filename, word_list):
        with open(filename, 'w') as file:
            current = word_list.head
            while current:
                word_obj = current.data
                file.write(f"{word_obj.word},{word_obj.difficulty},{word_obj.hint}\n")
                current = current.next

    def load_leaderboard(filename):
        leaderboard = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        if len(parts) == 2:
                            name, score = parts[0], int(parts[1])
                            leaderboard.append((name, score))
            leaderboard.sort(key=lambda x: (-x[1], x[0]))
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Starting with empty leaderboard.")
        return leaderboard

    def save_leaderboard(filename, leaderboard):
        leaderboard.sort(key=lambda x: (-x[1], x[0]))
        top5 = leaderboard[:5]
        with open(filename, 'w') as file:
            for name, score in top5:
                file.write(f"{name},{score}\n")
