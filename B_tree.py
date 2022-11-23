from bs4 import BeautifulSoup
import pandas as pd
# import urllib.request



class Search_B_tree():

    def __init__(self,link,indice):
        
        self.link = link
        self.indice = indice
        self.table = ""
        self.df = ""
        self.count = ""
        self.extension = ""

    def get_extension(self):

        extension = self.link.split(".")[-1]
        self.extension = extension

    def get_pandas_df(self):

        if self.extension == 'csv':
            self.df = pd.read_csv(self.link, encoding = 'cp1252', skiprows = 11, sep = ';')
        else:
            raise "extension is not defined"

        self.df.head()

    def size_of_df(self):
        pass

    def build_B_tree(self):
        pass