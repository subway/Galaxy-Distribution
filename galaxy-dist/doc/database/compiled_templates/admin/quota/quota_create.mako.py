# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1391895601.278119
_template_filename='templates/admin/quota/quota_create.mako'
_template_uri='/admin/quota/quota_create.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x2b65d4437ed0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b65d4437ed0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b65d4437ed0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        name = _import_ns.get('name', context.get('name', UNDEFINED))
        operation = _import_ns.get('operation', context.get('operation', UNDEFINED))
        default = _import_ns.get('default', context.get('default', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        def render_select(name,options):
            return render_render_select(context.locals_(__M_locals),name,options)
        out_groups = _import_ns.get('out_groups', context.get('out_groups', UNDEFINED))
        amount = _import_ns.get('amount', context.get('amount', UNDEFINED))
        in_users = _import_ns.get('in_users', context.get('in_users', UNDEFINED))
        in_groups = _import_ns.get('in_groups', context.get('in_groups', UNDEFINED))
        out_users = _import_ns.get('out_users', context.get('out_users', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
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
        __M_writer(u'\n\n<script type="text/javascript">\n    $().ready(function() {  \n        $(\'#groups_add_button\').click(function() {\n            return !$(\'#out_groups option:selected\').remove().appendTo(\'#in_groups\');\n        });\n        $(\'#groups_remove_button\').click(function() {\n            return !$(\'#in_groups option:selected\').remove().appendTo(\'#out_groups\');\n        });\n        $(\'#users_add_button\').click(function() {\n            return !$(\'#out_users option:selected\').remove().appendTo(\'#in_users\');\n        });\n        $(\'#users_remove_button\').click(function() {\n            return !$(\'#in_users option:selected\').remove().appendTo(\'#out_users\');\n        });\n        $(\'form#associate_quota_group_user\').submit(function() {\n            $(\'#in_groups option\').each(function(i) {\n                $(this).attr("selected", "selected");\n            });\n            $(\'#in_users option\').each(function(i) {\n                $(this).attr("selected", "selected");\n            });\n        });\n        //Temporary removal of select2 for inputs -- refactor this later.\n        $(\'select\').select2("destroy");\n    });\n</script>\n\n')
        # SOURCE LINE 48

        from galaxy.web.form_builder import SelectField
        operation_selectfield = SelectField( 'operation' )
        for op in ( '=', '+', '-' ):
            selected = op == operation
            operation_selectfield.add_option( op, op, selected )
        default_selectfield = SelectField( 'default' )
        selected = 'no' == default
        default_selectfield.add_option( 'No', 'no', selected )
        for typ in trans.app.model.DefaultQuotaAssociation.types.__dict__.values():
            selected = typ == default
            default_selectfield.add_option( 'Yes, ' + typ, typ, selected )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['selected','operation_selectfield','SelectField','typ','default_selectfield','op'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 60
        __M_writer(u'\n\n')
        # SOURCE LINE 62
        if message:
            # SOURCE LINE 63
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 65
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Create quota</div>\n    <div class="toolFormBody">\n        <form name="associate_quota_group_user" id="associate_quota_group_user" action="')
        # SOURCE LINE 69
        __M_writer(unicode(h.url_for(controller='admin', action='create_quota' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Name:</label>\n                <input  name="name" type="textfield" value="')
        # SOURCE LINE 72
        __M_writer(unicode(name))
        __M_writer(u'" size=40"/>\n            </div>\n            <div class="form-row">\n                <label>Description:</label>\n                <input  name="description" type="textfield" value="')
        # SOURCE LINE 76
        __M_writer(unicode(description))
        __M_writer(u'" size=40"/>\n            </div>\n            <div class="form-row">\n                <label>Amount</label>\n                <input  name="amount" type="textfield" value="')
        # SOURCE LINE 80
        __M_writer(unicode(amount))
        __M_writer(u'" size=40"/>\n                <div class="toolParamHelp" style="clear: both;">\n                    Examples: "10000MB", "99 gb", "0.2T", "unlimited"\n                </div>\n            </div>\n            <div class="form-row">\n                <label>Assign, increase by amount, or decrease by amount?</label>\n                ')
        # SOURCE LINE 87
        __M_writer(unicode(operation_selectfield.get_html()))
        __M_writer(u'\n            </div>\n            <div class="form-row">\n                <label>Is this quota a default for a class of users (if yes, what type)?</label>\n                ')
        # SOURCE LINE 91
        __M_writer(unicode(default_selectfield.get_html()))
        __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n                    Warning: Any user or group associations selected below will be ignored if this quota is used as a default.\n                </div>\n            </div>\n            <div class="form-row">\n                <div style="float: left; margin-right: 10px;">\n                    <label>Users associated with new quota</label>\n                    ')
        # SOURCE LINE 99
        __M_writer(unicode(render_select( "in_users", in_users )))
        __M_writer(u'<br/>\n                    <input type="submit" id="users_remove_button" value=">>"/>\n                </div>\n                <div>\n                    <label>Users not associated with new quota</label>\n                    ')
        # SOURCE LINE 104
        __M_writer(unicode(render_select( "out_users", out_users )))
        __M_writer(u'<br/>\n                    <input type="submit" id="users_add_button" value="<<"/>\n                </div>\n            </div>\n            <div class="form-row">\n                <div style="float: left; margin-right: 10px;">\n                    <label>Groups associated with new quota</label>\n                    ')
        # SOURCE LINE 111
        __M_writer(unicode(render_select( "in_groups", in_groups )))
        __M_writer(u'<br/>\n                    <input type="submit" id="groups_remove_button" value=">>"/>\n                </div>\n                <div>\n                    <label>Groups not associated with new quota</label>\n                    ')
        # SOURCE LINE 116
        __M_writer(unicode(render_select( "out_groups", out_groups )))
        __M_writer(u'<br/>\n                    <input type="submit" id="groups_add_button" value="<<"/>\n                </div>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="create_quota_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_select(context,name,options):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b65d4437ed0')._populate(_import_ns, [u'render_msg'])
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
        _mako_get_namespace(context, '__anon_0x2b65d4437ed0')._populate(_import_ns, [u'render_msg'])
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


