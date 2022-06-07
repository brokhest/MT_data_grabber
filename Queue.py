from multiprocessing import Lock
import json
import os
import pathlib

mutex = Lock()

directory = pathlib.Path().resolve()


class Queue:
    __file_name = "raw_data.gb"

    @staticmethod
    def add(ship):
        mutex.acquire()
        f = open(Queue.__file_name, 'a')
        f.write(json.dumps(ship) + '\n')
        f.close()
        mutex.release()

    @staticmethod
    def take():
        mutex.acquire()
        if not Queue.is_empty():
            with open(Queue.__file_name, 'r') as f:
                data = f.read().splitlines(True)
                ship = data[0]
                f.close()
            try:
                with open(Queue.__file_name, "w") as f:
                    f.writelines(data[1:])
                    f.truncate()
                    f.close()
            except FileNotFoundError:
                print('file not found')
            except OSError:
                print('osError')
            mutex.release()
            try:
                answer = json.loads(ship)
            except ValueError:
                answer = None
            return answer
        else:
            mutex.release()
            return None

    @staticmethod
    def is_empty():
        if not os.path.isfile(os.path.abspath(Queue.__file_name)):
            return True
        return os.path.getsize(os.path.abspath(Queue.__file_name)) == 0
