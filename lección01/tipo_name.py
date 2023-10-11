import math
from decimal import Decimal


#Nan (Not a Nuber)
a = float('nan')
print(f'a:{a}')

# Módulo Math
a = float('nan')
print(f'¿Es de tipo NaN(Not a Number)?: {math.isnan(a)}')

#Módulo decimal
a = Decimal('nan')
print(f'¿Es de tipo NaN(Not a Number)?: {math.isnan(a)}')