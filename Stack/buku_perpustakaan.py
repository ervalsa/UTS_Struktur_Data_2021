class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items


stack = Stack()
stack.push("Kalkulus 1")
stack.push("Kalkulus 2")
stack.push("Computer Science an Overview 12th Edition")
stack.push("Fisika Dasar 1")
stack.push("Computer Organization and Architecture 10th Edition")
print("Rak Buku :", stack.get_stack())
print("\nBuku yang diambil:", stack.pop())
print("\nSisa Buku di rak:", stack.get_stack())