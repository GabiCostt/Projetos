import requests
from tkinter import *

def pegar_cotacoes():
    requisitacao = requests.get('http://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisitacao_dic = requisitacao.json()

    cotacao_dolar = requisitacao_dic['USDBRL']['bid']
    cotacao_euro = requisitacao_dic['EURBRL']['bid']
    cotacao_btc = requisitacao_dic['BTCBRL']['bid']

    texto = f'Dólar: {cotacao_dolar} \nEuro: {cotacao_euro} \nBitcoin: {cotacao_btc}'

    texto_cotacoes['text'] = texto


janela = Tk()
janela.geometry('290x200')

janela.title('Cotação atual das moedas')

texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas') #respectivamente digitar em qual janela sera mostrada o label e o texto que ira aparecer
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Buscar Cotações', command=pegar_cotacoes) #respectivamente digitar em qual janela sera mostrada o label e o texto que ira aparecer
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=0, pady=10)

janela.mainloop()