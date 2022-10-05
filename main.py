import pandas as pd
import sqlite3

def database():
    df=pd.read_excel(r'data.xls')
    tab=df.groupby('API WELL  NUMBER').sum().reset_index()
    connection=sqlite3.connect('C:/Users/phili/Desktop/sqlite3/Details.db')
    tab.to_sql(
        name='table',
        con=connection,
        if_exists='replace',
        index=False,
        dtype={'API WELL  NUMBER':'integer',
                'OIL':'integer',
                'GAS':'integer',
                'BRINE':'integer'})

    connection.commit()
    connection.close()

database()