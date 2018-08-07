# -*- coding: utf-8 -*-
'''
Created on 6 de ago de 2018

@author: jeanm
'''
import re

from sqlalchemy import select, and_

from FFDao.core import players_table, stats_table, club_table
from numpy import integer
from _operator import contains
import json