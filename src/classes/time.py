#Class time
class Time:
    def __init__(self, t):
        self.t0_abs = t
        self.t = 0 #Simulation time
        self.dt = 0 #dt between loops
        self.t_aux = 0

    def update(self, t):
        self.t = t - self.t0_abs
        self.dt = self.t - self.t_aux
        self.t_aux = self.t

    def get_dt(self):
        return self.dt

    def get_t(self):
        return self.t

