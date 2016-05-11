import numpy as np

def f_fraedrich(T, Qfactor):
    var_T = T
    var_Q = 340 * Qfactor
    var_epsilon = 0.69
    var_sigma = 5.67E-8
    var_mu = 1
    var_a = 2.8
    var_b = 0.009

    var_p = var_mu * var_Q * var_b / var_epsilon / var_sigma
    var_q = - var_mu * var_Q * (1 - var_a) / var_epsilon / var_sigma

    var_h = 75
    var_rho = 1E3
    var_cw = 4.19E3
    var_c = var_h * var_rho * var_cw

    cut = 227.78
    res_above = var_epsilon * var_sigma / var_c * (- var_T ** 4 + var_p * var_T - var_q)
    res_below = var_epsilon * var_sigma / var_c * (- var_T ** 4 + var_p / 4 / var_b)

    return (T > cut) * res_above + (T <= cut) * res_below

def f_griffeldrazin(T, Qfactor):
    var_T = T
    var_Q = 340 * Qfactor
    var_mu = 1
    var_I = 1367
    var_T0 = 284.15
    var_sigma = 5.67E-8
    
    var_h = 75
    var_rho = 1E3
    var_cw = 4.19E3
    var_c = var_h * var_rho * var_cw

    return ((0.5 * np.tanh(var_T ** 6 / var_T0 ** 6) - 1) * var_sigma * var_T ** 4 + var_mu * var_Q * (0.58 + 0.2 * np.tanh(0.052 * (var_T - 276.15)))) / var_c
