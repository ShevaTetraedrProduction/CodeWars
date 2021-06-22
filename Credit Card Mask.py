def maskify(cc):
  return ('#' * (len(cc) - 4)) + cc[-4:]

print(maskify('NANANANANNANANANANANANANA BATMAN!'))
print(maskify('13421'))
print(maskify('Skippy'))