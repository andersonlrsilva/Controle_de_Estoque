from PySide6.QtWidgets import QApplication, QWidget
from ui.login import Ui_login


class Login(QWidget, Ui_login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("logon no sistema")
        self.adjustSize()
        self.setFixedSize(300, 400)

    # BOTÕES DO SISTEMA
        self.btnEntrar.clicked.connect(self.login)
        self.btnSair.clicked.connect(self.exit)

    # FUNÇÕES DO SISTEMA
    # sair do login
    def exit(self):
        exit()

    # login no sistema
    def login(self):
        print('loguei!')


if __name__ == "__main__":
    app = QApplication()
    window = Login()
    window.show()
    app.exec()
