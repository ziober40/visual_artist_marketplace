import string
import typing
from typing import Any
from enum import Enum
from pydantic import BaseModel, validator
from models.models import Direction


class OrderView(BaseModel):
    order_id: Any
    user_id: Any
    artwork_id: Any
    price: float
    direction: Direction
    is_canceled: bool