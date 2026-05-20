from PySide6.QtWidgets import QApplication, QWidget
import requests
import os
import subprocess
import sys
import tempfile
from classes.message import msgUpdWarning
from ui.update import Ui_Update


VERSAO_ATUAL = "1.1.1"
URL_UPDATE_INFO = "http://192.168.1.101/update.json"


class Update(QWidget, Ui_Update):
    def __init__(self):
        super(Update, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Atualização')
        self.labelVerInfo.setText(VERSAO_ATUAL)
        self.dados = []

# CONFIGURAÇÃO DO SISTEMA
        self.btnAtualizar.setDisabled(True)

# BOTÕES DO SISTEMA
        self.btnBuscAtua.clicked.connect(self.verificarUpdate)
        self.btnSair.clicked.connect(self.sair)
        self.btnAtualizar.clicked.connect(self.startUpdate)

# FUNÇÕES DO SISTEMA
    def sair(self):
        self.close()

# VERIFICA A ULTIMA VERSÃO DISPONÍVEL NO UPDATE
    def verificarUpdate(self):
        try:
            self.dados = requests.get(URL_UPDATE_INFO).json()
            if self.dados["versao"] > VERSAO_ATUAL:
                self.btnAtualizar.setDisabled(False)
                self.labelInfoNovaVersao.setText(self.dados['versao'])
                return self.dados["versao"], self.dados["url"]
            else:
                self.labelInfoNovaVersao.setText(self.dados['versao'])
                return None

        except:
            msgUpdWarning()

# BAIXA OS ARQUIVOS PARA O UPDATE NA PASTA TEMP
    def downloadUpdate(self, url):
        temp_zip = os.path.join(tempfile.gettempdir(), "update.zip")
        resposta = requests.get(url, stream=True)
        if resposta.status_code == requests.codes.OK:
            with open(temp_zip, "wb") as f:
                for chunk in resposta.iter_content(chunk_size=256):
                    f.write(chunk)
        else:
            resposta.raise_for_status()
        return temp_zip

# INICIA UPDATE
    def iniciarUpdate(self, zip_path):
        updater = os.path.join(os.path.dirname(sys.executable), "updater.exe")
        print(updater)
        subprocess.Popen([updater, zip_path, os.getcwd(), str(os.getpid())])
        sys.exit(0)

    def startUpdate(self):
        tmp_zip = self.downloadUpdate(self.dados["url"])  # type: ignore
        self.iniciarUpdate(tmp_zip)


if __name__ == '__main__':
    app = QApplication()
    window = Update()
    window.show()
    app.exec()
