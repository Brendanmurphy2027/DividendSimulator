import os
print("|| || ||   Welcome To The Dividend Simulator   || || ||")
class DividendSimulator:
    def __init__(self):
        print("|| || ||Dividend Simulator Has Been Initialized|| || ||\n")

    def simulate_growth(self, shares, share_price, yield_rate, years):
        for year in range(1, years + 1):
            dividend_income = (yield_rate / 100) * share_price * shares
            new_shares_bought = dividend_income / share_price
            shares += new_shares_bought

            print(f"Year {year}")
            print(f"Dividend Income: {dividend_income:.2f}")
            print(f"New Shares Bought: {new_shares_bought:.2f}")
            print(f"Total Shares: {shares:.2f}\n")

        total_value = shares * share_price
        return total_value, shares

    def main(self):
        shares = int(input("Enter the number of shares: "))
        current_share_price = float(input("Enter the price per share: "))
        annual_dividend_yield = float(input("Enter the annual dividend yield (e.g. 3.5 for 3.5%): "))
        simulation_years = int(input("Enter the simulation years: "))
        print("\nStarting Simulation...\n")

        final_value, final_shares = self.simulate_growth(shares, current_share_price, annual_dividend_yield, simulation_years)
        initial_value = shares * current_share_price
        growth_rate = ((final_value - initial_value) / initial_value) * 100

        print("----- Simulation Complete -----")
        print(f"Beginning Portfolio Value: ${initial_value:.2f}")
        print(f"Final Shares: {final_shares:.2f}")
        print(f"Final Portfolio Value: ${final_value:.2f}")
        print(f"Total Growth Rate: {growth_rate:.2f}%")

        self.write_to_file(final_value, final_shares, growth_rate, shares, current_share_price, simulation_years)

    def write_to_file(self, final_value, final_shares, growth_rate, shares, current_share_price, years):
        with open("dividend_yield.txt", "w") as dividend_yield_file:
            dividend_yield_file.write("Dividend Reinvestment Simulation Report\n")
            dividend_yield_file.write(f"Beginning Portfolio Value: ${shares * current_share_price:.2f}\n")
            dividend_yield_file.write(f"Final Shares: {final_shares:.2f}\n")
            dividend_yield_file.write(f"Final Portfolio Value: ${final_value:.2f}\n")
            dividend_yield_file.write(f"Total Growth Rate: {growth_rate:.2f}%\n")
        print("\nResults have been saved to dividend_yield.txt")

DividendSimulator().main()
