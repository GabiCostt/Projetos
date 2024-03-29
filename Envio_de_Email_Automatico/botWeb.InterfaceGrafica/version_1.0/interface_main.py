import tkinter as tk
from tkinter import scrolledtext
from funcoes import centralizar

def enviar_mensagemOutlook():
    """Uma função que abre automaticamente o navegador Google Chrome,
       entra no Microsoft Outlook e envia uma mensagem."""
        
    from time import sleep
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://outlook.live.com')
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
    sleep(2)
    #Incerir email
    navegador.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(email.get())
    navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    sleep(2)
    #Incerir senha
    navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(senha.get())
    navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
    sleep(7)
    navegador.find_element(By.XPATH, '//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[2]/div/div/span/button[2]/span/i/span/i').click()
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="Ribbon-588Dropdown"]/div/ul/li/div/ul/li[1]/button/div/span').click()
    #Incerir assunto da mensagem
    sleep(4)
    navegador.find_element(By.XPATH, '//*[@id="TextField250"]').send_keys(assunto.get())
    #Incerir mensagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="editorParent_1"]/div').send_keys(mensagem.get(index1='1.0', index2=tk.END))
    #Incerir destinatario 
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[3]/div/div/div[2]').send_keys(destinatario.get())
    #clicar em enviar email
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[2]/div[1]/div/span/button[1]/span/i').click()
    sleep(3)

def main():
    global email
    global senha
    global destinatario
    global assunto
    global mensagem

    root = tk.Tk()
    root.geometry('525x610')
    centralizar(root)
    root.title('Formulario')
    label_info = tk.Label(text='Formulario pra envio de Mensagem', justify='center')
    label_info.grid(row=0, column=0, padx=10, pady=10, columnspan=10)

    label_email_remetente  = tk.Label(text='E-mail:', justify='center')
    label_email_remetente.grid(row=1, column=0, padx=10, pady=10, columnspan=1)
    entry_email_remetente = tk.Entry()
    entry_email_remetente.grid(row=1, column=1, padx=10, pady=10, columnspan=9)
    entry_email_remetente.config(width=50, font=('Calibri', 12))
    email = entry_email_remetente

    label_senha_remetente  = tk.Label(text='Senha:', justify='center')
    label_senha_remetente.grid(row=2, column=0, padx=10, pady=10, columnspan=1)
    entry_senha_remetente = tk.Entry()
    entry_senha_remetente.grid(row=2, column=1, padx=10, pady=10, columnspan=9)
    entry_senha_remetente.config(width=50, font=('Calibri', 12))
    senha = entry_senha_remetente

    label_email_destinatario  = tk.Label(text='Para:', justify='center')
    label_email_destinatario.grid(row=3, column=0, padx=10, pady=10, columnspan=1)
    entry_email_destinatario = tk.Entry()
    entry_email_destinatario.grid(row=3, column=1, padx=10, pady=10, columnspan=9)
    entry_email_destinatario.config(width=50, font=('Calibri', 12))
    destinatario = entry_email_destinatario

    label_assunto = tk.Label(text='Assunto:', justify='center')
    label_assunto.grid(row=4, column=0, padx=10, pady=10, columnspan=1)
    entry_assunto = tk.Entry()
    entry_assunto.grid(row=4, column=1, padx=10, pady=10, columnspan=9)
    entry_assunto.config(width=50, font=('Calibri', 12))
    assunto = entry_assunto

    label_mensagem = tk.Label(text='Mensagem', justify='center')
    label_mensagem.grid(row=5, column=0, padx=10, pady=10, columnspan=10)

    entry_mensagem = scrolledtext.ScrolledText(master=None)
    entry_mensagem.grid(row=6, column=0, padx=10, pady=10, columnspan=9)
    entry_mensagem.config(height=15, width=60, font=('Calibri', 12))    
    mensagem = entry_mensagem

    button_enviar_mensagem = tk.Button(text='Enviar', width= 50, command=enviar_mensagemOutlook)
    button_enviar_mensagem.grid(row=7, column=0, padx=10, pady=10, columnspan=10)

    root.mainloop()




    


if __name__ == '__main__':
    main()


    