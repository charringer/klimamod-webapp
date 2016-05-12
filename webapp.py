#!/usr/bin/python3

from bottle import route, view, run, static_file, request
from helper.linkhelper import perm_params
from helper.plothelper import svg_plot
from mamath.euler import plot_euler
from mamath.stabanalysis import plot_stability, plot_comparison
from mamath.model import Model

@route('/')
@view('overview')
def overview():
    pp = perm_params(request.query)
    return dict(url_params=pp)

@route('/run/<modelid>')
def preparesimulation(modelid):
    pass

@route('/run/<modelid>/<initval:float>')
@view('runsimulation')
def runsimulation(modelid, initval):
    pp = perm_params(request.query)
    model = Model(modelid, pp)
    initval = float(initval)
    plot = svg_plot(plot_euler(model.get_f(), initval))
    return dict(plot=plot, url_params=pp)

@route('/stabanalysis/<modelid>')
@view('stabanalysis')
def stabanalysis(modelid):
    pp = perm_params(request.query)
    model = Model(modelid, pp)
    plot = svg_plot(plot_stability(model.get_f_with_Qfactor()))
    return dict(plot=plot, url_params=pp)

@route('/comparison')
@view('stabanalysis')
def comparison():
    pp = perm_params(request.query)
    model_f  = Model('fraedrich', pp)
    model_gd = Model('griffeldrazin', pp)
    plot = svg_plot(plot_comparison([model_f, model_gd]))
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
