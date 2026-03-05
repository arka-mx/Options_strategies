import matplotlib.pyplot as plt

class bear_put_spread:
    def __init__(self):
        self.set_otm = 1950 #buy
        self.set_itm = 1800 #sell
        self.set_otm_premium = 30
        self.set_itm_premium = 80
        self.payoffs = []
        
    
    def payoff(self):
        net_premium = -self.set_otm_premium+self.set_itm_premium
        self.spread = self.set_otm-self.set_itm
        payoff=0
        for spot_price in range(self.set_itm-2*self.spread,self.set_otm + 2*self.spread):
            if(spot_price<=self.set_itm):
                payoff = net_premium + spot_price-self.set_itm + self.set_otm-spot_price
                self.payoffs.append(payoff)
            elif(spot_price<=self.set_otm):
                payoff = net_premium + spot_price-self.set_otm
                self.payoffs.append(payoff)
            else:
                payoff = net_premium
                self.payoffs.append(net_premium)
    
    def plotting(self):
        x = list(range(self.set_itm-2*self.spread,self.set_otm + 2*self.spread))
        y = self.payoffs
        plt.legend()
        plt.plot(x,y,label = "Payoffs")
        plt.xlabel("Spot prices")
        plt.ylabel("Payoffs")
        plt.title("Bear put spread")
        plt.show()


obj = bear_put_spread()
obj.payoff()
obj.plotting()