# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399385609.585068
_template_filename='templates/webapps/galaxy/history/item_content.mako'
_template_uri='/history/item_content.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x2b80e4741410', context._clean_inheritance_tokens(), templateuri=u'/history/display.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b80e4741410')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b80e4741410')._populate(_import_ns, [u'*'])
        item_data = _import_ns.get('item_data', context.get('item_data', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        render_item = _import_ns.get('render_item', context.get('render_item', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(unicode(render_item( item, item_data )))
        return ''
    finally:
        context.caller_stack._pop_frame()


