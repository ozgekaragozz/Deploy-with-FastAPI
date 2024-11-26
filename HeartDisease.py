# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""

from pydantic import BaseModel

class HeartDisease(BaseModel):
    Age: int
    Sex: int
    RestingBP: int
    Cholesterol: int
    FastingBS: int  
    MaxHR: int
    ExerciseAngina: int  
    Oldpeak: float
    ST_Slope: float 
    ChestPainType_ATA: int 
    ChestPainType_NAP: int
    ChestPainType_TA: int
    RestingECG_Normal: int
    RestingECG_ST: int
