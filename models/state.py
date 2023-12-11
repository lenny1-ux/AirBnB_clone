#!/usr/bin/python3
"""To define the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This represents a state.

    Attributes:
        name (str): The state name.
    """

    name = ""
