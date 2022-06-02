import threading
import time
from DataGrabber import DataGrabber
from multiprocessing import Process
from Queue import Queue
from Analyzer import Analyzer
from DBHook import DBHook
from analysis_controller import AnalysisController

if __name__ == "__main__":
    page = {
        "x": 131.872,
        "y": 43.133,
        "z": 12
    }
    blocks = []
    text = {
        "x": 1773,
        "y": 751,
        "z": 12
    }
    blocks.append(text)
    text = {
        "x": 1774,
        "y": 751,
        "z": 12
    }
    blocks.append(text)
    DataGrabber.start_scan(page, blocks)
   #  # print(DataGrabber.get())
   #  #ship = Queue.take()
   #  #a = Analyzer()
   #  #ship = a.start()
   #  #print(ship)
   #  #DBHook.add(ship)
   # # print(DBHook.get(1))
   #
    time.sleep(60)
    print("stopping")
    DataGrabber.stop_scan(0)
   #  #print(Queue.is_empty())
   #  AnalysisController.start()
   #  AnalysisController.notify()




