#url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = " "

#sanitização da url
url = url.replace(" ","")

#validação da url
if url == " ":
    raise ValueError("Url esta vazia")

#separa bases e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]
print(url_parametro)

#busca um valor de um parâmetro

parametro_busca = ''
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)