class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return "Node: value " + str(self.value) 
    
class Tree:
    def __init__(self):
        self.root = None

    def add(self, pair):
        if self.root is None:
            self.root = Node(pair)
        else:
            parent = None
            whomst = None
            node = self.root
            while node is not None:
                parent = node
                if node.value[1] < pair[1]:
                    node = node.left
                    whomst = "left"
                elif node.value[1] >= pair[1]:
                    node = node.right
                    whomst = "right"
            if whomst == "left":
                parent.left = Node(pair)
            else:
                parent.right = Node(pair)
    
    def search(self, tok):
        if self.root is None:
            return None
        
        node = self.root
        while node is not None:
            if node.value[1] == tok:
                return node.value[0]
            elif node.value[1] < tok:
                node = node.left
            else:
                node = node.right
        return None

    def prettifyTree(self, node):
        string = ""
        if node!=None:
            string += str(node) + ': ' + 'left: ' + str(node.left) + ' ' + 'right: ' + str(node.right) + ' ' + '\n' + self.prettifyTree(node.left) + self.prettifyTree(node.right)
        return string

    def __str__(self):
        return self.prettifyTree(self.root)


class SymbolTable:
    def __init__(self):
        self.tree = Tree()
        self.lastID = 1

    def add(self, identifier):
        self.tree.add((self.lastID, str(identifier)))
        self.lastID += 1

    def search(self, identifier):
        return self.tree.search(str(identifier))

    def __str__(self):
        return str(self.tree)
'''
Tests

symTable = SymbolTable()
symTable.add("a")
symTable.add("b")
symTable.add(2)
print(symTable.search("a"))
print(symTable.search("b"))
print(symTable.search("c"))
print(symTable.search(2))
'''