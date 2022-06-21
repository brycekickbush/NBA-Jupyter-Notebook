#Author Bryce Kickbush
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats import endpoints
from nba_api.stats.static import teams #Static library not an API call
import pandas as pd
import matplotlib.pyplot as plt
import requests
import time

"""
Function that will create a list of all teamID's
Used for gathering information based on all NBA teams
"""
def createTeamList():
    teamID = [] #List of ID's
    allTeams = teams.get_teams() 
    for dicts in allTeams:
        teamID.append(dicts['id']) #Appends each teams ID into the teamID list
    return teamID
"""
Function that will create a dicionary containing teams:winPercentage between yearFloor and yearCeilning (inclusive)
"""
def winPercentageDict(self, yearFloor, yearCeiling):
    return ""

