from tkinter import *
from turtle import title

def somar(*number):
    total = 0
    for num in number:
        total += num
    return total


def dividir(a=0, b=0):
    return a / b
    

while True:
    usuario = int(input('Digite um valor inteiro: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in continuar:
        break

janela = Tk()

janela.title('Soma e Divisão')
label_soma = Label(janela, text='Qual opção você gostaria de efetuar?:')
label_soma.grid(column=0, row=0, padx=10, pady=10)
button_somar = Button(janela, text='SOMAR', command=somar)
button_somar.grid(column=0, row=1, padx=10, pady=10)
button_dividir = Button(janela, text='DIVIDIR', command=dividir)
button_dividir.grid(column=1, row=1, padx=10, pady=10)


janela.mainloop()