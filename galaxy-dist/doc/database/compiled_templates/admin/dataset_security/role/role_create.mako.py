# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1395878088.876685
_template_filename='templates/admin/dataset_security/role/role_create.mako'
_template_uri='/admin/dataset_security/role/role_create.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x15b7f310', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x15b7f310')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x15b7f310')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        name = _import_ns.get('name', context.get('name', UNDEFINED))
        in_users = _import_ns.get('in_users', context.get('in_users', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        def render_select(name,options):
            return render_render_select(context.locals_(__M_locals),name,options)
        create_group_for_role_checked = _import_ns.get('create_group_for_role_checked', context.get('create_group_for_role_checked', UNDEFINED))
        out_groups = _import_ns.get('out_groups', context.get('out_groups', UNDEFINED))
        in_groups = _import_ns.get('in_groups', context.get('in_groups', UNDEFINED))
        out_users = _import_ns.get('out_users', context.get('out_users', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n<script type="text/javascript">\n    $().ready(function() {  \n        $(\'#groups_add_button\').click(function() {\n            return !$(\'#out_groups option:selected\').remove().appendTo(\'#in_groups\');\n        });\n        $(\'#groups_remove_button\').click(function() {\n            return !$(\'#in_groups option:selected\').remove().appendTo(\'#out_groups\');\n        });\n        $(\'#users_add_button\').click(function() {\n            return !$(\'#out_users option:selected\').remove().appendTo(\'#in_users\');\n        });\n        $(\'#users_remove_button\').click(function() {\n            return !$(\'#in_users option:selected\').remove().appendTo(\'#out_users\');\n        });\n        $(\'form#associate_role_group_user\').submit(function() {\n            $(\'#in_groups option\').each(function(i) {\n                $(this).attr("selected", "selected");\n            });\n            $(\'#in_users option\').each(function(i) {\n                $(this).attr("selected", "selected");\n            });\n        });\n        //Temporary removal of select2 for inputs -- refactor this later.\n        $(\'select\').select2("destroy");\n    });\n</script>\n\n')
        # SOURCE LINE 48

        from galaxy.web.form_builder import CheckboxField
        create_group_for_role_checkbox = CheckboxField( 'create_group_for_role' )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['create_group_for_role_checkbox','CheckboxField'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        if message:
            # SOURCE LINE 54
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 56
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Create Role</div>\n    <div class="toolFormBody">\n        <form name="associate_role_group_user" id="associate_role_group_user" action="')
        # SOURCE LINE 60
        __M_writer(unicode(h.url_for(controller='admin', action='create_role' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Name:</label>\n                <input  name="name" type="textfield" value="')
        # SOURCE LINE 63
        __M_writer(unicode(name))
        __M_writer(u'" size=40"/>\n            </div>\n            <div class="form-row">\n                <label>Description:</label>\n                <input  name="description" type="textfield" value="')
        # SOURCE LINE 67
        __M_writer(unicode(description))
        __M_writer(u'" size=40"/>\n            </div>\n            <div class="form-row">\n                <div style="float: left; margin-right: 10px;">\n                    <label>Groups associated with new role</label>\n                    ')
        # SOURCE LINE 72
        __M_writer(unicode(render_select( "in_groups", in_groups )))
        __M_writer(u'<br/>\n                    <input type="submit" id="groups_remove_button" value=">>"/>\n                </div>\n                <div>\n                    <label>Groups not associated with new role</label>\n                    ')
        # SOURCE LINE 77
        __M_writer(unicode(render_select( "out_groups", out_groups )))
        __M_writer(u'<br/>\n                    <input type="submit" id="groups_add_button" value="<<"/>\n                </div>\n            </div>\n            <div class="form-row">\n                <div style="float: left; margin-right: 10px;">\n                    <label>Users associated with new role</label>\n                    ')
        # SOURCE LINE 84
        __M_writer(unicode(render_select( "in_users", in_users )))
        __M_writer(u'<br/>\n                    <input type="submit" id="users_remove_button" value=">>"/>\n                </div>\n                <div>\n                    <label>Users not associated with new role</label>\n                    ')
        # SOURCE LINE 89
        __M_writer(unicode(render_select( "out_users", out_users )))
        __M_writer(u'<br/>\n                    <input type="submit" id="users_add_button" value="<<"/>\n                </div>\n            </div>\n            <div class="form-row">\n')
        # SOURCE LINE 94
        if create_group_for_role_checked:
            # SOURCE LINE 95
            __M_writer(u'                    ')
            create_group_for_role_checkbox.checked = True 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 97
        __M_writer(u'                ')
        __M_writer(unicode(create_group_for_role_checkbox.get_html()))
        __M_writer(u' Create a new group of the same name for this role\n            </div>\n            <div class="form-row">\n                <input type="submit" name="create_role_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_select(context,name,options):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x15b7f310')._populate(_import_ns, [u'render_msg'])
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
        _mako_get_namespace(context, '__anon_0x15b7f310')._populate(_import_ns, [u'render_msg'])
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


