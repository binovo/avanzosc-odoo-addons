# Copyright 2019 Roberto Lizana - Trey, Jorge Camacho - Trey
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Mass Mailing Characterization",
    "version": "16.0.1.2.0",
    "category": "Marketing",
    "license": "AGPL-3",
    "author": "Trey (www.trey.es)",
    "website": "https://www.trey.es",
    "depends": [
        "base_characterization",
        "mass_mailing",
        "web",
        "website_blog",
        "website_blog_characterization",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/blog_post_view.xml",
        "views/mail_mass_mailing_view.xml",
        "views/res_partner_area_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "/mass_mailing_characterization/static/src/js/mass_mailing_characterization.js",
        ],
    },
    "installable": True,
    "auto_install": False,
    "license": "AGPL-3",
}
