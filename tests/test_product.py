"""Módulo de testes para o gerenciador de produtos."""
import unittest
from mercadolivresdk.internal.manager.product import ProductManager
from mercadolivresdk.internal.models.product import ProductAd, ProductDescription, Snapshot

class TestProductManager(unittest.TestCase):
    """Classe de testes para o gerenciador de produtos."""
    manager = None
    product_id = None

    def setUp(self) -> None:
        self.manager = ProductManager('APP_USR-5417402069385811-010612-021c94173d01ab90ae5021c7dbfc1995-592589493')
        self.product_id = 'MLB3360863607'


    def test_get_product(self):
        """Testa a obtenção de um produto."""
        # Act
        product = self.manager.get_product(self.product_id)

        # Assert
        self.assertEqual(product.id, self.product_id)
        self.assertEqual(product.site_id, 'MLB')
        self.assertIsInstance(product, ProductAd)
    
    def test_get_description(self):
        """Testa a obtenção da descrição de um produto."""
        # Act
        description = self.manager.get_product_description(self.product_id)

        description_expected = ProductDescription(
            text='',
            plain_text='A Dianauto é uma Concessionária Autorizada FIAT que opera '
               'apenas com peças novas, originais e genuínas!\n'
               '\n'
               ' Filtro de Óleo FIAT UNO ARGO CRONOS Strada PULSE\n'
               '\n'
               'Por que trocar o filtro de óleo?Dificulta a passagem do óleo, '
               'podendo causar falhas na lubrificação. A situação se agrava O '
               'óleo, com seus aditivos detergentes e dispersantes, carrega as '
               'sujeiras que iriam se depositar no motor. Na passagem pelo '
               'filtro, as impurezas maiores são retidas e as menores '
               'continuam em suspensão no óleo. Chega um momento em que o '
               'filtro, carregado de sujeira, caso ocorra o bloqueio total do '
               'filtro, o que pode causar graves danos ao motor.Quando trocar '
               'o filtro de óleo?O período da troca do filtro de óleo também é '
               'recomendado pelo fabricante do veículo e consta no manual do '
               'proprietário. Atualmente há fabricantes que recomendam a troca '
               'do filtro a cada troca de óleo, para que não se misture o óleo '
               'novo com os resíduos que se encontram no filtro.\xa0\n'
               '\n'
               'Compatível com:\n'
               '\n'
               '# UNO\n'
               'UNO VIVACE/RUA 1.0 EVO Fire Flex 8V 5p 2016 Gasolina\n'
               'UNO VIVACE Celeb. 1.0 EVO F.Flex 8V 5p 2016 Gasolina\n'
               'UNO WAY 1.0 EVO Fire Flex 8V 5p 2016 Gasolina\n'
               'UNO WAY Celeb. 1.0 EVO Fire Flex 8V 5p 2016 Gasolina\n'
               'UNO VIVACE 1.0 EVO Fire Flex 8V 3p 2016 Gasolina\n'
               'UNO VIVACE Celeb. 1.0 EVO F. Flex 8V 3p 2016 Gasolina\n'
               'UNO ATTRACTIVE 1.0 Fire Flex 8V 5p 2016 a 2021 Gasolina\n'
               'UNO Furgão 1.0 Fire Flex 8V 3p 2016 Gasolina\n'
               'UNO WAY RIO 450 1.0 EVO Flex 8V 5p 2016 Gasolina\n'
               'UNO ATTRACTIVE 1.0 Flex 6V 5p 2017 Gasolina\n'
               'UNO SPORTING 1.3 Flex 8V 5p 2017, 2018 Gasolina\n'
               'UNO SPORTING Dual./GSR 1.3 Flex 8V 5p 2017, 2018 Gasolina\n'
               'UNO WAY 1.0 Flex 6V 5p 2017 a 2021 Gasolina\n'
               'UNO WAY 1.3 Flex 8V 5p 2017 a 2021 Gasolina\n'
               'UNO WAY Dual./GSR 1.3 Flex 8V 5p 2017, 2018 Gasolina\n'
               'UNO DRIVE 1.0 Flex 6V 5p 2018 a 2021 Gasolina\n'
               'UNO CIAO 1.0 Fire Flex 8V 5p 2021 Gasolina\n'
               '\n'
               '# ARGO\n'
               'ARGO DRIVE 1.0 6V Flex 2018 a 2022 Gasolina\n'
               'ARGO DRIVE 1.3 8V Flex 2018 a 2021 Gasolina\n'
               'ARGO DRIVE GSR 1.3 8V Flex 2018, 2019, 2020 Gasolina\n'
               'ARGO 1.0 6V Flex. 2018 a 2022 Gasolina\n'
               'ARGO TREKKING 1.3 8V Flex 2020, 2021, 2022 Gasolina\n'
               'ARGO DRIVE S-DESIGN 1.3 8V Flex 2022 Gasolina\n'
               '\n'
               '# CRONOS\n'
               'CRONOS 1.3 8V Flex 2019 a 2022 Gasolina\n'
               'CRONOS DRIVE 1.3 8V Flex 2018 a 2022 Gasolina\n'
               'CRONOS DRIVE GSR 1.3 8V Flex 2018, 2019, 2020 Gasolina\n'
               '\n'
               '# Strada\n'
               'Strada Freedom 1.3 Flex 8V CS Plus 2021, 2022 Gasolina\n'
               'Strada Freedom 1.3 Flex 8V CD 2021, 2022 Gasolina\n'
               'Strada Volcano 1.3 Flex 8V CD 2021, 2022 Gasolina\n'
               'Strada Opening Edition 1.3 Flex 8V CD 2021 Gasolina\n'
               'Strada Ranch 1.3 Flex 8V CD Aut. 2022 Gasolina\n'
               'Strada Volcano 1.3 Flex 8V CD Aut. 2022 Gasolina\n'
               '\n'
               '# PULSE\n'
               'PULSE DRIVE 1.3 8V Flex Aut. 2022 Gasolina\n'
               'PULSE DRIVE 1.3 8V Flex Mec. 2022 Gasolina\n'
               '\n'
               '\n'
               'Envie todas as suas dúvidas antes da compra.\n'
               'Consulte nosso especialista online através do campo Perguntas '
               'e Respostas.\n'
               'Caso precise de informações sobre aplicação sempre informe o '
               'n° do Chassi do veículo, que se encontra no documento.\n'
               'Somos uma Concessionária Autorizada FIAT do GRUPO DINAUTO\n'
               '\n'
               '#1534177',
            last_updated='2024-02-17T04:01:21.654Z',
            date_created='2023-06-28T18:50:51.035Z',
            snapshot=Snapshot(
                url='http://descriptions.mlstatic.com/D-MLB3360863607.jpg?hash=8520c3b8559cb08aa7e782b8f5334ffe_0x0',
                width=0,
                height=0,
                status=''
            )
        )

        # Assert
        self.assertIsInstance(description, ProductDescription)
        self.assertEqual(description.text, description_expected.text)
        self.assertEqual(description.plain_text, description_expected.plain_text)
        self.assertEqual(description.last_updated, description_expected.last_updated)
        self.assertEqual(description.date_created, description_expected.date_created)
        self.assertEqual(description.snapshot, description_expected.snapshot)
        self.assertEqual(description, description_expected)
    
