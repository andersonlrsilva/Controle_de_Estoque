
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QRegularExpressionValidator, QKeyEvent
from PySide6.QtCore import QRegularExpression, Qt
from ui.login import Ui_login
from classes.database import Database
from classes.message import (msgInitTestLogin, msgLoginError, msgPasswdError,
                             msgGeneric)
import main


class Login(QWidget, Ui_login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("logon no sistema")
        self.adjustSize()
        self.setFixedSize(300, 400)
        self.tentativas_senha = 0
        self.tentativas_user = 0

    # CONFIGS ...
    # CAMPO USUARIO
        regex = QRegularExpression("[A-Za-z.]*")
        validador = QRegularExpressionValidator(regex)
        self.txtUsuario.setValidator(validador)
        self.txtUsuario.setMaxLength(20)
        self.txtUsuario.setPlaceholderText('Insira o Nome')

    # CAMPO SENHA
        self.txtSenha.setMaxLength(12)
        self.txtSenha.setPlaceholderText('Insira a senha')

    # BOTÕES DO SISTEMA
        self.btnEntrar.clicked.connect(self.logon)
        self.btnSair.clicked.connect(self.exit)

    # FUNÇÕES DO SISTEMA
    # Captura tecla enter e aciona botão login
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if not self.txtUsuario.text() or not self.txtSenha.text():
                return
            else:
                self.btnEntrar.click()

    # Sair do login
    def exit(self):
        exit()

    # Logon no sistema
    def logon(self):
        # VERIFICA SE USUARIO E SENHA ESTAO VAZIOS
        if (not self.txtUsuario.text()) or (not self.txtSenha.text()):
            msgGeneric()
            return False, "L003"

        db = Database()
        # TESTA CONEXÃO COM BANCO DE DADOS
        testCon = db.connect()
        if testCon is False:
            msgInitTestLogin()
            self.exit()
            return False

        # ENVIA USUARIO E SENHA PARA VALIDAÇÃO, E PEGA O RESULTADO
        logar = db.login(user=self.txtUsuario.text(),
                         passwd=self.txtSenha.text())

        # SE SENHA ESTIVER ERRADA, ENVIA MENSAGEM AO USUARIO
        if logar[0] is False and logar[1] == "L001":  # type:ignore
            self.tentativas_senha += 1
            msgPasswdError('Senha inválida', self.tentativas_senha)
            if self.tentativas_senha >= 5:
                self.exit()
            return False

        # SE NOME DE USUARIO NÃO EXISTIR ENVIA MENSAGEM PARA USUARIO
        if logar[0] is False and logar[1] == "L002":  # type:ignore
            self.tentativas_user += 1
            msgLoginError('Usuário Não cadastrado no sistema',
                          self.tentativas_user)
            if self.tentativas_user >= 5:
                self.exit()
            return False

        # SE LOGIN E SENHA ESTIVER CORRETO, ABRE A APLICAÇÃO INICIAL
        # PASSANDO ID, USUARIO E NIVEL
        if logar[0] is True:  # type: ignore
            userid = logar
            self.w = main.MainWindow(user=userid)
            self.w.show()
            self.close()
            return True


# INICIO DO PROGRAMA
if __name__ == "__main__":
    app = QApplication()
    window = Login()
    window.show()
    app.exec()
