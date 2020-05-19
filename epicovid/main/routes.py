from flask import render_template, request, Blueprint
from epicovid.main.data import Data
from datetime import datetime
from epicovid.main.data_adapter import getConfirmedCasesByCountry, getTotalDeathsByCountry, getRecoveredByCountry, getChartsData
import json

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home/')
def home():
    dataConf = Data()
    chartsData = getChartsData()
    return render_template('home.html',
                           chartsData=chartsData, data=dataConf)


@main.route('/totalConfirmed/')
def totalConfirmed():
    totalConfirmed = Data().getTotalConfirmed()
    return render_template('totalConfirmed.html', totalConfirmed=totalConfirmed)


@main.route('/confirmedCasesByCountry/')
def confirmedCasesByCountry():
    confirmedCasesByCountry = getConfirmedCasesByCountry()
    return render_template('confirmedCasesByCountry.html', confirmedCasesByCountry=confirmedCasesByCountry)

@main.route('/totalDeaths/')
def totalDeaths():
    totalDeath = Data().getTotalDeath()
    return render_template('totalDeaths.html', totalDeath=totalDeath)

@main.route('/deathsCasesByCountry/')
def deathsCasesByCountry():
    deathsCasesByCountry = getTotalDeathsByCountry()
    return render_template('deathsCasesByCountry.html', deathsCasesByCountry=deathsCasesByCountry)

@main.route('/totalRecovered/')
def totalRecovered():
    totalRecovered = Data().getTotalRecovered()
    return render_template('totalRecovered.html', totalRecovered=totalRecovered)

@main.route('/recoveredCasesByCountry/')
def recoveredCasesByCountry():
    recoveredCasesByCountry = getRecoveredByCountry()
    return render_template('recoveredCasesByCountry.html', recoveredCasesByCountry=recoveredCasesByCountry)

@main.route('/charts/')
def charts():
    chartsData = getChartsData()
    return render_template('charts.html', chartsData=chartsData)

@main.route('/map/')
def map(): 
    dataConf = Data()
    return render_template('map.html', data=dataConf)
