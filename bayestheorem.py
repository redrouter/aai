def bayes_theorem(p_e1, p_e2, p_a_e1, p_a_e2):

    p_a = p_e1 * p_a_e1 + p_e2 * p_a_e2

    p_e1_a = p_e1*p_a_e1 / p_a
    return p_e1_a

p_e1 = 1/2
p_e2 = 1/2
p_a_e1 = 3/5
p_a_e2 = 3/7
result = bayes_theorem(p_e1, p_e2, p_a_e1, p_a_e2)
print('P(E1|A) = %.3f%%' % (result))
