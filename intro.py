class BracketMapper:
    def __init__(self):
        self.brackets = {')': '(', '}': '{', ']': '['}

    def is_match(self, open_bracket, close_bracket):
        return self.brackets.get(close_bracket) == open_bracket
        
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
