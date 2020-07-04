hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

def computepay(h,r):
   if h<=40:
      pay=hr
   elif h>40:
      pay=40*r+(h-40)*r*1.5
      return(pay)
p = computepay(h,r)
print('Pay',p) 