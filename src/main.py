from PySide6.QtWidgets import QApplication, QMainWindow
import login
from ui.mainwindow import Ui_MainWindow
from classes.database import Database
from classes.message import msgInitTest


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.username = user[2]
        self.usernivel = user[3]
        self.userId = user[1]
        self.setWindowTitle(
            f'Usuário: {self.username}    ID: {self.userId}'
            f'   Nivel:{self.usernivel}')


if __name__ == "__main__":

    db = Database()
    test = db.connect()
    if test is False:
        msgInitTest()
        exit()

    app = QApplication()
    window = login.Login()
    window.show()
    app.exec()
