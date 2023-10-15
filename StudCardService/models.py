#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:03:12 2023

@author: xiaomingmo
"""

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base


    
class request(Base):
    __tablename__='student_card_request'
    
    id=Column(Integer, primary_key=True)
    name = Column(String,)
    stud_number = Column(Integer, index=True, unique=False)
    dob = Column(DateTime)
    email = Column(String)
    phone = Column(Integer)
    program = Column(String,)
    campus = Column(String)
    year = Column(Integer)
    card_number = Column(Integer, unique=True, index=True)
    status = Column(String, default='Pending')
    
'''
need to do something to generate unique card number
'''

# class files(Base):
#     __tablename__='support files'
    
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('request.id'))
#     file_name = Column(String)
#     file_url = Column(String)
#     owner_id = Column(Integer, ForeignKey("student_info.stud_number"), index=True)
