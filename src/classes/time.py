#Class time
class Time:
    def __init__(self, t):
        self.t0_abs = t
        self.t = 0      #Simulation time
        self.tp = 0     #Paused time
        self.tg = 0     #Game time
        self.dt = 0     #dt between loops
        self.t_aux = 0
    
    def t_paused(self, paused):
        if paused:
            self.tp += self.dt

    def update(self, t, paused):
        self.t = t - self.t0_abs
        self.dt = self.t - self.t_aux
        self.t_aux = self.t
        self.t_paused(paused)
        self.tg = self.t - self.tp

class Timer:
    def __init__(self):
        self.cond = False
        self.t = 0
    
    def reset(self):
        self.cond = False
        self.t = 0

    def timer(self, cond, tmax, dt): #return true during 'tmax' time
        if (cond or self.cond) and self.t<tmax:
            self.cond = True
            self.t += dt
            return True
        else:
            self.reset()
            return False

class Counter:
    def __init__(self):
        self.t = 0

    def reset(self):
        self.t = 0

    def counter(self, cond, tmax, dt): #return true after 'tmax' time and cond=True
        if cond:
            if self.t>=tmax:
                self.reset()
                return True
            else:
                self.t += dt
                return False
        else:
            self.reset()
            return False
