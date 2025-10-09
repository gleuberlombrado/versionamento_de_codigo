idade = int (input("Digite sua idade: ")) 
if idade <= 11:
    classificacao = "Criança"
elif 12 <= idade <= 18:
    classificacao = "Adolescente"
elif 19 <= idade <= 24:
    classificacao = "Jovem"
elif 25 <= idade <= 40:
    classificacao = "Adulto"
elif 41 <= idade <= 60:
    classificacao = "Meia Idade"
else:
    classificacao = "Idosoo"
print(f"Classificação: {classificacao}")