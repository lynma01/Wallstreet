import unittest
import sys
sys.path.append("..")

import sec_metadata

class TestMetadata(unittest.TestCase):

    def test1(self):
        text1 = "hello world"
        text2 = "hello world!"

        self.assertEqual(text1, text2)

    def timetest(self):
        """ some version this:
        
            startTime = time.time()

            list(SecMeta().get_filing_metadata(name="Oracle Corp", cik="0001341439", filing="", no_filings=500))

            execTime = (time.time() - startTime)
            print('Execution time in seconds: ' + str(execTime))

                    --------- Results ---------
            python metadata/sec_metadata.py (5 samples)
            Execution time in seconds: 2.77056884765625
            
            python metadata/sec_metadata2.py (5 samples)
            Execution time in seconds: 1.1275997161865234

            python metadata/sec_metadata.py (500 samples)
            Execution time in seconds: 18.38187527656555

            python metadata/sec_metadata2.py (500 samples)
            Execution time in seconds: 18.86088514328003

            python metadata/sec_metadata.py (500 samples)
            Execution time in seconds: 13.800028705596924

        """