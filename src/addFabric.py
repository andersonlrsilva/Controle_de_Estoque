from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget, QApplication
from libAction import prod
from ui.addFabric import Ui_AddFabricante
from libAction import libAddFabric
from classes.message import msgGeneric


class UiFabricante(QWidget, Ui_AddFabricante):
    def __init__(self, parent=None):
        super(UiFabricante, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Adicionar fabricante")


# BOTÕES DO SISTEMA
        self.btnSalvar.clicked.connect(self.salvar)
        self.btnCancelar.clicked.connect(self.sair)

# AJUSTES DO SISTEMA
        self.cmbEstado.setCurrentIndex(-1)

# FUNÇÕES DO SISTEMA
    def limpaform(self):
        self.txtFabricante.clear()
        self.txtCnpj.clear()
        self.txtEmail.clear()
        self.txtTelCtt.clear()
        self.txtTelCtt_2.clear()
        self.txtSite.clear()
        self.txtRua.clear()
        self.txtNumero.clear()
        self.cmbEstado.setCurrentIndex(-1)
        self.txtCep.clear()
        self.txtBairro.clear()

    def salvar(self):
        nomeFabric = libAddFabric.nomeFabric(self.txtFabricante.text())
        if nomeFabric is None:
            return

        cnpjFabric = libAddFabric.cnpjFabric(self.txtCnpj.text())
        if cnpjFabric is None:
            return

        emailFabric = libAddFabric.emailFabric(self.txtEmail.text())
        if emailFabric is None:
            return

        telefone = libAddFabric.telefoneFabric(self.txtTelCtt.text())
        if telefone is None:
            return

        site = libAddFabric.siteFabric(self.txtSite.text())
        if site is None:
            return

        rua = libAddFabric.ruaFabric(self.txtRua.text())
        if rua is None:
            return

        numero = libAddFabric.numeroFabric(self.txtNumero.text())
        if numero is None:
            return

        estado = libAddFabric.estadoFabric(self.cmbEstado.currentText())
        if estado is None:
            return

        cep = libAddFabric.cepFabric(self.txtCep.text())
        if cep is None:
            return

        bairro = libAddFabric.bairroFabric(self.txtBairro.text())
        if bairro is None:
            return

        frete = self.chboxFrete.isChecked()
        telefone2 = self.txtTelCtt_2.text()
        selfFornec = self.chboxselfFrabric.isChecked()

        insert = libAddFabric.gravaFabricante(
            nome=nomeFabric, cnpj=cnpjFabric,
            email=emailFabric, telefone=telefone,
            telefone2=telefone2, site=site,
            rua=rua, numero=numero, estado=estado, cep=cep, bairro=bairro,
            frete=frete, fornec=selfFornec)

        if insert[0] is None:  # type:ignore
            text = (f'Não foi possível gravar os dados do fabricante'
                    f'{nomeFabric}.\n'
                    f'Nenhuma alteração foi feita no banco de dados ou '
                    f'cadastro do fabricante.\n'
                    f'Caso o problema persista, entre em contato com'
                    f'o suporte técnico')
            title = 'Erro ao salvar alterações'
            msgGeneric(text=text, title=title)
            return

        if insert[0] is True:  # type:ignore
            text = f'Fabricante {insert[1]} inserido com sucesso'
            msgGeneric(title='Cadastro com Sucesso', text=text)
            # self.limpaForm()

    def sair(self):  # type: ignore
        self.close()


if __name__ == '__main__':
    app = QApplication()
    window = UiFabricante()
    window.show()
    app.setStyle('Fusion')
    app.exec()
