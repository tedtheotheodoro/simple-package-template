# image_processing_package_Theodoro_Fraga_DIO

Este é um pacote Python simples para fins educacionais focado em funcionalidades básicas de processamento de imagens. Foi desenvolvido como parte de um desafio da plataforma Digital Innovation One (DIO).

## Instalação

Você pode instalar este pacote diretamente via pip:

```bash
pip install image_processing_package_Theodoro_Fraga_DIO

*Nota: Certifique-se de ter o Python e o pip instalados.*

## Uso

Para usar as funcionalidades deste pacote, importe-o em seu script Python:

```python
# Exemplo básico de uso (assumindo que você tem um arquivo de imagem de teste)
from image_processing_package_Theodoro_Fraga_DIO import process_image_basic
from image_processing_package_Theodoro_Fraga_DIO import greet
import os

# Exemplo da função greet
message = greet("Usuário DIO")
print(message)

# Exemplo da função de processamento de imagem (requer uma imagem de teste)
test_image_path = "caminho/para/sua/imagem.jpg" # Substitua pelo caminho real da sua imagem de teste
output_image_path = "imagem_processada.jpg"

if os.path.exists(test_image_path):
    process_image_basic(test_image_path, output_image_path)
else:
    print(f"Arquivo de teste '{test_image_path}' não encontrado.")

*Nota: As funções de processamento de imagem no `file2_name.py` requerem que você tenha a biblioteca Pillow instalada, o que será feito automaticamente ao instalar o pacote.*

## Funcionalidades

Atualmente, este pacote inclui as seguintes funcionalidades básicas:

* `greet(name)`: Uma função simples de saudação (localizada em `file1_name.py`).
* `process_image_basic(image_path, output_path)`: Abre uma imagem, converte para escala de cinza e salva (localizada em `file2_name.py`).

## Autor

Theodoro Fraga
E-mail: theodorofragadecastro.dev@gmail.com
GitHub: [Link para o seu repositório deste projeto](https://github.com/tedtheotheodoro/simple-package-template.git)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.