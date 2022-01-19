import datetime
from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None
    idno: str = None


class CIF(BaseModel):
    loanid: str = None
    loan_type : str = None
    loan_status : str = None
    cif: str  = None
    loan_tenure : int = None
    loan_amount: int  = None
    interest : int = None
    idno : str = None
    fname : str = None
    lname : str = None
    dob : datetime.date = None
    gender : str = None
    marital_status : str = None
    income : int = None
    phone : str = None
    email : str = None
    isphoneverified : str = None
    isemailverified : str = None
    createdate : datetime.date = None
    updatedate : datetime.date = None
    source : str = None
    # limit: int  = None


class ResponseCIF(BaseModel):
    cif_list: List[CIF]

class Customer(BaseModel):
    idno : str = None
    fname : str = None
    lname : str = None
    dob : datetime.date = None
    age : int = None
    gender : str = None
    marital_status : str = None
    income : int = None
    phone : str = None
    email : str = None


class ResponseCustomer(BaseModel):
    customer : List[Customer]