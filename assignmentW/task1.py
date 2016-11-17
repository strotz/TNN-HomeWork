from math import exp, pow

print "Let's run"

W_xh=0.5
W_hh=-1.0
W_hy=-0.7

H_bias=-1.0

def sum(input, before):
	return W_xh * input + W_hh * before + H_bias

def sigma(input):
	return 1/(1+exp(-input))

def y_out(input):
	return W_hy * input

def e_out(input, target):
	return 0.5 * pow((target - input), 2)

z = sum(9, 0)
h = sigma(z)

z = sum(4, h)
h = sigma(z)
y = y_out(h)

print y
