import math
import json
import re

d_0_6m = 1 / ( 1 + 0.5 * 0.025 )
# d1 = ( 1 - 0.014 * d_0_6m ) / 1.014
d1 = ( 1 - 0.5 * 0.0280 * d_0_6m ) / ( 1 + 0.5 * 0.028 )
d2 = ( 1 - 0.5 * 0.0300 * ( d_0_6m + 1.5 * d1 )) / ( 1 + 0.5 * 1.5 * 0.0300 )

d3 = ( 1 - 0.5 * 0.0315 * ( d_0_6m + 1.5 * d1 + 2 * d2 ) ) / ( 1 + 0.5 * 1.5 * 0.0315 )

print(d_0_6m, d1, d2, d3)

# discount_factors = [
#     1/1.003,
# ]

# discount_factors_dict = {}

# # rate = [
# #     0.00300,
# #     0.00325,
# #     0.00335,
# #     0.00350,
# #     0.00360,
# # ]

# rates_table = {
#     # '1Y' : { 'rate' : 0.00300, 'diff': 1 },
#     '2Y' : { 'rate' : 0.00325, 'diff': 1 },
#     '3Y' : { 'rate' : 0.00335, 'diff': 1 },
#     '4Y' : { 'rate' : 0.00350, 'diff': 1 },
#     '5Y' : { 'rate' : 0.00360, 'diff': 1 },
#     '7Y' : { 'rate' : 0.00400, 'diff': 2 },
#     '10Y': { 'rate' : 0.00450, 'diff': 3 },
#     '15Y': { 'rate' : 0.00500, 'diff': 5 },
#     '20Y': { 'rate' : 0.00525, 'diff': 5 },
#     '30Y': { 'rate' : 0.00550, 'diff': 10 },
# }

# benchmark_tenors_involving_interpolation = [
#     '5Y', '7Y', '10Y', '15Y', '20Y', '30Y',
# ]

# # for tenor in rates_table:
# # 	print("rate: ", rates_table[tenor]['rate'], "diff: ", rates_table[tenor]['diff'])

# l1 = d1 * 0.003
# pv_prev = l1

# coefficients = []
# numerators = []

# results = {}
# # for i in range(1, 5):
# for tenor in rates_table:
# 	# print("discount_factors: ", discount_factors)
# 	# print("rate["+str(i)+"]: ", rate[i])
# 	# discount_factor_n_1 = ( pv_prev - rate[i] * sum(discount_factors) + discount_factors[-1] ) / ( ( rate[i] + 1 ) * discount_factors[-1] )
# 	# discount_factor = discount_factors[-1] * discount_factor_n_1
# 	# print("D("+str(i)+","+str(i+1)+"): ", discount_factor_n_1)
# 	# print("D(0,"+str(i+1)+"): ", discount_factor)

# 	print("check rate: ", rates_table[tenor]['rate'])

# 	if rates_table[tenor]['diff'] == 1:
# 		discount_factor = ( 1 - rates_table[tenor]['rate'] * sum(discount_factors) ) / ( rates_table[tenor]['rate'] + 1 )
# 	else:
# 		# discount_factor_tmp = sum(discount_factors)
# 		discount_factor_tmp = 0
# 		for i in range(5):
# 			discount_factor_tmp += discount_factors[i]

# 		factor = sum([ i for i in range(rates_table[tenor]['diff']) ]) / rates_table[tenor]['diff']
# 		factor1 = factor + 1
# 		print("check factor: ", factor , " factor1 : ", factor1)
# 		# factor * discount_factors[-1]
# 		if len(coefficients) == 0:
# 			coefficients.extend([factor, factor1])
# 		else:
# 			coefficients[-1] = coefficients[-1] + factor
# 			coefficients.append(factor1)
# 		print("coefficients: ", coefficients)
# 		for i in range(len(coefficients)):
# 			print("tenor: ", benchmark_tenors_involving_interpolation[i], " coefficient: ", coefficients[i])

# 		numerator = coefficients[-2] * discount_factors[-1]
# 		numerators.append(numerator)
# 		print("numerators: ", numerators)

# 		# add_interpolation_discount_factors = []
# 		# add_factors = []
# 		# for i in range(len(numerators)):
# 		# 	num = numerators[i]
# 		# 	num = num * coefficients[i]
# 		# 	add_factors.append(num)
# 		# print("check add_factors: ", add_factors)

