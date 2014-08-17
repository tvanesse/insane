# -*- coding: utf-8 -*-
"""
Insane Manager - abstract_models.py
Copyright (C) 2014  Thomas Vanesse

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import pycountry

class Entry(object):
    """
    A generic class that represents an entry within Insane.
    """

    def __init__(self, **kwargs):
        """
        Initialize an empty Entry.
        """
        self.amount     = 0
        self.name       = kwargs.get('name', "No name")
        self.detailed   = kwargs.get('detailed', "No detail.")



class Person(object):
    """
    A generic class that represents a person.
    """

    def __init__(self, **kwargs):
        """
        Initialize an empty Person.
        """
        self.first_name   = kwargs.get('first_name', None)
        self.last_name    = kwargs.get('last_name', None)
        self.address      = kwargs.get('address', None)
        self.email        = kwargs.get('email', None)
        self.phone_number = kwargs.get('phone_number', None)



class Address(object):
    """
    A generic class that represents a postal address.
    """

    def __init__(self, **kwargs):
        """
        Initialize an empty Address.
        """
        self.street_name  = kwargs.get('street_name', None)
        self.house_number = kwargs.get('house_number', None)
        self.box_number   = kwargs.get('box_number', None)
        self.city         = kwargs.get('city', None)
        self.zip_code     = kwargs.get('zip_code', None)
        self.country      = kwargs.get('country', pycountry.countries.get(alpha2='BE'))




class EmailAddress(object):
    """
    A generic class that represents an email address.
    """

    def __init__(self, user='foo', domain='bar.org'):
        self.user   = user
        self.domain = domain

    @property
    def addr(self):
        return self.user + '@' + self.domain

    def __str__(self):
        return self.addr