from Scanner import Scanner
from analysis_controller import AnalysisController
from multiprocessing import Process
from Calculator import CoordinatesCalculator


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
    def start_scan(coordinates):
        coordinates = CoordinatesCalculator.calculate(coordinates)
        new_scan = Scanner(coordinates['page'], coordinates['blocks'])
        p = Process(target=new_scan.start)
        p.start()
        # threading.Thread(target=new_scan.start).start()
        DataGrabber.__scans.append(new_scan)
        DataGrabber.__processes.append(p)
        AnalysisController.notify_started()
        AnalysisController.start()
        return

    @staticmethod
    def stop_scan(id):
        DataGrabber.__scans[id].stop()
        DataGrabber.__processes[id].terminate()
        del DataGrabber.__scans[id]
        del DataGrabber.__processes[id]
        if len(DataGrabber.__scans) == 0:
            AnalysisController.notify_ended()

