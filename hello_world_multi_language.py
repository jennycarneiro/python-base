""" Hello World in Multiple Languages / Olá, mundo multilíngue

Based on the language configured in the Windows operating system, the program shows the corresponding message. /
De acordo com a linguagem configurada no sistema operacional windows o programa exibe a mensagem correspondente.

Requirements / Requisitos:
- Windows OS only / Apenas Windows
- Python 3.x
- No external libraries needed / Não necessita bibliotecas externas

How to run / Como executar:
Run the script using Python 3 interpreter in a Windows environment. / Execute o script usando o interpretador Python 3 em ambiente Windows.
"""
__version__ = "0.0.1"
__author = "Jennyfer Carneiro"
__license__ = "Unlicense"

import ctypes
import locale

lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
current_language = locale.windows_locale.get(lang_id)

msg = "Hello, world!"

#Conditional statement / Aplicação de condicional
if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, mundo!"
elif current_language == "es_ES":
    msg = "¡Hola, mundo!"
  
print(msg)