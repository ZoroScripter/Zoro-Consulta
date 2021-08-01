import os
import time
import requests
#Api - https://www.consumidorpositivo.com.br/consulta-cpf-gratis/

os.system("clear")
print("\033[1;32m")
os.system("figlet Zoro-Painel")
print("\033[1;34m[*]Codado Por Zoro Com API de consumidor ksksks!!")
cpf_input = input("\033[1;35minforme o CPF: ")

if len(cpf_input) !=14:
	print("===> CPF INVALIDO!! <===")
	os.system("python3 cpf.py")

requests = requests.get("https://www.consumidorpositivo.com.br/consulta-cpf-gratis/".format(cpf_input))

address_data = requests.json()

if "erro" not in address_data:
	print("===<CPF CONSULTADO!!>===")
	print("CPF: {}".format(address_data["cpf"]))
	print("NASCIMENTO: {}".format(address_data["data_nasc"]))
	print("SEXO: {}".format(address_data["sexo"]))
	print("NOME: {}".format(address_data["nome"]))
	print("===================")
	print("===> Aguarde!! <===")
	time.sleep(4)
	print("""
	=======================
	vc fzr uma nv consulta??
	1 sim
	2 não
	""")
	op = input(">>>")
	if op == "1":
		os.system("python3 cpf.py")
	elif op == "2":
		os.system("python3 main.py")
else:
	os.system("python3 cpf.py")