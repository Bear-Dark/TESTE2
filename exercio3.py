from turtle import pd


print('Bem vindo ao estoque\nDigite 1 para entrar\nDigite 2 para sair\n')
opt = int(input("Escolha uma opção: "))

produtos_lista = []

def armazenarProduto():
  nomeProduto = input("Nome do produto: ")
  quantidadeProduto = input("Quantidade do produto: ")
  if not quantidadeProduto.isnumeric():
    print("Digite apenas números para a quantidade.")
    return
  codigoProduto = input("Codigo do produto: ")
  try:
    precoProduto = float(input('Digite o preço: '))
  except ValueError:
    print("Digite um valor numérico válido para o preço.")
    return

  produto = {
    "nome": nomeProduto,
    "quantidade": int(quantidadeProduto),
    "codigo": codigoProduto,
    "preco": precoProduto
  }
  produtos_lista.append(produto)
  print("Produto adicionado com sucesso!\n")

if (opt == 1):
  while True:
    armazenarProduto()
    continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
    if continuar != 's':
      break
  df = pd.DataFrame(produtos_lista)
  print("\nTabela de Produtos:")
  print(df)
elif opt == 2:
  print("Saindo ... ")
else:
  print("Opção inválida.")
znxckjzbxkjcv