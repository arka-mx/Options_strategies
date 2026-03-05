import matplotlib.pyplot as plt
import sys
class bull_call_spread:
    #initialising the derivative prices
    def __init__(self):
        self.set_atm = 120
        self.set_otm  =140
        self.set_atm_premium = 5
        self.set_otm_premium = 2
        self.set_market_price = 70
        self.payoffs = []
    #taking user input
    def user_input(self):
        self.set_atm=int(input("Enter the CALL option value that you are going to buy ATM = "))
        self.set_atm_premium = int(input("Enter the premium for this CALL option = "))
        self.set_otm=int(input("Enter the CALL option value that you are going to sell OTM = "))
        self.set_otm_premium = int(input("Enter the premium for this CALL option = "))
        if(self.set_otm_premium>self.set_atm_premium):
            print("ARBITRAGE !!")
            sys.exit()
        self.set_market_price = int(input("Enter the market price = "))
    
    #calculating the payoffs and appending them in an array
    def payoff(self):
        s = self.set_market_price
        self.spread = self.set_otm - self.set_atm
        for spot_price in range(s,2*self.spread+self.set_otm):
            if(spot_price<=self.set_atm):
                self.payoffs.append(-self.set_atm_premium+self.set_otm_premium)
            elif(spot_price>self.set_atm and spot_price<self.set_otm):
                self.payoffs.append(-self.set_atm_premium+self.set_otm_premium+spot_price-self.set_atm)
            else:
                self.payoffs.append(-self.set_atm_premium+self.set_otm_premium+self.spread)
    def payoff1(self):
        s=self.set_market_price
        self.spread = self.set_otm - self.set_atm
        for spot_price in range(s,2*self.spread+self.set_otm):
            self.payoffs.append(-self.set_atm_premium+self.set_otm_premium+ max(spot_price-self.set_atm,0) - max(spot_price-self.set_otm,0))
    #plotting the payoffs  
    def plotting(self):
        y = self.payoffs
        x = list(range(self.set_market_price,2*self.spread+self.set_otm))
        plt.plot(x,y,label="Payoffs")
        plt.legend()
        plt.xlabel("Spot prices")
        plt.ylabel("Payoffs")
        plt.title("Bull call spread")
        plt.show()
    

obj = bull_call_spread()
choice = input("Choose either USER or AUTO..\n")
if(choice=="USER"):
    obj.user_input()
obj.payoff1()
obj.plotting()