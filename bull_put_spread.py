import matplotlib.pyplot as plt
import sys
class bull_call_spread:
    #initialising the derivative prices
    def __init__(self):
        self.set_otm = 3450 #buy
        self.set_itm  =3500 #sell
        self.set_otm_premium = 60
        self.set_itm_premium = 90
        self.payoffs = []
    
    def payoff(self):
        self.spread = self.set_itm-self.set_otm
        net_premium = -self.set_otm_premium+self.set_itm_premium
        payoff=0
        for spot_price in range(self.set_otm - 2*self.spread,self.set_itm+2*self.spread):
            if(spot_price<=self.set_otm):
                payoff = net_premium + self.set_otm-spot_price -self.set_itm+spot_price
                self.payoffs.append(payoff)
            elif(spot_price<=self.set_itm):
                payoff = net_premium + spot_price - self.set_itm
                self.payoffs.append(payoff)
            else:
                payoff = net_premium
                self.payoffs.append(payoff)
    def payoff1(self):
        self.spread = self.set_itm-self.set_otm
        net_premium = -self.set_otm_premium + self.set_itm_premium
        for spot_price in range(self.set_otm-2*self.spread,self.set_itm+2*self.spread):
            self.payoffs.append(net_premium + max(self.set_otm-spot_price,0) -max(self.set_itm-spot_price,0) )

    def plotting(self):
        y = self.payoffs
        x = list(range(self.set_otm - 2*self.spread,self.set_itm+2*self.spread))
        plt.plot(x,y,label="Payoffs")
        plt.legend()
        plt.xlabel("Spot prices")
        plt.ylabel("Payoffs")
        plt.title("Bull put spread")
        plt.show()

obj = bull_call_spread()
obj.payoff1()
obj.plotting()