# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 23:11:57 2014

@author: Ken N
"""

station = {'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
           'number': 31705,
           'latitude': 48.8645278209514,
           'name': 'CHAMPEAUX (BAGNOLET)',
           'longitude': 2.416170724425901}

for k, v in station.items():
    print(k + " " + str(v))
