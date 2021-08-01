import os
import time
import requests
from data import covid,ip,covid,cpf_gerar,cep

os.system("clear")
os.system("pkg install figlet")
os.system("pip install requests")
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
	os.system("python3 cep.py")
elif op == "2":
	os.system("python3 ip.py")
elif op == "3":
	os.system("clear")
	os.system("figlet Zoro")
	print("\033[1;33mDigite O estado Para Saber A situação Da Covid!!")
	os.system("python3 covid.py")
elif op == "4":
    os.system("python3 cpf_gerar.py")
elif op == "5":
    os.system("python3 cnpj.py")
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
