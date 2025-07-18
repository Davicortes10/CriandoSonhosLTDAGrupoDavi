#para pegar a data de hoje
from datetime import date
import time

#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#importando os módulos de model
from model.pedido import Pedido

#importando os módulos de controle
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

from .CadastrarPedido import CadastrarPedido

#criação da classe janela
class Janela1:
    
    @staticmethod
    def mostrar_janela1(database_name: str) -> None:
        endereco = None
        """
        View para o usuário utilizar o software
        
        return None
        """
        
        a = 'y'
        
        menu = ItemControler.mostrar_itens_menu(database_name)

        print('--- Cardápio Disponível ---')
        print('ID | Nome                  | Tipo   | Preço   | Descrição')
        print('-------------------------------------------------------------')

        for item in menu:
            id_, nome, preco, tipo, descricao = item
            print(f"{id_:<2} | {nome:<21} | {tipo:<6} | R${preco:>6.2f} | {descricao}")

        while a=='y':
            lista_itens = []
            valor_total=0
            
            while True:
                a = input('Cadastrar pedido (y-Sim, n-Nao): ').strip().lower()
                if a in ('y', 'n'):
                    break
                print('Entrada inválida. Por favor, digite "y" para sim ou "n" para não.')
            
            if a=='y':
                cadastrarPedido = CadastrarPedido(a, valor_total, lista_itens, database_name)

                valor_total, lista_itens, numero_pedido=  cadastrarPedido.cadastrarPedidoView()
                
                print('\n----------Finalizar pedido----------\n')
                print(f'Numero do pedido: {numero_pedido}')
                while True:
                    delivery_input = input('Delivery (S/N): ').strip().lower()
                    if delivery_input == 's':
                        delivery = True
                        endereco = input('Endereco:').strip()
                        break
                    elif delivery_input == 'n':
                        delivery = False
                        endereco = ''
                        break
                    else:
                        print('Entrada inválida. Digite "S" para sim ou "N" para não.')
                
                while True:
                    try:
                        status_aux = int(input('Status do pedido (1-preparo, 2-pronto, 3-entregue): '))
                        if status_aux == 1:
                            status = 'preparo'
                            break
                        elif status_aux == 2:
                            status = 'pronto'
                            break
                        elif status_aux == 3:
                            status = 'entregue'
                            break
                        else:
                            print('Valor inválido. Digite 1, 2 ou 3.')
                    except ValueError:
                        print('Entrada inválida. Digite um número (1, 2 ou 3).')
 
                print(f'Valor Final: R${valor_total}')
                data_hoje = date.today()
                data_formatada = data_hoje.strftime('%d/%m/%Y')
                print(data_formatada)
                print(endereco)
                pedido = Pedido(status, str(delivery), endereco,data_formatada,float(valor_total))
                PedidoControler.insert_into_pedidos(database_name,pedido)
                for elem in lista_itens:
                    ItemControler.insert_into_itens_pedidos(database_name,elem)
                
            elif a=='n':
                print('Voltando ao Menu inicial')
                time.sleep(2)
                break
