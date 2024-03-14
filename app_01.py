"""
� Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.
"""

import threading
import time
import random


def worker(arr):
    print(sum(arr))


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    arr = []
    for _ in range(0, 1000000):
        arr.append(random.randint(0, 100))

    t = threading.Thread(target=worker, args=(arr,))
    threads.append(t)
    t.start()

    for t in threads:
        t.join()
    print(f'Время выполнения {time.time() - start_time:.2f} сек')
