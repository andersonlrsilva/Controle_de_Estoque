import requests
import os
import tempfile


def baixar_arquivo(url, endereco=None):
    endereco = os.path.join(tempfile.gettempdir(), "update.zip")
    resposta = requests.get(url, stream=True)
    print(resposta)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            for parte in resposta.iter_content(chunk_size=256):
                novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        print('oi')
        resposta.raise_for_status()


if __name__ == '__main__':
    test_url = "http://192.168.1.100/update/update.zip"
    baixar_arquivo(test_url)
