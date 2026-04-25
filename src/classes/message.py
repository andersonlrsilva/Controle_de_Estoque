from PySide6.QtWidgets import QApplication, QMessageBox


# MENSAGENS DE ERRO DE LOGIN
# SENHA INVALIDA
def msgPasswdError(text, tentativas):
    restam = 5 - tentativas
    msg_text = (f'Faltam {restam} tentativas, após isso seu login\n'
                'será bloqueado!')
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Erro ao tentar Logon')
    msg.setText(f'{text}: {msg_text}')
    msg.exec()


# MENSAGEM DE ERRO PARA LOGIN INVÁLIDO
def msgLoginError(text, tentativas):
    restam = 5 - tentativas
    msg_text = (f'Faltam {restam} tentativas, após isso seu login'
                ' será bloqueado!')
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Erro ao tentar Logon')
    msg.setText(f'{text}: {msg_text}')
    msg.exec()


# MENSAGEM DE TESTE DE BANCO DE DADOS AO ABRIR O SOFTWARE
def msgInitTest():
    app = QApplication()
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Erro ao tentar Logon')
    msg.setText('Não Foi possivel conectar ao Servidor. \n'
                'Tente novamente em alguns instantes. \n'
                'Se o problema persistir, entre em contato com o suporte. \n'
                'Encerrando o programa!')
    msg.exec()
    app.exec()


# MENSAGEM DE ERRO AO CONECTAR AO DATABASE DURANTE ABERTURA DO  LOGIN
def msgInitTestLogin():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Erro ao tentar Logon')
    msg.setText('Não Foi possivel conectar ao Servidor. \n'
                'Tente novamente em alguns instantes. \n'
                'Se o problema persistir, entre em contato com o suporte. \n'
                'Encerrando o programa!')
    msg.exec()


# MENSAGEM DE TEXTO PARA USUARIO OU SENHA VAZIOS
def msgGeneric():
    msg_text = ('Nome de Usuario ou senha não podem estar vazios')
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Erro ao tentar Logon')
    msg.setText(msg_text)
    msg.exec()
