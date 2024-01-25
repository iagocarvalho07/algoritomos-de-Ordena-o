import random

def gerar_numeros_aleatorios(tamanho):
  """
  Gera uma lista de números aleatórios no intervalo [0, 100].

  Args:
    tamanho: O tamanho da lista a ser gerada.

  Returns:
    Uma lista de números aleatórios.
  """

  # Gera uma lista de números inteiros no intervalo [0, 100].
  numeros = [random.randint(0, 100) for _ in range(tamanho)]

  return numeros
