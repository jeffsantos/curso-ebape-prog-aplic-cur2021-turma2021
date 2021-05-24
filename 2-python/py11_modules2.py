from financ import saldo

saldo_inic = 1000
minha_taxa = 0.09
total_meses = 36

saldo_final = saldo(saldo_inic, minha_taxa, total_meses)

print(saldo_final)