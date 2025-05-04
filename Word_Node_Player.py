class Word:
    def __init__(self, word, difficulty, hint):
        self.word = word
        self.difficulty = difficulty
        self.hint = hint

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0