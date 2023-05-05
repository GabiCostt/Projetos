import tkinter as tk
from tkinter import scrolledtext

def window_create():
    global email
    global senha
    global destinatario
    global assunto
    global mensagem

    root = tk.Tk()
    root.geometry('525x640')
    centralizar(root)
    root.title('Formulario')
    root.resizable(False, False)

    label_info = tk.Label(text='Formulario pra envio de Mensagem', justify='center', borderwidth=1, relief='sunken')
    label_info.grid(row=1, column=0, ipadx=157, ipady=2, columnspan=10)

    label_email_remetente  = tk.Label(text='E-mail:', justify='center', borderwidth=1, relief='sunken')
    label_email_remetente.grid(row=2, column=0, ipadx=20, ipady=2, columnspan=1)
    entry_email_remetente = tk.Entry()
    entry_email_remetente.grid(row=2, column=1, padx=10, pady=10, columnspan=9)
    entry_email_remetente.config(width=50, font=('Calibri', 12))
    email = entry_email_remetente

    label_senha_remetente  = tk.Label(text='Senha:', justify='center', borderwidth=1, relief='sunken')
    label_senha_remetente.grid(row=3, column=0, ipadx=20, ipady=2, columnspan=1)
    entry_senha_remetente = tk.Entry(show='*')
    entry_senha_remetente.grid(row=3, column=1, padx=10, pady=10, columnspan=9)
    entry_senha_remetente.config(width=50, font=('Calibri', 12))
    senha = entry_senha_remetente

    label_email_destinatario  = tk.Label(text='Para:', justify='center', borderwidth=1, relief='sunken')
    label_email_destinatario.grid(row=4, column=0, ipadx=25, ipady=2, columnspan=1)
    entry_email_destinatario = tk.Entry()
    entry_email_destinatario.grid(row=4, column=1, padx=10, pady=10, columnspan=9)
    entry_email_destinatario.config(width=50, font=('Calibri', 12))
    destinatario = entry_email_destinatario

    label_assunto = tk.Label(text='Assunto:', justify='center', borderwidth=1, relief='sunken')
    label_assunto.grid(row=5, column=0, ipadx=15, ipady=2, columnspan=1)
    entry_assunto = tk.Entry()
    entry_assunto.grid(row=5, column=1, padx=10, pady=10, columnspan=9)
    entry_assunto.config(width=50, font=('Calibri', 12))
    assunto = entry_assunto

    label_mensagem = tk.Label(text='Mensagem', justify='center', borderwidth=1, relief='sunken')
    label_mensagem.grid(row=6, column=0, ipadx=220, ipady=5, columnspan=10)

    entry_mensagem = scrolledtext.ScrolledText(master=None)
    entry_mensagem.grid(row=7, column=0, padx=10, pady=10, columnspan=9)
    entry_mensagem.config(height=15, width=60, font=('Calibri', 12))
    mensagem = entry_mensagem    

    button_enviar_mensagem = tk.Button(text='Enviar', width= 50, command=enviar_mensagemOutlook)
    button_enviar_mensagem.grid(row=8, column=0, padx=10, pady=10, columnspan=10)

    button_criar_documento = tk.Button(text='Criar Documento', width= 50, command=criar_arquivo_txt)
    button_criar_documento.grid(row=9, column=0, padx=10, pady=10, columnspan=10)


    root.mainloop()


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


def centralizar(win):
    # :param win: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()


def criar_arquivo_txt():
    import datetime as dt
    email_txt = email.get().strip()
    destinatario_txt = destinatario.get().strip()
    assunto_txt = assunto.get().capitalize().strip()
    mensagem_txt = mensagem.get(index1='1.0', index2=tk.END).strip()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime('%d/%m/%Y %H:%M')

    with open('Emails_enviados.txt', 'a') as arquivo:
            arquivo.write(str(f"\nDe: {email_txt}"
                                f"\nPara: {destinatario_txt}"
                                f"\nAssunto: {assunto_txt}"
                                f"\nMenssagem: {mensagem_txt}"
                                f"\nData de Envio: {data_criacao}") + "\n")
            arquivo.write(str('='*50))
