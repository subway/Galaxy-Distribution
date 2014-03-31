# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1394451996.9412
_template_filename='templates/webapps/galaxy/history/display_structured.mako'
_template_uri='history/display_structured.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_item_job', 'render_item_wf', 'render_item_hda', 'stylesheets', 'render_item', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x11563810', context._clean_inheritance_tokens(), templateuri=u'/root/history_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x11563810')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x11563810')._populate(_import_ns, [u'render_dataset'])
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        def render_item(entity,children):
            return render_render_item(context.locals_(__M_locals),entity,children)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 91
        __M_writer(u'\n\n')
        # SOURCE LINE 95
        __M_writer(u'\n\n')
        # SOURCE LINE 115
        __M_writer(u'\n\n')
        # SOURCE LINE 128
        __M_writer(u'\n\n')
        # SOURCE LINE 130
        for entity, children in items:
            # SOURCE LINE 131
            __M_writer(u'    ')
            __M_writer(unicode(render_item( entity, children )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_job(context,job,children):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x11563810')._populate(_import_ns, [u'render_dataset'])
        def render_item(entity,children):
            return render_render_item(context,entity,children)
        reversed = _import_ns.get('reversed', context.get('reversed', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 97
        __M_writer(u'\n\n    <div class="tool toolForm">\n        ')
        # SOURCE LINE 100

        tool = trans.app.toolbox.get_tool( job.tool_id )
        if tool:
            tool_name = tool.name
        else:
            tool_name = "Unknown tool with id '%s'" % job.tool_id       
                
        
        # SOURCE LINE 106
        __M_writer(u'\n        <div class="header toolFormTitle">Tool: ')
        # SOURCE LINE 107
        __M_writer(unicode(tool_name))
        __M_writer(u'</div>\n        <div class="body toolFormBody">\n')
        # SOURCE LINE 109
        for e, c in reversed( children ):
            # SOURCE LINE 110
            __M_writer(u'            ')
            __M_writer(unicode(render_item( e, c )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 112
        __M_writer(u'        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_wf(context,wf,children):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x11563810')._populate(_import_ns, [u'render_dataset'])
        def render_item(entity,children):
            return render_render_item(context,entity,children)
        reversed = _import_ns.get('reversed', context.get('reversed', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 117
        __M_writer(u'\n\n    <div class="workflow">\n        <div class="header">Workflow: ')
        # SOURCE LINE 120
        __M_writer(unicode(wf.workflow.name))
        __M_writer(u'</div>\n        <div class="body">\n')
        # SOURCE LINE 122
        for e, c in reversed( children ):
            # SOURCE LINE 123
            __M_writer(u'            ')
            __M_writer(unicode(render_item( e, c )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 125
        __M_writer(u'        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_hda(context,hda,children):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x11563810')._populate(_import_ns, [u'render_dataset'])
        render_dataset = _import_ns.get('render_dataset', context.get('render_dataset', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 93
        __M_writer(u'\n    ')
        # SOURCE LINE 94
        __M_writer(unicode(render_dataset( hda, hda.hid, display_structured=True )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x11563810')._populate(_import_ns, [u'render_dataset'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(unicode(h.css( "history" )))
        __M_writer(u'\n    <style type="text/css">\n        body {\n            background: white;\n            padding: 5px;\n        }\n        \n        .clickable {\n            cursor: pointer;\n        }\n        \n        .workflow {\n            border: solid gray 1px;\n            margin: 5px 0;\n            border-left-width: 5px;\n        }\n        \n        .workflow > .header {\n            background: lightgray;\n            padding: 5px 10px;\n            \n            font-weight: bold;\n        }\n        \n        .workflow > .body {\n            border-top: solid gray 1px;\n            padding: 5px;\n        }\n        \n        div.toolForm {\n            margin: 5px 0;\n            border-left-width: 5px;\n        }\n        div.toolFormBody {\n            padding: 5px 5px;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,entity,children):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x11563810')._populate(_import_ns, [u'render_dataset'])
        def render_item_hda(hda,children):
            return render_render_item_hda(context,hda,children)
        def render_item_wf(wf,children):
            return render_render_item_wf(context,wf,children)
        def render_item_job(job,children):
            return render_render_item_job(context,job,children)
        __M_writer = context.writer()
        # SOURCE LINE 81
        __M_writer(u'\n')
        # SOURCE LINE 82

        entity_name = entity.__class__.__name__
        if entity_name == "HistoryDatasetAssociation":
            render_item_hda( entity, children )
        elif entity_name == "Job":
            render_item_job( entity, children )
        elif entity_name == "WorkflowInvocation":
            render_item_wf( entity, children )
        
        
        # SOURCE LINE 90
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x11563810')._populate(_import_ns, [u'render_dataset'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n    ')
        # SOURCE LINE 46
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        $(function(){\n            \n            $(".workflow, .tool").each( function() {\n                var body = $(this).children( ".body" );\n                $(this).children( ".header" ).click( function() {\n                    body.toggle();\n                }).addClass( "clickable" );\n                // body.hide();\n            });\n            \n            $(".historyItem").each( function() {\n                var id = this.id;\n                var body = $(this).children( "div.historyItemBody" );\n                var peek = body.find( "pre.peek" )\n                $(this).children( ".historyItemTitleBar" ).find( ".historyItemTitle" ).wrap( "<a href=\'#\'></a>" ).click( function() {\n                    if ( body.is(":visible") ) {\n                        // Hiding stuff here\n                        if ( $.browser.mozilla ) { peek.css( "overflow", "hidden" ) }\n                        body.slideUp( "fast" );\n                    } else {\n                        // Showing stuff here\n                        body.slideDown( "fast", function() { \n                            if ( $.browser.mozilla ) { peek.css( "overflow", "auto" ); } \n                        });\n                    }\n                    return false;\n                });\n                body.hide();\n            });\n        });    \n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


