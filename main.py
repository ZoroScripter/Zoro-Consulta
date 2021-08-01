import os
import time
import requests
from data import cep,ip,covid,cpf_gerar,cnpj
os.system("clear")
os.system("pkg install figlet")
os.system("python3 main.py")
os.system("clear")
print("\033[1;36m")
print("""
:::::::::  ::::::::  :::::::::  :::::::::   ::::::::  
     :+:  :+:    :+: :+:    :+: :+:    :+: :+:    :+: 
    +:+   +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ 
   +#+    +#+    +:+ +#++:++#:  +#++:++#:  +#+    +:+ 
  +#+     +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ 
 #+#      #+#    #+# #+#    #+# #+#    #+# #+#    #+# 
#########  ########  ###    ### ###    ###  ########  
""")
#Começando o Painel!!
print("""\033[1;32m
(҂`_´) - By: Zoro
<,︻╦̵̵̿╤─ ҉ - -- --- - -- --\033[1;35m
=========================
CONSULTAS:              -
[1]CEP [ON]             =
[2]IP [ON]              -
[3]Covid19              =
[4]Gerar CPF            -
[5]CNPJ                 =
[6]Sair                 -
=========================
""")
op = input(">>> ")

#chamando as Consultas!!
if op == "1":
	cep.consultar()
elif op == "2":
	ip.consultar()
elif op == "3":
	covid.consultar()
elif op == "4":
    cpf_gerar.consultar()
elif op == "5":
    cnpj.consultar()
elif op == "6":
	os.system("clear")
	time.sleep(2)
	print("Saindo...")
	time.sleep(5)
	exit()
else:
	os.system("python3 main.py")


#Recado!!
#================================================================#
#Bem Este Painel Foi preciso ser pago para Ter As Consultas!!    #
#E eu queria que vcs me ajudassem a poder pagar o painel para    #
#ter mais consultas liberadas para vc!!                          #
#================================================================#

#Como vcs pode me ajudar:
#######################################
#Se inscrevam no meu Canal: Zoro     #
#Deixem o like nos meus Vídeos      #
#Ativem as notificações!!          #
###################################
