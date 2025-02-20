email_tmpl = """
Olá, %(nome)s
 
Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver
%(texto)s
 
Clique agora em %(links)s
 
Apenas %(quantidade)d disponíveis!
 
Preço promocional %(preco).2f
"""

clientes = ["maria", "joao", "jose"]

for cliente in clientes:
    print(email_tmpl
         %{ 
         "nome": cliente,
         "produto": "caneta",
         "texto": "Escrever muito bem",
         "link": "https://canetas.com",
         "quantidade": 1
         "preco": 50.0,
         }
    )
