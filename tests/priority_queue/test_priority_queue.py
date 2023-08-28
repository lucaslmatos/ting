from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    items = [{"nome_do_arquivo": "item_1.txt",
              "qtd_linhas": 8},
             {"nome_do_arquivo": "item_2.txt",
              "qtd_linhas": 2}]

    for item in items:
        queue.enqueue(item)

    assert len(queue) == 2

    assert queue.search(0) == items[1]
    assert queue.search(1) == items[0]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(4)

    assert queue.dequeue() == items[1]
    assert queue.dequeue() == items[0]
