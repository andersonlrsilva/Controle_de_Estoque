from PySide6.QtWidgets import QWidget, QApplication
from ui.addFabric import Ui_AddFabricante


class UiFabricante(QWidget, Ui_AddFabricante):
    def __init__(self, parent=None):
        super(UiFabricante, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Adicionar fabricante")


# BOTÕES DO SISTEMA
        self.btnSalvar.clicked.connect(self.salvar)
        self.btnCancelar.clicked.connect(self.sair)


# FUNÇÕES DO SISTEMA


    def salvar(self):
        ...

    def sair(self):
        self.close()


if __name__ == '__main__':
    app = QApplication()
    window = UiFabricante()
    window.show()
    app.setStyle('Fusion')
    app.exec()
