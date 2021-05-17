def saldo(saldo, taxa, nmeses):
  i = 0
  while i < nmeses:
    saldo = saldo * taxa + saldo
    i += 1

  return saldo

saldo_final1 = saldo(1000,0.07,12)
saldo_final2 = saldo(1000,0.08,12)
saldo_final3 = saldo(1000,0.07,24)

saldo_inic = 1000
minha_taxa = 0.09
total_meses = 36

saldo_final4 = saldo(saldo_inic, minha_taxa, total_meses)

print(saldo_final1)

print(saldo_final2)

print(saldo_final3)

print(saldo_final4)