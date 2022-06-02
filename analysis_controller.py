import threading
import time
from multiprocessing import Process
from Queue import Queue
from Analyzer import Analyzer
import threading


class AnalysisController:
    __analyzers = []
    __has_scanners = True
    __in_work = False
    __processes = []
    __empty = False

    @staticmethod
    def start():
        if AnalysisController.__in_work:
            return
        AnalysisController.__in_work = True
        AnalysisController.__has_scanners = True
        analysis = Analyzer()
        AnalysisController.__analyzers.append(analysis)
        AnalysisController.__start_analysis()
        threading.Thread(target=AnalysisController.__check_file).start()
        return


    @staticmethod
    def __check_file():
        while True:
            if Queue.is_empty() and not AnalysisController.__has_scanners:
                AnalysisController.__stop_analysis()
                AnalysisController.__in_work = False
                return
            time.sleep(20)

    @staticmethod
    def __start_analysis():
        for analysis in AnalysisController.__analyzers:
            p = Process(target=analysis.start)
            p.start()
            AnalysisController.__processes.append(p)
            # threading.Thread(target=analysis.start).start()
        return

    @staticmethod
    def __stop_analysis():
        for analysis in AnalysisController.__analyzers:
            analysis.stop()
        for process in AnalysisController.__processes:
            process.terminate()
        return

    @staticmethod
    def notify():
        AnalysisController.__has_scanners = False


