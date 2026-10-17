from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    allergies:List[str]
    phone:Dict[str,str]





    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
       return value.upper()

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ["hbl.com","ubl.com"]

        domain_names = value.split("@")[-1]

        if domain_names not in valid_domains:
            raise ValueError(f"Invalid domain name. Please choose from {valid_domains}")
        return value

    


def show_patient(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.phone)



patient_info = {

    "name": "JOHN DOE",
    "email": "john.doe@hbl.com",
    "age": 30,
    "weight": 70.5,
    "allergies": ["pollen", "dust"],
    "phone": {"home": "123-456-7890", "work": "987-654-3210"}
}

patient1 = Patient(**patient_info)

show_patient(patient1)
