# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1385062952.328552
_template_filename='templates/webapps/galaxy/admin/index.mako'
_template_uri='/webapps/galaxy/admin/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['left_panel', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x2aea90116d50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2aea90116d50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2aea90116d50')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 121
        __M_writer(u'\n\n')
        # SOURCE LINE 126
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2aea90116d50')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        installing_repository_ids = _import_ns.get('installing_repository_ids', context.get('installing_repository_ids', UNDEFINED))
        installed_repositories = _import_ns.get('installed_repositories', context.get('installed_repositories', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>Administration</div>\n    </div>\n    <div class="unified-panel-body">\n        <div class="toolMenu">\n            <div class="toolSectionList">\n                <div class="toolSectionTitle">Security</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 52
        __M_writer(unicode(h.url_for( controller='admin', action='users' )))
        __M_writer(u'" target="galaxy_main">Manage users</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 53
        __M_writer(unicode(h.url_for( controller='admin', action='groups' )))
        __M_writer(u'" target="galaxy_main">Manage groups</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 54
        __M_writer(unicode(h.url_for( controller='admin', action='roles' )))
        __M_writer(u'" target="galaxy_main">Manage roles</a></div>\n')
        # SOURCE LINE 55
        if trans.app.config.allow_user_impersonation:
            # SOURCE LINE 56
            __M_writer(u'                            <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin', action='impersonate' )))
            __M_writer(u'" target="galaxy_main">Impersonate a user</a></div>\n')
            pass
        # SOURCE LINE 58
        __M_writer(u'                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Data</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 64
        __M_writer(unicode(h.url_for( controller='admin', action='quotas' )))
        __M_writer(u'" target="galaxy_main">Manage quotas</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 65
        __M_writer(unicode(h.url_for( controller='library_admin', action='browse_libraries' )))
        __M_writer(u'" target="galaxy_main">Manage data libraries</a></div>\n')
        # SOURCE LINE 66
        if trans.app.config.enable_beta_job_managers:
            # SOURCE LINE 67
            __M_writer(u'                            <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='data_admin', action='manage_data' )))
            __M_writer(u'" target="galaxy_main">Manage local data</a></div>\n')
            pass
        # SOURCE LINE 69
        __M_writer(u'                        <div class="toolTitle"><a href="')
        __M_writer(unicode(h.url_for( controller='data_manager' )))
        __M_writer(u'" target="galaxy_main">Manage local data (beta)</a></div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Server</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 76
        __M_writer(unicode(h.url_for( controller='admin', action='view_datatypes_registry' )))
        __M_writer(u'" target="galaxy_main">View data types registry</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 77
        __M_writer(unicode(h.url_for( controller='admin', action='view_tool_data_tables' )))
        __M_writer(u'" target="galaxy_main">View data tables registry</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 78
        __M_writer(unicode(h.url_for( controller='admin', action='tool_versions' )))
        __M_writer(u'" target="galaxy_main">View tool lineage</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 79
        __M_writer(unicode(h.url_for( controller='admin', action='reload_tool' )))
        __M_writer(u'" target="galaxy_main">Reload a tool\'s configuration</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 80
        __M_writer(unicode(h.url_for( controller='admin', action='memdump' )))
        __M_writer(u'" target="galaxy_main">Profile memory usage</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 81
        __M_writer(unicode(h.url_for( controller='admin', action='jobs' )))
        __M_writer(u'" target="galaxy_main">Manage jobs</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 82
        __M_writer(unicode(h.url_for( controller='admin', action='review_tool_migration_stages' )))
        __M_writer(u'" target="galaxy_main">Review tool migration stages</a></div>\n')
        # SOURCE LINE 83
        if installing_repository_ids:
            # SOURCE LINE 84
            __M_writer(u'                            <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='monitor_repository_installation', tool_shed_repository_ids=installing_repository_ids )))
            __M_writer(u'" target="galaxy_main">Monitor installing tool shed repositories</a></div>\n')
            pass
        # SOURCE LINE 86
        if installed_repositories:
            # SOURCE LINE 87
            __M_writer(u'                            <div class="toolTitle"><a href="')
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='reset_metadata_on_selected_installed_repositories' )))
            __M_writer(u'" target="galaxy_main">Reset metadata for tool shed repositories</a></div>\n                            <div class="toolTitle"><a href="')
            # SOURCE LINE 88
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_repositories' )))
            __M_writer(u'" target="galaxy_main">Manage installed tool shed repositories</a></div>\n')
            pass
        # SOURCE LINE 90
        __M_writer(u'                    </div>\n                </div>\n')
        # SOURCE LINE 92
        if trans.app.tool_shed_registry and trans.app.tool_shed_registry.tool_sheds:
            # SOURCE LINE 93
            __M_writer(u'                    <div class="toolSectionPad"></div>\n                    <div class="toolSectionTitle">Tool sheds</div>\n                    <div class="toolSectionBody">\n                        <div class="toolSectionBg">                        \n                            <div class="toolTitle"><a href="')
            # SOURCE LINE 97
            __M_writer(unicode(h.url_for( controller='admin_toolshed', action='browse_tool_sheds' )))
            __M_writer(u'" target="galaxy_main">Search and browse tool sheds</a></div>\n                        </div>\n                    </div>\n')
            pass
        # SOURCE LINE 101
        __M_writer(u'                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Form Definitions</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 105
        __M_writer(unicode(h.url_for( controller='forms', action='browse_form_definitions' )))
        __M_writer(u'" target="galaxy_main">Manage form definitions</a></div>\n                    </div>\n                </div>\n                <div class="toolSectionPad"></div>\n                <div class="toolSectionTitle">Sample Tracking</div>\n                <div class="toolSectionBody">\n                    <div class="toolSectionBg">\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 112
        __M_writer(unicode(h.url_for( controller='external_service', action='browse_external_services' )))
        __M_writer(u'" target="galaxy_main">Manage sequencers and external services</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 113
        __M_writer(unicode(h.url_for( controller='request_type', action='browse_request_types' )))
        __M_writer(u'" target="galaxy_main">Manage request types</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 114
        __M_writer(unicode(h.url_for( controller='requests_admin', action='browse_requests' )))
        __M_writer(u'" target="galaxy_main">Sequencing requests</a></div>\n                        <div class="toolTitle"><a href="')
        # SOURCE LINE 115
        __M_writer(unicode(h.url_for( controller='requests_common', action='find_samples', cntrller='requests_admin' )))
        __M_writer(u'" target="galaxy_main">Find samples</a></div>\n                    </div>\n                </div>\n            </div>\n        </div>    \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2aea90116d50')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'Galaxy Administration')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2aea90116d50')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 123
        __M_writer(u'\n    ')
        # SOURCE LINE 124
        center_url = h.url_for( controller='admin', action='center', message=message, status=status ) 
        
        __M_writer(u'\n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="')
        # SOURCE LINE 125
        __M_writer(unicode(center_url))
        __M_writer(u'"> </iframe>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2aea90116d50')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'    \n')
        # SOURCE LINE 10
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging", "tool_menu" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 13
        __M_writer(u'    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n    <style type="text/css">\n        body { margin: 0; padding: 0; overflow: hidden; }\n        #left {\n            background: #C1C9E5 url(')
        # SOURCE LINE 18
        __M_writer(unicode(h.url_for('/static/style/menu_bg.png')))
        __M_writer(u') top repeat-x;\n        }\n\n        .unified-panel-body {\n            overflow: auto;\n        }\n        .toolMenu {\n            margin: 8px 0 0 10px;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2aea90116d50')._populate(_import_ns, [u'render_msg'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n    ')
        # SOURCE LINE 35

        self.has_left_panel=True
        self.has_right_panel=False
        self.active_view="admin"
            
        
        # SOURCE LINE 39
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2aea90116d50')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n    ')
        # SOURCE LINE 31
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


