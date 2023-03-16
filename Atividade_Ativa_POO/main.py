class Categoria:
    def __init__(self, numero, nome, transmissao, combustivel, marca):
        self.numero = numero
        self.nome = nome
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca

class Carro:
    def __init__(self, categoria, modelo, ano, placa):
        self.categoria = categoria
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.disponivel = True

class Cliente:
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

class Locadora:
    def __init__(self, carro, cliente, inicio, fim):
        self.carro = carro
        self.cliente = cliente
        self.inicio = inicio
        self.fim = fim
        self.carro.disponivel = False

categorias = [
    Categoria(1, 'SUV', 'Automática', 'Flex', 'Hiunday'),
    Categoria(2, 'Picape', 'Manual', 'Diesel', 'Toyotax'),
    Categoria(3, 'Hacht', 'Manual', 'Gasolina', 'Fiat'),
    Categoria(4, 'Sedan', 'Manual', 'GNV', 'Chevrolet'),
]

carros = []
clientes = []
locacoes = []


def add_Carros():
    print('Categorias:')
    for categoria in categorias:
        print(f'{categoria.numero}) {categoria.nome}')
    while True:
        resposta = input('O carro que será cadastrado está em uma das categorias listadas acima [S/N]: ')
        if resposta.upper() == 'S':
            categoria_numero = int(input('Escolha o número da CATEGORIA do novo carro: '))
            categoria = next((c for c in categorias if c.numero == categoria_numero), None)
            if categoria:
                break
            else:
                print('Categoria inválida. Tente novamente!')
        elif resposta.upper() == 'N':
            nome = input('Nome da categoria: ')
            transmissao = input('Informe a Transmissão: ')
            combustivel = input('Informe o tipo de Combustível: ')
            marca = input('Informe a Marca: ')
            categoria = Categoria(len(categorias)+1, nome, transmissao, combustivel, marca)
            categorias.append(categoria)
            break
        else:
            print('Resposta inválida. Tente novamente!')
    modelo = input('Informe o Modelo: ')
    ano = input('Ano: ')
    placa = input('Placa: ')
    carro = Carro(categoria, modelo, ano, placa)
    carros.append(carro)
    print('Carro cadastrado com sucesso!')
    print(f'Carro {carro.modelo}: Placa: {carro.placa} Placa: {carro.placa}')

def add_Cliente():
    nome = input('Nome: ')
    cpf = input('CPF: ')
    rg = input('RG: ')
    cliente = Cliente(nome, cpf, rg)
    clientes.append(cliente)
    print('Cliente cadastrado com sucesso!')

def fazer_Locacao():
    if not carros:
        print('Nenhum carro cadastrado.')
        return
    if not clientes:
        print('Nenhum cliente cadastrado.')
        return

    carros_disponiveis = [c for c in carros if c.disponivel]
    if not carros_disponiveis:
        print('Não existem carros disponíveis para locação.')
        return

    print('Carros disponíveis:')
    for i, carro in enumerate(carros_disponiveis):
        print(f'{i + 1}) {carro.modelo} - {carro.categoria.nome}')

    while True:
        try:
            carro_index = int(input('Qual Carro o cliente quer alugar: '))
            carro = carros_disponiveis[carro_index - 1]
            break
        except (ValueError, IndexError) as e:
            print('Opção inválida. Tente novamente.')

    while True:
        cpf = input('CPF do cliente que irá alugar: ')
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente:
            break
        else:
            print('Cliente não encontrado. Tente novamente.')

    inicio = input('Data de início da locação (DD/MM/AAAA): ')
    fim = input('Data de fim da locação (DD/MM/AAAA): ')

    locacao = Locadora(carro, cliente, inicio, fim)
    locacoes.append(locacao)
    print('Locação realizada com sucesso!')
    print(f'Carro {carro.modelo} agora está indisponível.')

def listar_locacoes():
    if not locacoes:
        print('Nenhuma locação realizada.')
        return

    for i, locacao in enumerate(locacoes):
        print(
            f'{i + 1}) Cliente: {locacao.cliente.nome} - Carro: {locacao.carro.modelo} - Período: {locacao.inicio} a {locacao.fim}')

def listar_carros_disponiveis():
    print('Lista de carros disponíveis:')
    carros_disponiveis = [c for c in carros if c.disponivel]
    if not carros_disponiveis:
        print('Nenhum carro disponível no momento.')
    else:
        for i, carro in enumerate(carros_disponiveis):
            print(f'{i + 1}) {carro.modelo} - {carro.categoria.nome} - Disponível: {carro.disponivel}')


while True:
    print('---- Bem-vindo a MOVIDA! ----')
    print('1) Cadastrar Carro')
    print('2) Cadastrar Cliente')
    print('3) Realizar Locação')
    print('4) Listar Locações')
    print('5) Listar carros disponíveis')
    print('6) Sair')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        add_Carros()
    elif opcao == '2':
        add_Cliente()
    elif opcao == '3':
        fazer_Locacao()
    elif opcao == '4':
        listar_locacoes()
    elif opcao == '5':
        listar_carros_disponiveis()
    elif opcao == '6':
        print('Obrigada!')
        break
    else:
        print('Opção inválida. Tente novamente.')
