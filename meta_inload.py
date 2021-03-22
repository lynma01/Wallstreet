import src.metadata.sec_metadata as md

if __name__ == "__main__":
    list(md.SecMeta().get_filing_metadata(name="Oracle Corp", cik="0001341439", filing="10-K", no_filings=5))

    print('metadata inload complete!')

