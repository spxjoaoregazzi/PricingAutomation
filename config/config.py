# -*- coding: utf-8 -*-
"""
@author: joao.regazzi
"""

from utils import lastbusyday
import datetime as dt

# GENERAL
date = str(lastbusyday(dt.date.today())) # Se vc ta vendo de D-1
#date = str(dt.date.today()) # Se vc ta vendo de D0

# BBG API
username = 'coloque seu user'
password = 'coloque sua senha'

# OBS: Esse código está desatualizado e não considera feriados
