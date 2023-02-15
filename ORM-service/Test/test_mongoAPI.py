import pytest
import sys

sys.path.insert(0, "..")

from datetime import datetime
from mongoengine import *
from ..Schema import Exact

connection = connect("mongoenginetest", host="mongomock://localhost")

Schemas = {"Exact": Exact}


def test_Schema_updatebyExternalId_new():
    data = {
        "data": {
            "companyId": 17,
            "company": "TEST ComPany",
            "customers": "On",
            "invoices": "Off",
            "vendors": "On",
            "vendorsInvoices": "Off",
            "payments": "On",
            "exactServer": "TESTSERVER.com",
            "clientId": "clientId",
            "clientSecret": "clientSecret",
            "dataTransferred": datetime.utcnow(),
            "dataModified": datetime.utcnow(),
        }
    }
    for key, value in Schemas.items():
        result = value.updatebyCompanyId(data)
        assert key == value.__name__
        assert data["data"]["exactServer"] == result["exactServer"]


def test_Schema_updatebyExternalId_update():
    data = {
        "data": {
            "companyId": 17,
            "company": "TEST ComPany",
            "customers": "On",
            "invoices": "Off",
            "vendors": "On",
            "vendorsInvoices": "Off",
            "payments": "On",
            "exactServer": "TESTSERVER.com",
            "clientId": "clientId",
            "clientSecret": "clientSecret",
            "dataTransferred": datetime.utcnow(),
            "dataModified": datetime.utcnow(),
        }
    }
    for key, value in Schemas.items():
        assert key == value.__name__
        result = value.updatebyCompanyId(data)
        print(key)
        print(result)
        assert result["companyId"] == 17
