import matplotlib.pyplot as plt

class long_straddle:
    def __init__(self):
        self.set_call=200 #buy
        self.set_put=200#buy
        self.set_call_premium=30
        self.set_put_premium=10
        self.payoffs = []
        
    
    def payoff(self):
        net_premium = -self.set_put_premium-self.set_call_premium
        self.spread = self.set_put-self.set_call
        for spot_price in range(50,350):
            self.payoffs.append(net_premium + max(self.set_put-spot_price,0) + max(spot_price-self.set_call,0))
    
    def plotting(self):
        x = list(range(50,350))
        y = self.payoffs
        plt.legend()
        plt.plot(x,y,label = "Payoffs")
        plt.xlabel("Spot prices")
        plt.ylabel("Payoffs")
        plt.title("Long straddle")
        plt.show()


obj = long_straddle()
obj.payoff()
obj.plotting()