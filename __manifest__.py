# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    "name": 'Document Smart Buttons',
    "version": '10.1',
    "description": """
        Show a attachment smart button on a product and partner, so you can easely attached documents.
    """,
    "author": 'Odoo Experts',
    "website": 'https://www.odooexperts.nl',

    "category": " ",
    'images': [],
    "depends": ['sale'],
    "init_xml": [],
    'data': [
        "view/res_partner_view.xml",
        "view/product_view.xml",
    ],
    "test": [],
    "demo_xml": [],
    "installable": True,
    'auto_install': False,
    'license': 'LGPL-3',

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
