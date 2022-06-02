from Scanner import Scanner
import threading
from analysis_controller import AnalysisController
from multiprocessing import Process


class DataGrabber:
    __scans = []
    __processes = []

    @staticmethod
    def get():
        response = []
        for scan in DataGrabber.__scans:
            entry = scan.get()
            entry.update({"id": DataGrabber.__scans.index(scan)})
            response.append(entry)
        return response

    @staticmethod
    def start_scan(page, blocks):
        new_scan = Scanner(page, blocks)
        p = Process(target=new_scan.start)
        p.start()
        # threading.Thread(target=new_scan.start).start()
        DataGrabber.__scans.append(new_scan)
        DataGrabber.__processes.append(p)
        AnalysisController.start()
        return

    @staticmethod
    def stop_scan(id):
        DataGrabber.__scans[id].stop()
        DataGrabber.__processes[id].terminate()
        del DataGrabber.__scans[id]
        if len(DataGrabber.__scans) == 0:
            AnalysisController.notify()
