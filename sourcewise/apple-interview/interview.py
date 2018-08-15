r = 0.0085
f = 0.00166
p = 3000
n = 360
sumc = 0
sumn = 0
for i in range(n):
    sumc = (1+r-f)*(sumc + p)
    sumi = (1+0-f)*(sumn + p)
    sumn = (1+0-0)*(sumn + p)
print(sumc, sumi, sumn)