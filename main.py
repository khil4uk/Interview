class Stack:
    def __init__(self):
        self.stack_list = []

    def isEmpty(self):
        "isEmpty - проверка стека на пустоту. Метод возвращает True или False."
        return bool(self.stack_list)

    def push(self, item):
        "push - добавляет новый элемент на вершину стека. Метод ничего не возвращает."
        self.stack_list.append(item)

    def pop(self):
        "pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека."
        return self.stack_list.pop()

    def peek(self):
        "peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется."
        return self.stack_list[-1]

    def size(self):
        "size - возвращает количество элементов в стеке."
        return len(self.stack_list)


def balance(string_):
    """Метод проверки сбалансированности скобок"""
    balansed = True
    stack = Stack()
    for i in string_:
        if i in '({[':
            stack.push(i)
        else:
            if not stack.isEmpty():
                balansed = False
                break
            elif stack.peek() == '(' and i == ')':
                stack.pop()
                continue
            elif stack.peek() == '{' and i == '}':
                stack.pop()
                continue
            elif stack.peek() == '[' and i == ']':
                stack.pop()
                continue
            else:
                balansed = False
                break
    if balansed == True:
        return 'Сбалансировано'
    else:
        return 'Несбалансировано'

if __name__ == '__main__':
    print(balance('{{[()]}}'))
