import random
from datetime import date

# Listas de dados fictícios
nomes = ["Alice", "Bob", "Carol", "David", "Eva", "Fernando", "Milena", "Samara", "Julia", "Isabela"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Ferreira", "Rodrigues", "Gomes", "Rabelo", "Marinheiro"]
cidades = ["São Paulo, SP", "Rio de Janeiro, RJ", "Belo Horizonte", "Brasília", "Belém, PA", "Porto Alegre, RS", "Curitiba, PR", "Recife, PE", "Fortaleza, CE", "Manaus, AM", "Brasília, DF", "Salvador, BA"]
areas_atuacao = ["Engenharia", "Medicina", "Tecnologia", "Marketing", "Educação", "Arte", "Professor(a)", "Designer Gráfico(a)", "Programador(a) de Software", "Enfermeio(a)", "Jornalista", "Advogado(a)"]

# Função para gerar uma data de nascimento aleatória entre 1950 e 2000
def gerar_data_nascimento():
    ano = random.randint(1950, 2005)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)  # Assumindo 28 dias para simplificar
    return date(ano, mes, dia)

# Variável para manter o último código gerado
ultimo_codigo = 1

# Função para gerar um código de perfil sequencial
def gerar_codigo_perfil():
    global ultimo_codigo
    codigo = ultimo_codigo
    ultimo_codigo += 1
    return codigo

# Função para gerar um número de CPF aleatório
def gerar_cpf():
    cpf = [str(random.randint(0, 9)) for _ in range(11)]
    return ''.join(cpf)

# Função para gerar informações aleatórias
def gerar_informacoes_aleatorias():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    cidade_nascimento = random.choice(cidades)
    area_atuacao = random.choice(areas_atuacao)
    data_nascimento = gerar_data_nascimento()
    cpf = gerar_cpf()
    email = f"{nome.lower()}.{sobrenome.lower()}@gmail.com"
    endereco = f"{random.randint(1000, 9999)} {random.choice(['Rua', 'Avenida'])} {random.choice(nomes)} {random.choice(sobrenomes)}, {cidade_nascimento.split(',')[0]}"
    telefone = f"({random.randint(10, 99)}) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    
    return {
        "codigo_perfil": gerar_codigo_perfil(),
        "nome_completo": f"{nome} {sobrenome}",
        "data_nascimento": data_nascimento.strftime("%Y-%m-%d"),
        "cidade_nascimento": cidade_nascimento,
        "area_atuacao": area_atuacao,
        "cpf": cpf,
        "email": email,
        "endereco": endereco,
        "telefone": telefone
    }

# Pergunta ao usuário quantos perfis deseja gerar
num_perfis = int(input("Quantos perfis deseja gerar? "))

# Gerar e exibir os perfis aleatórios
for _ in range(num_perfis):
    pessoa_aleatoria = gerar_informacoes_aleatorias()
    print("Código de Perfil:", pessoa_aleatoria["codigo_perfil"])
    print("Nome Completo:", pessoa_aleatoria["nome_completo"])
    print("Data de Nascimento:", pessoa_aleatoria["data_nascimento"])
    print("Cidade de Nascimento:", pessoa_aleatoria["cidade_nascimento"])
    print("Área de Atuação:", pessoa_aleatoria["area_atuacao"])
    print("CPF:", pessoa_aleatoria["cpf"])
    print("E-mail:", pessoa_aleatoria["email"])
    print("Endereço:", pessoa_aleatoria["endereco"])
    print("Telefone:", pessoa_aleatoria["telefone"])
    print()
