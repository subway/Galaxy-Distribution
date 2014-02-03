# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389658996.360696
_template_filename='templates/webapps/galaxy/history/view.mako'
_template_uri='history/view.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'body', 'init', 'javascripts', 'center_panel']


# SOURCE LINE 5

def inherit(context):
    if context.get('use_panels'):
        return '/webapps/galaxy/base_panels.mako'
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x2b5d1c1e1610', context._clean_inheritance_tokens(), templateuri=u'/root/history_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b5d1c1e1610')] = ns

    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x2b5d1c1e0e90', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b5d1c1e0e90')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x2b5d1c1e1a90', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b5d1c1e1a90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1610')._populate(_import_ns, [u'render_dataset'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e0e90')._populate(_import_ns, [u'get_history_link', u'get_controller_name'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1a90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 89
        __M_writer(u'\n\n')
        # SOURCE LINE 97
        __M_writer(u'\n\n')
        # SOURCE LINE 101
        __M_writer(u'\n\n')
        # SOURCE LINE 160
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1610')._populate(_import_ns, [u'render_dataset'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e0e90')._populate(_import_ns, [u'get_history_link', u'get_controller_name'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1a90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n    ')
        # SOURCE LINE 25
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 26
        __M_writer(unicode(h.css( "history", "autocomplete_tagging" )))
        __M_writer(u'\n\n    <style type="text/css">\n\n        /* these don\'t appear to be used? */\n        .page-body\n        {\n            padding: 10px;\n            float: left;\n            width: 65%;\n        }\n        .page-meta\n        {\n            float: right;\n            width: 27%;\n            padding: 0.5em;\n            margin: 0.25em;\n            vertical-align: text-top;\n            border: 2px solid #DDDDDD;\n            border-top: 4px solid #DDDDDD;\n        }\n\n\n        body {\n            padding: 0px;\n            margin: 0px;\n        }\n\n        div.unified-panel-body {\n            position: absolute;\n            top: 0px;\n            width: 100%;\n        }\n\n        #history-name-area {\n            margin: 12px 0px 0px 16px;\n            font-size: 120%;\n        }\n        #top-links {\n            margin: 4px 0px 8px 16px;\n        }\n\n        .historyItemContainer {\n            /*padding-right: 3px;*/\n        }\n        .historyItemBody {\n            display: none;\n        }\n        div.historyItemWrapper {\n            margin: 0px 4px 0px 4px ;\n            border-left: 1px solid #999999;\n            border-right: 1px solid #999999;\n        }\n        /* TODO: unify with other history css and into .less */\n    </style>\n\n    <noscript>\n        <style>\n            .historyItemBody {\n                display: block;\n            }\n        </style>\n    </noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1610')._populate(_import_ns, [u'render_dataset'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e0e90')._populate(_import_ns, [u'get_history_link', u'get_controller_name'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1a90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        def center_panel():
            return render_center_panel(context)
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n    ')
        # SOURCE LINE 100
        __M_writer(unicode(center_panel()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1610')._populate(_import_ns, [u'render_dataset'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e0e90')._populate(_import_ns, [u'get_history_link', u'get_controller_name'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1a90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 91
        __M_writer(u'\n')
        # SOURCE LINE 92

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        
        
        # SOURCE LINE 96
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1610')._populate(_import_ns, [u'render_dataset'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e0e90')._populate(_import_ns, [u'get_history_link', u'get_controller_name'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1a90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 16
        __M_writer(unicode(h.js( "libs/jquery/jstorage" )))
        __M_writer(u'\n    <script type="text/javascript">\n        $(function() {\n            init_history_items( $("div.historyItemWrapper"), false, "nochanges" );\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1610')._populate(_import_ns, [u'render_dataset'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e0e90')._populate(_import_ns, [u'get_history_link', u'get_controller_name'])
        _mako_get_namespace(context, '__anon_0x2b5d1c1e1a90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        datasets = _import_ns.get('datasets', context.get('datasets', UNDEFINED))
        show_deleted = _import_ns.get('show_deleted', context.get('show_deleted', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        use_panels = _import_ns.get('use_panels', context.get('use_panels', UNDEFINED))
        get_history_link = _import_ns.get('get_history_link', context.get('get_history_link', UNDEFINED))
        render_dataset = _import_ns.get('render_dataset', context.get('render_dataset', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        history = _import_ns.get('history', context.get('history', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 103
        __M_writer(u'\n')
        # SOURCE LINE 105
        __M_writer(u'    ')

        ##TODO: is there a better way to create this URL? Can't use 'f-username' as a key b/c it's not a valid identifier.
        href_to_published_histories = h.url_for( controller='/history', action='list_published')
        if history.user is not None:
            href_to_user_histories = h.url_for( controller='/history', action='list_published', xxx=history.user.username).replace( 'xxx', 'f-username')
        else:
            href_to_user_histories = h.url_for( controller='/history', action='list_published' )##should this instead be be None or empty string?
            
        
        # SOURCE LINE 112
        __M_writer(u'\n    \n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">\n')
        # SOURCE LINE 117
        __M_writer(u'            <div id="history-name-area" class="historyLinks" style="color: gray; font-weight: bold; padding: 0px 0px 5px 0px">\n                <div id="history-name">')
        # SOURCE LINE 118
        __M_writer(unicode(history.get_display_name()))
        __M_writer(u'</div>\n            </div>\n\n            <div id="top-links" class="historyLinks" style="padding: 0px 0px 5px 0px">\n')
        # SOURCE LINE 122
        if not history.purged:
            # SOURCE LINE 123
            __M_writer(u'                    <a href="')
            __M_writer(unicode(h.url_for(controller='history', action='imp', id=trans.security.encode_id(history.id) )))
            __M_writer(u'">import and start using history</a> |\n                    <a href="')
            # SOURCE LINE 124
            __M_writer(unicode(get_history_link( history )))
            __M_writer(u'">')
            __M_writer(unicode(_('refresh')))
            __M_writer(u'</a> |\n')
            pass
        # SOURCE LINE 126
        if show_deleted:
            # SOURCE LINE 127
            __M_writer(u'                    <a href="')
            __M_writer(unicode(h.url_for(controller='history', action='view', id=trans.security.encode_id(history.id), show_deleted=False, use_panels=use_panels )))
            __M_writer(u'">')
            __M_writer(unicode(_('hide deleted')))
            __M_writer(u'</a> |\n')
            # SOURCE LINE 128
        else:
            # SOURCE LINE 129
            __M_writer(u'                    <a href="')
            __M_writer(unicode(h.url_for(controller='history', action='view', id=trans.security.encode_id(history.id), show_deleted=True, use_panels=use_panels )))
            __M_writer(u'">')
            __M_writer(unicode(_('show deleted')))
            __M_writer(u'</a> |\n')
            pass
        # SOURCE LINE 131
        __M_writer(u'                <a href="#" class="toggle">collapse all</a>\n            </div>\n\n')
        # SOURCE LINE 134
        if history.deleted:
            # SOURCE LINE 135
            __M_writer(u'                <div class="warningmessagesmall">\n                    ')
            # SOURCE LINE 136
            __M_writer(unicode(_('You are currently viewing a deleted history!')))
            __M_writer(u'\n                </div>\n                <p></p>\n')
            pass
        # SOURCE LINE 140
        __M_writer(u'\n')
        # SOURCE LINE 141
        if not datasets:
            # SOURCE LINE 142
            __M_writer(u'                <div class="infomessagesmall" id="emptyHistoryMessage">\n\n')
            # SOURCE LINE 144
        else:    
            # SOURCE LINE 146
            for data in datasets:
                # SOURCE LINE 147
                if data.visible:
                    # SOURCE LINE 148
                    __M_writer(u'                        <div class="historyItemContainer visible-right-border" id="historyItemContainer-')
                    __M_writer(unicode(data.id))
                    __M_writer(u'">\n                            ')
                    # SOURCE LINE 149
                    __M_writer(unicode(render_dataset( data, data.hid, show_deleted_on_refresh = show_deleted, for_editing=False )))
                    __M_writer(u'\n                        </div>\n')
                    pass
                pass
            # SOURCE LINE 153
            __M_writer(u'\n                <div class="infomessagesmall" id="emptyHistoryMessage" style="display:none;">\n')
            pass
        # SOURCE LINE 156
        __M_writer(u'                    ')
        __M_writer(unicode(_("Your history is empty. Click 'Get Data' on the left pane to start")))
        __M_writer(u'\n                </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


