# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1395877554.776674
_template_filename=u'templates/user/info.mako'
_template_uri=u'/user/info.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_user_info']


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
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cntrller = context.get('cntrller', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        is_admin = cntrller == 'admin' and trans.user_is_admin() 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_admin'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 76
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_user_info(context):
    context.caller_stack._push_frame()
    try:
        username = context.get('username', UNDEFINED)
        h = context.get('h', UNDEFINED)
        is_admin = context.get('is_admin', UNDEFINED)
        user = context.get('user', UNDEFINED)
        cntrller = context.get('cntrller', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        email = context.get('email', UNDEFINED)
        t = context.get('t', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    <h2>Manage User Information</h2>\n')
        # SOURCE LINE 7
        if not is_admin:
            # SOURCE LINE 8
            __M_writer(u'        <ul class="manage-table-actions">\n            <li>\n                <a class="action-button"  href="')
            # SOURCE LINE 10
            __M_writer(unicode(h.url_for( controller='user', action='index', cntrller=cntrller )))
            __M_writer(u'">User preferences</a>\n            </li>\n        </ul>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'    <div class="toolForm">\n        <form name="login_info" id="login_info" action="')
        # SOURCE LINE 15
        __M_writer(unicode(h.url_for( controller='user', action='edit_info', cntrller=cntrller, user_id=trans.security.encode_id( user.id ) )))
        __M_writer(u'" method="post" >\n            <div class="toolFormTitle">Login Information</div>\n            <div class="form-row">\n                <label>Email address:</label>\n                <input type="text" name="email" value="')
        # SOURCE LINE 19
        __M_writer(unicode(email))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Public name:</label>\n')
        # SOURCE LINE 23
        if t.webapp.name == 'tool_shed':
            # SOURCE LINE 24
            if user.active_repositories:
                # SOURCE LINE 25
                __M_writer(u'                        <input type="hidden" name="username" value="')
                __M_writer(unicode(username))
                __M_writer(u'"/>\n                        ')
                # SOURCE LINE 26
                __M_writer(unicode(username))
                __M_writer(u'\n                        <div class="toolParamHelp" style="clear: both;">\n                            You cannot change your public name after you have created a repository in this tool shed.\n                        </div>\n')
                # SOURCE LINE 30
            else:
                # SOURCE LINE 31
                __M_writer(u'                        <input type="text" name="username" size="40" value="')
                __M_writer(unicode(username))
                __M_writer(u'"/>\n                        <div class="toolParamHelp" style="clear: both;">\n                            Your public name provides a means of identifying you publicly within this tool shed. Public\n                            names must be at least four characters in length and contain only lower-case letters, numbers,\n                            and the \'-\' character.  You cannot change your public name after you have created a repository\n                            in this tool shed.\n                        </div>\n')
                pass
            # SOURCE LINE 39
        else:
            # SOURCE LINE 40
            __M_writer(u'                    <input type="text" name="username" size="40" value="')
            __M_writer(unicode(username))
            __M_writer(u'"/>\n                    <div class="toolParamHelp" style="clear: both;">\n                        Your public name is an optional identifier that will be used to generate addresses for information\n                        you share publicly. Public names must be at least four characters in length and contain only lower-case\n                        letters, numbers, and the \'-\' character.\n                    </div>\n')
            pass
        # SOURCE LINE 47
        __M_writer(u'            </div>\n            <div class="form-row">\n                <input type="submit" name="login_info_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n    <p></p>\n    <div class="toolForm">\n        <form name="change_password" id="change_password" action="')
        # SOURCE LINE 55
        __M_writer(unicode(h.url_for( controller='user', action='edit_info', cntrller=cntrller, user_id=trans.security.encode_id( user.id ) )))
        __M_writer(u'" method="post" >\n            <div class="toolFormTitle">Change Password</div>\n')
        # SOURCE LINE 57
        if not is_admin:
            # SOURCE LINE 58
            __M_writer(u'                <div class="form-row">\n                    <label>Current password:</label>\n                    <input type="password" name="current" value="" size="40"/>\n                </div>\n')
            pass
        # SOURCE LINE 63
        __M_writer(u'            <div class="form-row">\n                <label>New password:</label>\n                <input type="password" name="password" value="" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Confirm:</label>\n                <input type="password" name="confirm" value="" size="40"/>\n            </div>\n            <div class="form-row">\n                <input type="submit" name="change_password_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


