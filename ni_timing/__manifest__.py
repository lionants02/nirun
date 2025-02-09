#  Copyright (c) 2021-2023 NSTDA

{
    "name": "Nirun - Timing",
    "summary": "This is base module for managing Timing",
    "version": "16.0.0.1.0",
    "development_status": "Alpha",
    "category": "Medical",
    "author": "NSTDA, Piruin P.",
    "website": "https://nirun.life/",
    "license": "LGPL-3",
    "maintainers": ["piruin"],
    "depends": ["ni_coding"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron_data.xml",
        "data/ni.timing.dow.csv",
        "data/ni.timing.event.csv",
        "data/ni.timing.template.csv",
        "views/ni_timing_dow_view.xml",
        "views/ni_timing_event_view.xml",
        "views/ni_timing_template_views.xml",
        "views/ni_timing_template_tod_views.xml",
        "views/ni_timing_tod_views.xml",
        "views/ni_timing_timing_tod_views.xml",
        "views/ni_timing_timing_views.xml",
        "views/ni_timing_menu.xml",
    ],
    "application": False,
    "auto_install": False,
    "installable": True,
}
