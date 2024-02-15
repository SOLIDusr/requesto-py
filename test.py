import src.requesto as rq


db = rq.postgresqlConnect(host="83.220.170.127", port="5432", userName="dolta", dbName="coredb", autoParce=True,
                          schemaName="public")
for table in db.tables:
    print(table)