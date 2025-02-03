import math

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def get_nominal_returns(self):

        nominal_returns = [math.nan] * 120


        for idx in range(120, len(self.df)):
        # Loop to account for reinvested dividends
            R_t_1 = 0
            R_t = 0
            P_t_1 = 0
            P_t = 0
            for i in range(120):
                if i == 0:
                    R_t  = self.df["P"].iloc[idx-120+i]
                    P_t = self.df["P"].iloc[idx-120+i]
                else:
                    P_t_1 = self.df["P"].iloc[idx-120+i-1]
                    d_t_1 = self.df["D"].iloc[idx-120+i-1]
                    R_t_1 = (R_t/P_t) * (P_t_1 + d_t_1/12)

                    R_t = R_t_1
                    P_t = P_t_1

                ret = (R_t / self.df["P"].iloc[idx-120]) ** (1/10) - 1    
            nominal_returns.append(ret)
            
        return nominal_returns
    
    def get_real_returns(self):
        real_returns = [math.nan]*120
        for i in range(120,len(self.df)):
            curr_real_price = self.df["Real Total Return Price"][i]
            # accumulated_dividends = df["D"][i-120:i].sum()
            accumulated_dividends = 0
            prev_real_price = self.df["Real Total Return Price"][i-120]

            real_annual_return = (( (curr_real_price + accumulated_dividends) / prev_real_price ) ** (1/10)) - 1
            real_returns.append(real_annual_return)

        return real_returns
    
    def get_real_bond_returns(self):
        bond_returns = [math.nan]*120
        for i in range(len(self.df)-120):
            ret = (self.df['Real Bond Returns'][i+120]/self.df['Real Bond Returns'][i])**(1/10) - 1
            bond_returns.append( ret ) 
        return bond_returns
