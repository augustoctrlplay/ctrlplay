def tabuada(valor, inicio = 0, fim = 10):
    if inicio > fim: inicio, fim = fim, inicio

    texto = ''

    for i in range(fim + 1): texto += f'{i} X {valor} = {i * valor}\n'
    
    return texto

print(tabuada(5))