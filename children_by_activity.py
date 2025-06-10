""" Report of children by activity / Relatório de crianças por atividade

"""
__version__ = "0.0.2"

sala1 = ["Erik", "Maria", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca)]

for nome_atividade, atividade in atividades:
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print(f"{nome_atividade} sala 1", atividade_sala1)
    print(f"{nome_atividade} sala 2", atividade_sala2)
    print("-" * 40)