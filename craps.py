from random import randint
from time import sleep
def lancar_dados():
    dado1 = randint(2,6)
    dado2= randint(2,6)
    soma_dos_dados = dado1 + dado2
    return soma_dos_dados

def jogar_craps():
    resultado = lancar_dados()
    for i in range(3,0,-1):
        print(f'Lançando dados em {i}...')
        sleep(1)
        
    print(f'Resultado do primeiro lançamento: {resultado}')
    if (resultado == 7 or resultado == 11):
        print("Vencedor Natural")
        return 
    elif (resultado == 3 or resultado == 2 or resultado == 12):
        print("Perdedor Craps")
        return 
    else:
        ponto = resultado
        print(f'Sou ponto é {ponto}. Continue Jogando')
        for i in range(3,0,-1):
            print(f'Lançando dados em {i}...')
            sleep(1)
        while True:
            sleep(2)
            resultado = lancar_dados()
            print(f"Resultado do Lançamento: {resultado}")
            if resultado == ponto:
                print("Você venceu! Você repetiu o ponto")
                return
            elif resultado == 7:
                print("Você perdeu! Saiu 7 antes de repetir o ponto")
                return
            
    
jogar_craps()
        

