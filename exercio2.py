import random

def number():
  num = random.randint(1, 10)
  attempts = 3
  while attempts > 0:
    user_input = float(input('Digite um número: '))
    if( num == user_input):
      print("Parabéns você acertou o número!")
      return
    elif (user_input < num):
      print("O número é maior")
    else:
      print("O número é menor", num)
    attempts -= 1
    if( attempts > 0):
      print(f"Você tem {attempts} tentativa restante.")
  print(f"Suas tentativas acabaram. O número era {num}.")

number()