# 		discount_factor = ( 1 - rates_table[tenor]['rate'] * ( discount_factor_tmp + sum(numerators) ) ) / ( factor1 * rates_table[tenor]['rate'] + 1 )
# 		print("discount_factor[" , tenor, "]: ", discount_factor)
		
# 		# discount_factors.append( discount_factor )
# 		# print("check discount_factors111: ", discount_factors)
# 		# continue



# 	# discount_factor = ( 1 - rate[i] * sum(discount_factors) ) / ( rate[i] + 1 )

# 	discount_factors.append(discount_factor)
# 	# print(i, discount_factors[i])
# 	# implied_rate = ( 1 / math.pow(discount_factors[i], 1 / ((i+1)*360)) - 1 ) * 360
# 	# implied_rate = ( ( 1 / ( discount_factors[i] ** ((i+1)/360) ) ) - 1 ) * 360
	
# 	#implied_rate = ( ( 1 / ( discount_factors[i] ** (1/((i+1)*360)) ) ) - 1 ) * 360
# 	# implied_rate = 1 / discount_factor

# 	# print("i : ", i , "implied_rate: ", implied_rate)
# 	# pv = sum(discount_factors[0:i+1]) * ( ((1/discount_factors[i])-1) / (i+1) )
	
# 	#pv = sum(discount_factors[0:i+1]) * rate[i]

# 	pv = 1 - discount_factor

# 	# print("check discount_factors: ", discount_factors, " and rate: ", rate[i])
# 	print("so pv should be : ", pv)
# 	# tmp = (1 / discount_factors[i]) * (pv - pv_prev)
# 	tmp = ( 1 / discount_factor ) * ( pv - pv_prev )
# 	f_val = 360 * (math.pow((tmp+1), 1/360) - 1)
# 	# print("dis_fac:", discount_factors[i], "\tf"+str(i+1), f_val, "\tpv"+str(i+1), pv)
# 	print("dis_fac:", discount_factor, "\tf"+str(tenor.replace('Y','')), f_val, "\tpv"+str(tenor.replace('Y','')), pv)
# 	pv_prev = pv

# 	results[tenor] = {'dis_fac' : discount_factor, 'pv' : pv}
# 	discount_factors_dict[tenor] = discount_factor
	
# print(json.dumps(results, indent=4))

# print(json.dumps(discount_factors_dict, indent=4))

# discount_factors_dict['6Y'] = discount_factors_dict['5Y'] + 1/2 * ( discount_factors_dict['7Y'] - discount_factors_dict['5Y'] )

# discount_factors_dict['8Y'] = discount_factors_dict['7Y'] + 1/3 * ( discount_factors_dict['10Y'] - discount_factors_dict['7Y'] )
# discount_factors_dict['9Y'] = discount_factors_dict['7Y'] + 2/3 * ( discount_factors_dict['10Y'] - discount_factors_dict['7Y'] )

# discount_factors_dict['11Y'] = discount_factors_dict['10Y'] + 1/5 * ( discount_factors_dict['15Y'] - discount_factors_dict['10Y'] )
# discount_factors_dict['12Y'] = discount_factors_dict['10Y'] + 2/5 * ( discount_factors_dict['15Y'] - discount_factors_dict['10Y'] )
# discount_factors_dict['13Y'] = discount_factors_dict['10Y'] + 3/5 * ( discount_factors_dict['15Y'] - discount_factors_dict['10Y'] )
# discount_factors_dict['14Y'] = discount_factors_dict['10Y'] + 4/5 * ( discount_factors_dict['15Y'] - discount_factors_dict['10Y'] )

# discount_factors_dict['16Y'] = discount_factors_dict['15Y'] + 1/5 * ( discount_factors_dict['20Y'] - discount_factors_dict['15Y'] )
# discount_factors_dict['17Y'] = discount_factors_dict['15Y'] + 2/5 * ( discount_factors_dict['20Y'] - discount_factors_dict['15Y'] )
# discount_factors_dict['18Y'] = discount_factors_dict['15Y'] + 3/5 * ( discount_factors_dict['20Y'] - discount_factors_dict['15Y'] )
# discount_factors_dict['19Y'] = discount_factors_dict['15Y'] + 4/5 * ( discount_factors_dict['20Y'] - discount_factors_dict['15Y'] )

