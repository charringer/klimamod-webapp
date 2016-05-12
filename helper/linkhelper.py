from bottle import template
from mamath.model import Model

def link(href, name, url_params={}):
    paramstr = "&".join([key+"="+val for key, val in url_params.items()])
    if paramstr:
        paramstr = "?" + paramstr
    return template(
        "<a href=\"{{!href}}\">{{name}}</a>",
        href=href+paramstr, name=name)

def perm_params(params, report_bad_values = False):
    pp = {}
    bad = ""
    for key, value in params.items():
        if value and key in Model.param_keys:
            try:
                fvalue = float(value)
                pp[key] = str(fvalue)
            except ValueError as err:
                bad += key + ": " + str(err)
    if report_bad_values:
        return (pp, bad)
    else:
        return pp
