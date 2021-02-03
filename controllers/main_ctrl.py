import os
import time

from PyQt5.QtCore import QObject, pyqtSlot, QThreadPool

from controllers.tripplesat_task import tripplesat_task
from worker.worker import *

class MainController(QObject):

    status_signal = pyqtSignal(str)
    complete_signal = pyqtSignal(str)
    img_preview_signal = pyqtSignal(str)

    def __init__(self, model, main_view):
        super().__init__()
        self.base_path = os.path.dirname(os.path.realpath(__file__))

        self._view = main_view
        self._model = model
        self.threadpool = QThreadPool()

        # from Controller to View
        self.status_signal.connect(self._view.print2ststusbar)
        self.complete_signal.connect(self._view.redraw_image)
        self.img_preview_signal.connect(self._view.redraw_image)

        # from View to Controller
        self._view.input_file_signal.connect(self.change_input_file)
        self._view.run_main_task_signal.connect(self.run_main_task)
        self._view.add_class_signal.connect(self.add_class)

    @pyqtSlot(str)
    def change_input_file(self, value):
        print('CONTROLLER: change_input_file value=', value)
        self._model.input_file = value

    @pyqtSlot(str)
    def add_class(self, value):
        print('CONTROLLER: add_class value=', value)
        self._model.add_lda_lern_class(value)

    @pyqtSlot(bool)
    def run_main_task(self):
        self.oh_no()

    def execute_this_fn(self, progress_callback, status_callback, redraw_img):
        '''for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n*100/4)'''
        a = tripplesat_task(progress_callback, status_callback, redraw_img, self._model)
        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")
        self.complete_signal.emit('./new_img.png')


    def oh_no(self):
        # Pass the function to execute
        worker = Worker(self.execute_this_fn)  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)

        worker.signals.status.connect(self.status_signal)
        worker.signals.redraw_img.connect(self.img_preview_signal)

        # Execute
        self.threadpool.start(worker)

    '''@pyqtSlot(int)
    def change_amount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.even_odd = 'odd' if value % 2 else 'even'

        # calculate button enabled state
        self._model.enable_reset = True if value else False


'''