# discount_factors_dict['21Y'] = discount_factors_dict['20Y'] + 1/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['22Y'] = discount_factors_dict['20Y'] + 2/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['23Y'] = discount_factors_dict['20Y'] + 3/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['24Y'] = discount_factors_dict['20Y'] + 4/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['25Y'] = discount_factors_dict['20Y'] + 5/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['26Y'] = discount_factors_dict['20Y'] + 6/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['27Y'] = discount_factors_dict['20Y'] + 7/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['28Y'] = discount_factors_dict['20Y'] + 8/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )
# discount_factors_dict['29Y'] = discount_factors_dict['20Y'] + 9/10 * ( discount_factors_dict['30Y'] - discount_factors_dict['20Y'] )

# # sorted(discount_factors_dict.keys(), key=lambda s: int(re.search(r'\d+', s).group()))
# # discount_factors_dict = dict(sorted(discount_factors_dict.items(), key=lambda s: int(re.search(r'\d+', s).group())))

# # Create new dictionary
# discount_factors_dict_sorted = {}

# # sort the keys and store them in a new variable
# sorted_tenors = sorted(discount_factors_dict.keys(), key=lambda s: int(re.search(r'\d+', s).group()))

# # for all the values in sorted_value
# for tenor in sorted_tenors:
# 	print("tenor: ", tenor)
# 	# match the key element with un-sorted dictionary
# 	for key, value in discount_factors_dict.items():
# 		if key == tenor:
# 			# when matched place the key and value in the new dict
# 			discount_factors_dict_sorted[key] = value

# print(json.dumps(discount_factors_dict_sorted, indent=4))

# discount_factors_list = []
# for key, value in discount_factors_dict_sorted.items():
# 	discount_factors_list.append( value )

# for i in range(1, len(discount_factors_list)):
# 	discount_factor_numerator   = discount_factors_list[i-1]
# 	discount_factor_denominator = discount_factors_list[i]
# 	factor = discount_factor_numerator / discount_factor_denominator
# 	f_val = 360 * (math.pow(factor, 1/360) - 1)
# 	pv = 1 - discount_factor_denominator
# 	j = i+2
# 	print("f"+str(f'{j:02d}')+": ", round(f_val,10), "\td"+str(f'{j:02d}')+": ", round(discount_factors_list[i],10), "\tpv"+str(f'{j:02d}')+": ", round(pv,10))
# 	# # print(i, discount_factors[i])
# 	# # implied_rate = ( 1 / math.pow(discount_factors[i], 1 / ((i+1)*360)) - 1 ) * 360
# 	# # implied_rate = ( ( 1 / ( discount_factors[i] ** ((i+1)/360) ) ) - 1 ) * 360
	
# 	# #implied_rate = ( ( 1 / ( discount_factors[i] ** (1/((i+1)*360)) ) ) - 1 ) * 360
# 	# # implied_rate = 1 / discount_factor

# 	# # print("i : ", i , "implied_rate: ", implied_rate)
# 	# # pv = sum(discount_factors[0:i+1]) * ( ((1/discount_factors[i])-1) / (i+1) )
	
# 	# #pv = sum(discount_factors[0:i+1]) * rate[i]

# 	# pv = 1 - discount_factor

# 	# # print("check discount_factors: ", discount_factors, " and rate: ", rate[i])
# 	# print("so pv should be : ", pv)
# 	# # tmp = (1 / discount_factors[i]) * (pv - pv_prev)
# 	# tmp = ( 1 / discount_factor ) * ( pv - pv_prev )
# 	# f_val = 360 * (math.pow((tmp+1), 1/360) - 1)
# 	# # print("dis_fac:", discount_factors[i], "\tf"+str(i+1), f_val, "\tpv"+str(i+1), pv)
# 	# print("dis_fac:", discount_factor, "\tf"+str(tenor.replace('Y','')), f_val, "\tpv"+str(tenor.replace('Y','')), pv)
# 	# pv_prev = pv

# 	# results[tenor] = {'dis_fac' : discount_factor, 'pv' : pv}
# 	# discount_factors_dict[tenor] = discount_factor


