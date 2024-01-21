def merge_sort(lista):
  """
  Ordena a lista usando o algoritmo Mergesort.

  Args:
    lista: A lista a ser ordenada.

  Returns:
    A lista ordenada.
  """

  if len(lista) <= 1:
    return lista

  meio = len(lista) // 2
  metade_esquerda = merge_sort(lista[:meio])
  metade_direita = merge_sort(lista[meio:])

  return merge(metade_esquerda, metade_direita)

def merge(lista_esquerda, lista_direita):
  """
  Combina duas listas ordenadas em uma única lista ordenada.

  Args:
    lista_esquerda: A primeira lista a ser combinada.
    lista_direita: A segunda lista a ser combinada.

  Returns:
    A lista combinada.
  """

  lista_ordenada = []
  i = 0
  j = 0

  while i < len(lista_esquerda) and j < len(lista_direita):
    if lista_esquerda[i] < lista_direita[j]:
      lista_ordenada.append(lista_esquerda[i])
      i += 1
    else:
      lista_ordenada.append(lista_direita[j])
      j += 1

  lista_ordenada.extend(lista_esquerda[i:])
  lista_ordenada.extend(lista_direita[j:])

  return lista_ordenada
