def temp_convert(c):
    return 9/5 * c + 32

def km_to_m(km):
    return 1000 * km

# temp = 34.5
# print(temp_convert(temp))

temps = [34.5,36.7,32.56,33.56,38.7,36.45]
# f = []
# for i in range(len(temps)):
#     f.append(temp_convert(temps[i]))
#
# print(f)

kms = [45.5, 230, 34.33, 154]
# ms = []
# for i in range(len(kms)):
#     ms.append(km_to_m(kms[i]))

f = list(map(temp_convert, temps))
print(f)

ms = list(map(km_to_m, kms))
print(ms)