numbers = input('Sample Data: ')
print(f'List: {(numbers.replace(",", "")).split()}')
print(f'Tuple: {tuple((numbers.replace(",", "")).split())}')
