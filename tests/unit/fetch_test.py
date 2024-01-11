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


def test_3_pg_fetches_all(resource_setup):
    assert resource_setup.fetchAll()

