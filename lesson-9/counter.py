from time import time
import threading

N = 2 * 100_000_000

def coundown(n):
    while n > 0:
        n -= 1


def run():
    t1 = time()
    coundown(N)
    t2 = time()
    print("single", t2 - t1)  # 10

    t1 = time()
    n_threads = 8
    threads = [
        threading.Thread(target=coundown, args=(N // n_threads,))
        for _ in range(n_threads)
    ]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    t2 = time()
    print('threads', t2 - t1)


if __name__ == '__main__':
    run()
