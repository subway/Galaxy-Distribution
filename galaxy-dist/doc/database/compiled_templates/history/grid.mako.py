# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384522078.599725
_template_filename='templates/webapps/galaxy/history/grid.mako'
_template_uri='/history/grid.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['grid_javascripts', 'grid_body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x192d6310', context._clean_inheritance_tokens(), templateuri=u'/refresh_frames.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x192d6310')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../grid_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x192d6310')._populate(_import_ns, [u'handle_refresh_frames'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n')
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x192d6310')._populate(_import_ns, [u'handle_refresh_frames'])
        handle_refresh_frames = _import_ns.get('handle_refresh_frames', context.get('handle_refresh_frames', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(unicode(parent.grid_javascripts()))
        __M_writer(u'\n\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(handle_refresh_frames()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_grid_body(context,grid):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x192d6310')._populate(_import_ns, [u'handle_refresh_frames'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n    ')
        # SOURCE LINE 12
        __M_writer(unicode(self.make_grid( grid )))
        __M_writer(u'\n    <br/>\n    <div class="toolParamHelp" style="clear: both;">\n        Histories that have been deleted for more than a time period specified by the Galaxy administrator(s) may be permanently deleted.\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


