# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399327087.120515
_template_filename='templates/webapps/galaxy/page/create.mako'
_template_uri='page/create.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['javascripts']


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
    return runtime._inherit_from(context, u'/form.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n<script type="text/javascript">\n$(function(){\n    var page_name = $("input[name=page_title]");\n    var page_slug = $("input[name=page_slug]");\n    page_name.keyup(function(){\n        page_slug.val( $(this).val().replace(/\\s+/g,\'-\').replace(/[^a-zA-Z0-9\\-]/g,\'\').toLowerCase() )\n    });    \n})\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


