import random

passLen = int(input('Enter the length of password : '))
s = 'wegksajfdsjfsfisf1221!@#$'
p = ''.join(random.sample(s,passLen))
print(p)



