#  Copyright (c) 2022-2023. NSTDA
from odoo import api, fields, models


class Procedure(models.Model):
    _name = "ni.procedure"
    _description = "Procedure"
    _inherit = [
        "ni.workflow.event.mixin",
        "ni.identifier.mixin",
        "mail.thread",
        "ni.period.mixin",
    ]
    _order = "occurrence DESC,id DESC"
    _identifier_ts_field = "period_start"
    _workflow_occurrence_field = "period_start"

    name = fields.Char(related="code_id.name", store=True)
    code_id = fields.Many2one("ni.procedure.code", "Procedure", tracking=True)
    code = fields.Char(related="code_id.code")
    category_id = fields.Many2one(
        related="code_id.category_id", tracking=True, store=True
    )

    location_id = fields.Many2one("ni.location", tracking=True)
    outcome_id = fields.Many2one(
        "ni.procedure.outcome",
        tracking=True,
        readonly=True,
        states={"completed": [("readonly", False)]},
    )
    outcome_display_class = fields.Selection(related="outcome_id.display_class")
    note = fields.Text(help="Further Information")
    performer_id = fields.Many2one(
        "hr.employee", required=True, default=lambda self: self.env.user.employee_id
    )

    def _name_search(
        self, name="", args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        args = list(args or [])
        if not (name == "" and operator == "ilike"):
            args += ["|", ("name", operator, name), ("identifier", operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    def name_get(self):
        return [(rec.id, rec._name_get()) for rec in self]

    def _name_get(self):
        procedure = self
        name = procedure.name or procedure.code_id.name
        if self._context.get("show_category") and procedure.category_id:
            name = "{},{}".format(procedure.category_id.name, name)
        if self._context.get("show_code") and procedure.code_id.code:
            name = "[{}] {}".format(name, procedure.code_id.code)
        if self._context.get("show_patient"):
            name = "{}: {}".format(procedure.patient_id._name_get(), name)
        if self._context.get("show_state"):
            name = "{} ({})".format(name, procedure._get_state_label())
        if self._context.get("show_identifier"):
            name = "{} - {}".format(name, procedure.identifier)
        return name

    @api.onchange("code_id")
    def onchange_code(self):
        for rec in self:
            if rec.code_id.duration_hours:
                rec.duration_hours = rec.code_id.duration_hours

    @property
    def _workflow_name(self):
        return self.code_id.name

    @property
    def _workflow_summary(self):
        res = self.outcome_id.name or self.name
        if self.note:
            "{}; {}".format(res, self.note)
        return res
