import sys
from broccoli.worker import BroccoliWorker

if __name__ == '__main__':
    worker = BroccoliWorker('localhost', 6379, 0, 'tasks', sys.argv[1])
    worker.run()