def bubble_sort(vetor):
  """
  Ordena um vetor usando o algoritmo Bubble Sort.

  Args:
    vetor: O vetor a ser ordenado.

  Returns:
    O vetor ordenado.
  """

  # Variável para controlar o loop externo.
  n = len(vetor) - 1

  # Loop externo para iterar sobre o vetor.
  while n > 0:

    # Variável para controlar o loop interno.
    i = 0

    # Loop interno para comparar elementos adjacentes.
    while i < n:

      # Se o elemento atual for maior que o próximo elemento,
      # troque as posições deles.
      if vetor[i] > vetor[i + 1]:
        vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]

      # Incremente o contador do loop interno.
      i += 1

    # Decremente o contador do loop externo.
    n -= 1

  return vetor
