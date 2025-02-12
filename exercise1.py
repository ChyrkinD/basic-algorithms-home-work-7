class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_in_bst(root):
    if root is None:
        return None  
    
    current = root
    while current.right is not None:  
        current = current.right
    return current.key  

def main():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.right.right = Node(40)

    print(find_max_in_bst(root))  # Виведе: 40

if __name__ == "__main__":
    main()