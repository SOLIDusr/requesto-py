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


def test_1_pg_insert(resource_setup):
    assert resource_setup.insert("username, id, points, gay", "'name41', 5, 20000, false")
    assert resource_setup.insert("username, id, points, gay", "'Con', 6, 12, false")
    assert resource_setup.insert("username, id", "'conn', 8")
    assert resource_setup.insert("id", "9")

