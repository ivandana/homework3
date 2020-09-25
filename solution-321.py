#solution 3.21

quarter, dime, nickel, penny = 25, 10, 5, 1
q_count, d_count, n_count, p_count = 0, 0, 0, 0 

dollar_in_cents = 100
balance = 0

cost_of_purchase = int(input('Enter an amount in cents:'))
print(f'Cost of purchase is {cost_of_purchase} cents.')
balance = dollar_in_cents - cost_of_purchase

if not balance:
  print (f'Your change is {balance}') 

print(f'Your change is :')
if balance >= 25:
    q_count = balance//quarter
    if q_count != 0:
      print(f'{q_count} quarter(s)')
    balance %= quarter

if balance >= 10:
    d_count = balance//dime
    if d_count != 0:
      print(f'{d_count} dime(s)')
    balance %= dime

if balance >= 5:
    n_count = balance//nickel
    if n_count != 0:
      print(f'{q_count} nickel(s)')
    balance %= nickel

if balance >= 0:
    p_count = balance//penny
    if p_count != 0:
      print(f'{p_count} penny(ies)')
    balance = 0              
