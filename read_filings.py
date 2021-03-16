from beautifulsoup4 import BeautifulSoup

with open("./sec-edgar-filings/AAPL/8-K/0001104659-15-019336/filing-details.html", "r") as f:
    read_data = BeautifulSoup(f, 'html.parser')

    print(read_data.getText())
