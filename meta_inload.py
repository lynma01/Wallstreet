import metadata.sec_metadata as md

print(list(md.SecMeta().get_filing_metadata(name="Oracle Corp", cik="0001341439", filing="10-K", no_filings=5)))

