"""
EXERCÍCIO 114: Site está acessível?
Crie um código em python que teste se o site Pudim está acessível pelo
computador usado.
"""
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Não foi possivel acessar o site pudim no momento.')
else:
    print('O site "pudim" foi acessado com sucesso!')

    # pega o código completo do site em html
    # print(site.read())
C:\Users\Henrique Santos\PycharmProjects