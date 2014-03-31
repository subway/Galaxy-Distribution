# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1393452977.719249
_template_filename='templates/webapps/galaxy/visualization/scatterplot.mako'
_template_uri='visualization/scatterplot.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'body', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 195
        __M_writer(u'\n\n')
        # SOURCE LINE 247
        __M_writer(u'\n\n')
        # SOURCE LINE 256
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(unicode(h.css(
    "base",
    "autocomplete_tagging",
    "jquery-ui/smoothness/jquery-ui"
)))
        # SOURCE LINE 9
        __M_writer(u'\n\n<style type="text/css">\n/*TODO: use/move into base.less*/\n* { margin: 0px; padding: 0px; }\n\n/* -------------------------------------------- general layout */\ndiv.tab-pane {\n    padding: 8px;\n}\n\n/* -------------------------------------------- header */\n.header {\n    margin-bottom: 8px;\n}\n\n#chart-header {\n    padding : 8px;\n    background-color: #ebd9b2;\n    margin-bottom: 16px;\n    overflow: auto;\n}\n\n#chart-header .subtitle {\n    margin: -4px 0px 0px 4px;\n    padding : 0;\n    color: white;\n    font-size: small;\n}\n\n/* -------------------------------------------- main layout */\n#scatterplot {\n    /*from width + margin of chart?*/\n}\n\n.scatterplot-container .tab-pane {\n}\n\n/* -------------------------------------------- all controls */\n\n#scatterplot input[type=button],\n#scatterplot select {\n    width: 100%;\n    max-width: 256px;\n    margin-bottom: 8px;\n}\n\n#scatterplot .help-text,\n#scatterplot .help-text-small {\n    color: grey;\n}\n\n#scatterplot .help-text {\n    padding-bottom: 16px;\n}\n\n#scatterplot .help-text-small {\n    padding: 4px;\n    font-size: smaller;\n}\n\n#scatterplot > * {\n}\n\n#scatterplot input[value=Draw] {\n    display: block;\n    margin-top: 16px;\n}\n\n#scatterplot .numeric-slider-input {\n    max-width: 70%;\n}\n\n/* -------------------------------------------- data controls */\n\n/* -------------------------------------------- chart controls */\n#chart-control .form-input {\n    /*display: table-row;*/\n}\n\n#chart-control label {\n    /*text-align: right;*/\n    margin-bottom: 8px;\n    /*display: table-cell;*/\n}\n\n#chart-control .slider {\n    /*display: table-cell;*/\n    height: 8px;\n    display: block;\n    margin: 8px 0px 0px 8px;\n}\n\n#chart-control .slider-output {\n    /*display: table-cell;*/\n    float: right;\n}\n\n#chart-control input[type="text"] {\n    border: 1px solid lightgrey;\n}\n\n\n/* -------------------------------------------- statistics */\n#stats-display table#chart-stats-table {\n    width: 100%;\n}\n\n#stats-display #chart-stats-table th {\n    width: 30%;\n    padding: 4px;\n    font-weight: bold;\n    color: grey;\n}\n\n#stats-display #chart-stats-table td {\n    border: solid lightgrey;\n    border-width: 1px 0px 0px 1px;\n    padding: 4px;\n}\n\n#stats-display #chart-stats-table td:nth-child(1) {\n    border-width: 1px 0px 0px 0px;\n    padding-right: 1em;\n    text-align: right;\n    font-weight: bold;\n    color: grey;\n}\n\n/* -------------------------------------------- load indicators */\n#loading-indicator {\n    margin: 12px 0px 0px 8px;\n}\n\n#scatterplot #loading-indicator .loading-message {\n    font-style: italic;\n    font-size: smaller;\n    color: grey;\n}\n\n/* -------------------------------------------- chart area */\n#chart-holder {\n    overflow: auto;\n    margin-left: 8px;\n}\n\nsvg .grid-line {\n    fill: none;\n    stroke: lightgrey;\n    stroke-opacity: 0.5;\n    shape-rendering: crispEdges;\n    stroke-dasharray: 3, 3;\n}\n\nsvg .axis path, svg .axis line {\n    fill: none;\n    stroke: black;\n    shape-rendering: crispEdges;\n}\n\nsvg .axis text {\n    font-family: monospace;\n    font-size: 12px;\n}\n\nsvg #x-axis-label, svg #y-axis-label {\n    font-family: sans-serif;\n    font-size: 10px;\n}\n\nsvg .glyph {\n    stroke: none;\n    fill: black;\n    fill-opacity: 0.2;\n}\n    \n/* -------------------------------------------- info box */\n.chart-info-box {\n    border-radius: 4px;\n    padding: 4px;\n    background-color: white;\n    border: 1px solid black;\n}\n\n</style>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        hda = context.get('hda', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 249
        __M_writer(u'\n    <!--dataset info-->\n    <div id="chart-header" class="header">\n        <h2 class="title">Scatterplot of \'')
        # SOURCE LINE 252
        __M_writer(unicode(hda.name))
        __M_writer(u'\'</h2>\n        <p class="subtitle">')
        # SOURCE LINE 253
        __M_writer(unicode(hda.info))
        __M_writer(u'</p>\n    </div>\n    <div id="scatterplot" class="scatterplot-control-form"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        query_args = context.get('query_args', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        hda = context.get('hda', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 197
        __M_writer(u'\n')
        # SOURCE LINE 198
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        # SOURCE LINE 199
        __M_writer(unicode(h.js(

    "libs/underscore",
    "libs/jquery/jquery-ui",
    "libs/d3",

    "mvc/base-mvc",
    "utils/LazyDataLoader",
    "viz/scatterplot"
)))
        # SOURCE LINE 208
        __M_writer(u'\n\n')
        # SOURCE LINE 210
        __M_writer(unicode(h.templates(
    "../../templates/compiled/template-visualization-scatterplotControlForm",
    "../../templates/compiled/template-visualization-dataControl",
    "../../templates/compiled/template-visualization-chartControl",
    "../../templates/compiled/template-visualization-chartDisplay",
    "../../templates/compiled/template-visualization-statsDisplay"
)))
        # SOURCE LINE 216
        __M_writer(u'\n\n')
        # SOURCE LINE 218
        __M_writer(unicode(h.js(
    "mvc/visualizations/scatterplotControlForm",
)))
        # SOURCE LINE 220
        __M_writer(u'\n\n<script type="text/javascript">\n$(function(){\n\n    var hda             = ')
        # SOURCE LINE 225
        __M_writer(unicode(h.to_json_string( trans.security.encode_dict_ids( hda.to_dict() ) )))
        __M_writer(u',\n        querySettings   = ')
        # SOURCE LINE 226
        __M_writer(unicode(h.to_json_string( query_args )))
        __M_writer(u',\n        chartConfig     = _.extend( querySettings, {\n            containerSelector : \'#chart\',\n            //TODO: move to ScatterplotControlForm.initialize\n            marginTop   : ( querySettings.marginTop > 20 )?( querySettings.marginTop ):( 20 ),\n\n            xColumn     : querySettings.xColumn,\n            yColumn     : querySettings.yColumn,\n            idColumn    : querySettings.idColumn\n        });\n    //console.debug( querySettings );\n\n    var settingsForm = new ScatterplotControlForm({\n        dataset         : hda,\n        apiDatasetsURL  : "')
        # SOURCE LINE 240
        __M_writer(unicode(h.url_for( controller='/api/datasets', action='index' )))
        __M_writer(u'",\n        el              : $( \'#scatterplot\' ),\n        chartConfig     : chartConfig\n    }).render();\n\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


