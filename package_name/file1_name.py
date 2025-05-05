def greet(name="World"):
  """
  Função simples para retornar uma saudação.
  """
  return f"Hello, {name}!"

if __name__ == "__main__":
  # Exemplo de uso da função
  message = greet("Test")
  print(message)