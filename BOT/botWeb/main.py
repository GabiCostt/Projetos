from importacoes import *

destinatario = 'alessandracssudi@hotmail.com'
assunto = 'E-mail automatico'
msg ='''
Olá mamaezinha, este é um email automatico que estou testando,
espero que você goste!!!'''

"""Uma função que abre automaticamente o navegador google chrome,
entra no microsoft outlook e envia uma mensagem predefinida."""
def main():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://outlook.live.com')
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
    sleep(2)
    #Incerir email
    navegador.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(email)
    navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    sleep(2)
    #Incerir senha
    navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(senha)
    navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
    sleep(7)
    navegador.find_element(By.XPATH, '//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[2]/div/div/span/button[2]/span/i/span/i').click()
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="Ribbon-588Dropdown"]/div/ul/li/div/ul/li[1]/button/div/span').click()
    #Incerir assunto da mensagem
    sleep(4)
    navegador.find_element(By.XPATH, '//*[@id="TextField250"]').send_keys(assunto)
    #Incerir mensagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="editorParent_1"]/div').send_keys(msg)
    #Incerir destinatario 
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[3]/div/div/div[2]').send_keys(destinatario)
    #clicar em enviar email
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[2]/div[1]/div/span/button[1]/span/i').click()
    
if __name__ == '__main__':
    main()
