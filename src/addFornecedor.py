from PySide6.QtWidgets import QWidget, QApplication
from ui.addFornecedor import Ui_Fornecedor
from libAction import libAddFornec
from classes.message import msgGeneric


class Fornecedor(QWidget, Ui_Fornecedor):
    def __init__(self, parent=None):
        super(Fornecedor, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Adicionar fornecedor")


# BOTÕES DO SISTEMA
        self.btnSalvar.clicked.connect(self.salvar)
        self.btnCancelar.clicked.connect(self.sair)

# AJUSTES DO SISTEMA


# FUNÇÕES DO SISTEMA+

    def limpaform(self):
        self.txtFornecedor.clear()
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

    def sair(self):  # type: ignore
        self.close()

    def salvar(self):
        nomeFornec = libAddFornec.nomeFornec(self.txtFornecedor.text())
        if nomeFornec is None:
            return

        cnpjFornec = libAddFornec.cnpjFornec(self.txtCnpj.text())
        if cnpjFornec is None:
            return

        emailFornec = libAddFornec.emailFornec(self.txtEmail.text())
        if emailFornec is None:
            return

        telefone = libAddFornec.telefoneFornec(self.txtTelCtt.text())
        if telefone is None:
            return

        site = libAddFornec.siteFornec(self.txtSite.text())
        if site is None:
            return

        rua = libAddFornec.ruaFornec(self.txtRua.text())
        if rua is None:
            return

        numero = libAddFornec.numeroFornec(self.txtNumero.text())
        if numero is None:
            return

        estado = libAddFornec.estadoFornec(self.cmbEstado.currentText())
        if estado is None:
            return

        cep = libAddFornec.cepFornec(self.txtCep.text())
        if cep is None:
            return

        bairro = libAddFornec.bairroFornec(self.txtBairro.text())
        if bairro is None:
            return

        frete = self.chboxFrete.isChecked()
        telefone2 = self.txtTelCtt_2.text()

        insert = libAddFornec.gravaFornecedor(
            nome=nomeFornec, cnpj=cnpjFornec,
            email=emailFornec, telefone=telefone,
            telefone2=telefone2, site=site,
            rua=rua, numero=numero, estado=estado, cep=cep, bairro=bairro,
            frete=frete)

        if insert[0] is None:  # type:ignore
            text = (f'Não foi possível gravar os dados do fabricante'
                    f'{nomeFornec}.\n'
                    f'Nenhuma alteração foi feita no banco de dados ou '
                    f'cadastro do fabricante.\n'
                    f'Caso o problema persista, entre em contato com'
                    f'o suporte técnico')
            title = 'Erro ao salvar alterações'
            msgGeneric(text=text, title=title)
            return

        if insert[0] is True:  # type:ignore
            text = f'Fornecedor {insert[1]} inserido com sucesso'
            msgGeneric(title='Cadastro com Sucesso', text=text)
            self.limpaform()


if __name__ == '__main__':
    app = QApplication()
    window = Fornecedor()
    window.show()
    app.setStyle('Fusion')
    app.exec()
