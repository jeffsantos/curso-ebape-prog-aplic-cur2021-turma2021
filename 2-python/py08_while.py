
saldo = 1000
taxa_mes = 0.7/100
nmeses = 12

print("While ----")
i= 0
while i < nmeses:
  saldo = saldo * taxa_mes + saldo
  print(i)
  i+=1

print(f"O saldo final após {nmeses} meses é de {saldo}")