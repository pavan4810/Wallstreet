from wallstreet import Stock, Call, Put


def get_tickers():
    tickers_list = []
    tickers_file_path = 'tickers'  # Replace with your file path
    with open(tickers_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            tickers_list.append(line.strip())

        print("List of tickers considered :", tickers_list)
    return tickers_list


if __name__ == "__main__":
    tickers = get_tickers()
    for ticker in tickers:
        print("Fetching data for :", ticker)
        ticker_calls = Call('SPY')
        ticker_expirations = ticker_calls.expirations
        print("Expirations ", ticker_expirations)
        for expiration in ticker_expirations:
            date, month, year = expiration.split('-')
            c = Call('SPY', d=int(date), m=int(month), y=int(year))
            for strike in c.strikes:
                c.set_strike(strike)
                print(strike, [c.theta, c.rho, c.vega, c.gamma, c.delta, c.implied_volatility, c.volume, c.open_interest, c.cp, c.change, c.price, c.ask, c.bid])
