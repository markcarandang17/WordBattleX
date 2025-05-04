import random
from Word_Node_Player import Node

class WordList:
    def __init__(self):
        self.head = None

    def add_word(self, word):
        new_node = Node(word)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_word(self, target_word):
        current = self.head
        prev = None
        while current:
            if current.data.word == target_word:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search_word(self, target_word):
        current = self.head
        while current:
            if current.data.word == target_word:
                return True
            current = current.next
        return False

    def get_random_word(self, difficulty):
        candidates = []
        current = self.head
        while current:
            if current.data.difficulty == difficulty:
                candidates.append(current.data)
            current = current.next
        return random.choice(candidates) if candidates else None