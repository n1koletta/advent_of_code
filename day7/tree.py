class Node():

    def __init__(self,name,parent, size =0):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
    
    def __str__(self):
        return f"{self.name}, ({self.size})"

    def __repr__(self):
        self.__str__()

    def __lt__(self,other):
        return self.size<other

    def __le__(self,other):
        return self.size <= other

    def __ge__(self,other):
        return self.size >= other

    def __add__(self,other):
        return self.size + other

    def __radd__(self,other):
        return self.size + other


class Tree():
    
    def __init__(self):
        self.root = Node('/',None)
        self.pwd = self.root
        self.dirs = []

    def add_node(self,name,size=0):
        if size == 0 : #i.e. it's a directory
            node = Node(name,self.pwd)
            self.pwd.children.append(node)
            self.dirs.append(node)
            self.pwd = node
        
        else: #it's a file
            node = Node(name,self.pwd,size)
            self.pwd.children.append(node)

    def go_up(self):
        self.pwd = self.pwd.parent

    def update_sizes(self):
        for child in self.root.children:
            self.root.size += self.update_size_children(child)

    def update_size_children(self,node):
        for child in node.children:
            node.size += self.update_size_children(child)

        return node.size