num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in num: is_prime = True
if num > 1:
 for i in range(1,15, num):
  if num % i == 0:
   is_prime = False
  break
if is_prime: primes.append(num)
else: not_primes.append(num)
print("Простые числа:", primes)
print("Не простые числа:", not_primes)
