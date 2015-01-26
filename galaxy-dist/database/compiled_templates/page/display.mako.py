# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399385602.241672
_template_filename='templates/webapps/galaxy/page/display.mako'
_template_uri='page/display.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'render_item', 'javascripts', 'render_item_header', 'render_item_links']


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
    return runtime._inherit_from(context, u'/display_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 87
        __M_writer(u'\n\n')
        # SOURCE LINE 123
        __M_writer(u'\n\n')
        # SOURCE LINE 127
        __M_writer(u'\n\n')
        # SOURCE LINE 130
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 89
        __M_writer(u'\n    ')
        # SOURCE LINE 90
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 91
        __M_writer(unicode(h.css( "base", "history", "autocomplete_tagging" )))
        __M_writer(u'\n    <style type="text/css">\n        .toggle { display: none; }\n        .embedded-item h4 {\n            margin: 0px;\n        }\n')
        # SOURCE LINE 98
        __M_writer(u'        .page-body > table {\n            padding: 8px 5px 5px;\n            min-width: 500px; \n            border: none;\n            margin-top: 1em;\n            margin-bottom: 1em;\n        }\n        .page-body caption { \n            text-align: left;\n            background: #E4E4B0; \n            padding: 5px; \n            font-weight: bold; \n        }\n        .page-body > table td {\n            width: 25%;\n            padding: 0.2em 0.8em;\n        }\n')
        # SOURCE LINE 116
        __M_writer(u'        .embedded-item .trackster-nav-container {\n            height: inherit;\n        }\n        .embedded-item .trackster-nav {\n            position: inherit;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,page,page_data=None):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 132
        __M_writer(u'\n    ')
        # SOURCE LINE 133
        __M_writer(unicode(page_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n    \n        $(function() {\n\n            // Setup embedded content:\n            //  (a) toggles for showing/hiding embedded content;\n            //  (b) ...\n            $(\'.embedded-item\').each( function() {\n                var container = $(this);\n            \n                // Show embedded item.\n                var show_embedded_item = function() {\n                    var ajax_url = container.find("input[type=hidden]").val();\n                    // Only get item content if it\'s not already there.\n                    var item_content = $.trim(container.find(".item-content").text());\n                    if (!item_content) {\n                        $.ajax({\n                            type: "GET",\n                            url: ajax_url,\n                            error: function() { alert("Getting item content failed."); },\n                            success: function( item_content ) {\n                                container.find(".summary-content").hide("fast");\n                                container.find(".item-content").html(item_content);\n                                container.find(".expanded-content").show("fast");\n                                container.find(".toggle-expand").hide();\n                                container.find(".toggle").show();\n\n                                // Init needed for history items.\n                                init_history_items( container.find("div.historyItemWrapper"), "noinit", "nochanges" ); \n                                container.find( "div.historyItemBody:visible" ).each( function() {\n                                    if ( $.browser.mozilla ) {\n                                        $(this).find( "pre.peek" ).css( "overflow", "hidden" );\n                                    }\n                                    $(this).hide();\n                                });\n                                make_popup_menus();\n                            }\n                        });\n                    } else {\n                        container.find(".summary-content").hide("fast");\n                        container.find(".expanded-content").show("fast");\n                        container.find(".toggle-expand").hide();\n                        container.find(".toggle").show();\n                    }\n                };\n            \n                // Hide embedded item.\n                var hide_embedded_item = function() {\n                    container.find(".expanded-content").hide("fast");\n                    container.find(".summary-content").show("fast");\n                    container.find(".toggle").hide();\n                    container.find(".toggle-expand").show();\n                };\n            \n                // Setup toggle expand.\n                var toggle_expand = $(this).find(\'.toggle-expand\');\n                toggle_expand.click( function() {\n                    show_embedded_item();\n                    return false;\n                });\n            \n                // Setup toggle contract.\n                var toggle_contract = $(this).find(\'.toggle\');\n                toggle_contract.click( function() {\n                    hide_embedded_item();\n                    return false;\n                });\n            \n                // Setup toggle embed.\n                var toggle_embed = $(this).find(\'.toggle-embed\');\n                toggle_embed.click( function() {\n                    if (container.find(".expanded-content").is(":visible")) {\n                        hide_embedded_item();\n                    } else {\n                        show_embedded_item();\n                    }\n                    return false;\n                });\n            });\n        });\n    \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_header(context,item):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 125
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,page):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 129
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


