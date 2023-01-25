import json

from . import LOGGER
import numpy as np
import os
import pandas as pd
from datetime import datetime  # Permet de gerer les temps d'execution
import configparser  # Permet de parser le fichier de paramètres #pip install configparser
from termcolor import colored as cl  # text customization
from pandas_profiling import ProfileReport


# ----------------------------------------------------------
# UTILS
# ----------------------------------------------------------
def class_items(obj):
    temp = obj.__dict__
    for item in obj.__dict__:
        print(f"- {item} : {temp[item]}")


def list_intersection(list_a: list, list_b: list):
    return list(set(list_a).intersection(set(list_b)))


def list_difference(list_a, list_b):
    return list(set(list_a).difference(set(list_b)))


def diff_date(x, y):
    return ((x - y) / np.timedelta64(1, 'D')).astype(float)


# Fonction servant de minuteur
def timer(start_time=None):
    """
    --> Fonction servant de miniteur
     en entrée (in) : soit None soit un autre minuteur (timer) de debut
     en sortie (out) : affichage du temps d'execution d'un programme
     exemple d'utilisation :  start = timer(None)
                             puis programmes puis
                              end = timer(start)
    """
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print(cl(f"Time taken: {thour} hours {tmin} minutes and {round(tsec, 2)} seconds.", attrs=['bold'],
                 color='green'))
        # print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))


# Fonction pour la lecture du fichier de configuration
def read_json(config_filename: str, key: str = None):
    if not os.path.isfile(config_filename):
        raise ValueError(f"'{config_filename}' file not found")

    f = open(config_filename, encoding="utf-8")
    data = json.load(f)  # parse le JSON
    if key is None:
        return data
    elif key not in data.keys():
        raise ValueError(f"Wrong key '{key}'. Availables keys: '{data.keys()}' ")
    else:
        return data[key]


def param_recup_training(config_filename, section_title):
    """
    --> Function for configuration file : permet de recuperer les params d'entrainement de config
    en entrée : (2)
            - str config_filename : nom du fichier de config
            - str section_title : la section du fichier
    en sortie : les differents paramètres de config
            - str site_name : le nom du site,
            - str date_name : le nom de la date,
            - int window_size : la taille de fenetre choisie et
            - str path_to_data :le chemien d'acces au données

    Allure du fichier de config
        [Step 2 Training]
            site: Romans
            date: Date
            source: ..\Data\Data_cleaned
            windows_size: 30
    """
    if not os.path.isfile(config_filename):
        raise ValueError(f"'{config_filename}' file not found")

    config = configparser.RawConfigParser()  # On créé un nouvel objet "config"
    config.read(config_filename)  # On lit le fichier de paramètres
    # On récupère les valeurs des différents paramètres
    # Récupération basique dans des variables
    site_name = config.get(section_title, 'site_name')
    date_name = config.get(section_title, 'date_name')
    path_to_data = config.get(section_title, 'source')
    window_size = int(config.get(section_title, 'windows_size'))
    # utiliser un dico pour la sortie
    return site_name, date_name, window_size, path_to_data


""""
Samples:
    - df.apply
        `def get_alarms(sta,end):
            return data_algo[(data_algo.TSTART >= sta) & (data_algo.TSTART <= end)].Alarm_number.values

        slices['alarms'] = slices.apply(lambda x: get_alarms(x.time, x.time_end), axis=1)`

    - change column type to timestamp
        df['time'] = df['time'].apply(pd.to_datetime, format='%Y-%m-%dT%H:%M:%S') -

    - pd.options.plotting.backend = "plotly"
    - 

data frame “df” is passed to melt() function
id_vars is the variable which need to be left unaltered which is “countries”
var_name are the column names so we named it as ‘metrics’
value_name are its values so we named it as ‘values’


# cols = list(df.columns)
# a, b, = cols.index('TSTART'), cols.index('TEND')
# cols[a], cols[b] = cols[b], cols[a]
# df = df[cols]


"""