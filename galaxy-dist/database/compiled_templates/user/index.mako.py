# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1385061717.756123
_template_filename='templates/user/index.mako'
_template_uri='/user/index.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x12a1ba50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x12a1ba50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x12a1ba50')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        t = _import_ns.get('t', context.get('t', UNDEFINED))
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        if message:
            # SOURCE LINE 5
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        if trans.user:
            # SOURCE LINE 9
            __M_writer(u'    <h2>')
            __M_writer(unicode(_('User preferences')))
            __M_writer(u'</h2>\n    <p>You are currently logged in as ')
            # SOURCE LINE 10
            __M_writer(unicode(trans.user.email))
            __M_writer(u'.</p>\n    <ul>\n')
            # SOURCE LINE 12
            if t.webapp.name == 'galaxy':
                # SOURCE LINE 13
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(h.url_for( controller='user', action='manage_user_info', cntrller=cntrller )))
                __M_writer(u'">')
                __M_writer(unicode(_('Manage your information')))
                __M_writer(u'</a></li>\n            <li><a href="')
                # SOURCE LINE 14
                __M_writer(unicode(h.url_for( controller='user', action='set_default_permissions', cntrller=cntrller )))
                __M_writer(u'">')
                __M_writer(unicode(_('Change default permissions')))
                __M_writer(u'</a> for new histories</li>\n            <li><a href="')
                # SOURCE LINE 15
                __M_writer(unicode(h.url_for( controller='user', action='api_keys', cntrller=cntrller )))
                __M_writer(u'">')
                __M_writer(unicode(_('Manage your API keys')))
                __M_writer(u'</a></li>\n            <li><a href="')
                # SOURCE LINE 16
                __M_writer(unicode(h.url_for( controller='user', action='toolbox_filters', cntrller=cntrller )))
                __M_writer(u'">')
                __M_writer(unicode(_('Manage your ToolBox filters')))
                __M_writer(u'</a></li>\n')
                # SOURCE LINE 17
                if trans.app.config.enable_openid:
                    # SOURCE LINE 18
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(h.url_for( controller='user', action='openid_manage', cntrller=cntrller )))
                    __M_writer(u'">')
                    __M_writer(unicode(_('Manage OpenIDs')))
                    __M_writer(u'</a> linked to your account</li>\n')
                    pass
                # SOURCE LINE 20
                if trans.app.config.use_remote_user:
                    # SOURCE LINE 21
                    if trans.app.config.remote_user_logout_href:
                        # SOURCE LINE 22
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(trans.app.config.remote_user_logout_href))
                        __M_writer(u'" target="_top">')
                        __M_writer(unicode(_('Logout')))
                        __M_writer(u'</a></li>\n')
                        pass
                    # SOURCE LINE 24
                else:
                    # SOURCE LINE 25
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(h.url_for( controller='user', action='logout', logout_all=True )))
                    __M_writer(u'" target="_top">')
                    __M_writer(unicode(_('Logout')))
                    __M_writer(u'</a> ')
                    __M_writer(unicode(_('of all user sessions')))
                    __M_writer(u'</li>\n')
                    pass
                # SOURCE LINE 27
            else:
                # SOURCE LINE 28
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(h.url_for( controller='user', action='manage_user_info', cntrller=cntrller )))
                __M_writer(u'">')
                __M_writer(unicode(_('Manage your information')))
                __M_writer(u'</a></li>\n            <li><a href="')
                # SOURCE LINE 29
                __M_writer(unicode(h.url_for( controller='user', action='api_keys', cntrller=cntrller )))
                __M_writer(u'">')
                __M_writer(unicode(_('Manage your API keys')))
                __M_writer(u'</a></li>\n            <li><a href="')
                # SOURCE LINE 30
                __M_writer(unicode(h.url_for( controller='repository', action='manage_email_alerts', cntrller=cntrller )))
                __M_writer(u'">')
                __M_writer(unicode(_('Manage your email alerts')))
                __M_writer(u'</a></li>\n            <li><a href="')
                # SOURCE LINE 31
                __M_writer(unicode(h.url_for( controller='user', action='logout', logout_all=True )))
                __M_writer(u'" target="_top">')
                __M_writer(unicode(_('Logout')))
                __M_writer(u'</a> ')
                __M_writer(unicode(_('of all user sessions')))
                __M_writer(u'</li>\n')
                pass
            # SOURCE LINE 33
            __M_writer(u'    </ul>\n')
            # SOURCE LINE 34
            if t.webapp.name == 'galaxy':
                # SOURCE LINE 35
                __M_writer(u'        <p>\n            You are using <strong>')
                # SOURCE LINE 36
                __M_writer(unicode(trans.user.get_disk_usage( nice_size=True )))
                __M_writer(u'</strong> of disk space in this Galaxy instance.\n')
                # SOURCE LINE 37
                if trans.app.config.enable_quotas:
                    # SOURCE LINE 38
                    __M_writer(u'                Your disk quota is: <strong>')
                    __M_writer(unicode(trans.app.quota_agent.get_quota( trans.user, nice_size=True )))
                    __M_writer(u'</strong>.\n')
                    pass
                # SOURCE LINE 40
                __M_writer(u'            Is your usage more than expected?  See the <a href="http://wiki.g2.bx.psu.edu/Learn/Managing%20Datasets" target="_blank">documentation</a> for tips on how to find all of the data in your account.\n        </p>\n')
                pass
            # SOURCE LINE 43
        else:
            # SOURCE LINE 44
            if not message:
                # SOURCE LINE 45
                __M_writer(u'        <p>')
                __M_writer(unicode(n_('You are currently not logged in.')))
                __M_writer(u'</p>\n')
                pass
            # SOURCE LINE 47
            __M_writer(u'    <ul>\n        <li><a href="')
            # SOURCE LINE 48
            __M_writer(unicode(h.url_for( controller='user', action='login' )))
            __M_writer(u'">')
            __M_writer(unicode(_('Login')))
            __M_writer(u'</li>\n        <li><a href="')
            # SOURCE LINE 49
            __M_writer(unicode(h.url_for( controller='user', action='create', cntrller='user' )))
            __M_writer(u'">')
            __M_writer(unicode(_('Register')))
            __M_writer(u'</a></li>\n    </ul>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


