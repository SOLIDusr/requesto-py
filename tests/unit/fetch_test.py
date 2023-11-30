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


def test_1_pg_fetches_one(resource_setup):
    assert resource_setup.fetchOne("points", "id = 3")
    assert resource_setup.fetchOne()


def test_2_pg_fetches_many(resource_setup):
    assert resource_setup.fetchMany(size=3)
    assert resource_setup.fetchMany(size=72) != True


def test_3_pg_fetches_all(resource_setup):
    assert resource_setup.fetchAll()
    assert resource_setup.fetchAll("id")
    assert resource_setup.fetchAll("id", "points > 5000")
