def bayes_theorem(p_e1, p_e2, p_a_e1, p_a_e2):

    p_a = p_e1 * p_a_e1 + p_e2 * p_a_e2

    p_e1_a = p_e1*p_a_e1 / p_a
    return p_e1_a
#P(E1)
p_e1 = 1/2
#P(E2)
p_e2 = 1/2
#P(A|E1)
p_a_e1 = 3/5
#P(A|E2)
p_a_e2 = 3/7
# calculate P(A|B)
result = bayes_theorem(p_e1, p_e2, p_a_e1, p_a_e2)
# summarize
print('P(E1|A) = %.3f%%' % (result))
