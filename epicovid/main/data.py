import pandas as pd
from datetime import datetime, date, timedelta
import math
from epicovid.main.date import REGIONS

LINK = "https://raw.githubusercontent.com"
USER = "CSSEGISandData"
REPONAME = "COVID-19"
BRANCH = "master"
PATHTOFILE = f"csse_covid_19_data/csse_covid_19_daily_reports"


class Data:

    def __init__(self):
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()
        self.df3 = pd.DataFrame()
        self.totalConfirmedByDay, self.totalDeathByDay = [], []
        self.TotalConfirmedByDay = []
        self.allData = []
        self.tabConf = []
        self.confirmedByCountry, self.deathByCountry, self.recoveredByCountry = [], [], []
        self.confirmedByProvince, self.deathByProvince, self.recoveredByProvince = [], [], []

        last_update = date.today()
        while self.df.empty == True:
            try:
                url = f"{LINK}/{USER}/{REPONAME}/{BRANCH}/{PATHTOFILE}/{last_update.strftime('%m-%d-%Y')}.csv"
                self.df = pd.read_csv(url, error_bad_lines=False)
                url2 = f"{LINK}/{USER}/{REPONAME}/{BRANCH}/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
                self.df2 = pd.read_csv(url2, error_bad_lines=False)
                url3 = f"{LINK}/{USER}/{REPONAME}/{BRANCH}/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
                self.df3 = pd.read_csv(url3, error_bad_lines=False)
            except:
                last_update -= timedelta(days=1)
        self.lastUpdate = last_update
        self.fillConfirmedByDay()
        self.fillDeathByDay()
        #self.allData = self.df.values.tolist()
        self.region = REGIONS
        self.min, self.max = self.minMaxConfirmed()
        self.fillByCountry()
        self.fillByProvince()
        self.initTabConf()

    def initTabConf(self):
        for index, row in self.df.iterrows():
            if math.isnan(row['Lat']) or math.isnan(row['Long_']) or math.isnan(row['Confirmed']):
                continue
            self.tabConf.append((row['Lat'], row['Long_'], row['Confirmed']))

    def minMaxConfirmed(self):
        return (self.df["Confirmed"].min(), self.df["Confirmed"].max())

    def fillConfirmedByDay(self):
        """ Fill the tab of global confirmed cases by day
        """
        values = list(self.df2)
        for day in values[4:]:
            total = sum(self.df2[day])
            self.totalConfirmedByDay.append((day, total))

    def fillDeathByDay(self):
        """ Fill the tab  of global death count by day
        """
        values = list(self.df3)
        for day in values[4:]:
            total = sum(self.df3[day])
            self.totalDeathByDay.append((day, total))

    def getTotalConfirmed(self):
        return(sum(self.df['Confirmed']))

    def fillByCountry(self):
        """ Fill the tab confirmed, death and recovered by country of the class
        """
        for row in self.df.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered'].sum().iterrows():
            self.confirmedByCountry.append((row[0], row[1][0]))
            self.deathByCountry.append((row[0], row[1][1]))
            self.recoveredByCountry.append((row[0], row[1][2]))

    def fillByProvince(self):
        """ Fill the tab confirmed, death and recovered by province of the class
        """
        for row in self.df.groupby('Province_State')['Confirmed', 'Deaths', 'Recovered'].sum().iterrows():
            self.confirmedByProvince.append((row[0], row[1][0]))
            self.deathByProvince.append((row[0], row[1][1]))
            self.recoveredByProvince.append((row[0], row[1][2]))

    def getTotalDeath(self):
        return(sum(self.df['Deaths']))

    def getTotalRecovered(self):
        return(sum(self.df['Recovered']))
