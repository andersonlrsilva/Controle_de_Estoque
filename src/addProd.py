from PySide6.QtWidgets import QApplication, QWidget
from ui.addProd import Ui_AddProd
from libAction import prod
from PySide6.QtGui import QDoubleValidator
from classes.message import msgGeneric


class addProd(QWidget, Ui_AddProd):
    def __init__(self):
        super(addProd, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Cadastro de Produtos')


# AJUSTES
        # CODIGO SKU
        self.txtCodSku.setValidator(QDoubleValidator())
        # CODIGO DE BARRAS
        self.txtCodBarras.setValidator(
            QDoubleValidator(bottom=0, top=9999999999))


# BOTÕES DO SISTEMA
        self.btnGravarProd.clicked.connect(self.incluirProd)
        self.btnLimpaForm.clicked.connect(self.limpaForm)
        self.btnSair.clicked.connect(self.sair)

# FUNÇOES DO SISTEMA
    def incluirProd(self):
        # VALIDA NOME DO PRODUTO
        nome = prod.prodName(self.txtNomeProd.text())
        if nome is None:
            return

        # VALIDA NOME COMERCIAL DO PRODUTO
        nomeComercial = prod.prodComName(self.txtNomeComercial.text())
        if nomeComercial is None:
            return

        # VALIDA MARCA DO PRODUTO
        marca = prod.prodMarca(self.txtMarca.text())
        if marca is None:
            return

        # VALIDA CODIGO SKU DO PRODUTO
        codSku = prod.prodSku(self.txtCodSku.text())
        if codSku is None:
            return

        # VALIDA CODIGO DE BARRAS DO PRODUTO
        codBarras = prod.prodbarcode(self.txtCodBarras.text())
        if codBarras is None:
            return

        # VALIDA FORNECEDOR DO PRODUTO
        fornecedor = prod.prodFonecedor(self.txtFornecedor.text())
        if fornecedor is None:
            return

        # GRAVA OS DADOS DO PRODUTO NO BANCO
        insert = prod.gravaDb(name=nome, prodName=nomeComercial,
                              marca=marca, sku=codSku, codBarras=codBarras,
                              fornecedor=fornecedor)

        if insert is None:
            text = (f'Não foi possível gravar os dados do produto {nome}.\n'
                    f'Nenhuma alteração foi feita no banco de dados ou '
                    f'cadastro do produto.\n'
                    f'Caso o problema persista, entre em contato com'
                    f'o suporte técnico')
            title = 'Erro ao salvar alterações'
            msgGeneric(text=text, title=title)
            return

        if insert[0] is True:
            text = f'Produto {insert[1]} inserido com sucesso'
            print(text)
            msgGeneric(title='Cadastro com Sucesso', text=text)

        if insert[0] is False:
            print(insert[0], insert[1])

    def limpaForm(self):
        self.txtNomeProd.clear()
        self.txtNomeComercial.clear()
        self.txtMarca.clear()
        self.txtCodSku.clear()
        self.txtCodBarras.clear()
        self.txtFornecedor.clear()

    def sair(self):
        self.close()


# INICIA APP
if __name__ == '__main__':
    app = QApplication()
    window = addProd()
    window.show()
    app.exec()
