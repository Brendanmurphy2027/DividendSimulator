# Dividend Simulator
A simple command-line Python tool that simulates dividend reinvestment growth over time. This project helps investors understand the power of compounding dividends by automatically reinvesting earnings into new shares each year.

Features
User-friendly console interface

Simulates annual dividend compounding and share reinvestment

Displays yearly breakdown of dividend income, new shares purchased, and total shares

Calculates final portfolio value and total growth rate after simulation

Automatically exports results to dividend_yield.txt

How It Works
The program asks for:

Number of starting shares

Current share price

Annual dividend yield (percentage)

Number of years to simulate

It calculates dividend income each year and reinvests it into buying new shares.

After completing the simulation, a performance summary is printed and written to a file.

Example Output
text
|| || ||   Welcome To The Dividend Simulator   || || ||

Enter the number of shares: 100
Enter the price per share: 50
Enter the annual dividend yield (e.g. 3.5 for 3.5%): 4
Enter the simulation years: 5

Starting Simulation...

Year 1
Dividend Income: 200.00
New Shares Bought: 4.00
Total Shares: 104.00

...
----- Simulation Complete -----
Beginning Portfolio Value: $5000.00
Final Shares: 121.67
Final Portfolio Value: $6083.33
Total Growth Rate: 21.67%
Results have been saved to dividend_yield.txt
Output File
The file dividend_yield.txt stores a full summary of your simulation, including:

Beginning portfolio value

Final shares and value

Total growth rate

Requirements
Python 3.8 or higher

Works on Windows, macOS, and Linux

How to Run
Clone the repository

text
git clone https://github.com/yourusername/dividend-simulator.git
cd dividend-simulator
Run the script

text
python3 dividend_simulator.py
Future Improvements
Support for variable dividend growth per year

Integration of share price appreciation

Visualization of reinvestment performance with matplotlib
