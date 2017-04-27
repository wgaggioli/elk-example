import argparse
import time
from threading import Thread

import requests


class RequestThread(Thread):
    def __init__(self, url):
        self.url = url
        super(RequestThread, self).__init__(target=self.make_request)

    def make_request(self):
        requests.get(self.url)


class Worker(object):
    def __init__(self):
        self.thread = None

    @property
    def busy(self):
        if self.thread and not self.thread.is_alive():
            self.thread = None
        return self.thread is not None

    def run_thread(self, thread):
        self.thread = thread
        self.thread.start()

    def join(self):
        self.thread.join()


class WorkerGroup(object):
    def __init__(self, num_workers):
        self.workers = [self._generate_worker() for i in range(num_workers)]

    def get_available_worker(self):
        for worker in self.workers:
            if not worker.busy:
                return worker
        time.sleep(0.5)
        return self.get_available_worker()

    def _generate_worker(self):
        return Worker()


if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('url')
     parser.add_argument('workers', type=int)
     parser.add_argument('total_requests', type=int)

     args = parser.parse_args()
     threads = [RequestThread(args.url) for i in range(args.total_requests)]
     worker_group = WorkerGroup(args.workers)

     while threads:
         worker = worker_group.get_available_worker()
         worker.run_thread(threads.pop())

     for worker in worker_group.workers:
         worker.join()
