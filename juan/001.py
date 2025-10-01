ano_atual = int(input("digite o ano atual: "))

ano_nascimento = int(input("Digite o ano que você nasceu: "))

idade = ano_atual - ano_nascimento

if idade >= 18:
  
  print(f"Você nasceu em {ano_nascimento}. Neste ano de {ano_atual}, você tem {idade} anos e já possui mais de 18 anos")

else:
  
  print(f"Você nasceu em {ano_nascimento}. Neste ano de {ano_atual}, você tem {idade} anos e não possui mais de 18 anos.")