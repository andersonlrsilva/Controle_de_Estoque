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
def msgUserEmpty():
    msg_text = ('Nome de Usuario ou senha não podem estar vazios')
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Erro ao tentar Logon')
    msg.setText(msg_text)
    msg.exec()


# MENSAGEM DE TEXTO PARA USUARIO OU SENHA VAZIOS
def msgUpDate(versao):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Atualização encontrada')
    msg.setText(f'Atualização para a versao {versao} esta disponivel.')
    msg.exec()


def msgUpdWarning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle('Erro de Atualização')
    msg.setText('Não foi possível buscar o servidor de atualização.\n'
                'Entre em contato com o suporte e informe o código UPD0001')
    msg.exec()


# MENSAGEM ERRO GENERICA
def msgGeneric(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec()
