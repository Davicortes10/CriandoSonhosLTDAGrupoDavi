from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

class CadastrarPedido:
    def __init__(self, yN, valor_total, lista_itens,database_name):
        self.database_name = database_name,
        self.lista_itens = lista_itens,
        self.valor_total = valor_total,
        self.yN = yN
    def cadastrarPedidoView(self):
        if self.yN =='y':
            print('----------Cadastrar pedido----------\n')
            adicionar = 'y'
            pedidos = PedidoControler.search_in_pedidos_all(self.database_name)
            numero_pedido = len(pedidos)+1
            while adicionar == 'y':
                item = int(input('Numero do item: '))
                quantidade = int(input('Quantidade: '))
                
                #calculando em tempo de execução o valor do pedido
                a = ItemControler.valor_item(self.database_name, item)
                b = a[0][0]*quantidade
                print(b)
                self.valor_total+=b
                
                for x in range(0,quantidade):#acrescentado o mesmo item várias vezes, de acordo com a quantidade
                    self.lista_itens.append((numero_pedido,item))
                
                adicionar = str(input('Adicionar novo item? (y-Sim, n-Nao): '))
        return self.valor_total, self.lista_itens


            
