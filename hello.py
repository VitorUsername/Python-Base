#!/usr/bin/env python3
# SHEBANG é um comentário especial que será executdado antes do meu programa iniciar,

# --> DOCSTRING comentários mult-linhas
#--> RECOMENDO SEMPRE FAZER A DOCUMENTAÇÃO EM INGLES
"""
Primeiro colocar oque é o programa

Dependendo da língua configurada no (env) o programa exibe a mensagem
correspondente

Como usar:

Tenha a variável LANG devidamente Configurada ex:

    export LANG_BR

Execução:

    python hello.py
    ou
    ./hello.py
    
"""

#--> METADADOS
__version__="0.0.1"
__author__="Vitor"
__lincense__="Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Hola, Mundo"
elif current_language == "it_IT":
    msg = "Ciao, Mundo!"
 
print("Ola,  Mundo!".upper()) # .upper() usado para deixar as letras de uma string maiúscula #horas
