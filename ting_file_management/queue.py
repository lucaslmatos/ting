from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, value):
        self.queue.append(value)
        self._size += 1

    def dequeue(self):
        if self._size > 0:
            returned = self.queue[0]
            self.queue = self.queue[1:]
            self._size -= 1
            return returned
        else:
            return None

    def search(self, index):
        if index >= 0 and index < self._size:
            return self.queue[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
