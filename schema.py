from pydantic import BaseModel

class CustomerData(BaseModel):

    SeniorCitizen: int
    Dependents: str
    tenure: int
    InternetService: str
    MultipleLines: str
    OnlineSecurity: str
    TechSupport: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float