tot = 0.0
count = 0
while True:
    i = input('Enter a number: ')

    if i == 'stop':
        break
    try:
        inp = float(i)
    except:
        print('Invalid number')
        continue
    tot = tot + inp
    count = count + 1
print('Total is: ', tot)
print('Count is: ', count)
print('Average is :', tot/count)
