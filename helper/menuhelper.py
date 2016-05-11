from bottle import template
from helper.linkhelper import link

def render_menu(menu, url_params):
    output = "<ul>\n"
    for item in menu:
        output += render_item(item, url_params)
    output += "</ul>\n"
    return output

def render_item(item, url_params):
    output = "<li>"
    if 'route' in item:
        output += link(item['route'], item['name'], url_params)
    else:
        output += template("{{name}}", name=item['name'])
    if 'children' in item:
        output += "\n"
        output += render_menu(item['children'], url_params)
    output += "</li>\n"
    return output
