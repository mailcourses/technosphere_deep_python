from time import time
import threading
import requests


def make_requests(urls):
    for url in urls:
        resp = requests.get(url)


def run():
    urls = ['https://python.org', 'https://mail.ru'] * 10
    half_urls = ['https://python.org', 'https://mail.ru'] * 1

    t1 = time()
    make_requests(urls)
    t2 = time()
    print("single", t2 - t1)  # 10

    t1 = time()
    n_threads = 10
    threads = [
        threading.Thread(target=make_requests, args=(half_urls,))
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
