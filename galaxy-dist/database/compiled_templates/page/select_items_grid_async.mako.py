# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1400717744.204384
_template_filename='templates/webapps/galaxy/page/select_items_grid_async.mako'
_template_uri='/page/select_items_grid_async.mako'
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
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x2b0ce82e3950', context._clean_inheritance_tokens(), templateuri=u'../grid_base.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b0ce82e3950')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x2b0ce82e36d0', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b0ce82e36d0')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b0ce82e3950')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x2b0ce82e36d0')._populate(_import_ns, [u'render_message'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        num_pages = _import_ns.get('num_pages', context.get('num_pages', UNDEFINED))
        render_message = _import_ns.get('render_message', context.get('render_message', UNDEFINED))
        render_grid_table_body_contents = _import_ns.get('render_grid_table_body_contents', context.get('render_grid_table_body_contents', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        show_item_checkboxes = _import_ns.get('show_item_checkboxes', context.get('show_item_checkboxes', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(unicode(render_grid_table_body_contents( grid, show_item_checkboxes=show_item_checkboxes )))
        __M_writer(u'\n*****\n')
        # SOURCE LINE 7
        __M_writer(unicode(num_pages))
        __M_writer(u'\n*****\n')
        # SOURCE LINE 9
        __M_writer(unicode(render_message( message, status )))
        return ''
    finally:
        context.caller_stack._pop_frame()


