class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min_in_bst(root):
    if root is None:
        return None  
    
    current = root
    while current.left is not None:  
        current = current.left
    return current.key  

def main():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)

    print(find_min_in_bst(root))  # Виведе: 5   

if __name__ == "__main__":
    main()