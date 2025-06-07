# 💱 Currency Exchange App (Tkinter + AlphaVantage)

This mini desktop app lets you convert currencies in real-time using the AlphaVantage API. It’s simple, sleek, and uses themed widgets so your eyes don’t bleed. 

## 🧾 What It Does

* Converts currency values between EUR, USD, and GBP
* Uses real-time exchange rates from AlphaVantage
* Built with `Tkinter`, `ttkthemes`, and `ttk` 

## 🧪 Tech Stack

* `Python`
* `Tkinter` + `ttk` for GUI
* `ttkthemes` (for the sweet Equilux dark mode)
* `requests` for HTTP requests to the AlphaVantage API

## 📦 Requirements

You'll need to install two libraries:
requests and ttkthemes

You also need an [AlphaVantage API key](https://www.alphavantage.co/support/#api-key). One-liner signup, no soul-selling required.

## 🚀 How to Run

```bash
python CE.py
```

## 🎯 How to Use

1. Enter the amount you want to convert.
2. Select the “From” currency.
3. Select the “To” currency.
4. Click `Convert`.
5. Marvel at the magic of exchange rates.

## 🧠 Behind the Scenes

It sends a GET request to this endpoint:

```
https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=XXX&to_currency=YYY&apikey=YOUR_KEY
```

Then parses the JSON response to get the current exchange rate and multiply it by your entered amount.


