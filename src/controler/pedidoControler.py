#Necessário para realizar import em python
import sys
import time
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#importando a classe Pedido
from model.pedido import Pedido
from model.database import Database


#definindo a classe PedidoControler, nela estão os métodos
class PedidoControler:
    
    #adiciona um pedido ao banco de dados
    @staticmethod
    def insert_into_pedidos(database_name: str, data: object):
        """
        Adiciona um novo pedido ao banco de dados.

        :param database_name: Nome do banco de dados (string)
        :param data: Objeto contendo os dados do pedido (Pedido)
        :return: True se inserção for bem-sucedida, código de erro caso contrário
        """
        print(f"Verificando tipo de database_name: {database_name}, Tipo: {type(database_name)}")

        if not isinstance(database_name, str):  # Verifique se database_name é uma string
            print("Erro: O nome do banco de dados deve ser uma string!")
            return False
        
        result = Pedido.insert_into_pedidos(database_name, data)
        return result

    @staticmethod
    def search_in_pedidos_all(database_name: str) -> list:
        """
        Recupera todos os pedidos do banco de dados.

        :param database_name: Nome do banco de dados (string)
        :return: Lista de todos os pedidos, ou código de erro em caso de falha
        """
        print(f"Verificando tipo de database_name: {database_name}, Tipo: {type(database_name)}")

        if not isinstance(database_name, str):  # Verifique se database_name é uma string
            print("Erro: O nome do banco de dados deve ser uma string!")
            return []
        
        search = Pedido.search_in_pedidos_all(database_name)
        result = []
        new_item = ''
        if len(search) > 0:            
            for elem in search:
                new_item = Pedido(elem[1], elem[2], elem[3], elem[4], elem[5])
                result.append(new_item)
        return result

    @staticmethod
    def search_in_pedidos_id(database_name: str, indice: int) -> list:
        """
        Recupera um pedido específico pelo seu ID.

        :param database_name: Nome do banco de dados (string)
        :param indice: ID do pedido a ser recuperado (int)
        :return: Lista contendo o pedido encontrado, ou código de erro em caso de falha
        """
        if not isinstance(database_name, str):
            print("Erro: O nome do banco de dados deve ser uma string!")
            return []
        
        result = Pedido.search_in_pedidos_id(database_name, indice)
        return result

    @staticmethod
    def update_pedido_status_id(database_name: str, indice: int, status: str) -> bool:
        """
        Atualiza status de um determinado pedido informado pelo indice
        :param database_name: Nome do banco de dados (string).
        :param indice: ID do pedido a ser buscado (int).
        :param status: Novo estado do pedido a ser atualizado (str)
        :return: Dados do pedido (list) ou código de erro (string).
        """
        if status == 1:
            status = 'preparo'
        elif status == 2:
            status = 'pronto'
        elif status == 3:
            status = 'entregue'
        else:
            return False

        if not isinstance(database_name, str):
            print("Erro: O nome do banco de dados deve ser uma string!")
            return False
        
        result = Pedido.update_pedido_status(database_name, indice, status)
        return result
    
    @staticmethod
    def get_id_all(database_name):
        """
        Retorna o id de todos os pedidos existentes
        :param database_name: nome do banco de dados a ser acessado (str)
        :return: lista com os id || código de erro
        """
        if not isinstance(database_name, str):
            print("Erro: O nome do banco de dados deve ser uma string!")
            return []
        
        lista = []
        id_pedidos = Pedido.get_id_all(database_name)
        if id_pedidos:
            for id in id_pedidos:
                lista.append(id[0])
        return lista
        
#---------------MANUTENÇÕES---------------#
#pefectiva - atualizar estado do pedido - fazendo
#perfectiva - saber quanto está sendo o faturamento da loja em um período definido pelo usuário
    
#adaptiva - mostrar todos os pedidos - feita
#adaptativa - migrar de txt para um banco de dados sqlite3 - não se aplica
    