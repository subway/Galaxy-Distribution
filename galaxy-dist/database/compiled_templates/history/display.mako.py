# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1386156828.786798
_template_filename='templates/webapps/galaxy/history/display.mako'
_template_uri='history/display.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'render_item', 'javascripts', 'render_item_links']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x1f1d5f10', context._clean_inheritance_tokens(), templateuri=u'/root/history_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1f1d5f10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/display_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1f1d5f10')._populate(_import_ns, [u'render_dataset'])
        published_item_data = _import_ns.get('published_item_data', context.get('published_item_data', UNDEFINED))
        published_item = _import_ns.get('published_item', context.get('published_item', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 5
 
        history = published_item 
        datasets = published_item_data
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datasets','history'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 47
        __M_writer(u'\n\n')
        # SOURCE LINE 84
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1f1d5f10')._populate(_import_ns, [u'render_dataset'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 16
        __M_writer(unicode(h.css( "history" )))
        __M_writer(u'\n    <style type="text/css">\n        .historyItemBody {\n            display: none;\n        }\n        .column {\n            float: left;\n            padding: 10px;\n            margin: 20px;\n            background: #666;\n            border: 5px solid #ccc;\n            width: 300px;\n        }\n    </style>\n\n    <noscript>\n        <style>\n            .historyItemBody {\n                display: block;\n            }\n        </style>\n    </noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,history,datasets):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1f1d5f10')._populate(_import_ns, [u'render_dataset'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        show_deleted = _import_ns.get('show_deleted', context.get('show_deleted', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        render_dataset = _import_ns.get('render_dataset', context.get('render_dataset', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\n')
        # SOURCE LINE 50
        if history.deleted:
            # SOURCE LINE 51
            __M_writer(u'        <div class="warningmessagesmall">\n            ')
            # SOURCE LINE 52
            __M_writer(unicode(_('You are currently viewing a deleted history!')))
            __M_writer(u'\n        </div>\n        <p></p>\n')
            pass
        # SOURCE LINE 56
        __M_writer(u'\n')
        # SOURCE LINE 57
        if not datasets:
            # SOURCE LINE 58
            __M_writer(u'        <div class="infomessagesmall" id="emptyHistoryMessage">\n')
            # SOURCE LINE 59
        else:    
            # SOURCE LINE 61
            __M_writer(u'        <table class="annotated-item">\n            <tr><th>Dataset</th><th class="annotation">Annotation</th></tr>\n')
            # SOURCE LINE 63
            for data in datasets:
                # SOURCE LINE 64
                __M_writer(u'                <tr>\n')
                # SOURCE LINE 65
                if data.visible:
                    # SOURCE LINE 66
                    __M_writer(u'                        <td>\n                            <div class="historyItemContainer visible-right-border" id="historyItemContainer-')
                    # SOURCE LINE 67
                    __M_writer(unicode(data.id))
                    __M_writer(u'">\n                                ')
                    # SOURCE LINE 68
                    __M_writer(unicode(render_dataset( data, data.hid, show_deleted_on_refresh = show_deleted, for_editing=False )))
                    __M_writer(u'\n                            </div>\n                        </td>\n                        <td class="annotation">\n')
                    # SOURCE LINE 72
                    if hasattr( data, "annotation") and data.annotation is not None:
                        # SOURCE LINE 73
                        __M_writer(u'                            ')
                        __M_writer(unicode(data.annotation))
                        __M_writer(u'\n')
                        pass
                    # SOURCE LINE 75
                    __M_writer(u'                        </td>\n')
                    pass
                # SOURCE LINE 77
                __M_writer(u'                </tr>\n')
                pass
            # SOURCE LINE 79
            __M_writer(u'        </table>\n        <div class="infomessagesmall" id="emptyHistoryMessage" style="display:none;">\n')
            pass
        # SOURCE LINE 82
        __M_writer(u'            ')
        __M_writer(unicode(_("This history is empty.")))
        __M_writer(u'\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1f1d5f10')._populate(_import_ns, [u'render_dataset'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,history):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1f1d5f10')._populate(_import_ns, [u'render_dataset'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n    <a \n        href="')
        # SOURCE LINE 42
        __M_writer(unicode(h.url_for( controller='/history', action='imp', id=trans.security.encode_id(history.id) )))
        __M_writer(u'"\n        class="icon-button import"\n')
        # SOURCE LINE 45
        __M_writer(u'        style="width: 100%"\n        title="Import history">Import history</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


