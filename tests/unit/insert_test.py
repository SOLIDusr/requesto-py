import psycopg2
import pytest
import src.requesto as rq


@pytest.fixture()
def resource_setup():
    database = rq.postgresqlConnect(host="83.220.170.127",
                                    port="5432",
                                    userName="dolta",
                                    dbName="coredb")
    uD = database.Table("userData", database.connection.getCursor())
    return uD


def test_1_insert(resource_setup):
    assert resource_setup.insert("username, id, points, gay", "'khabib', 5, 20000, false")
    assert resource_setup.insert("username, id, points, gay", "'Com', 6, 12, false")


def test_2_insert_error(resource_setup):
    assert not resource_setup.insert("user, id, points, gay", "'khabib', 5, 20000, true")
    assert not resource_setup.insert("points, gay", "'20000', true")
    assert not resource_setup.insert("username, id, points, gay", "'khabib', 2, 20000, true")

