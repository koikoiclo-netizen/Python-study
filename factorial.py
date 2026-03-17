n = 7
result = 1

for i in range (1,n+1):
  result = result * i

print(result)


"関数ver"
def factorial(n):
    result = 1
    for i in range(2, n + 1):
     result *=  i
    return result

print(factorial(7))
