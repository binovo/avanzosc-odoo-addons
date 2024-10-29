# Copyright 2018 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


def migrate(cr, version):
    if not version:
        return

    cr.execute("""
CREATE TABLE _partner_characterization_migration AS 
SELECT 
    id AS partner_id, 
    associated_type AS associated_type_id,
    entity_character AS entity_character_id 
FROM 
    res_partner;           
""")
