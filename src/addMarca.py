from PySide6.QtWidgets import QApplication, QWidget
from ui.addmarca import Ui_AddMarca
from classes.database import Database


class Addmarca(QWidget, Ui_AddMarca):
    def __init__(self):
        super(Addmarca, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Cadastro de Produtos')


# BOTOES DO SISTEMA
        self.btnCancelar.clicked.connect(self.sair)
        self.btnSalvar.clicked.connect(self.gravadb)
# FUNÇÕES DO SISTEMA
    # SAIR DO SISTEMA

    def sair(self):
        self.close()

    # GRAVAR DADOS NO DB
    def gravadb(self):
        marca = self.txtMarca.text()
        site = self.txtSite.text()
        db = Database()
        grava = db.inserirMarca(site=site, marca=marca)
        if grava == True:
            print('ok')
        else:
            print('erro')


        # INICIA APP
if __name__ == '__main__':
    app = QApplication()
    app.setStyle("Fusion")
    window = Addmarca()
    window.show()
    app.exec()
