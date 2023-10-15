#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:01:34 2023

@author: xiaomingmo
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL_DATABASE = 'postgresql://xiaomingmo:1234@localhost:5432/StudCard'
URL_DATABASE = 'postgresql://postgres:postgres@postgres_student_card:5432/student_card'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()