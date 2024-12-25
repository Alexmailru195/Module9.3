class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node

    def remove_from_head(self):
        if self.head is None:
            return "Список пуст"
        removed_node = self.head
        self.head = self.head.next_node
        if self.head:
            self.head.prev_node = None
        else:
            self.tail = None
        return f"Удалены данные {removed_node.data} из головы списка."

    def remove_from_tail(self):
        if self.tail is None:
            return "Список пуст"
        removed_node = self.tail
        self.tail = self.tail.prev_node
        if self.tail:
            self.tail.next_node = None
        else:
            self.head = None
        return f"Удалены данные {removed_node.data} из хвоста списка."

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_head(data)
            return
        current_node = self.head
        for _ in range(index - 1):
            if current_node is None:
                break
            current_node = current_node.next_node
        if current_node is None:
            self.insert_at_tail(data)
        else:
            new_node = Node(data, current_node.next_node, current_node)
            if current_node.next_node:
                current_node.next_node.prev_node = new_node
            current_node.next_node = new_node

    def remove_node_index(self, index):
        if index < 0:
            return "Индекс не может быть отрицательным."
        if index == 0:
            return self.remove_from_head()
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                return "Индекс вне диапазона."
            current_node = current_node.next_node
        if current_node is None:
            return "Индекс вне диапазона."
        if current_node.prev_node:
            current_node.prev_node.next_node = current_node.next_node
        if current_node.next_node:
            current_node.next_node.prev_node = current_node.prev_node
        if current_node == self.tail:  # Если это был хвост
            self.tail = current_node.prev_node
        return f"Удалены данные {current_node.data} по индексу {index}."

    def remove_node_data(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev_node:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node.prev_node
                if current_node == self.head:  # Если это был голова
                    self.head = current_node.next_node
                if current_node == self.tail:  # Если это был хвост
                    self.tail = current_node.prev_node
                return f"Удалены данные {data}."
            current_node = current_node.next_node
        return f"Данные {data} не найдены."

    def len_ll(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, from_tail=False):
        if from_tail:
            return self.contains_from_tail(data)
        else:
            return self.contains_from_head(data)


# Пример использования
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_index(1, 1.5)

    print("Список с начала:")
    ll.print_ll_from_head()

    print("Список с конца:")
    ll.print_ll_from_tail()

    print(ll.remove_node_data(2))
    print("Список после удаления 2:")
    ll.print_ll_from_head()

    print(ll.len_ll())
    print(ll.contains_from(1, from_tail=False))
