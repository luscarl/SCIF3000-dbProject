import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from qry_generation_trsch import formatAirports

# # Define your PostgreSQL database connection
db_uri = 'postgresql://student003:chihrusvfnihdipp@dataviation-database-1.chl8zbfpbhhh.ap-southeast-2.rds.amazonaws.com/dataviation_tutorial'

# # Create an SQLAlchemy engine
engine = create_engine(db_uri, echo=False)
conn = engine.connect()

def generateAl(origin, orig_continent, destination):
    final = formatTopAlst(orig_continent) + formatTopAlend(origin, destination)
    topal_df = pd.read_sql_query(text(final), conn)
    variables = topal_df['airline'].tolist()
    firstal = variables[0]
    secal = variables[1]
    thirdal = variables[2]
    fourthal = variables[3]
    return topal_df

def formatAlfirst(continent):
    firstStr = """
    SELECT "Op Al" as airline, SUM("Seats") as seats
    """ + "FROM cirium_traffic_"+continent

    return firstStr
    

def formatTopAlst(continent):
    firstStr = """
    SELECT "Op Al" as airline, SUM("Total Pax") AS total_pax
    """ + "FROM cirium_traffic_"+continent

    return firstStr

def formatTopAlend(orig, dest):
    finalstr = """
    Group by airline
    Order by total_pax DESC
    limit 4;
    """
    origstr = formatAirports(orig)
    deststr = formatAirports(dest)
    if len(dest) == 0 or dest[0]=='':
        return """
        WHERE "Orig" IN
        """ + origstr + """
        AND "Stop-1 Airport" is null
        """ + finalstr
    
    final = """
        WHERE "Orig" IN
    """ + origstr + """
    AND "Dest" IN
    """ + deststr + """
    AND "Stop-1 Airport" is null
    """ + finalstr

    return final
    return finalstr
    
# SELECT "Op Al" as airline, SUM("Total Pax") AS total_pax
# FROM cirium_traffic_asia
# Group by airline
# Order by total_pax DESC
# limit 3;
