import pytest
import src.requesto as rq


@pytest.fixture()
def resource_setup():
    database = rq.postgresqlConnect(host="83.220.170.127",
                                    port="5432",
                                    userName="dolta",
                                    dbName="coredb")
    return database


def test_1_pg_insert(resource_setup):
    assert resource_setup.tables[0] in ["userdata", "test"]
    assert resource_setup.tables
    assert len(resource_setup.tables) == 2
