#!/usr/bin/python3
""" Place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class Place that inherits from BaseModel

    :param city_id: city's id
    :type city_id: str
    :param user_id: user's id
    :type user_id: str
    :param name: place's name
    :type name: str
    :param description: place's description
    :type description: str
    :param number_rooms: number of rooms
    :type number_rooms: int
    :param number_bathrooms: number of bathrooms
    :type number_bathrooms: int
    :param max_guest: maximum of guests
    :type max_guest: int
    :param price_by_night: price/night
    :type price_by_night: int
    :param latitude: position
    :type latitute: float
    :param longitude: position
    :type city_id: float
    :param amenity_ids: ids
    :type amenity_ids: list of str
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
