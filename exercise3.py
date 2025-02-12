class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_of_bst(root):
    if root is None:
        return 0  
    
    return root.key + sum_of_bst(root.left) + sum_of_bst(root.right)

def main():
    # Приклад використання:
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)

    print(sum_of_bst(root))  # Виведе: 80 (20 + 10 + 30 + 5 + 15)   

if __name__ == "__main__":
    main()