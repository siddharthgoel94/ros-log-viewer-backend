from pydantic import BaseModel

class Log(BaseModel):
    timestamp: str
    severity: str
    node: str
    message: str
