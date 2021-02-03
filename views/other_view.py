from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QAction, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal
# from project_new.views.other_view_ui import Ui_OtherWindow
from views.other_view_ui import Ui_OtherWindow

class OtherView(QMainWindow):

    # signals to controller
    input_file_signal = pyqtSignal(str)
    add_class_signal = pyqtSignal(str)
    run_main_task_signal = pyqtSignal(bool)

    def __init__(self, model):
        super().__init__()

        self._model = model
        self._ui = Ui_OtherWindow()
        self._ui.setupUi(self)

        # listen for model event signals
        self._model.input_file_changed.connect(self.on_model_input_file_changed)
        self._model.class_added.connect(self.on_model_class_add)

        # connect menu form ui to view
        # menu
        self._ui.open_input_file.triggered.connect(self.change_input_file_click)
        self._ui.add_class_dir.triggered.connect(self.add_class_click)
        self._ui.run_main_task.triggered.connect(self.run_main_task_click)


    # from model
    @pyqtSlot(str)
    def on_model_input_file_changed(self, value):
        print('VIEW: модель обновилась, on_input_file_changed, value=', value)
        self._print2ststusbar('VIEW: модель обновилась, on_input_file_changed, value=' + value)
        # self.addClass(value)

    @pyqtSlot(dict)
    def on_model_class_add(self, lda_class: dict):
        print('VIEW: on_model_class_add, модель обновилась, on_class_add, value=', lda_class)
        self._print2ststusbar('VIEW: модель обновилась, on_class_add, value=' + lda_class['path'])
        self._add_class(lda_class['path'])

    # from view to controller
    @pyqtSlot(bool)
    def change_input_file_click(self):
        file_name = self._show_input_file_dialog()[0]
        print('VIEW: change_input_file_click, file_name', file_name)
        self._print2ststusbar('VIEW: change_input_file_click, file_name = ' + file_name)

        if file_name is not None:
            self.input_file_signal.emit(file_name)

    @pyqtSlot(bool)
    def add_class_click(self):
        dir_name = self._show_input_dir_dialog()
        print('VIEW: add_class_click, dir_name', dir_name)
        self._print2ststusbar('VIEW: add_class_click, dir_name = ' + str(dir_name))
        if dir_name is not None:
            self.add_class_signal.emit(dir_name)

    @pyqtSlot(bool)
    def run_main_task_click(self):
        print('VIEW: run_main_task_click ')
        self._print2ststusbar('VIEW: run_main_task_click')
        self.run_main_task_signal.emit(True)

    # View func
    def _add_class(self, value):
        name = str(value).split('/')[-1]
        tmp_verticalLayout_3 = QtWidgets.QVBoxLayout()
        tmp_verticalLayout_3.setSpacing(5)
        tmp_verticalLayout_3.setObjectName('class_' + name)
        tmp_label = QtWidgets.QLabel(self._ui.left)
        tmp_label.setObjectName("label")
        tmp_label.setText(str(value))
        tmp_verticalLayout_3.addWidget(tmp_label)

        tmp_lineEdit = QtWidgets.QLineEdit(self._ui.left)
        tmp_lineEdit.setObjectName("lineEdit")
        tmp_lineEdit.setText(name)
        tmp_verticalLayout_3.addWidget(tmp_lineEdit, 0, QtCore.Qt.AlignTop)


        tmp_horizontalLayout_buttons = QtWidgets.QVBoxLayout()
        tmp_horizontalLayout_buttons.setSpacing(1)
        tmp_horizontalLayout_buttons.setObjectName('buttons_' + name)
        tmp_horizontalLayout_buttons.setStretch(1, 1)

        tmp_pushButton_rename = QtWidgets.QPushButton(self._ui.left)
        tmp_pushButton_rename.setObjectName("pushButton_rename_" + name)
        tmp_pushButton_rename.setText("Переименовать")
        tmp_pushButton_delete = QtWidgets.QPushButton(self._ui.left)
        tmp_pushButton_delete.setObjectName("pushButton_delete_" + name)
        tmp_pushButton_delete.setText("Удалить")

        tmp_horizontalLayout_buttons.addWidget(tmp_pushButton_rename, 1, QtCore.Qt.AlignBaseline)
        tmp_horizontalLayout_buttons.addWidget(tmp_pushButton_delete, 1, alignment=QtCore.Qt.AlignBaseline)
        tmp_verticalLayout_3.addLayout(tmp_horizontalLayout_buttons)

        # tmp_verticalLayout_3.setStretch(5, 1)
        self._ui.class_verticalLayout.addLayout(tmp_verticalLayout_3)
            # QFileDialog.getO  .getOpenFileName(self, 'Open file', '/home')[0]

    def _show_input_dir_dialog(self):
        return QFileDialog.getExistingDirectory(self, 'Выберите директорию', self._model.curpath)

    def _show_input_file_dialog(self):
        return QFileDialog.getOpenFileName(self, 'Виберите файл', self._model.curpath)

    @pyqtSlot(str)
    def print2ststusbar(self, msg):
        self._print2ststusbar(msg)

    def _print2ststusbar(self, msg):
        self._ui.statusbar.showMessage(str(msg))

    @pyqtSlot(str)
    def redraw_image(self, done):
        if done:
            self.draw_image(done)

    def draw_image(self, src):
        self._ui.lb.setPixmap(QPixmap(src))
        pass



