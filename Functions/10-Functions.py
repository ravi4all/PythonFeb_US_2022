temps = [34.5,36.7,32.56,33.56,38.7,36.45]
kms = [45.5, 230, 34.33, 154]

f = list(map(lambda c : 9 / 5 * c + 32, temps))
print(f)

ms = list(map(lambda km : km * 1000, kms))
print(ms)