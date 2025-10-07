idade = int(input("digite sua idade: "))

if idade >= 0 and idade <= 11:
    print("classificação: criança")

if idade >= 12 and idade <= 18:
    print("classificação: adoslencente")

if idade >= 19 and idade <= 24:
    print ("classificação: jovem")

if idade >= 25 and idade <= 40:
    print ("classificação: adulto")

if idade >= 41 and idade <= 59:
    print ("classificação: meia idade")

if idade >= 60:
    print("classificação: idoso")
