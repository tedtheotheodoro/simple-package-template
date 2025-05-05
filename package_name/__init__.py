# Importa funções dos outros arquivos para facilitar o acesso
from .file1_name import greet
from .file2_name import process_image_basic

# Opcional: definir quais nomes serão exportados ao usar 'from package_name import *'
__all__ = ["greet", "process_image_basic"]

print("Pacote package_name sendo inicializado!")