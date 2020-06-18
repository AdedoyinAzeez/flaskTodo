#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:32:18 2020

@author: adedoyinazeez
"""

from app.py import db
import os

if bool(os.environ.get('DEBUG', '')):
    db.drop_all()
db.create_all()

