# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399385560.78189
_template_filename='templates/webapps/galaxy/page/select_items_grid.mako'
_template_uri='/page/select_items_grid.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x13b33890', context._clean_inheritance_tokens(), templateuri=u'../grid_base.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x13b33890')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x13b33890')._populate(_import_ns, [u'*'])
        stylesheets = _import_ns.get('stylesheets', context.get('stylesheets', UNDEFINED))
        grid_javascripts = _import_ns.get('grid_javascripts', context.get('grid_javascripts', UNDEFINED))
        render_grid_header = _import_ns.get('render_grid_header', context.get('render_grid_header', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        render_grid_table = _import_ns.get('render_grid_table', context.get('render_grid_table', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(unicode(grid_javascripts()))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(unicode(stylesheets()))
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(unicode(render_grid_header( grid, False )))
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(unicode(render_grid_table( grid, show_item_checkboxes=True )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


