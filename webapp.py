#!/usr/bin/python3

from bottle import route, view, run, static_file, request
from helper.linkhelper import perm_params
from helper.plothelper import svg_plot
from mamath.euler import plot_euler
from mamath.stabanalysis import plot_stability, plot_comparison
from mamath.models import f_fraedrich, f_griffeldrazin

@route('/')
@view('overview')
def overview():
    pp = perm_params(request.query)
    return dict(url_params=pp)

@route('/run/<model>')
def preparesimulation(model):
    pass

@route('/run/<model>/<initval:float>')
@view('runsimulation')
def runsimulation(model, initval):
    if model == 'fraedrich':
        f = f_fraedrich
    elif model == 'griffeldrazin':
        f = f_griffeldrazin
    else:
        raise ValueError("unknown model: %s" % model)
    initval = float(initval)
    plot = svg_plot(plot_euler(f, initval))

    pp = perm_params(request.query)
    return dict(plot=plot, url_params=pp)

@route('/stabanalysis/<model>')
@view('stabanalysis')
def stabanalysis(model):
    if model == 'fraedrich':
        f = f_fraedrich
    elif model == 'griffeldrazin':
        f = f_griffeldrazin
    else:
        raise ValueError("unknown model: %s" % model)
    plot = svg_plot(plot_stability(f))
    pp = perm_params(request.query)
    return dict(plot=plot, url_params=pp)

@route('/comparison')
@view('stabanalysis')
def comparison():
    plot = svg_plot(plot_comparison(
                        [(f_fraedrich, "Fraedrich")
                        ,(f_griffeldrazin, "Griffel & Drazin")]))
    pp = perm_params(request.query)
    return dict(plot=plot, url_params=pp)

@route('/tweakparams')
@view('tweakparams')
def tweakparams():
    taction = request.query.get('taction')
    pp, bad = perm_params(request.query, True)
    return dict(taction=taction, bad_values=bad, url_params=pp)

@route('/static/<path:path>')
def serve_static_file(path):
    return static_file(path, root="static")

run(host='localhost', port=8080, debug=True)
