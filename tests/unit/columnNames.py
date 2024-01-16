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
    uD = resource_setup.Table("userData", resource_setup.cursor)
    assert uD.columns
    assert len(uD.columns) != 0
    assert "username" in uD.columns
    assert "id" in uD.columns
    assert "email" in uD.columns
    assert "password" in uD.columns
    testDB = resource_setup.Table("test", resource_setup.cursor)
    assert testDB is not None
