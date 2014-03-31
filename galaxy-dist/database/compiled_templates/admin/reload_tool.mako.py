# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1393453359.168796
_template_filename='templates/admin/reload_tool.mako'
_template_uri='/admin/reload_tool.mako'
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
    ns = runtime.TemplateNamespace('__anon_0xb4eaf10', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0xb4eaf10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xb4eaf10')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        tool_id = _import_ns.get('tool_id', context.get('tool_id', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        toolbox = _import_ns.get('toolbox', context.get('toolbox', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n<script type="text/javascript">\n$().ready(function() {\n')
        # SOURCE LINE 6
        if tool_id:
            # SOURCE LINE 7
            __M_writer(u'    var focus_el = $("input[name=reload_tool_button]");\n')
            # SOURCE LINE 8
        else:
            # SOURCE LINE 9
            __M_writer(u'    var focus_el = $("select[name=tool_id]");\n')
            pass
        # SOURCE LINE 11
        __M_writer(u'    focus_el.focus();\n});\n</script>\n\n')
        # SOURCE LINE 15
        if message:
            # SOURCE LINE 16
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 18
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Reload Tool</div>\n    <div class="toolFormBody">\n    <form name="reload_tool" id="reload_tool" action="')
        # SOURCE LINE 22
        __M_writer(unicode(h.url_for( controller='admin', action='reload_tool' )))
        __M_writer(u'" method="post" >\n        <div class="form-row">\n            <label>\n                Tool to reload:\n            </label>\n            <select name="tool_id">\n')
        # SOURCE LINE 28
        for key, val in toolbox.tool_panel.items():
            # SOURCE LINE 29
            if key.startswith( 'tool' ):
                # SOURCE LINE 30
                __M_writer(u'                        <option value="')
                __M_writer(unicode(val.id))
                __M_writer(u'">')
                __M_writer(unicode(val.name))
                __M_writer(u'</option>\n')
                # SOURCE LINE 31
            elif key.startswith( 'section' ):
                # SOURCE LINE 32
                __M_writer(u'                        <optgroup label="')
                __M_writer(unicode(val.name))
                __M_writer(u'">\n                        ')
                # SOURCE LINE 33
                section = val 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['section'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                # SOURCE LINE 34
                for section_key, section_val in section.elems.items():
                    # SOURCE LINE 35
                    if section_key.startswith( 'tool' ):
                        # SOURCE LINE 36
                        __M_writer(u'                                ')
                        selected_str = "" 
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['selected_str'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n')
                        # SOURCE LINE 37
                        if section_val.id == tool_id:
                            # SOURCE LINE 38
                            __M_writer(u'                                     ')
                            selected_str = " selected=\"selected\"" 
                            
                            __M_locals_builtin_stored = __M_locals_builtin()
                            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['selected_str'] if __M_key in __M_locals_builtin_stored]))
                            __M_writer(u'\n')
                            pass
                        # SOURCE LINE 40
                        __M_writer(u'                                <option value="')
                        __M_writer(unicode(section_val.id))
                        __M_writer(u'"')
                        __M_writer(unicode(selected_str))
                        __M_writer(u'>')
                        __M_writer(unicode(section_val.name))
                        __M_writer(u'</option>\n')
                        pass
                    pass
                pass
            pass
        # SOURCE LINE 45
        __M_writer(u'            </select>\n        </div>\n        <div class="form-row">\n            <input type="submit" name="reload_tool_button" value="Reload"/>\n        </div>\n    </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


