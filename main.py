# GRUPO
# Carolina de Jesus Menezes
# João Vitor Canella Rodrigues de Mesquita
# Matheus Vieira da Cunha e Silva
# Ruan Roberto da Silva Bastos
# Eutelina Cristina Ramos Machado

import threading
import time

# Criacao do lock lock
lock = threading.Lock()

# Memoria compartilhada
saldo = 1000
iteracoes = 5000

##################################
# OPERACOES SEM LOCK (INSEGURAS)
##################################

def depositar_sem_lock():
    global saldo
    for _ in range(iteracoes):
        temp = saldo
        time.sleep(0.000001)
        temp += 1
        saldo = temp

def sacar_sem_lock():
    global saldo
    for _ in range(iteracoes):
        temp = saldo
        time.sleep(0.000001)
        temp -= 1
        saldo = temp

##################################
##################################
##################################

##################################
# OPERACOES COM LOCK (SEGURAS)
##################################

def depositar_com_lock():
    global saldo
    for _ in range(iteracoes):
        with lock:
            temp = saldo
            time.sleep(0.000001)
            temp += 1
            saldo = temp

def sacar_com_lock():
    global saldo
    for _ in range(iteracoes):
        with lock:
            temp = saldo
            time.sleep(0.000001)
            temp -= 1
            saldo = temp

##################################
##################################
##################################

def executar_teste(usar_lock):
    global saldo
    saldo = 1000  
    
    modo = 'COM' if usar_lock else 'SEM'
    print(f"\n--- Execucao {modo} Lock ---")
    print(f"Saldo inicial: {saldo}")

    if usar_lock:
        t1 = threading.Thread(target=depositar_com_lock, name="Thread-Deposito-Com-Lock")
        t2 = threading.Thread(target=sacar_com_lock, name="Thread-Saque-Com-Lock")
    else:
        t1 = threading.Thread(target=depositar_sem_lock, name="Thread-Deposito-Sem-Lock")
        t2 = threading.Thread(target=sacar_sem_lock, name="Thread-Saque-Sem-Lock")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Saldo final esperado: 1000")
    print(f"Saldo final real: {saldo}")
    
    if saldo == 1000:
        print("Resultado: SUCESSO")
    else:
        print(f"Resultado: FALHA")

if __name__ == "__main__":
    executar_teste(usar_lock=False)
    executar_teste(usar_lock=True)
