import pytest
import src.requesto as rq


@pytest.fixture()
def resource_setup():
    pass


def test_1_pg_table(resource_setup):
    database = rq.postgresqlConnect(host="83.220.170.127",
                                    port="5432",
                                    userName="dolta",
                                    dbName="coredb")
    assert database
    assert database is not None


def test_2_sqlt_table(resource_setup):
    assert rq.sqliteConnection(ifMemory=True)
    assert rq.sqliteConnection(filename="")



