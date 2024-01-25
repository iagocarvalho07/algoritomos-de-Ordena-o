def insertion_sort(lista):
  """
  Ordena uma lista em ordem crescente usando o algoritmo de ordenação por inserção.

  Args:
    lista: A lista a ser ordenada.

  Returns:
    Uma lista ordenada.
  """

  # Começa com a segunda posição da lista.

  for i in range(1, len(lista)):

    # Armazena o elemento atual.

    chave = lista[i]

    # Inicializa o índice do elemento anterior.

    j = i - 1

    # Enquanto o elemento atual for menor que o elemento anterior...

    while j >= 0 and chave < lista[j]:

      # ...move o elemento anterior para a frente.

      lista[j + 1] = lista[j]

      # Diminui o índice do elemento anterior.

      j -= 1

    # Insere o elemento atual na posição correta.

    lista[j + 1] = chave

  return lista
