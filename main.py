estoque = {"maca": [1.50, 30], "banana": [5, 20], "pera": [3, 50], "laranja": [2.50, 15], "morango": [8, 20]}

x = float(input("Qual das ações você deseja realizar, 1: incluir um produto; 2: Dar baixa em um produto; 3: Mostrar o estoque; 4: Sair?:"))
if x == 1:
    tipo = input("Qual o tipo do produto:")
    preco = float(input("Qual o preço:"))
    quantidade = float(input("Qual a quantidade?"))
    if estoque.get(tipo):
        print("Ja existe o produto", tipo)
    else:
        estoque[tipo] = preco, quantidade
    print(estoque)
if x==2:
    tipo = input("Produto a dar baixa:")
    quantidade = float(input("Qual será a nova quantidade?"))
    if tipo in estoque.keys():
        estoque[tipo] = quantidade
    else:
        print("Não é possivel dar baixa neste item.")
    print(estoque)
if x == 3:
    print(estoque)
if x == 4:
    print("Programa encerrado")








