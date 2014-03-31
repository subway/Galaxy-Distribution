# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1395666872.649122
_template_filename='templates/grid_base_async.mako'
_template_uri='grid_base_async.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x17a4ead0', context._clean_inheritance_tokens(), templateuri=u'./grid_base.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x17a4ead0')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x17a4e310', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x17a4e310')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x17a4ead0')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x17a4e310')._populate(_import_ns, [u'render_message'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_message = _import_ns.get('render_message', context.get('render_message', UNDEFINED))
        render_grid_table_body_contents = _import_ns.get('render_grid_table_body_contents', context.get('render_grid_table_body_contents', UNDEFINED))
        grid = _import_ns.get('grid', context.get('grid', UNDEFINED))
        render_grid_table_footer_contents = _import_ns.get('render_grid_table_footer_contents', context.get('render_grid_table_footer_contents', UNDEFINED))
        show_item_checkboxes = _import_ns.get('show_item_checkboxes', context.get('show_item_checkboxes', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4

    # Set flag to indicate whether grid has operations that operate on multiple items.
        multiple_item_ops_exist = False
        for operation in grid.operations:
            if operation.allow_multiple:
                multiple_item_ops_exist = True
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['multiple_item_ops_exist','operation'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(unicode(render_grid_table_body_contents( grid, show_item_checkboxes=( show_item_checkboxes or multiple_item_ops_exist ) )))
        __M_writer(u'\n*****\n')
        # SOURCE LINE 14
        __M_writer(unicode(render_grid_table_footer_contents( grid, show_item_checkboxes=( show_item_checkboxes or multiple_item_ops_exist ) )))
        __M_writer(u'\n*****\n')
        # SOURCE LINE 16
        __M_writer(unicode(render_message( message, status )))
        return ''
    finally:
        context.caller_stack._pop_frame()


