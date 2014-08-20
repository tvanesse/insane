# -*- coding: utf-8 -*-
"""
Insane Manager - glue.py
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

========================================================================

glue.py
-------
This file handles the gluing between the GUI and the logic models.

"""
from gui import MainWindow

class ProfitGlue(object):

    def __init__(self, main_window):
        self.main_window = main_window

    def display_profit(self, profit):
        """
        Update the GUI to display the Profit informations on the right panel.
        """
        # Retrieve the widgets to be updated from the main window
        builder                 = self.main_window.builder
        bill_ref_entry          = builder.get_object("bill_ref_entry")
        description_text_buffer = builder.get_object("profit_description_buffer")

        # Update the widgets
        bill_ref_entry.set_text(profit.bill_ref)
        description_text_buffer.set_text(profit.detailed)

    def display_customer(self, customer):
        """
        Update the GUI to display the Customer informations on the right panel.
        """
        # Retrieve the widgets to be updated from the main window
        builder            = self.main_window.builder
        company_name_entry = builder.get_object("company_name_entry")
        first_name_entry   = builder.get_object("first_name_entry")
        last_name_entry    = builder.get_object("last_name_entry")
        email_addr_entry   = builder.get_object("email_addr_entry")

        # Update the widgets
        company_name_entry.set_text(customer.company_name)
        first_name_entry.set_text(customer.first_name)
        last_name_entry.set_text(customer.last_name)
        email_addr_entry.set_text(str(customer.email))



if __name__ == "__main__":
    from gi.repository import Gtk
    from models import Profit, Customer
    from generic_models import EmailAddress

    mw = MainWindow()
    p1 = ProfitGlue(mw)

    prof = Profit(bill_ref="WEB-1234", detailed="Un sex-toy wallon pour le festival de la saucisse à la foire de Libramont.")
    p1.display_profit(prof)

    cust = Customer(company_name="Saucisses Wallonnes sprl", first_name="Rémy", last_name="Durand", email=EmailAddress(user="remy", domain="sauciflar.be"))
    p1.display_customer(cust)

    Gtk.main()