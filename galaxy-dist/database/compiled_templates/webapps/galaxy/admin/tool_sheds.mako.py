# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1385062963.491122
_template_filename='templates/webapps/galaxy/admin/tool_sheds.mako'
_template_uri='/webapps/galaxy/admin/tool_sheds.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x23517dd0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x23517dd0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23517dd0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        if message:
            # SOURCE LINE 12
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Accessible Galaxy tool sheds</div>\n    <div class="toolFormBody">\n        <div class="form-row">\n            <table class="grid">\n                ')
        # SOURCE LINE 20
        shed_id = 0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['shed_id'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 21
        for name, url in trans.app.tool_shed_registry.tool_sheds.items():
            # SOURCE LINE 22
            __M_writer(u'                    <tr class="libraryTitle">\n                        <td>\n                            <div style="float: left; margin-left: 1px;" class="menubutton split popup" id="dataset-')
            # SOURCE LINE 24
            __M_writer(unicode(shed_id))
            __M_writer(u'-popup">\n                                <a class="view-info" href="')
            # SOURCE LINE 25
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_shed', tool_shed_url=url )))
            __M_writer(u'">')
            __M_writer(unicode(name))
            __M_writer(u'</a>\n                            </div>\n                            <div popupmenu="dataset-')
            # SOURCE LINE 27
            __M_writer(unicode(shed_id))
            __M_writer(u'-popup">\n                                <a class="action-button" href="')
            # SOURCE LINE 28
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_shed', tool_shed_url=url )))
            __M_writer(u'">Browse valid repositories</a>\n                                <a class="action-button" href="')
            # SOURCE LINE 29
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='find_tools_in_tool_shed', tool_shed_url=url )))
            __M_writer(u'">Search for valid tools</a>\n                                <a class="action-button" href="')
            # SOURCE LINE 30
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='find_workflows_in_tool_shed', tool_shed_url=url )))
            __M_writer(u'">Search for workflows</a>\n                            </div>\n                        </td>\n                    </tr>\n                    ')
            # SOURCE LINE 34
            shed_id += 1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['shed_id'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'                </tr>\n            </table>\n        </div>\n        <div style="clear: both"></div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23517dd0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(h.css( "library" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23517dd0')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Configured Galaxy tool sheds')
        return ''
    finally:
        context.caller_stack._pop_frame()


