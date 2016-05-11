menu_code = \
[{
    'name':  "Overview",
    'route': "/",
},{
    'name': "Run simulation",
    'children': [{
        'name':  "Fraedrich",
        'route': "/run/fraedrich",
    },{
        'name':  "Griffel & Drazin",
        'route': "/run/griffeldrazin",
    }],
},{
    'name': "Stability analysis",
    'children': [{
        'name':  "Fraedrich",
        'route': "/stabanalysis/fraedrich",
    },{
        'name':  "Griffel & Drazin",
        'route': "/stabanalysis/griffeldrazin",
    },{
        'name':  "Comparsion",
        'route': "/comparison",
    }],
},{
    'name':  "Tweak parameters",
    'route': "/tweakparams",
}]
