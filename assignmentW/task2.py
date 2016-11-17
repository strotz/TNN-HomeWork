from math import exp, pow

print "Let's run"

W_xh=-0.1
W_hh=0.5
W_hy=0.25

H_bias=0.4

def sum(input, before):
	return W_xh * input + W_hh * before + H_bias

def sigma(input):
	return 1/(1+exp(-input))

def y_out(input):
	return W_hy * input

def e_out(input, target):
	return 0.5 * pow((target - input), 2)

z1 = sum(18, 0)
h1 = sigma(z1)
y1 = y_out(h1)
t1 = 0.1
e1 = e_out(y1, t1)
print z1, h1, y1, e1

z2 = sum(9, h1)
h2 = sigma(z2)
y2 = y_out(h2)
t2 = -0.1
e2 = e_out(y2, t2)
print z2, h2, y2, e2

z3 = sum(-8, h2)
h3 = sigma(z3)
y3 = y_out(h3)
t3 = -0.2
e3 = e_out(y3, t3)
print z3, h3, y3, e3

E1 = -1.0 * (t1 - y1) * W_hy * z1 * (1 - z1)
E2 = -1.0 * (t2 - y2) * W_hy * z2 * (1 - z2) * W_hh * z1 * (1 - z1)
print E1 + E2
