# -*- coding: utf-8 -*-
{
    'name': "membership_mass_invoicing",

    'summary': """
            Give the ability to mass invoice memberships
        """,

    'description': """
            Give the ability to mass invoice memberships
        """,

    'author': "MokaTourisme",
    'version': '0.1',

    'depends': ['membership'],

    # always loaded
    'data': [
        "wizard/membership_invoice_views.xml",
    ],
}
