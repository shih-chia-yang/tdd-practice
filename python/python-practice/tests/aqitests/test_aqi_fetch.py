import pytest
import sys,unittest
sys.path.append("../../src/aqi")
import fetch_data

class TestAqi:
    def test_api_request(self):
        text=fetch_data.api_request(r"https://opendata.epa.gov.tw/webapi/api/rest/"
                                            r"datastore/355000000I-000259?sort=SiteName&offset=0&limit=1000")
        assert bool(text) is True