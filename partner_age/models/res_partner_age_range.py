#  Copyright (c) 2023 NSTDA

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartnerDateRange(models.Model):
    _name = "res.partner.age.range"
    _description = "Partner Age Range"

    def _default_age_from(self):
        age_from = 0
        last_age_range = self.env["res.partner.age.range"].search(
            [], order="age_to desc", limit=1
        )
        if last_age_range:
            age_from = last_age_range.age_to + 1
        return age_from

    name = fields.Char(string="Name", required=True)
    age_from = fields.Integer(
        string="From", required=True, default=lambda self: self._default_age_from()
    )
    age_to = fields.Integer(string="To", required=True)

    _sql_constraints = [("name_uniq", "unique (name)", "A name must be unique !")]

    @api.constrains("age_from", "age_to")
    def _validate_range(self):
        for rec in self:
            if rec.age_from >= rec.age_to:
                raise ValidationError(
                    _("%s is not a valid range (%s >= %s)")
                    % (rec.name, rec.age_from, rec.age_to)
                )
            range_id = rec.search(
                [
                    ("age_from", "<=", rec.age_to),
                    ("age_to", ">=", rec.age_from),
                    ("id", "!=", rec.id),
                ],
                limit=1,
            )
            if range_id:
                raise ValidationError(
                    _("%s is overlapping with range %s") % (rec.name, range_id.name)
                )
