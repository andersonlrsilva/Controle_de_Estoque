from PySide6.QtWidgets import QApplication, QWidget
import requests
import os
import subprocess
import sys
import zipfile
import tempfile
from classes.message import msgUpDate, msgUpdWarning
from ui.update import Ui_Update


VERSAO_ATUAL = "1.9.0"
URL_UPDATE_INFO = "http://127.0.0.1/update.json"


class Update(QWidget, Ui_Update):
    def __init__(self):
        super(Update, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Atualização')
        self.labelVerInfo.setText(VERSAO_ATUAL)

        self.btnAtualizar.setDisabled(True)

        self.btnBuscAtua.clicked.connect(self.verificar_update)
        self.btnSair.clicked.connect(self.sair)

    def sair(self):
        self.close()
# VERIFICA A ULTIMA VERAO DISPONIVEL NO UPDATE

    def verificar_update(self):
        try:
            resposta = requests.get(URL_UPDATE_INFO, timeout=10)
            r = resposta.status_code
            dados = requests.get(URL_UPDATE_INFO).json()
            if dados["versao"] > VERSAO_ATUAL:
                self.btnAtualizar.setDisabled(False)
                self.labelInfoNovaVersao.setText(dados['versao'])
                return dados["versao"], dados["url"]
            else:
                self.labelInfoNovaVersao.setText(dados['versao'])
                return None

        except:
            msgUpdWarning()

# BAIXA OS ARQUIVOS PARA O UPDATE NA PASTA TEMP

    def downloadUpdate(self, url):
        temp_zip = os.path.join(tempfile.gettempdir(), "update.zip")
        with requests.get(url, stream=True) as r:
            with open(temp_zip, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
        return temp_zip

    # INICIA UPDATE

    def iniciar_update(self, zip_path):
        updater = os.path.join(os.path.dirname(sys.executable), "updater.exe")
        subprocess.Popen([updater, zip_path, os.getcwd(), str(os.getpid())])
        sys.exit(0)

    def main(self):
        upd = self.verificar_update()
        print(upd)
        if upd:
            versao, url = upd
            print('upd date')

        #     zip_path = downloadUpdate(url)

        #     iniciar_update(zip_path)

        #     print("rodando app versao", VERSAO_ATUAL)


if __name__ == '__main__':
    app = QApplication()
    window = Update()
    window.show()
    app.exec()
