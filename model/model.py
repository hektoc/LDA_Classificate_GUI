import os

from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):

    # signals to view (in __init__)
    class_added = pyqtSignal(dict)
    input_file_changed = pyqtSignal(str)

    # base_path
    @property
    def base_path(self):
        return self._base_path

    @property
    def curpath(self):
        return self._curpath

    @curpath.setter
    def curpath(self, value):
        print('curpath.setter', value)
        self._curpath = value

    @property
    def input_file(self):
        print('MODEL: input_file, self._input_file=', self._input_file)
        return self._input_file

    @input_file.setter
    def input_file(self, value):
        self._input_file = value
        print('MODEL: input_file.setter, _input_file = ', value)
        self.curpath = os.path.dirname(os.path.realpath(value))
        self.input_file_changed.emit(value)

    @property
    def lda_lern_classes(self):
        return self._lda_lern_classes

    def add_lda_lern_class(self, lda_lern_class):
            self._lda_lern_classes.append(lda_lern_class)
            print('MODEL: add_lda_lern_class,  = _lda_lern_classes append', lda_lern_class)
            info2view = {"name": lda_lern_class, 'path':  lda_lern_class}
            self.curpath = os.path.dirname(os.path.realpath(lda_lern_class))
            self.class_added.emit(info2view)

    '''@property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_changed.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)'''

    def __init__(self):
        super().__init__()

        # self._amount = 0
        # self._even_odd = ''
        self._input_file = ''
        # self._enable_reset = False
        self._lda_lern_classes = []
        self._base_path = os.path.dirname(os.path.realpath(__file__) + '/project_new/without_flaash')
        self._curpath = self._base_path
