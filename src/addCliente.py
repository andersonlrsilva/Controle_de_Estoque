import code
from libAction.libAddFabric import estadoFabric
from libAction.validador_ie import validar
from PySide6.QtWidgets import QApplication, QWidget, QComboBox
from ui.addCliente import Ui_addCliente
from libAction.libdefault import nameValidation, validateDoc, dataValidator
from classes.message import msgGeneric
from classes.database import Database
from PySide6.QtGui import QDoubleValidator, QIntValidator
from libAction.validador_ie import validaIeRg
from classes.database import Database


class Uiaddcliente(QWidget, Ui_addCliente):
    def __init__(self):
        super(Uiaddcliente, self).__init__()
        self.setupUi(self)


# BOTÕES DO SISTEMA
        self.btnCancelar.clicked.connect(self.exit)
        self.btnGravar.clicked.connect(self.gravacliente)


# AJUSTES DO SISTEMA
        # AJUSTA CAMPO TIPO CLIENTE
        self.cmbTipoCliente.setCurrentIndex(-1)
        self.txtCpfCnpj.setValidator(QDoubleValidator())
        self.cmbTipoCliente.currentTextChanged.connect(self.mudaCliente)
        self.txtCpfCnpj.setMaxLength(0)
        self.txtTel1.setValidator(QDoubleValidator())
        self.txtTel1.setMaxLength(11)
        self.txtTel2.setValidator(QDoubleValidator())
        self.txtTel2.setMaxLength(11)
        self.txtCel.setValidator(QDoubleValidator())
        self.txtCel.setMaxLength(11)

        # AJUSTA CAMPO IE RG
        self.txtIeRg.setValidator(QDoubleValidator())
        self.txtIeRg.setMaxLength(0)

# FUNÇÕES DO SISTEMA
# MUDA CAMPO CNPJ / CPF
    def mudaCliente(self):
        if self.cmbTipoCliente.currentText() == 'Juridico':
            self.txtCpfCnpj.clear()
            self.txtCpfCnpj.setMaxLength(14)
            self.txtIeRg.clear()
            self.txtIeRg.setMaxLength(14)

        if self.cmbTipoCliente.currentText() == 'Fisica':
            self.txtCpfCnpj.clear()
            self.txtCpfCnpj.setMaxLength(11)
            self.txtIeRg.clear()
            self.txtIeRg.setMaxLength(13)

# VERIFICA DADOS
    def validacampos(self):
        # VERIFICA SE NOME FANTASIA ESTA VAZIO
        nomefantasia = nameValidation(self.txtNomeFantasia.text())
        if nomefantasia is None:
            msgGeneric(title='Erro de Cadastro', text='Nome fantasia vazio')
            return False

        # VERIFICA SE NOME FANTASIA CONTÉM CARACTERES INVÁLIDOS
        if nomefantasia is False:
            msgGeneric(title='Erro de Cadastro', text='Nome fantasia não '
                       'pode conter caracteres inválidos')
            return False

        # VERIFICA SE RAZÃO SOCIAL ESTA VAZIA
        razaosocial = nameValidation(self.txtRazoaSocial.text())
        if razaosocial is None:
            msgGeneric(title='Erro de Cadastro', text='Razão vazio')
            return False

        # VERIFICA SE RAZAO SOCIAL CONTÉM CARACTERES INVÁLIDOS
        if razaosocial is False:
            msgGeneric(title='Erro de Cadastro', text='Razao social não '
                       'pode conter caracteres inválidos')
            return False

        # VERIFICA CPF OU CNPJ
        tipocliente = self.cmbTipoCliente.currentText()
        if not tipocliente:
            msgGeneric(title='Erro no Cadastro', text='Escolha pessoa fisica '
                       'ou jurica')
            return False

        # VALIDA DOCUMENTO
        validaDoc = validateDoc(tipo=tipocliente, dados=self.txtCpfCnpj.text())
        if validaDoc[0] is False:  # type:ignore
            msgGeneric(title='Erro no Cadastro',
                       text=validaDoc[1])  # type:ignore
            return False

        # VALIDA INSCRIÇÃO ESTADUAL
        uf = self.cmboxUf.currentText()
        tipo = self.cmbTipoCliente.currentText()
        dados = self.txtIeRg.text()
        validaIe = validaIeRg(uf=uf, tipo=tipo, dados=dados)
        if validaIe is False:
            print('deu ruim')
            return False

        # VALIDA RAMO DE ATIVIDADE
        ramo = nameValidation(self.txtAtividade.text())
        if ramo is None:
            return False
        if ramo is False:
            return False

        # VALIDA CAMPO CLIENTE DESDE
        clientedesde = self.dateEditCliente.text()
        if clientedesde is None:
            return

        # VALIDA EMAIL
        clientEmail = nameValidation(self.txtEndereco.text())

        # VALIDA SITE
        site = self.txtUrl.text()

        # VALIDA DATA
        data = dataValidator(self.dateEditCliente.text())
        print(data)

        # VALIDA ENDEREÇO
        endereco = self.txtEndereco.text()
        numero = self.txtNumero.text()
        estado = self.cmbEstado.currentText()
        cidade = self.txtCidade.text()
        bairro = self.txtBairro.text()

        return True

# GRAVA CLIENTE

    def gravacliente(self):
        confirm = self.validacampos()
        if confirm is True:
            con = Database()
            con.gravaCliente(code=self.txtCodeCliente.text(),
                             fantasia=self.txtNomeFantasia.text(),
                             razao=self.txtRazoaSocial.text(),
                             tipocliente=self.cmbTipoCliente.currentIndex(),
                             cpf=self.txtCpfCnpj.text(),
                             ie_rg=self.txtIeRg.text(),
                             uf=self.cmboxUf.currentText(),
                             ramo=self.txtAtividade.text(),
                             datacliente=data
                             )


# SAIR DO SISTEMA

    def exit(self):
        exit()


if __name__ == '__main__':
    app = QApplication()
    window = Uiaddcliente()
    app.setStyle("fusion")
    window.show()
    app.exec()
