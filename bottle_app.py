#!/usr/bin/python3

from bottle import route, view, request, static_file, redirect, run,default_app
from bottle import Response
from helper.linkhelper import perm_params, make_url
from helper.plothelper import svg_plot, headerless_svg, downloadable_svg
from climath.euler import plot_euler
from climath.stabanalysis import plot_stability, plot_comparison
from climath.model import Model

@route('/')
@view('overview')
def overview():
    pp = perm_params(request.query)
    return dict(url_params=pp)

@route('/run/<modelid>')
@view('preparesimulation')
def preparesimulation(modelid):
    pp = perm_params(request.query)
    model = Model(modelid, pp)
    initval = request.query.get('initval')
    if initval:
        redirect(make_url('/run/'+modelid+'/'+initval, pp))
    else:
        return dict(model=model, url_params=pp)

@route('/run/<modelid>/<initval:float>')
@view('runsimulation')
def runsimulation(modelid, initval):
    pp = perm_params(request.query)
    model = Model(modelid, pp)
    initval = float(initval)
    plot = svg_plot(plot_euler(model.get_f(), initval, 100))
    if 'dl' in request.query:
        return Response(body=downloadable_svg(plot))
        ## somehow these headers get ignored: :-(
        #headers=[
        #  ('Content-Type', 'image/svg+xml'),
        #  ('Content-Disposition', 'attachment; filename="plot.svg"'),
        #])
    else:
        return dict(plot=headerless_svg(plot), model=model, url_params=pp)

@route('/stabanalysis/<modelid>')
@view('stabanalysis')
def stabanalysis(modelid):
    pp = perm_params(request.query)
    model = Model(modelid, pp)
    plot = svg_plot(plot_stability(model.get_f_with_Qfactor()))
    if 'dl' in request.query:
        return Response(body=downloadable_svg(plot))
    else:
        return dict(plot=headerless_svg(plot), model=model, url_params=pp)

@route('/comparison')
@view('comparison')
def comparison():
    pp = perm_params(request.query)
    model_f  = Model('fraedrich', pp)
    model_gd = Model('griffeldrazin', pp)
    plot = svg_plot(plot_comparison([model_f, model_gd]))
    if 'dl' in request.query:
        return Response(body=downloadable_svg(plot))
    else:
        return dict(plot=headerless_svg(plot), url_params=pp)

@route('/tweakparams')
@view('tweakparams')
def tweakparams():
    taction = request.query.get('taction')
    pp, bad = perm_params(request.query, True)
    return dict(taction=taction, bad_values=bad, url_params=pp)

@route('/static/<path:path>')
def serve_static_file(path):
    return static_file(path, root="static")

application = default_app()

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
