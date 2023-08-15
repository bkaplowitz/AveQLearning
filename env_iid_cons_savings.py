import numpy as np
# TODO: Clone and replace with
#  simple Kaplan et al variant from Matlab Code.
class ConsSavingsIID:
    # Params
    beta = 0.96
    risk_aver = 2
    r = 0.04
    R = 1+r
    # Income Grid
    mu_y= 1
    sd_y = 0.4
    ny = 5
    # Asset Grid
    na = 80
    amax = 50
    borrow_lim = 0.0
    agrid_par = 0.5
    max_iter = 1000
    tol_iter = 1.0e-6
    nsim = 50_000
    tsim = 1000
    agrid = linspace(0,1,na)
    
    
    
    
    
    def generator(self, T):
        trans = np.zeros(shape=(T, self.S*self.A, self.S))
        for sa in range(self.S*self.A):
            s_next = np.random.choice(self.S, T, p=self.P[sa])
            trans[[_ for _ in range(T)], sa, s_next] = 1.0
        return trans
