#  Copyright (c) 2021-2023 NSTDA

{
    "name": "Medication",
    "version": "16.0.0.4.0",
    "development_status": "Alpha",
    "category": "Medical/Medication",
    "author": "NSTDA, Piruin P.",
    "website": "https://nirun.life/",
    "license": "LGPL-3",
    "maintainers": ["piruin"],
    "depends": [
        "ni_patient",
        "product",
        "ni_timing",
        "uom_alias",
        "ni_condition",
        "ni_practitioner",
    ],
    "data": [
        "security/ni_medication_group.xml",
        "security/ni_medication_rules.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/product_category_data.xml",
        "data/uom_uom_data.xml",
        "data/ni_medication_form_data.xml",
        "data/ni_medication_admin_location_data.xml",
        "data/ni_medication_dosage_method_data.xml",
        "data/ni_medication_dosage_route_data.xml",
        "views/ni_medication_form_views.xml",
        "views/ni_medication_ingredient_views.xml",
        "views/ni_medication_views.xml",
        "views/ni_medication_admin_location_views.xml",
        "views/ni_medication_statement_views.xml",
        "views/ni_medication_dispense_views.xml",
        "views/ni_medication_dosage_views.xml",
        "views/ni_medication_unit_views.xml",
        "views/ni_medication_menus.xml",
        "views/ni_patient_views.xml",
        "views/ni_encounter_views.xml",
        "reports/medication_label_report.xml",
        "reports/medication_label_template.xml",
    ],
    "application": True,
    "auto_install": False,
    "installable": True,
}
