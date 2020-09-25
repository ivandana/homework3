#Solution 3.11

SENTINEL = -1
miles_per_gallon = 0.0
total_miles_per_gallon = 0.0
total_miles, total_gallon = 0.0, 0.0

while True:
    gallon = float(input('Enter gallon used (-1 to exit):'))
    if gallon == SENTINEL:
      #print(f'The mile/gallon for this tank was {total_miles_per_gallon:.6f}')
      break
    miles = float(input('Enter the miles driven:'))
    miles_per_gallon = miles/gallon
    total_miles += miles
    total_gallon += gallon
    
    print(f'The mile/gallon for this tank was {miles_per_gallon:.6f}')
    
print(f'The overall miles/gallon was {total_miles/total_gallon:.6f}')

