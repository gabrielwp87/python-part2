
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular,
             "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))
	
	
	
    #    PyDev console: starting.
    #Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
    #from teste import cria_conta, deposita, saca, extrato
    #conta = cria_conta(123, "Gabriel", 55.0, 1000.0)
    #deposita(conta, 300)
    #extrato(conta)
    #Saldo 355.0
    #saca(conta, 100.0)
    #extrato(conta)
    #Saldo 255.0