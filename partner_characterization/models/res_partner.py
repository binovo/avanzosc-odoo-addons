# Copyright 2018 Maite Esnal - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    commercial_country_ids = fields.Many2many(
        comodel_name="res.country",
        relation="rel_commmercial_countries",
        column1="partner_id",
        column2="country_id",
        string="Commercial Interest Countries",
    )
    commercial_imp_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="rel_commercial_implatation",
        column1="partner_id",
        column2="commercial_imp_id",
        string="Commercial Implantation",
    )
    productive_imp_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="rel_productive_implatation",
        column1="partner_id",
        column2="productive_imp_id",
        string="Productive Implantation",
    )
    subscription_date = fields.Date()
    unsubscription_date = fields.Date()
    associated = fields.Selection(
        selection=[
            ("yes", "Yes"),
            ("no", "No"),
            ("potential", "Associated " "potential"),
        ],
        default="no",
    )
    sme_business = fields.Boolean(
        default=True,
        string="SME",
    )
    associated_type_id = fields.Many2one(
        comodel_name='associated.partner.type',
        string='Associated Type'
    )
    entity_character_id = fields.Many2one(
        comodel_name='entity.partner.character',
        string='Entity Character'
    )
    sme_business = fields.Boolean(default=True, string='SME')
    sector_character = fields.Many2one(
        comodel_name="res.character",
    )
    group_of_control = fields.Boolean(
        default=False,
        string="Group of control",
    )
    have_participation = fields.Boolean(
        string="Do you have participation of NO SMEs or venture capital"
        "entities in your shareholding?"
    )
    number_of_employees = fields.Integer(
        string="Number of employees",
    )
    economic_data_ids = fields.One2many(
        comodel_name="res.partner.economic_data",
        inverse_name="partner_id",
        string="Economic Data",
    )
    economic_date = fields.Date(
        string="Economic Data Date",
    )
    real_total_turnover = fields.Integer(
        string="Real total turnover",
    )
    real_number_employees = fields.Integer(
        string="Real number of employees",
    )
    real_external_billing = fields.Integer(
        string="Real external billing",
    )
    real_external_employees_number = fields.Integer(
        string="Real external employees number"
    )
    real_investment_RD = fields.Integer(
        string="Real investment R & D",
    )
    expected_total_billing = fields.Integer(
        string="Expected total billing",
    )
    expected_total_employees_number = fields.Integer(
        string="Expected total employees number"
    )
    expected_external_billing = fields.Integer(
        string="Expected external billing",
    )
    expected_external_employees_number = fields.Integer(
        string="Expected external employees number"
    )
    expected_investment_RD = fields.Integer(
        string="Expected investment R & D",
    )
    activity_id = fields.Many2one(
        string="Activity",
        comodel_name="res.activity",
        copy=False,
    )
    activity_type_ids = fields.Many2many(
        string="Activity Types",
        comodel_name="res.activity.type",
        relation="rel_partner_activity_type",
        column1="partner_id",
        column2="type_id",
        copy=False,
    )
    specialization_ids = fields.Many2many(
        string="Specializations",
        comodel_name="res.area.specialization",
        relation="rel_partner_specialization",
        column1="partner_id",
        column2="specialization_id",
        copy=False,
    )
    area_ids = fields.Many2many(
        string="Areas",
        comodel_name="res.partner.area",
        relation="rel_partner_area",
        column1="partner_id",
        column2="area_id",
        copy=False,
    )
    committee_ids = fields.Many2many(
        string="Committees",
        comodel_name="res.committee",
        relation="rel_partner_committee",
        column1="partner_id",
        column2="committee_id",
        copy=False,
    )
    team_ids = fields.Many2many(
        string="Teams",
        comodel_name="res.team",
        relation="rel_partner_team",
        column1="partner_id",
        column2="team_id",
        copy=False,
    )
    structure_ids = fields.Many2many(
        string="Structures",
        comodel_name="res.structure",
        relation="rel_partner_structure",
        column1="partner_id",
        column2="structure_id",
        copy=False,
    )
    main_contact = fields.Boolean()
    assembly = fields.Boolean()
    joint = fields.Boolean()
    bidding = fields.Boolean()
    foundation_year = fields.Integer()
    incorporate_user_id = fields.Many2one(
        comodel_name="res.users",
        string="Incorporate EE",
        domain="[('share', '!=', False)]",
    )
    interlocutor_user_id = fields.Many2one(
        comodel_name="res.users",
        string="Interlocutor EE",
        domain="[('share', '!=', False)]",
    )


class ResPartnerEconomicdata(models.Model):
    _name = "res.partner.economic_data"
    _description = "Economic Data from Partner"
    _order = "partner_id,economic_date DESC"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=True,
    )
    economic_date = fields.Date(
        string="Economic Data Date",
        required=True,
    )
    real_total_turnover = fields.Float(
        string="Real total turnover",
    )
    real_number_employees = fields.Integer(
        string="Real number of employees",
    )
    real_external_billing = fields.Integer(
        string="Real external billing",
    )
    real_external_employees_number = fields.Integer(
        string="Real external employees number"
    )
    real_investment_RD = fields.Integer(
        string="Real investment R & D",
    )
    expected_total_billing = fields.Integer(
        string="Expected total billing",
    )
    expected_total_employees_number = fields.Integer(
        string="Expected total employees number"
    )
    expected_external_billing = fields.Integer(
        string="Expected external billing",
    )
    expected_external_employees_number = fields.Integer(
        string="Expected external employees number"
    )
    expected_investment_RD = fields.Integer(
        string="Expected investment R & D",
    )

    _sql_constraint = [
        (
            "unique_partner_economic_date",
            "unique(partner_id, economic_date)",
            "There can only be one economic info per partner and date",
        ),
    ]

    def name_get(self):
        res = []
        for data in self:
            economic_date = fields.Date.from_string(data.economic_date)
            res.append(
                (data.id, "[{}] {}".format(economic_date.year, data.partner_id.name))
            )
        return res


class ResPartnerAssociateType(models.Model):
    _name = 'associated.partner.type'
    _description = 'Associate Type'

    name = fields.Char(string='Associate Type', required=True, translate=True)


class ResPartnerEntityNature(models.Model):
    _name = 'entity.partner.character'
    _description = 'Entity Nature'

    name = fields.Char(string='Entity Nature', required=True, translate=True)
