import threading
import time
import yfinance as yf

print("|| || ||   Welcome To The Dividend Simulator   || || ||")


class DividendSimulator:
    def __init__(self):
        print("|| || ||Dividend Simulator Has Been Initialized|| || ||\n")
        self.final_value = None
        self.final_shares = None

    def simulate_growth(self, shares, share_price, yield_rate, years):
        for year in range(1, years + 1):
            dividend_income = (yield_rate / 100) * share_price * shares
            new_shares_bought = dividend_income / share_price
            shares += new_shares_bought

            print(f"Year {year}")
            print(f"Dividend Income: {dividend_income:.2f}")
            print(f"New Shares Bought: {new_shares_bought:.2f}")
            print(f"Total Shares: {shares:.2f}\n")

            time.sleep(1)

        self.final_value = shares * share_price
        self.final_shares = shares

    def get_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        info = stock.info
        dividend_yield = info.get("dividendYield")
        current_price = info.get("regularMarketPrice")
        if dividend_yield is not None:
            dividend_yield *= 1  # convert to percentage
        return dividend_yield, current_price

    def main(self):
        while True:
            ticker = input("Enter the ticker symbol: ").upper()
            dividend_yield, current_price = self.get_stock_data(ticker)

            if dividend_yield is None or dividend_yield == 0:
                print(f"No dividend yield found for {ticker}. Please enter another ticker with dividends.\n")
                continue
            if current_price is None or current_price == 0:
                print(f"Could not fetch price for {ticker}. Please enter a valid ticker.\n")
                continue

            print(f"Dividend yield for {ticker}: {dividend_yield:.2f}%")
            print(f"Current stock price for {ticker}: ${current_price:.2f}\n")
            break

        shares = int(input("Enter the number of shares: "))
        simulation_years = int(input("Enter the simulation years: "))
        print("\nStarting Simulation...\n")

        sim_thread = threading.Thread(
            target=self.simulate_growth,
            args=(shares, current_price, dividend_yield, simulation_years)
        )
        sim_thread.start()
        sim_thread.join()

        initial_value = shares * current_price
        growth_rate = ((self.final_value - initial_value) / initial_value) * 100

        print("----- Simulation Complete -----")
        print(f"Beginning Portfolio Value: ${initial_value:.2f}")
        print(f"Final Shares: {self.final_shares:.2f}")
        print(f"Final Portfolio Value: ${self.final_value:.2f}")
        print(f"Total Growth Rate: {growth_rate:.2f}%")

        self.write_to_file(self.final_value, self.final_shares, growth_rate, shares, current_price, simulation_years,
                           ticker, dividend_yield)

    def write_to_file(self, final_value, final_shares, growth_rate, shares, current_price, years, ticker,
                      dividend_yield):
        with open("dividend_yield.txt", "w") as file:
            file.write("Dividend Reinvestment Simulation Report\n")
            file.write(f"Ticker Symbol: {ticker}\n")
            file.write(f"Dividend Yield: {dividend_yield:.2f}%\n")
            file.write(f"Beginning Portfolio Value: ${shares * current_price:.2f}\n")
            file.write(f"Final Shares: {final_shares:.2f}\n")
            file.write(f"Final Portfolio Value: ${final_value:.2f}\n")
            file.write(f"Total Growth Rate: {growth_rate:.2f}%\n")
            file.write(f"Simulation Years: {years}\n")
        print("\nResults have been saved to dividend_yield.txt")


DividendSimulator().main()
