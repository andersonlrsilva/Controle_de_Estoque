from classes.message import msgInitTest
from classes.database import Database
from ui.mainwindow import Ui_MainWindow
import login
from PySide6.QtWidgets import QApplication, QMainWindow


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

# AJUSTES DO MENU
        # ITENS DESABILITADOS
        self.menuEstoque.setDisabled(True)
        self.menuClientes.setDisabled(True)
        self.menuVendas.setDisabled(True)
        self.menuFinanceiro.setDisabled(True)
        self.menuRH.setDisabled(True)
        # self.menuconfigura_o.setDisabled(True)
        self.menuajuda.setDisabled(True)

# MENU
# MENU SISTEMA
        self.action_exitSystem.triggered.connect(self.exitsystem)
# MENU CONFIGURAÇÃO > DATABASE > RECRIA DATABASE
# MENU UPDATE >

# FUNÇÕES DO SISTEMA
    # sair do sistema
    def exitsystem(self):
        for widget in QApplication.allWidgets():
            widget.close()
        # exit()
    # INICIA O PROGRAMA


if __name__ == "__main__":
    db = Database()
    test = db.connect()
    if test is False:
        msgInitTest()
        main = MainWindow('sair')
        main.exitsystem()

    app = QApplication()
    window = login.Login()
    window.show()
    app.exec()
