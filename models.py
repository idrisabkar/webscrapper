from typing import Optional
from pydantic import BaseModel


class Body(BaseModel):
    url: str
    selector: str
    tag: Optional[str] = None
