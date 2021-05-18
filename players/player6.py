import numpy as np
from scipy.optimize import minimize 

class player:
    name = '1st best response'
    def __init__(self): 
        self.i = None
    
    def play(self, state, history):
        i = self.i 
        j = 1-self.i 
        
        pmin,pmax = state['actions'][i]
        c = state['marginal_cost']
        delta = state['discount_factor']
        
        if len(history) == 0: 
            # initial play 
            p = (pmax - pmin)/2.0
        else: 

            p_lag = history[-1]
            pi_lag = p_lag[i]
            pj_lag = p_lag[j]

            profit_fun = state['payoffs'][i]

            if i == 0: 
                f = lambda p: -1.*profit_fun(p, pj_lag)
            else: 
                f = lambda p: -1.*profit_fun(pj_lag, p)

            res = minimize(f, pj_lag)
            pi = res.x

            
            # first idea: undercut by 10% 
            p = pj_lag * 0.9 
            
            # check if the price has gone too low 
            if (p - pmin) / (pmax - pmin) < 0.1: 
                # hike to maximum (hoping the friend follows)
                p = pmax
        
        FAIL = (p < pmin) or (p > pmax)
        if FAIL: 
            p = np.random.uniform(pmin, pmax)
        
        return p