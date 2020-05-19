from epicovid.main.data import Data
from datetime import datetime


def getConfirmedCasesByCountry():
    data = Data().confirmedByCountry
    sorted_list = sorted(data, key=lambda x: x[1], reverse=True)
    return sorted_list


def getTotalDeathsByCountry():
    data = Data().deathByCountry
    sorted_list = sorted(data, key=lambda x: x[1], reverse=True)
    return sorted_list


def getRecoveredByCountry():
    data = Data().recoveredByCountry
    sorted_list = sorted(data, key=lambda x: x[1], reverse=True)
    return sorted_list


class Charts():
    def __init__(self, confirmedCases, deathCount, newCases):
        self.confirmedCases = confirmedCases
        self.deathCount = deathCount
        self.newCases = newCases


class ChartData():
    def __init__(self, legend, values, labels):
        self.legend = legend
        self.values = values
        self.labels = labels


def getChartsData():
    return Charts(getConfirmedCasesData(),
                  getDeathCountData(),
                  getNewCasesData())


def getConfirmedCasesData():
    legend = 'Confirmed cases'
    totalConfirmedByDay = Data().totalConfirmedByDay
    dates, values = [], []
    for item in totalConfirmedByDay:
        dates.append(datetime.strptime(item[0], '%m/%d/%y'))
        values.append(item[1])
    return ChartData(legend, values, dates)


def getDeathCountData():
    legend = 'Death count'
    totalDeathCountByDay = Data().totalDeathByDay
    dates, values = [], []
    for item in totalDeathCountByDay:
        dates.append(datetime.strptime(item[0], '%m/%d/%y'))
        values.append(item[1])
    return ChartData(legend, values, labels=dates)


def getNewCasesData():
    legend = 'New cases'
    totalConfirmedByDay = Data().totalConfirmedByDay
    dates, values = [], []
    prev, new = 0, 0
    for item in totalConfirmedByDay:
        dates.append(datetime.strptime(item[0], '%m/%d/%y'))
        new = item[1] - prev
        values.append(new)
        prev += new
    return ChartData(legend, values, dates)
