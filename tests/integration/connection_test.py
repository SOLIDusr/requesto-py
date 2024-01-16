import pytest
import src.requesto as rq


@pytest.fixture()
def resource_setup():
    database = rq.postgresqlConnect(host="83.220.170.127",
                                    port="5432",
                                    userName="dolta",
                                    dbName="coredb")
    return database


def test_1_pg_table(resource_setup):
    assert resource_setup.Table("userdata", resource_setup.cursor)
    assert resource_setup.Table

