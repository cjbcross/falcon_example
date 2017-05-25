import json
import pandas as pd
from sqlalchemy import create_engine
import datetime

sql = "SELECT id,areaid,"
sql += "stateclassid, namelookup_class(stateclassid),"
sql += "lastmodbyid, namelookup_user(lastmodbyid), lastmoddate, "
sql += "revision, name, description, deleted, "
sql += "(SELECT count(1) FROM lro_rules_attach where ruleid=E.id) as uploadcount,"
sql += "namelookup_area(areaid) as areaname, "
sql += "productid, namelookup_lroproduct(productid)  as productname, intervalchoice, "
sql += "(SELECT namelookup_class(theraclassid) from lro_products P where P.id=E.productid ) as theraname, "
sql += "exchangesetid, (SELECT name from lro_currency_sets S where S.id=E.exchangesetid ) as exchangesetname "
sql += " FROM lro_rules E"

def return_sql():
    engine = create_engine('postgresql://postgres:postgres@localhost/sas_lro', convert_unicode=True)
    con = engine.connect()
    df = pd.read_sql(sql, con)
    return df.to_json(orient='records')
