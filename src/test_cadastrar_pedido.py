import unittest
from unittest.mock import patch, MagicMock
from controler.itemControler import ItemControler
from controler.pedidoControler import PedidoControler
from view.CadastrarPedido import CadastrarPedido  # ajuste esse import conforme seu projeto

class TestCadastrarPedido(unittest.TestCase):

    @patch('builtins.input')
    @patch.object(ItemControler, 'valor_item')
    @patch.object(PedidoControler, 'search_in_pedidos_all')
    def test_cadastrar_pedido_confirmacao_funciona(self, mock_pedidos_all, mock_valor_item, mock_input):
        # Simula itens já cadastrados
        mock_pedidos_all.return_value = [1, 2]  # Já existem 2 pedidos

        # Simula o valor retornado para um item
        mock_valor_item.return_value = [(10.0,)]

        # Simula sequência de inputs: item, quantidade, confirmação, depois fim
        mock_input.side_effect = [
            '1',  # item
            '2',  # quantidade
            'y',  # deseja adicionar mais
            '1',  # item novamente
            '1',  # quantidade
            'n'   # finaliza
        ]

        # Executa
        pedido = CadastrarPedido('y', 0.0, [], 'fake_database.db')
        valor_total, lista_itens, numero = pedido.cadastrarPedidoView()

        # Verificações
        self.assertEqual(valor_total, 30.0)  # 10 * 2 + 10 * 1
        self.assertEqual(numero, 3)  # já haviam 2 pedidos
        self.assertEqual(len(lista_itens), 3)
        self.assertListEqual(lista_itens, [(3,1), (3,1), (3,1)])

if __name__ == '__main__':
    unittest.main()
