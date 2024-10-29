
def migrate(cr, version):
    if not version:
        return

    cr.execute("""
UPDATE res_partner
SET associated_type_id = CASE 
        WHEN pcm.associated_type_id = 'partner' THEN associate_type_partner.res_id
        WHEN pcm.associated_type_id = 'junior' THEN associate_type_junior_partner.res_id
        WHEN pcm.associated_type_id = 'strategic' THEN associate_type_strategic_partner.res_id
        WHEN pcm.associated_type_id = 'strategic_junior' THEN associate_type_user_partner.res_id
        ELSE NULL
    END,
    entity_character_id = CASE 
        WHEN pcm.entity_character_id = 'company' THEN entity_nature_company.res_id
        WHEN pcm.entity_character_id = 'training_center' THEN entity_nature_training_centre.res_id
        WHEN pcm.entity_character_id = 'research_center' THEN entity_nature_research_centre.res_id
        WHEN pcm.entity_character_id = 'organism' THEN entity_nature_organisation.res_id
        ELSE NULL
    END
FROM 
    _partner_characterization_migration AS pcm
INNER JOIN 
    ir_model_data AS associate_type_partner
ON 
    associate_type_partner.name = 'associate_type_partner' 
    AND associate_type_partner.module = 'partner_characterization'
INNER JOIN 
    ir_model_data AS associate_type_junior_partner
ON 
    associate_type_junior_partner.name = 'associate_type_junior_partner' 
    AND associate_type_junior_partner.module = 'partner_characterization'
INNER JOIN 
    ir_model_data AS associate_type_strategic_partner
ON 
    associate_type_strategic_partner.name = 'associate_type_strategic_partner' 
    AND associate_type_strategic_partner.module = 'partner_characterization'
INNER JOIN 
    ir_model_data AS associate_type_user_partner
ON 
    associate_type_user_partner.name = 'associate_type_user_partner' 
    AND associate_type_user_partner.module = 'partner_characterization'
INNER JOIN 
        ir_model_data AS entity_nature_company
    ON 
        entity_nature_company.name = 'entity_nature_company' 
        AND entity_nature_company.module = 'partner_characterization'
    INNER JOIN 
        ir_model_data AS entity_nature_training_centre
    ON 
        entity_nature_training_centre.name = 'entity_nature_training_centre' 
        AND entity_nature_training_centre.module = 'partner_characterization'
    INNER JOIN 
        ir_model_data AS entity_nature_research_centre
    ON 
        entity_nature_research_centre.name = 'entity_nature_research_centre' 
        AND entity_nature_research_centre.module = 'partner_characterization'
    INNER JOIN 
        ir_model_data AS entity_nature_organisation
    ON 
        entity_nature_organisation.name = 'entity_nature_organisation' 
        AND entity_nature_organisation.module = 'partner_characterization'
    WHERE 
        pcm.partner_id = res_partner.id;
    """)

    cr.execute("DROP TABLE _partner_characterization_migration;")