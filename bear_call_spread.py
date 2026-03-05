import matplotlib.pyplot as plt

class bear_call_spread:
    def __init__(self):
        self.set_otm = 1950 #buy
        self.set_itm = 1800 #sell
        self.set_otm_premium = 30
        self.set_itm_premium = 80
        self.payoffs = []
    
    def payoff(self):
        net_premium = -self.set_otm_premium+self.set_itm_premium
        self.spread= self.set_otm-self.set_itm
        for spot_price in range(self.set_itm-2*self.spread,self.set_otm+2*self.spread):
            self.payoffs.append(net_premium + max(spot_price-self.set_otm,0) - max(spot_price-self.set_itm,0))
    
    def plotting(self):
        x = list(range(self.set_itm-2*self.spread,self.set_otm + 2*self.spread))
        y = self.payoffs
        plt.legend()
        plt.plot(x,y,label = "Payoffs")
        plt.xlabel("Spot prices")
        plt.ylabel("Payoffs")
        plt.title("Bear call spread")
        plt.show()

obj = bear_call_spread()
obj.payoff()
obj.plotting()