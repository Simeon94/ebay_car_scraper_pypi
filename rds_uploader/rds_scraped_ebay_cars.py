import sys
import os.path
#sys.path.append(os.path.join(os.path.dirname(__file__), r'C:\Users\Simeon\PycharmProjects\car_scraper_packages'))
from car_scraper.car_scraping_1 import Carscraper
#import boto3
import psycopg2 
from sqlalchemy import create_engine
import os
import pandas as pd


class DataHandling:

    def __init__(self):
        self.carscraper = Carscraper()
        self.DATABASE_TYPE = 'postgresql'
        self.DBAPI = 'psycopg2'
        self.HOST = 'aicoredb.cjpo05djrpn0.eu-west-2.rds.amazonaws.com'  #input('Enter your host address: ')  # 'aicoredb.cjpo05djrpn0.eu-west-2.rds.amazonaws.com' '[18.132.161.210]'
        self.USER = 'postgres'  #input('Enter your user: ')  # postgres
        self.PASSWORD = input('Enter your password: ') 
        self.PORT = 5432
        self.DATABASE = 'postgres'
        self.cur = None
        self.df = None
        self.car_df = None
        #self.conn = psycopg2.connect(f"dbname=self.DATABASE user=self.USER password=self.PASSWORD host=18.132.161.210 port=5432")
        self.conn = psycopg2.connect(f"dbname=postgres user=postgres password={self.PASSWORD} host=18.132.161.210 port=5432")
        self.cur = self.conn.cursor()

        


    def load_csv(self):
        with open(r"car_data_df.csv", 'r') as f:
             self.cars_data_df = pd.read_csv(f, index_col=0)
        print(self.cars_data_df )
        

    def create_rds_table(self):
        self.cur.execute("DROP TABLE IF EXISTS cars")
        self.cur.execute("CREATE TABLE cars (manufacturer VARCHAR(255), model VARCHAR(255), sale_price VARCHAR(255), year VARCHAR(255), transmission VARCHAR(255), fuel VARCHAR(255), mileage VARCHAR(255), condition VARCHAR(255), location VARCHAR(255), contact_number VARCHAR(255))")
        self.conn.commit()


    def store_data_in_database(self):
        #engine = create_engine(f"{self.DATABASE_TYPE}+{self.DBAPI}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}")
        
        engine = create_engine(
            f"{self.DATABASE_TYPE}+{self.DBAPI}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}")
        engine.connect()
        self.cars_data_df.to_sql('cars', engine, if_exists='replace', index=False)

    def query_database(self):
        self.cur.execute("SELECT * FROM cars")
        result = self.cur.fetchall()
        for r in result:
            print(r)
        self.conn.close()

    def run_data(self):
        self.load_csv()
        self.create_rds_table()
        self.store_data_in_database()
        self.query_database()

pushdata = DataHandling()

pushdata.run_data()