#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:59:35 2023

@author: xiaomingmo
"""

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated, Optional
from pydantic import BaseModel
from datetime import date
from random import randint

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

#base models set up
class studBase(BaseModel):
    stud_number:int
    name:str
    program:str

class createRequest(studBase):
    dob: date
    email: Optional[str]
    phone: int
    campus:str
    year:int
    # file_name:str
    # file_url:str

class studCard(studBase):
    card_number:int
    status:str
    
    class Config():
        orm_mode = True
    
#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

#generate random card number
def generate_card_number():
    card_num = randint(10000000, 216692634)
    return card_num

#create endpoints
@app.post('/apply_student_card/')
async def create_request(request:createRequest, db:db_dependency):
    db_request = models.request(
        name=request.name,
        stud_number=request.stud_number,
        program=request.program,
        dob=request.dob,
        email=request.email,
        phone=request.phone,
        campus=request.campus,
        year=request.year,
        card_number=generate_card_number()
        )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return ('Application successfully submit!')

@app.get('/card_records', response_model=List[createRequest])
async def get_records_by_stud_id(stud_id:int, db:db_dependency):
        result = db.query(models.request).filter(models.request.stud_number == stud_id).all()
        if result is None:
            raise HTTPException(status_code=404, detail='Student number not found!')
        return result

@app.get('/request_status', response_model=studCard)
async def get_request_status(request_id:int, db:db_dependency):
    result = db.query(models.request).filter(models.request.id == request_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail='Request record not found!')
    return result