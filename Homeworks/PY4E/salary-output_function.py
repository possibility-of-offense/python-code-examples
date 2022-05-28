def computepay(h, r):
    calc_left_hours_pay = 0
    pay = 0
    
    if h > 40 :
        regular_hours_pay = 40 * r 

        left_hours = h - 40
        calc_left_hours_pay = left_hours * r * 1.5
        pay = regular_hours_pay + calc_left_hours_pay
    elif h <= 40 :
        pay = h * r
        
    return pay

hrs = input("Enter Hours:")
hrs_float = float(hrs)

rate = input("Enter Rate:")
rate_float = float(rate)

p = computepay(hrs_float, rate_float)
print("Pay", p)