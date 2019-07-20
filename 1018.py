notes = [100, 50, 20, 10, 5, 2, 1]

N = int(input())
print(N)

for amount in notes:
    number_of_notes = N // amount
    N -= amount * number_of_notes
    print('{} nota(s) de R$ {},00'.format(number_of_notes, amount))
