# Emojilang parser
from sys import argv

class ASTNode:
    def __init__(self, children) -> None:
        self.children = children
    
    def get(self, idx): 
        return self.children[idx]



class AST:
    def __init__(self, root: ASTNode) -> None:
        self.root = root


path = argv[0]

with open(path, "r") as file:
    lines = file.readlines()
    