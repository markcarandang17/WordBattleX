from File_Manager import FileManager
import random

class GameEngine:
    def __init__(self, player, word_list, difficulty):
        self.player = player
        self.word_list = word_list
        self.difficulty = difficulty
        self.rounds = 3

    def start_game(self):
        for _ in range(self.rounds):
            word_obj = self.word_list.get_random_word(self.difficulty)
            if not word_obj:
                print("No words available for this difficulty. Game ends early.")
                break
            base_points = {'Easy': 10, 'Medium': 20, 'Hard': 30}.get(self.difficulty, 0)
            if self.difficulty == 'Easy':
                scrambled = self.generate_scrambled_word(word_obj.word)
                print(f"Complete the word: {scrambled}")
            elif self.difficulty == 'Medium':
                print(f"Unscramble the word: {word_obj.hint}")
            else:
                print(f"Definition: {word_obj.hint}")

            attempts = 0
            max_attempts = 3
            correct = False
            while attempts < max_attempts and not correct:
                user_input = input("Enter your answer: ").strip().lower()
                if user_input == word_obj.word.lower():
                    correct = True
                    points = base_points - (attempts * 2)
                    points = max(points, 0)
                    self.player.score += points
                    print(f"Correct! +{points} points.")
                else:
                    print("Incorrect. Try again.")
                    attempts += 1
            if not correct:
                print(f"The correct answer was: {word_obj.word}")

        print(f"Game Over, {self.player.name}! Final Score: {self.player.score}")
        leaderboard = FileManager.load_leaderboard('leaderboard.txt')
        leaderboard.append((self.player.name, self.player.score))
        FileManager.save_leaderboard('leaderboard.txt', leaderboard)

    def generate_scrambled_word(self, word):
        if len(word) <= 1:
            return word
        replace_count = min(2, len(word) - 1)
        indices = random.sample(range(len(word)), replace_count)
        scrambled = list(word)
        for i in indices:
            scrambled[i] = '_'
        return ''.join(scrambled)