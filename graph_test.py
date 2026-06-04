# ==========================================
# AI TRADING SIMULATOR
# Resume-Level Beginner Quant Project
# ==========================================
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import random

# ------------------------------------------
# SPLASH WINDOW
# ------------------------------------------

splash = tk.Tk()

splash.title("Loading")

splash.geometry("500x300")

splash.configure(bg="black")

# Splash Text
splash_label = tk.Label(
    splash,
    text="ZUMBO TRADING PROJECT",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="black"
)

splash_label.pack(expand=True)

# Close splash after 3 seconds
splash.after(3000, splash.destroy)

# Run splash screen
splash.mainloop()

# ------------------------------------------
# MAIN WINDOW
# ------------------------------------------

root = tk.Tk()

root.title("AI Trading Simulator")

root.geometry("900x800")

root.configure(bg="#e6f2ff")

# ------------------------------------------
# INITIAL DATA
# ------------------------------------------

balance = 10000

portfolio = 0

stock_price = 100

price_history = [stock_price]

trade_history = []

# ------------------------------------------
# TITLE
# ------------------------------------------

title = tk.Label(
    root,
    text="AI TRADING SIMULATOR",
    font=("Arial", 24, "bold"),
    bg="#e6f2ff",
    fg="#003366"
)

title.pack(pady=20)

# ------------------------------------------
# BALANCE LABEL
# ------------------------------------------

balance_label = tk.Label(
    root,
    text=f"Balance: ₹{balance}",
    font=("Arial", 16),
    bg="#e6f2ff"
)

balance_label.pack()

# ------------------------------------------
# PORTFOLIO LABEL
# ------------------------------------------

portfolio_label = tk.Label(
    root,
    text=f"Stocks Owned: {portfolio}",
    font=("Arial", 16),
    bg="#e6f2ff"
)

portfolio_label.pack()

# ------------------------------------------
# STOCK PRICE LABEL
# ------------------------------------------

price_label = tk.Label(
    root,
    text=f"Current Stock Price: ₹{stock_price}",
    font=("Arial", 18, "bold"),
    bg="#e6f2ff",
    fg="green"
)

price_label.pack(pady=20)

# ------------------------------------------
# TRADE HISTORY BOX
# ------------------------------------------

history_box = tk.Text(
    root,
    height=5,
    width=70,
    font=("Arial", 12)
)

history_box.pack(pady=20)

# ------------------------------------------
# UPDATE MARKET FUNCTION
# ------------------------------------------

def update_market():

    global stock_price

    # Random market movement
    change = random.randint(-10, 10)

    stock_price += change

    price_history.append(stock_price)

    # Minimum stock price
    if stock_price < 10:
        stock_price = 10

    price_label.config(
        text=f"Current Stock Price: ₹{stock_price}"
    )

    # AI Suggestion
    if change > 5:
        ai_text = "AI Suggestion: Market rising quickly"

    elif change < -5:
        ai_text = "AI Suggestion: Market falling"

    else:
        ai_text = "AI Suggestion: Stable market"

    ai_label.config(text=ai_text)

# ------------------------------------------
# BUY STOCK FUNCTION
# ------------------------------------------

def buy_stock():

    global balance
    global portfolio

    if balance >= stock_price:

        balance -= stock_price

        portfolio += 1

        history_box.insert(
            tk.END,
            f"Bought stock at ₹{stock_price}\n"
        )

        update_labels()

    else:

        messagebox.showwarning(
            "Insufficient Balance",
            "Not enough money to buy stock"
        )

# ------------------------------------------
# SELL STOCK FUNCTION
# ------------------------------------------

def sell_stock():

    global balance
    global portfolio

    if portfolio > 0:

        balance += stock_price

        portfolio -= 1

        history_box.insert(
            tk.END,
            f"Sold stock at ₹{stock_price}\n"
        )

        update_labels()

    else:

        messagebox.showwarning(
            "No Stocks",
            "You do not own any stocks"
        )

# ------------------------------------------
# UPDATE LABELS FUNCTION
# ------------------------------------------

def update_labels():

    balance_label.config(
        text=f"Balance: ₹{balance}"
    )

    portfolio_label.config(
        text=f"Stocks Owned: {portfolio}"
    )

# ------------------------------------------
# AI ANALYSIS FUNCTION
# ------------------------------------------

def show_analysis():

    total_assets = balance + (portfolio * stock_price)

    profit = total_assets - 10000

    if profit > 1000:
        analysis = "Excellent Trading Performance"

    elif profit > 0:
        analysis = "Good Trading Strategy"

    else:
        analysis = "Loss Detected - Improve Strategy"

    message = f"""
FINAL ANALYSIS

Current Balance: ₹{balance}

Stocks Owned: {portfolio}

Total Assets: ₹{total_assets}

Profit/Loss: ₹{profit}

AI Analysis:
{analysis}
"""

    messagebox.showinfo(
        "Trading Analysis",
        message
    )

# ------------------------------------------
# AI LABEL
# ------------------------------------------

ai_label = tk.Label(
    root,
    text="AI Suggestion: Waiting for market movement",
    font=("Arial", 14, "italic"),
    bg="#e6f2ff",
    fg="blue"
)

ai_label.pack(pady=10)

# ------------------------------------------
# BUTTON FRAME
# ------------------------------------------

button_frame = tk.Frame(root, bg="#e6f2ff")

button_frame.pack(pady=20)

# ------------------------------------------
# BUY BUTTON
# ------------------------------------------

buy_button = tk.Button(
    button_frame,
    text="Buy Stock",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    padx=20,
    pady=10,
    command=buy_stock
)

buy_button.grid(row=0, column=0, padx=10)

# ------------------------------------------
# SELL BUTTON
# ------------------------------------------

sell_button = tk.Button(
    button_frame,
    text="Sell Stock",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    padx=20,
    pady=10,
    command=sell_stock
)

sell_button.grid(row=0, column=1, padx=10)

# ------------------------------------------
# UPDATE MARKET BUTTON
# ------------------------------------------

market_button = tk.Button(
    button_frame,
    text="Update Market",
    font=("Arial", 14, "bold"),
    bg="#007acc",
    fg="white",
    padx=20,
    pady=10,
    command=update_market
)

market_button.grid(row=0, column=2, padx=10)

# ------------------------------------------
# ANALYSIS BUTTON
# ------------------------------------------

analysis_button = tk.Button(
    root,
    text="Show AI Analysis",
    font=("Arial", 14, "bold"),
    bg="#222222",
    fg="white",
    padx=20,
    pady=10,
    command=show_analysis
)

analysis_button.pack(pady=20)

#graph function

def show_graph():

    plt.plot(price_history)

    plt.title("Stock Price Graph")

    plt.xlabel("Updates")

    plt.ylabel("Price")

    plt.grid(True)

    plt.show()

#graph button function

graph_button = tk.Button(
    root,
    text="GRAPH TEST",
    bg="yellow"
)

graph_button.pack(pady=10)

root.mainloop()