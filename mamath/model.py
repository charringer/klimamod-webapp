import numpy as np

class Model(object):
    default_params = {
        'var_epsilon': 0.69,
        'var_Q': 340.0,
        'var_mu': 1.0,
    }

    param_keys = default_params.keys()

    def __init__(self, modelid, params={}):
        self.params = self.default_params.copy()

        self.set_model(modelid)
        self.set_params(params)

    def set_model(self, modelid):
        if modelid == 'fraedrich':
            self.name = 'Fraedrich'
            self.f = self.__f_fraedrich
        elif modelid == 'griffeldrazin':
            self.name = 'Griffel & Drazin'
            self.f = self.__f_griffeldrazin
        else:
            raise ValueError('unknown model: %s' % modelid)

    def set_params(self, params):
        unknown_params = params.keys() - self.default_params.keys()
        if unknown_params:
            raise ValueError('unknown params: %s' % unknown_params)
        for key, value in params.items():
            self.params[key] = float(value)

    def get_f(self):
        return lambda T: self.f(T, 1)

    def get_f_with_Qfactor(self):
        return lambda T, Qf: self.f(T, Qf)

    def __f_fraedrich(self, T, Qfactor):
        var_T = T
        var_Q = self.params['var_Q'] * Qfactor
        var_epsilon = self.params['var_epsilon']
        var_mu = self.params['var_mu']

        var_sigma = 5.67E-8
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

    def __f_griffeldrazin(self, T, Qfactor):
        var_T = T
        var_Q = self.params['var_Q'] * Qfactor
        var_mu = self.params['var_mu']

        var_I = 1367
        var_T0 = 284.15
        var_sigma = 5.67E-8

        var_h = 75
        var_rho = 1E3
        var_cw = 4.19E3
        var_c = var_h * var_rho * var_cw

        return ((0.5 * np.tanh(var_T ** 6 / var_T0 ** 6) - 1) * var_sigma * var_T ** 4 + var_mu * var_Q * (0.58 + 0.2 * np.tanh(0.052 * (var_T - 276.15)))) / var_c
