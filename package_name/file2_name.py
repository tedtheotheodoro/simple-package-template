# package_name/file2_name.py
from PIL import Image
import os

def process_image_basic(image_path, output_path="processed_image.jpg"):
  """
  Abre uma imagem, converte para escala de cinza e salva.

  Args:
    image_path (str): Caminho para o arquivo de imagem de entrada.
    output_path (str): Caminho para salvar a imagem processada.
  """
  try:
    img = Image.open(image_path)
    img_gray = img.convert("L") # Converte para escala de cinza
    img_gray.save(output_path)
    print(f"Imagem processada salva em: {output_path}")
    return True
  except FileNotFoundError:
    print(f"Erro: Arquivo não encontrado em {image_path}")
    return False
  except Exception as e:
    print(f"Ocorreu um erro ao processar a imagem: {e}")
    return False

if __name__ == "__main__":
  # Exemplo de uso da função (requer uma imagem de teste)
  # Crie um arquivo de imagem de teste (ex: test_image.jpg) na mesma pasta
  test_image = "test_image.jpg" # Substitua pelo nome do seu arquivo de imagem de teste
  if os.path.exists(test_image):
    process_image_basic(test_image, "test_processed.jpg")
  else:
    print(f"Arquivo de teste '{test_image}' não encontrado. Crie um para testar a função.")