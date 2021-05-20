
saldo = 1000
taxa_mes = 0.7/100
nmeses = 12

print("For -----")
for i in range(nmeses):
    saldo = saldo * taxa_mes + saldo
    print(i)

print(f"O saldo final após {nmeses} meses é de {saldo}")