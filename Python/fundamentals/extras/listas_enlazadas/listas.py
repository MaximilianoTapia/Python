class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
    else:
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

LinkedList.append = append

def delete_node(self, key):
    current = self.head

    # Caso especial: si el nodo a eliminar es el nodo cabeza
    if current and current.data == key:
        self.head = current.next
        current = None
        return

    prev = None
    while current and current.data != key:
        prev = current
        current = current.next

    if current is None:
        return

    prev.next = current.next
    current = None

LinkedList.delete_node = delete_node

def insert_before(self, target, data):
    new_node = Node(data)

    if not self.head:
        self.head = new_node
        return

    if self.head.data == target:
        new_node.next = self.head
        self.head = new_node
        return

    current = self.head
    prev = None
    while current and current.data != target:
        prev = current
        current = current.next

    if current is None:
        return

    prev.next = new_node
    new_node.next = current

LinkedList.insert_before = insert_before

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Agregar un nuevo nodo al final
my_list.append(4)

# Eliminar un nodo existente
my_list.delete_node(2)

# Insertar un nodo antes de un valor dado
my_list.insert_before(3, 5)
