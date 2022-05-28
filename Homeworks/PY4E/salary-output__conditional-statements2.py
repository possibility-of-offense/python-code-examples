hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter Rate:')
r = float(rate)

if h > 40:
    sum = 40 * r
    diff = (h - 40) * r * 1.5
    print(float(sum + diff))
else:
    print(float(h * r))