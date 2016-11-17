from math import exp, pow

print "Let's run"

W_xh=0.5
W_hh=-1.0
W_hy=-0.7

H_bias=-1.0

def sigma(input):
	return 1/(1+exp(-input))

def sigma_back(output):
	return output * (1-output)

def h_out(input, before):
	sum = W_xh * input + W_hh * before + H_bias
	return sigma(sum)

def y_out(input):
	return W_hy * input

def e_out(input, target):
	return 0.5 * pow((target - input), 2)

h = h_out(9, 0)
h = h_out(4, h)

print h
