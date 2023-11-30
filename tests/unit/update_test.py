import pytest
import src.requesto as rq


@pytest.fixture()
def resource_setup():
    database = rq.postgresqlConnect(host="83.220.170.127",
                                    port="5432",
                                    userName="dolta",
                                    dbName="coredb")
    uD = database.Table("userData", database.cursor)
    return uD


def test_1_pg_update(resource_setup):
    assert resource_setup.update("username, points, gay", "'name41', 20000, false", "id = 5")
    assert resource_setup.update("username, points, gay", "'name41', 20000, false")
    assert resource_setup.update("points", "0", "gay = true")


def test_2_pg_update(resource_setup):
    assert resource_setup.update("points", "0", "gay = true")
