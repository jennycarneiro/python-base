email_tmplate = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para %(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria", "João", "Jennyfer"]

for cliente in clientes:
    print(email_tmplate % {
        "nome": cliente,
        "produto": "caneta",
        "texto": "escrever muito bem",
        "link": "canetafofinha.com",
        "quantidade": 1,
        "preco": 59.9
    })
    