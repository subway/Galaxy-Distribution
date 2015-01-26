# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399385554.123758
_template_filename='templates/webapps/galaxy/page/editor.mako'
_template_uri='page/editor.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'init', 'javascripts', 'center_panel']


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
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n\n')
        # SOURCE LINE 59
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n    ')
        # SOURCE LINE 31
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 32
        __M_writer(unicode(h.css( "base", "autocomplete_tagging", "embed_item" )))
        __M_writer(u"\n    <style type='text/css'>\n        .galaxy-page-editor-button\n        {\n            position: relative;\n            float: left; \n            padding: 0.2em;\n        } \n    </style>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="user"
        self.overlay_visible=False
        
        
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        page = context.get('page', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        // Define variables needed by galaxy.pages script.\n        var page_id = "')
        # SOURCE LINE 16
        __M_writer(unicode(trans.security.encode_id(page.id)))
        __M_writer(u'",\n            page_list_url = \'')
        # SOURCE LINE 17
        __M_writer(unicode(h.url_for( controller='page', action='list' )))
        __M_writer(u'\',\n            list_objects_url = "')
        # SOURCE LINE 18
        __M_writer(unicode(h.url_for(controller='page', action='LIST_ACTION' )))
        __M_writer(u'",\n            set_accessible_url = "')
        # SOURCE LINE 19
        __M_writer(unicode(h.url_for( controller='ITEM_CONTROLLER', action='set_accessible_async' )))
        __M_writer(u'",\n            get_name_and_link_url = "')
        # SOURCE LINE 20
        __M_writer(unicode(h.url_for( controller='ITEM_CONTROLLER', action='get_name_and_link_async' )))
        __M_writer(u'?id=",\n            list_histories_for_selection_url = "')
        # SOURCE LINE 21
        __M_writer(unicode(h.url_for(controller='page', action='list_histories_for_selection' )))
        __M_writer(u'",\n            get_history_annotation_table_url = "')
        # SOURCE LINE 22
        __M_writer(unicode(h.url_for(controller='page', action='get_history_annotation_table' )))
        __M_writer(u'",\n            editor_base_path = "')
        # SOURCE LINE 23
        __M_writer(unicode(h.url_for('/static/wymeditor')))
        __M_writer(u'/",\n            iframe_base_path = "')
        # SOURCE LINE 24
        __M_writer(unicode(h.url_for('/static/wymeditor/iframe/galaxy')))
        __M_writer(u'/",\n            save_url = "')
        # SOURCE LINE 25
        __M_writer(unicode(h.url_for(controller='page', action='save' )))
        __M_writer(u'";\n    </script>\n    ')
        # SOURCE LINE 27
        __M_writer(unicode(h.js( "libs/jquery/jquery.form", "libs/jquery/jstorage", "libs/jquery/jquery.wymeditor", "libs/jquery/jquery.autocomplete", "galaxy.autocom_tagging", "galaxy.pages")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        util = context.get('util', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 43
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner" style="float: right">\n            <a id="save-button" class="panel-header-button">Save</a>\n            <a id="close-button" class="panel-header-button">Close</a>\n        </div>\n        <div class="unified-panel-header-inner">\n            Page Editor <span style="font-weight: normal">| Title : ')
        # SOURCE LINE 51
        __M_writer(unicode(page.title))
        __M_writer(u'</span>\n        </div>\n    </div>\n\n    <div class="unified-panel-body">\n        <textarea name="page_content">')
        # SOURCE LINE 56
        __M_writer(unicode(util.unicodify( page.latest_revision.content )))
        __M_writer(u'</textarea>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


