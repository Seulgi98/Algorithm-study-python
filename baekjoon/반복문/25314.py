N = int(input())
n = int(N/4)
long_string = ""

for i in range(0, n):
    long_string += "long "

print(long_string + "int")