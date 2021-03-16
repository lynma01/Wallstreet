from sec_edgar_downloader import Downloader

# Initialize a downloader instance. If no argument is passed
# to the constructor, the package will download filings to
# the current working directory.
dl = Downloader("./filings")

# Get all 8-K filings for Apple (ticker: AAPL)
dl.get("8-K", "AAPL")