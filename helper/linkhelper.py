from bottle import template
from climath.model import Model

def link(href, name, url_params={}):
    return template("<a href=\"{{!href}}\">{{name}}</a>",
                    href=make_url(href, url_params), name=name)

def make_url(href, url_params={}):
    paramstr = "&".join([key+"="+val for key, val in url_params.items()])
    if paramstr:
        paramstr = "?" + paramstr
    return href + paramstr

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
