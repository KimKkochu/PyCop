from Lexer import lexer

class Node:
    def __init__(self, item) -> None:
        self.data = item
        self.left = None
        self.right = None
