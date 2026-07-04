from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui.addProd import Ui_AddProd
from libAction import prod
from PySide6.QtGui import QDoubleValidator, QPixmap
from classes.message import msgGeneric
from PySide6.QtCore import Qt


class UiaddProd(QWidget, Ui_AddProd):
    def __init__(self):
        super(UiaddProd, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Cadastro de Produtos')
        self.image_data = ''


# AJUSTES
        # CODIGO SKU
        self.txtCodSku.setValidator(QDoubleValidator())
        self.txtCodSku.setMaxLength(24)

        # CODIGO DE BARRAS
        self.txtCodBarras.setMaxLength(24)
        self.txtCodBarras.setValidator(
            QDoubleValidator(bottom=0, top=9999999999))

        # CODIGO CEST
        self.txtCest.setMaxLength(7)

        # CODIGO NCM
        self.txtNcm.setMaxLength(10)

        # NOME PRODUTO
        self.txtNomeProd


# BOTÕES DO SISTEMA
        self.btnGravarProd.clicked.connect(self.incluirProd)
        self.btnLimpaForm.clicked.connect(self.limpaForm)
        self.btnSair.clicked.connect(self.sair)
        self.btnAddFabric.clicked.connect(self.addFabric)
        self.btnAddFornec.clicked.connect(self.addFornec)
        self.btnAddMarca.clicked.connect(self.addMarca)
        self.btnSalvaFoto.clicked.connect(self.loadImage)

# FUNÇOES DO SISTEMA
    # ABRE PAGINA PARA ADICIONAR FABRICANTE
    def addFabric(self):
        import addFabric
        self.w = addFabric.UiFabricante()
        self.w.show()

    # ABRE A PAGINA PARA ADICIONAR FORNCEDOR
    def addFornec(self):
        import addFornecedor
        self.w = addFornecedor.UiFornecedor()
        self.w.show()

    # ABRE A PAGINA PARA ADICIONAR MARCA
    def addMarca(self):
        import addMarca
        self.w = addMarca.Addmarca()
        self.w.show()

    # ATUALIZA FABRICANTE / MARCA / FORNECEDOR
    def atualizaComboBox(self):
        fabric = prod.updateComboBox('FABRICANTE')
        if fabric is None:
            return
        for dado in fabric:  # type: ignore
            self.cmbFabric.addItems(dado)  # type: ignore

        self.cmbFabric.setCurrentIndex(-1)

        fornc = prod.updateComboBox('FORNECEDOR')
        if fornc is None:
            return
        for dado in fornc:  # type: ignore
            self.cmbFornec.addItems(dado)  # type: ignore

        self.cmbFornec.setCurrentIndex(-1)

        marca = prod.updateComboBox('MARCA')
        if marca is None:
            return
        for dado in marca:  # type: ignore
            self.cmbMarca.addItems(dado)  # type: ignore

        self.cmbMarca.setCurrentIndex(-1)

    # CARREGA FOTO DO  PRODUTO
    def loadImage(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Selecione uma imagem",
                "",
                "Image Files (*.png *.jpg *.bmp, *webp)"
            )

            if file_path:
                pixmap = QPixmap(file_path)
                if pixmap.isNull():
                    print("Erro ao carregar a imagem.")
                    return
            with open(file_path, 'rb') as file:
                self.image_data = file.read()
                self.labelFoto.setPixmap(pixmap.scaled(  # type: ignore
                    self.labelFoto.width(), self.labelFoto.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                ))
        except Exception as e:
            text = f'Erro ao carregar a imagem Erro {e}.'
            title = "Erro"

    # CONFIRMA DADOS E INCLUI NO SISTEMA
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
        marca = prod.prodMarca(self.cmbMarca.currentText())
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
        fornecedor = prod.prodFornecedor(self.cmbFornec.currentText())
        if fornecedor is None:
            return

        # VALIDA FABRICANTE DO PRODUTO
        fabricante = prod.prodFabricante(self.cmbFabric.currentText())
        if fornecedor is None:
            return

        # VALIDA CODIGO CEST
        codCest = prod.prodCest(self.txtCest.text())
        if codCest is None:
            return

        # VALIDA CODIGO NCM
        codNcm = prod.prodNcm(self.txtNcm.text())
        if codNcm is None:
            return

        # DESCRIÇÃO DO PRODUTO
        descr = self.txtAplicacao.toPlainText()
        print(descr)

        if not self.image_data:
            title = 'Erro no cadastro'
            text = 'Imagem do produto não pode estar vazia'
            msgGeneric(title=title, text=text)
            print('caiu na imagen')
            return

        # GRAVA OS DADOS DO PRODUTO NO BANCO
        insert = prod.gravaProduto(name=nome, prodName=nomeComercial,
                                   marca=marca, sku=codSku, codBarras=codBarras,
                                   fornecedor=fornecedor, fabricante=fabricante,
                                   codncm=codNcm, codcest=codCest,
                                   image=self.image_data, desc=descr)

        # SE HOUVER ERRO NA GRAVAÇÃO DO DATABASE
        if insert[0] is None:  # type:ignore
            text = (f'Não foi possível gravar os dados do produto {nome}.\n'
                    f'Nenhuma alteração foi feita no banco de dados ou '
                    f'cadastro do produto.\n'
                    f'Caso o problema persista, entre em contato com'
                    f'o suporte técnico')
            title = 'Erro ao salvar alterações'
            msgGeneric(text=text, title=title)
            return

        # MENSAGEM PARA USUÁRIO SE GRAVAÇÃO FOR BEM SUCEDIDA
        if insert[0] is True:  # type:ignore
            text = f'Produto {insert[1]} inserido com sucesso'  # type:ignore
            msgGeneric(title='Cadastro com Sucesso', text=text)
            self.limpaForm()

        # MENSAGEM PARA USUÁRIO CASO GRAVAÇÃO RESULTAR EM ERRO
            if insert[0] is False:  # type:ignore
                print(insert[0], insert[1])  # type:ignore

    # LIMPA O FORMULARIO APÓS GRAVAR OS DADOS NO BANCO DE DADOS
    def limpaForm(self):
        self.txtNomeProd.clear()
        self.txtNomeComercial.clear()
        self.txtCest.clear()
        self.txtCodSku.clear()
        self.txtCodBarras.clear()
        self.txtNcm.clear()
        self.cmbFornec.setCurrentIndex(-1)
        self.cmbMarca.setCurrentIndex(-1)
        self.cmbFabric.setCurrentIndex(-1)
        self.labelFoto.clear()
        self.txtAplicacao.clear()

    # SAIR DO SISTEMA
    def sair(self):
        self.close()


    # INICIA APP
if __name__ == '__main__':
    app = QApplication()
    app.setStyle("Fusion")
    window = UiaddProd()
    window.show()
    window.atualizaComboBox()
    app.exec()
