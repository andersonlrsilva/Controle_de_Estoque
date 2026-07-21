# from classes.message import msgInitTest
# from classes.database import Database
from ui.mainwindow import Ui_MainWindow
# import login
from PySide6.QtWidgets import QApplication, QMainWindow
import update


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
        self.menuClientes.setDisabled(True)
        self.menuVendas.setDisabled(True)
        self.menuFinanceiro.setDisabled(True)
        self.menuRH.setDisabled(True)
        self.menuajuda.setDisabled(True)

# MENU
# MENU SISTEMA >
        # Sair do sistema
        self.actionExitSystem.triggered.connect(self.exitsystem)
# MENU CADASTROS >
        # Cadasto de Fornecedores
        self.actionFronecedores.triggered.connect(self.cadFornecedor)
        # Cadastro de Fabricantes
        self.actionFabricantes.triggered.connect(self.cadFabricante)
        # Cadastro de Clientes
        self.actionClientes.triggered.connect(self.cadCliente)
# MENU ESTOQUE >
        # Cadastro de produtos
        self.actionCadProdutos.triggered.connect(self.cadprod)
# MENU ATUALIZAÇÃO >
        # Busca Atualização
        self.actionBuscarAtualizacao.triggered.connect(self.buscaAtualizacao)

# FUNÇÕES DO SISTEMA

    # CADASTRO DE CLIENTES

    def cadCliente(self):
        import addCliente
        self.cadcliente = addCliente.Uiaddcliente()
        self.cadcliente.show()

    # CADASTRO DE FORNECEDORES
    def cadFabricante(self):
        import addFabric
        self.cadfabr = addFabric.UiFabricante()
        self.cadfabr.show()

    # CADASTRO DE FORNECEDORES
    def cadFornecedor(self):
        import addFornecedor
        self.cadFor = addFornecedor.UiFornecedor()
        self.cadFor.show()

    # CADASTRO DE PRODUTOS
    def cadprod(self):
        import addProd
        self.cad = addProd.UiaddProd()
        self.cad.show()
        self.cad.atualizaComboBox()

    # SAIR DO SISTEMA
    def exitsystem(self):
        for widget in QApplication.allWidgets():
            widget.close()
            exit()

    def buscaAtualizacao(self):
        self.w = update.Update()
        self.w.show()

    # INICIA O PROGRAMA
if __name__ == "__main__":
    # db = Database()
    # test = db.connect()
    # if test is False:
    #     msgInitTest()
    #     main = MainWindow('sair')
    #     main.exitsystem()

    # app = QApplication()
    # window = login.Login()
    # window.show()
    # app.exec()

    app = QApplication()
    window = MainWindow('anderson')
    app.setStyle("fusion")
    window.show()
    app.exec()
