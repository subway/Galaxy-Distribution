# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384452864.359865
_template_filename=u'templates/webapps/galaxy/dataset/display.mako'
_template_uri=u'/dataset/display.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['title', 'center_panel', 'right_panel', 'render_item', 'init', 'render_item_links', 'render_deleted_data_message', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x25ae6c50', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x25ae6c50')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace('__anon_0x25ae6e50', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x25ae6e50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/display_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 57
        __M_writer(u'\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 83
        __M_writer(u'\n\n')
        # SOURCE LINE 95
        __M_writer(u'\n\n')
        # SOURCE LINE 119
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n    Galaxy | ')
        # SOURCE LINE 56
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u' | ')
        __M_writer(filters.html_escape(unicode(get_item_name( item ) )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        item_data = _import_ns.get('item_data', context.get('item_data', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 97
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n                ')
        # SOURCE LINE 100
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u'\n            | ')
        # SOURCE LINE 101
        __M_writer(filters.html_escape(unicode(get_item_name( item ) )))
        __M_writer(u'\n        </div>\n    </div>\n    \n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">        \n            <div class="page-body">\n                <div style="float: right">\n                    ')
        # SOURCE LINE 109
        __M_writer(unicode(self.render_item_links( item )))
        __M_writer(u'\n                </div>\n                <div>\n                    ')
        # SOURCE LINE 112
        __M_writer(unicode(self.render_item_header( item )))
        __M_writer(u'\n                </div>\n                \n                ')
        # SOURCE LINE 115
        __M_writer(unicode(self.render_item( item, item_data )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        render_community_tagging_element = _import_ns.get('render_community_tagging_element', context.get('render_community_tagging_element', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 121
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            About this ')
        # SOURCE LINE 124
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u'\n        </div>\n    </div>\n    \n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">\n            <div style="padding: 10px;">\n                <h4>Author</h4>\n                \n                <p>')
        # SOURCE LINE 133
        __M_writer(filters.html_escape(unicode(item.history.user.username )))
        __M_writer(u'</p>\n                \n                <div><img src="https://secure.gravatar.com/avatar/')
        # SOURCE LINE 135
        __M_writer(unicode(h.md5(item.history.user.email)))
        __M_writer(u'?d=identicon&s=150"></div>\n\n')
        # SOURCE LINE 138
        __M_writer(u'                \n')
        # SOURCE LINE 140
        __M_writer(u'        \n')
        # SOURCE LINE 142
        __M_writer(u'                <p>\n                <h4>Tags</h4>\n                <p>\n')
        # SOURCE LINE 146
        __M_writer(u'                <div>\n                    Community:\n                    ')
        # SOURCE LINE 148
        __M_writer(unicode(render_community_tagging_element( tagged_item=item, tag_click_fn='community_tag_click', use_toggle_link=False )))
        __M_writer(u'\n')
        # SOURCE LINE 149
        if len ( item.tags ) == 0:
            # SOURCE LINE 150
            __M_writer(u'                        none\n')
            pass
        # SOURCE LINE 152
        __M_writer(u'                </div>\n')
        # SOURCE LINE 154
        __M_writer(u'                <p>\n                <div>\n                    Yours:\n                    ')
        # SOURCE LINE 157
        __M_writer(unicode(render_individual_tagging_element( user=trans.get_user(), tagged_item=item, elt_context='view.mako', use_toggle_link=False, tag_click_fn='community_tag_click' )))
        __M_writer(u'\n                </div>\n            </div>    \n        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,data,data_to_render):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        def render_deleted_data_message(data):
            return render_render_deleted_data_message(context,data)
        truncated = _import_ns.get('truncated', context.get('truncated', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n    ')
        # SOURCE LINE 70
        __M_writer(unicode( render_deleted_data_message( data ) ))
        __M_writer(u'\n')
        # SOURCE LINE 71
        if data_to_render:
            # SOURCE LINE 72
            if truncated:
                # SOURCE LINE 73
                __M_writer(u'            <div class="warningmessagelarge">\n                 This dataset is large and only the first megabyte is shown below. | \n                 <a href="')
                # SOURCE LINE 75
                __M_writer(unicode(h.url_for( controller='dataset', action='display_by_username_and_slug', username=data.history.user.username, slug=trans.security.encode_id( data.id ), preview=False )))
                __M_writer(u'">Show all</a>\n            </div>\n')
                pass
            # SOURCE LINE 79
            __M_writer(u'        <pre style="font-size: 135%">')
            __M_writer(filters.html_escape(unicode( data_to_render )))
            __M_writer(u'</pre>\n')
            # SOURCE LINE 80
        else:
            # SOURCE LINE 81
            __M_writer(u"        <p align='center'>Cannot show dataset content</p>\n")
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n')
        # SOURCE LINE 46

        self.has_left_panel=False
        self.has_right_panel=True
        self.message_box_visible=False
        self.active_view="user"
        self.overlay_visible=False
        
        
        # SOURCE LINE 52
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,data):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 59
        __M_writer(u'\n')
        # SOURCE LINE 61
        __M_writer(u'    <a href="')
        __M_writer(unicode(h.url_for( controller='/dataset', action='display', dataset_id=trans.security.encode_id( data.id ), to_ext=data.ext )))
        __M_writer(u'" class="icon-button disk" title="Save dataset"></a>\n        <a \n            href="')
        # SOURCE LINE 63
        __M_writer(unicode(h.url_for( controller='/dataset', action='imp', dataset_id=trans.security.encode_id( data.id ) )))
        __M_writer(u'"\n            class="icon-button import" \n            title="Import dataset"></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_deleted_data_message(context,data):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 85
        __M_writer(u'\n')
        # SOURCE LINE 86
        if data.deleted:
            # SOURCE LINE 87
            __M_writer(u'        <div class="errormessagelarge" id="deleted-data-message">\n            You are viewing a deleted dataset.\n')
            # SOURCE LINE 89
            if data.history and data.history.user == trans.get_user():
                # SOURCE LINE 90
                __M_writer(u'                <br />\n                <a href="#" onclick="$.ajax( {type: \'GET\', cache: false, url: \'')
                # SOURCE LINE 91
                __M_writer(unicode(h.url_for( controller='dataset', action='undelete_async', dataset_id=trans.security.encode_id( data.id ) )))
                __M_writer(u'\', dataType: \'text\', contentType: \'text/html\', success: function( data, textStatus, jqXHR ){ if (data == \'OK\' ){ $( \'#deleted-data-message\' ).slideUp( \'slow\' ) } else { alert( \'Undelete failed.\' ) } }, error: function( data, textStatus, jqXHR ){ alert( \'Undelete failed.\' ); } } );">Undelete</a>\n')
                pass
            # SOURCE LINE 93
            __M_writer(u'        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x25ae6c50')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x25ae6e50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        first_chunk = _import_ns.get('first_chunk', context.get('first_chunk', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        # SOURCE LINE 9
        if item.datatype.CHUNKABLE:
            # SOURCE LINE 10
            __M_writer(u'\n    <script type="text/javascript">\n        require.config({ \n            baseUrl: "')
            # SOURCE LINE 13
            __M_writer(unicode(h.url_for('/static/scripts')))
            __M_writer(u'",\n            shim: {\n                "libs/backbone/backbone": { exports: "Backbone" },\n                "libs/backbone/backbone-relational": ["libs/backbone/backbone"]\n            }\n        });\n\n        require([\'mvc/data\'], function(data) {\n            // \n            // Use tabular data display progressively by deleting data from page body\n            // and then showing dataset view.\n            // \n            $(\'.page-body\').children().remove();\n\n            data.createTabularDatasetChunkedView(\n                // Dataset config. TODO: encode id.\n                _.extend( ')
            # SOURCE LINE 29
            __M_writer(unicode(h.to_json_string( item.to_dict() )))
            __M_writer(u', \n                        {\n                            chunk_url: "')
            # SOURCE LINE 31
            __M_writer(unicode(h.url_for( controller='/dataset', action='display', 
                                             dataset_id=trans.security.encode_id( item.id ))))
            # SOURCE LINE 32
            __M_writer(u'",\n                            first_data_chunk: ')
            # SOURCE LINE 33
            __M_writer(unicode(first_chunk))
            __M_writer(u"\n                        } \n                ),\n                // Append view to body.\n                $('.page-body')\n            );\n        });\n    </script>\n\n")
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


