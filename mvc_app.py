import sys
from PyQt5.QtWidgets import QApplication
from model.model import Model
from controllers.main_ctrl import MainController
# from project.views.main_view import MainView
from views.other_view import OtherView

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()


        self.main_view = OtherView(self.model)
        self.main_controller = MainController(self.model, self.main_view)
        self.main_view.show()  # .showFullScreen()
        self.init()

    def init(self):
        pass

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())