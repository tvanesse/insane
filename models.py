# -*- coding: utf-8 -*-
"""
Insane Manager - models.py
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

from abstract_models import *

class Expense(Entry):
    """
    A subclass of Entry that represents an expense.
    """

    def __init__(self, exo_ratio=1):
        """
        Initialize an Expense.
        """
        super(Expense, self).__init__()
        if exo_ratio > 1 or exo_ratio < 0 :
            raise Exception("The exoneration ratio must be between 0 and 1.")
        else:
            self.exo_ratio = exo_ratio    # defines the proportion of self.amount that can be exonerated



class Profit(Entry):
    """
    A subclass of Entry that represents a profit.
    """

    def __init__(self):
        """
        Initialize a Profit.
        """
        super(Profit, self).__init__()




if __name__ == "__main__":
    e0 = Expense()
    print(e0.amount)

    e1 = Expense(0.5)
    print(e1.exo_ratio)

    try:
        e2 = Expense(1.2)
    except Exception:
        print("1.2 is greater than 1 !")