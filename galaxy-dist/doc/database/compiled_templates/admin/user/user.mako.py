# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1395878061.81854
_template_filename='templates/admin/user/user.mako'
_template_uri='/admin/user/user.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_select', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x1671c890', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1671c890')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1671c890')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        def render_select(name,options):
            return render_render_select(context.locals_(__M_locals),name,options)
        in_roles = _import_ns.get('in_roles', context.get('in_roles', UNDEFINED))
        out_groups = _import_ns.get('out_groups', context.get('out_groups', UNDEFINED))
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        out_roles = _import_ns.get('out_roles', context.get('out_roles', UNDEFINED))
        in_groups = _import_ns.get('in_groups', context.get('in_groups', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n<script type="text/javascript">\n$().ready(function() {  \n    $(\'#roles_add_button\').click(function() {\n        return !$(\'#out_roles option:selected\').remove().appendTo(\'#in_roles\');\n    });\n    $(\'#roles_remove_button\').click(function() {\n        return !$(\'#in_roles option:selected\').remove().appendTo(\'#out_roles\');\n    });\n    $(\'#groups_add_button\').click(function() {\n        return !$(\'#out_groups option:selected\').remove().appendTo(\'#in_groups\');\n    });\n    $(\'#groups_remove_button\').click(function() {\n        return !$(\'#in_groups option:selected\').remove().appendTo(\'#out_groups\');\n    });\n    $(\'form#associate_user_role_group\').submit(function() {\n        $(\'#in_roles option\').each(function(i) {\n            $(this).attr("selected", "selected");\n        });\n        $(\'#in_groups option\').each(function(i) {\n            $(this).attr("selected", "selected");\n        });\n    });\n});\n</script>\n\n')
        # SOURCE LINE 46
        if message:
            # SOURCE LINE 47
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">User \'')
        # SOURCE LINE 51
        __M_writer(unicode(user.email))
        __M_writer(u'\'</div>\n    <div class="toolFormBody">\n        <form name="associate_user_role_group" id="associate_user_role_group" action="')
        # SOURCE LINE 53
        __M_writer(unicode(h.url_for(controller='admin', action='manage_roles_and_groups_for_user', id=trans.security.encode_id( user.id ) )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <div style="float: left; margin-right: 10px;">\n                    <label>Roles associated with \'')
        # SOURCE LINE 56
        __M_writer(unicode(user.email))
        __M_writer(u"'</label>\n                    ")
        # SOURCE LINE 57
        __M_writer(unicode(render_select( "in_roles", in_roles )))
        __M_writer(u'<br/>\n                    <input type="submit" id="roles_remove_button" value=">>"/>\n                </div>\n                <div>\n                    <label>Roles not associated with \'')
        # SOURCE LINE 61
        __M_writer(unicode(user.email))
        __M_writer(u"'</label>\n                    ")
        # SOURCE LINE 62
        __M_writer(unicode(render_select( "out_roles", out_roles )))
        __M_writer(u'<br/>\n                    <input type="submit" id="roles_add_button" value="<<"/>\n                </div>\n            </div>\n            <div class="form-row">\n                <div style="float: left; margin-right: 10px;">\n                    <label>Groups associated with \'')
        # SOURCE LINE 68
        __M_writer(unicode(user.email))
        __M_writer(u"'</label>\n                    ")
        # SOURCE LINE 69
        __M_writer(unicode(render_select( "in_groups", in_groups )))
        __M_writer(u'<br/>\n                    <input type="submit" id="groups_remove_button" value=">>"/>\n                </div>\n                <div>\n                    <label>Groups not associated with \'')
        # SOURCE LINE 73
        __M_writer(unicode(user.email))
        __M_writer(u"'</label>\n                    ")
        # SOURCE LINE 74
        __M_writer(unicode(render_select( "out_groups", out_groups )))
        __M_writer(u'<br/>\n                    <input type="submit" id="groups_add_button" value="<<"/>\n                </div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="user_roles_groups_edit_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_select(context,name,options):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1671c890')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n    <select name="')
        # SOURCE LINE 14
        __M_writer(unicode(name))
        __M_writer(u'" id="')
        __M_writer(unicode(name))
        __M_writer(u'" style="min-width: 250px; height: 150px;" multiple>\n')
        # SOURCE LINE 15
        for option in options:
            # SOURCE LINE 16
            __M_writer(u'            <option value="')
            __M_writer(unicode(option[0]))
            __M_writer(u'">')
            __M_writer(unicode(option[1]))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 18
        __M_writer(u'    </select>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1671c890')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            $("input:text:first").focus();\n        })\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


