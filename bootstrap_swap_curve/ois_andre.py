import math

d1 = 1 / 1.003
d2 = 1 / 1.0065
d3 = 1 / 1.01005
d4 = 1 / 1.014

d5 = 1 / 1.018
d7 = 1 / 1.028
d6 = (d5 + d7) / 2

d10 = 1 / (1 + 0.0045 * 10)

d8 = d7 + 1/3 * (d10-d7)
d9 = d7 + 2/3 * (d10-d7)

d15 = 1 / (1 + 0.005 * 15)

d11 = d10 + 1/5 * (d15-d10)
d12 = d10 + 2/5 * (d15-d10)
d13 = d10 + 3/5 * (d15-d10)
d14 = d10 + 4/5 * (d15-d10)

d20 = 1 / (1 + 0.00525 * 20)

d16 = d15 + 1/5 * (d20-d15)
d17 = d15 + 2/5 * (d20-d15)
d18 = d15 + 3/5 * (d20-d15)
d19 = d15 + 4/5 * (d20-d15)

d30 = 1 / (1 + 0.0055 * 30)

d21 = d20 + 1/10 * (d30-d20)
d22 = d20 + 2/10 * (d30-d20)
d23 = d20 + 3/10 * (d30-d20)
d24 = d20 + 4/10 * (d30-d20)
d25 = d20 + 5/10 * (d30-d20)
d26 = d20 + 6/10 * (d30-d20)
d27 = d20 + 7/10 * (d30-d20)
d28 = d20 + 8/10 * (d30-d20)
d29 = d20 + 9/10 * (d30-d20)

discount_factors = [
    d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30
]

l1 = d1 * 0.003
pv_prev = l1
for i in range(1, 30):
	# print(i, discount_factors[i])
	pv = sum(discount_factors[0:i+1]) * ( ((1/discount_factors[i])-1) / (i+1) )
	tmp = (1 / discount_factors[i]) * (pv - pv_prev)
	f_val = 360 * (math.pow((tmp+1), 1/360) - 1)
	print("dis_fac:", discount_factors[i], "\tf"+str(i+1), f_val, "\tpv"+str(i+1), pv)
	pv_prev = pv


