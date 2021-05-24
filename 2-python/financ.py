def saldo(saldo, taxa, nmeses):
  i = 0
  while i < nmeses:
    saldo = saldo * taxa + saldo
    i += 1

  return saldo

def teste():
  return 10 + 10