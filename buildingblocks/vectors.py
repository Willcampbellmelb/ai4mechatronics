def elementwise_multiplication(vec_a,vec_b):
	assert (len (vec_a) == len(vec_b))
	output = [0 for x in range(len(vec_b))]
	for i in range(len(a)):
		output[i] = vec_a[i] * vec_b[i]
	return output

def elementwise_addition(vec_a,vec_b):
	assert (len (vec_a) == len(vec_b))
	output = [0 for x in range(len(vec_b))]
	for i in range(len(a)):
		output[i] = vec_a[i] + vec_b[i]
	return output



def vector_sum(vec_a):
	output = 0
	for i in range(len(vec_a)):
		output += vec_a[i]
	return output

def vector_average(vec_a):
	#vector sum / num of entries in vector
	return vector_sum(vec_a)/ len(vec_a)

def dot_product(vec_a, vec_b):
	output = elementwise_multiplication(vec_a, vec_b)
	dot = vector_sum(output)
	return dot

a = [ 2, 2, 5 ]
b = [ 2, 2, 3 ]

mlply = elementwise_multiplication(a,b)
print (mlply)

add = elementwise_addition(a,b)
print (add)

vec_summing = vector_sum(a)
print (vec_summing)

avg = vector_average(a)
print(avg)

dot_p = dot_product(a,b)
print(dot_p)
