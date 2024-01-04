from pydantic import BaseModel, Field
from guardrails.validators import ValidRange
from typing import List

class CompanyInfo(BaseModel):
  name: str = Field(description = "Name of the company the applicant has worked with")
  years: int = Field(validators = [ValidRange(min=0,max=50,on_fail='fix')], description = "Number of years the applicant has worked in that particular company" )

class ApplicantInfo(BaseModel):
    name: str = Field(description = "Name of the applicant")
    univ: str = Field(description = "Name of the university the applicant went to")
    experience: int = Field(validators = [ValidRange(min=0,max=50,on_fail='fix')], description = "Total professional experience in years")
    experience_list: List[CompanyInfo] = Field(description = "List of companies the applicant has worked before")
    database_experience: int = Field(validators = [ValidRange(min=0,max=50,on_fail='fix')], description = "Total experience database systems in years")
    python_experience: int = Field(validators = [ValidRange(min=0,max=50,on_fail='fix')], description = "Total python experience in years")
