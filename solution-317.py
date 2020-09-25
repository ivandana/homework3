#solution 3.17

print('(a)')
for i in range(1,11):
    print(f'{"* " * i:<20}')

print()

print('(b)')
for j in range(1,11):
    p = 11 - j
    print(f'{"* " * p:<20}')

print()

print('(c)')
for k in range(1,11):
    p = 11 - k
    print(f'{"* " * p:>20}')

print()

print('(d)')
for l in range(1,11):
    print(f'{"* " * l:>20}')

print()    