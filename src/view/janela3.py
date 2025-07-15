import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controler.itemControler import ItemControler

class Janela3:
    @staticmethod
    def mostrar_janela3(database_name: str):
        print("\n" + "="*50)
        print(" "*15 + "CADASTRO DE NOVO ITEM")
        print("="*50 + "\n")
        
        # Lista temporária para armazenar o novo item
        novo_item = []
        
        try:
            # Coletar dados do novo item
            nome = input("Nome do item (ex: Calabresa): ").strip()
            while not nome:
                print("O nome não pode ser vazio!")
                nome = input("Nome do item: ").strip()
            
            preco = float(input("Preço (ex: 35.90): R$ ").strip())
            while preco <= 0:
                print("O preço deve ser maior que zero!")
                preco = float(input("Preço: R$ ").strip())
            
            tipo = input("Tipo (ex: pizza, bebida, sobremesa): ").strip().lower()
            while not tipo:
                print("O tipo não pode ser vazio!")
                tipo = input("Tipo: ").strip().lower()
            
            descricao = input("Descrição (ingredientes/detalhes): ").strip()
            
            # Adiciona à lista no formato (nome, preço, tipo, descrição)
            novo_item.append((
                nome,
                float(preco),
                tipo,
                descricao
            ))
            
            # Confirmação visual
            print("\n" + "-"*50)
            print("CONFIRMAÇÃO DO ITEM:")
            print(f"Nome: {nome}")
            print(f"Preço: R$ {preco:.2f}")
            print(f"Tipo: {tipo.capitalize()}")
            print(f"Descrição: {descricao}")
            print("-"*50 + "\n")
            
            # Confirmação do usuário
            confirmar = input("Confirmar cadastro? (s/n): ").strip().lower()
            if confirmar == 's':
                # Adicionar ao banco de dados
                novoItem = ItemControler.create_item(novo_item[0])
                if ItemControler.insert_into_item(database_name,novoItem):
                    print("\nItem cadastrado com sucesso!")
                else:
                    print("\n❌ Erro ao cadastrar item no banco de dados!")
            else:
                print("\nOperação cancelada pelo usuário")
                
        except ValueError:
            print("\nErro: Valor inválido inserido (certifique-se de usar números para o preço)")
        except Exception as e:
            print(f"\nErro inesperado: {str(e)}")