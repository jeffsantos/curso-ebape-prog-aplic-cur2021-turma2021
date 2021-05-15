
saldo = 1000
taxa_mes = 0.7/100
nmeses = 12


for i in range(nmeses-1):
    saldo = saldo * taxa_mes + saldo

print(f"O saldo final após {nmeses} meses é de {saldo}")