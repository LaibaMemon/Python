hrs = raw_input("Enter Hours:")
h = float(hrs)

rate = raw_input("Enter Rate:")
rate = float(rate)

if h <= 40:
    pay = h * rate
elif h > 40:
    pay = 40*rate + (h-40)*rate*1.5

print pay