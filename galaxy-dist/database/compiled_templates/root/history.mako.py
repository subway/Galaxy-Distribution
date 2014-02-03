# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383768052.554499
_template_filename='templates/webapps/galaxy/root/history.mako'
_template_uri='root/history.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['title', 'get_hda_url_templates', 'stylesheets', 'get_current_user', 'get_history_url_templates', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 7
    ns = runtime.TemplateNamespace('__anon_0xc741850', context._clean_inheritance_tokens(), templateuri=u'/utils/localization.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0xc741850')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xc741850')._populate(_import_ns, [u'localize_js_strings'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 95
        __M_writer(u'\n\n\n')
        # SOURCE LINE 105
        __M_writer(u'\n\n\n')
        # SOURCE LINE 296
        __M_writer(u'\n\n')
        # SOURCE LINE 382
        __M_writer(u'\n\n<body class="historyPage"></body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xc741850')._populate(_import_ns, [u'localize_js_strings'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(_('Galaxy History')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_hda_url_templates(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xc741850')._populate(_import_ns, [u'localize_js_strings'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\n')
        # SOURCE LINE 34

        from urllib import unquote_plus
        
        hda_class_name      = 'HistoryDatasetAssociation'
        encoded_id_template = '<%= id %>'
        
        hda_ext_template    = '<%= file_ext %>'
        meta_type_template  = '<%= file_type %>'
        
        url_dict = {
            # ................................................................ warning message links
            'purge' : h.url_for( controller='dataset', action='purge_async',
                dataset_id=encoded_id_template ),
            #TODO: hide (via api)
            'unhide' : h.url_for( controller='dataset', action='unhide',
                dataset_id=encoded_id_template ),
            #TODO: via api
            'undelete' : h.url_for( controller='dataset', action='undelete',
                dataset_id=encoded_id_template ),
        
            # ................................................................ title actions (display, edit, delete),
            'display' : h.url_for( controller='dataset', action='display',
                dataset_id=encoded_id_template, preview=True, filename='' ),
            'edit' : h.url_for( controller='dataset', action='edit',
                dataset_id=encoded_id_template ),
        
            #TODO: via api
            'delete' : h.url_for( controller='dataset', action='delete_async',
                dataset_id=encoded_id_template ),
        
            # ................................................................ download links (and associated meta files),
            'download' : h.url_for( controller='dataset', action='display',
                dataset_id=encoded_id_template, to_ext=hda_ext_template ),
            'meta_download' : h.url_for( controller='dataset', action='get_metadata_file',
                hda_id=encoded_id_template, metadata_name=meta_type_template ),
        
            # ................................................................ primary actions (errors, params, rerun),
            'report_error' : h.url_for( controller='dataset', action='errors',
                id=encoded_id_template ),
            'show_params' : h.url_for( controller='dataset', action='show_params',
                dataset_id=encoded_id_template ),
            'rerun' : h.url_for( controller='tool_runner', action='rerun',
                id=encoded_id_template ),
            'visualization' : h.url_for( controller='visualization', action='index' ),
        
            # ................................................................ secondary actions (tagging, annotation),
            'tags' : {
                'get' : h.url_for( controller='tag', action='get_tagging_elt_async',
                    item_class=hda_class_name, item_id=encoded_id_template ),
                'set' : h.url_for( controller='tag', action='retag',
                    item_class=hda_class_name, item_id=encoded_id_template ),
            },
            'annotation' : {
                'get' : h.url_for( controller='dataset', action='get_annotation_async',
                    id=encoded_id_template ),
                'set' : h.url_for( controller='/dataset', action='annotate_async',
                    id=encoded_id_template ),
            },
        }
        
        
        # SOURCE LINE 93
        __M_writer(u'\n')
        # SOURCE LINE 94
        __M_writer(unicode( unquote_plus( h.to_json_string( url_dict ) ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xc741850')._populate(_import_ns, [u'localize_js_strings'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 298
        __M_writer(u'\n    ')
        # SOURCE LINE 299
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 300
        __M_writer(unicode(h.css(
        "base",
        "history",
        "autocomplete_tagging"
    )))
        # SOURCE LINE 304
        __M_writer(u'\n    <style>\n')
        # SOURCE LINE 307
        __M_writer(u'        /*---- page level */\n        .warningmessagesmall {\n            margin: 8px 0 0 0;\n        }\n        #message-container div {\n        }\n        #message-container [class$="message"] {\n            margin: 8px 0 0 0;\n            cursor: pointer;\n        }\n\n        /*---- history level */\n        #history-controls {\n            margin-bottom: 5px;\n            padding: 5px;\n        }\n\n        #history-title-area {\n            margin: 0px 0px 5px 0px;\n        }\n        #history-name {\n            word-wrap: break-word;\n            font-weight: bold;\n            /*color: gray;*/\n        }\n        .editable-text {\n            border: solid transparent 1px;\n        }\n        #history-name-container input {\n            width: 90%;\n            margin: -2px 0px -3px -4px;\n            font-weight: bold;\n        }\n\n        #quota-message-container {\n            margin: 8px 0px 5px 0px;\n        }\n        #quota-message {\n            margin: 0px;\n        }\n\n        #history-secondary-links #history-refresh {\n            text-decoration: none;\n        }\n        /*too tweaky*/\n        #history-annotate {\n            margin-right: 3px;\n        }\n\n        #history-tag-area, #history-annotation-area {\n            margin: 10px 0px 10px 0px;\n        }\n\n        /*---- HDA level */\n        .historyItem div.errormessagesmall {\n            font-size: small;\n            margin: 0px 0px 4px 0px;\n        }\n        .historyItem div.warningmessagesmall {\n            font-size: small;\n            margin: 0px 0px 4px 0px;\n        }\n        .historyItemBody {\n            display: none;\n        }\n\n        .historyItemTitle {\n            text-decoration: underline;\n            cursor: pointer;\n        }\n        .historyItemTitle:hover {\n            text-decoration: underline;\n        }\n\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_current_user(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xc741850')._populate(_import_ns, [u'localize_js_strings'])
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n')
        # SOURCE LINE 100

    #TODO: move to root.history, using base.controller.usesUser, unify that with users api
        user_json = trans.webapp.api_controllers[ 'users' ].show( trans, 'current' )
        return user_json
        
        
        # SOURCE LINE 104
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_history_url_templates(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xc741850')._populate(_import_ns, [u'localize_js_strings'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12

        from urllib import unquote_plus
        
        history_class_name      = 'History'
        encoded_id_template     = '<%= id %>'
        
        url_dict = {
            'rename'        : h.url_for( controller="history", action="rename_async",
                                id=encoded_id_template ),
            'tag'           : h.url_for( controller='tag', action='get_tagging_elt_async',
                                item_class=history_class_name, item_id=encoded_id_template ),
            'annotate'      : h.url_for( controller="history", action="annotate_async",
                                id=encoded_id_template )
        }
        
        
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 27
        __M_writer(unicode( unquote_plus( h.to_json_string( url_dict ) ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xc741850')._populate(_import_ns, [u'localize_js_strings'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        show_deleted = _import_ns.get('show_deleted', context.get('show_deleted', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        def get_hda_url_templates():
            return render_get_hda_url_templates(context)
        history_json = _import_ns.get('history_json', context.get('history_json', UNDEFINED))
        show_hidden = _import_ns.get('show_hidden', context.get('show_hidden', UNDEFINED))
        def get_current_user():
            return render_get_current_user(context)
        hda_id = _import_ns.get('hda_id', context.get('hda_id', UNDEFINED))
        def get_history_url_templates():
            return render_get_history_url_templates(context)
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        localize_js_strings = _import_ns.get('localize_js_strings', context.get('localize_js_strings', UNDEFINED))
        hda_json = _import_ns.get('hda_json', context.get('hda_json', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 109
        __M_writer(u'\n')
        # SOURCE LINE 110
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n')
        # SOURCE LINE 112
        __M_writer(unicode(h.js(
    "libs/jquery/jstorage",
    "libs/jquery/jquery.autocomplete", "galaxy.autocom_tagging",
    "mvc/base-mvc",
    "utils/localization"
)))
        # SOURCE LINE 117
        __M_writer(u'\n\n')
        # SOURCE LINE 119
        __M_writer(unicode(h.templates(
    "helpers-common-templates",
    "template-warningmessagesmall",
    
    "template-history-historyPanel",

    "template-hda-warning-messages",
    "template-hda-titleLink",
    "template-hda-failedMetadata",
    "template-hda-hdaSummary",
    "template-hda-downloadLinks",
    "template-hda-tagArea",
    "template-hda-annotationArea",
    "template-hda-displayApps",
)))
        # SOURCE LINE 133
        __M_writer(u'\n\n')
        # SOURCE LINE 136
        __M_writer(unicode(h.js(
    "mvc/user/user-model", "mvc/user/user-quotameter",
    "mvc/dataset/hda-model", "mvc/dataset/hda-base", "mvc/dataset/hda-edit",
    "mvc/history/history-model", "mvc/history/history-panel"
)))
        # SOURCE LINE 140
        __M_writer(u'\n\n')
        # SOURCE LINE 142
        __M_writer(unicode(localize_js_strings([
    # not needed?: "Galaxy History",
    'refresh',
    'collapse all',
    'hide deleted',
    'hide hidden',
    'You are currently viewing a deleted history!',
    "Your history is empty. Click 'Get Data' on the left pane to start",

    # from history_common.mako
    'Download',
    'Display Data',
    'View data',
    'Edit attributes',
    'Delete',
    'Job is waiting to run',
    'View Details',
    'Job is currently running',
    #'Run this job again',
    'Metadata is being Auto-Detected.',
    'No data: ',
    'format: ',
    'database: ',
    #TODO localized data.dbkey??
    'Info: ',
    #TODO localized display_app.display_name??
    # _( link_app.name )
    # localized peek...ugh
    'Error: unknown dataset state',
])))
        # SOURCE LINE 171
        __M_writer(u'\n    \n<script type="text/javascript">\nfunction galaxyPageSetUp(){\n    //TODO: move to base.mako\n    // moving global functions, objects into Galaxy namespace\n    top.Galaxy                  = top.Galaxy || {};\n    \n    if( top != window ){\n        top.Galaxy.mainWindow       = top.Galaxy.mainWindow     || top.frames.galaxy_main;\n        top.Galaxy.toolWindow       = top.Galaxy.toolWindow     || top.frames.galaxy_tools;\n        top.Galaxy.historyWindow    = top.Galaxy.historyWindow  || top.frames.galaxy_history;\n    }\n\n    window.Galaxy = top.Galaxy;\n}\n\n// add needed controller urls to galaxy_config\ngalaxy_config[\'hda\'] = ')
        # SOURCE LINE 189
        __M_writer(unicode(get_hda_url_templates()))
        __M_writer(u";\ngalaxy_config['history'] = ")
        # SOURCE LINE 190
        __M_writer(unicode(get_history_url_templates()))
        __M_writer(u";\n\n$(function(){\n    galaxyPageSetUp();\n    // ostensibly, this is the App\n\n    //NOTE: for debugging on non-local instances (main/test)\n    //  1. load history panel in own tab\n    //  2. from console: new PersistentStorage( '__history_panel' ).set( 'debugging', true )\n    //  -> history panel and hdas will display console logs in console\n    var debugging = false;\n    if( sessionStorage.getItem( '__history_panel' ) ){\n        debugging = new PersistentStorage( '__history_panel' ).get( 'debugging' );\n        if( debugging ){\n            console.debug( '(debugging)' );\n        }\n    }\n\n    // get the current user (either from the top frame's Galaxy or if in tab via the bootstrap)\n    Galaxy.currUser = Galaxy.currUser || new User(")
        # SOURCE LINE 209
        __M_writer(unicode( get_current_user() ))
        __M_writer(u');\n    if( debugging ){ Galaxy.currUser.logger = console; }\n\n    var page_show_deleted = ')
        # SOURCE LINE 212
        __M_writer(unicode( 'true' if show_deleted == True else ( 'null' if show_deleted == None else 'false' ) ))
        __M_writer(u',\n        page_show_hidden  = ')
        # SOURCE LINE 213
        __M_writer(unicode( 'true' if show_hidden  == True else ( 'null' if show_hidden  == None else 'false' ) ))
        __M_writer(u",\n\n    //  ...use mako to 'bootstrap' the models\n        historyJson = ")
        # SOURCE LINE 216
        __M_writer(unicode( history_json ))
        __M_writer(u',\n        hdaJson     = ')
        # SOURCE LINE 217
        __M_writer(unicode( hda_json ))
        __M_writer(u";\n\n    //TODO: add these two in root.history\n    // add user data to history\n    // i don't like this history+user relationship, but user authentication changes views/behaviour\n    historyJson.user = Galaxy.currUser.toJSON();\n\n    // set up messages passed in\n")
        # SOURCE LINE 225
        if message:
            # SOURCE LINE 226
            __M_writer(u'    historyJson.message = "')
            __M_writer(unicode(_( message )))
            __M_writer(u'"; historyJson.status = "')
            __M_writer(unicode(status))
            __M_writer(u'";\n')
            pass
        # SOURCE LINE 228
        __M_writer(u"\n    // create the history panel\n    var history = new History( historyJson, hdaJson, ( debugging )?( console ):( null ) );\n    var historyPanel = new HistoryPanel({\n            model           : history,\n            urlTemplates    : galaxy_config,\n            logger          : ( debugging )?( console ):( null ),\n            // is page sending in show settings? if so override history's\n            show_deleted    : page_show_deleted,\n            show_hidden     : page_show_hidden\n        });\n    historyPanel.render();\n\n    // set up messages passed in\n")
        # SOURCE LINE 242
        if hda_id:
            # SOURCE LINE 243
            __M_writer(u'    var hdaId = "')
            __M_writer(unicode(hda_id))
            __M_writer(u'";\n    // have to fake \'once\' here - simplify when bbone >= 1.0\n    historyPanel.on( \'rendered:initial\', function scrollOnce(){\n        this.off( \'rendered:initial\', scrollOnce, this );\n        this.scrollToId( hdaId );\n    }, historyPanel );\n')
            pass
        # SOURCE LINE 250
        __M_writer(u'\n    // QUOTA METER is a cross-frame ui element (meter in masthead, watches hist. size built here)\n    //TODO: the quota message (curr. in the history panel) belongs somewhere else\n    //TODO: does not display if in own tab\n    if( Galaxy.quotaMeter ){\n        // unbind prev. so we don\'t build up massive no.s of event handlers as history refreshes\n        if( top.Galaxy.currHistoryPanel ){\n            Galaxy.quotaMeter.unbind( \'quota:over\',  top.Galaxy.currHistoryPanel.showQuotaMessage );\n            Galaxy.quotaMeter.unbind( \'quota:under\', top.Galaxy.currHistoryPanel.hideQuotaMessage );\n        }\n\n        // show/hide the \'over quota message\' in the history when the meter tells it to\n        Galaxy.quotaMeter.bind( \'quota:over\',  historyPanel.showQuotaMessage, historyPanel );\n        Galaxy.quotaMeter.bind( \'quota:under\', historyPanel.hideQuotaMessage, historyPanel );\n\n        // update the quota meter when current history changes size\n        //TODO: can we consolidate the two following?\n        historyPanel.model.bind( \'rendered:initial change:nice_size\', function(){\n            if( Galaxy.quotaMeter ){ Galaxy.quotaMeter.update() }\n        });\n\n        // having to add this to handle re-render of hview while overquota (the above do not fire)\n        historyPanel.on( \'rendered rendered:initial\', function(){\n            if( Galaxy.quotaMeter && Galaxy.quotaMeter.isOverQuota() ){\n                historyPanel.showQuotaMessage();\n            }\n        });\n    }\n    // set it up to be accessible across iframes\n    top.Galaxy.currHistoryPanel = historyPanel;\n\n    //ANOTHER cross-frame element is the history-options-button...\n    //TODO: the options-menu stuff need to be moved out when iframes are removed\n    //TODO: move to pub-sub\n    //TODO: same strings ("Include...") here as in index.mako - brittle\n    if( ( top.document !== window.document ) &&  ( Galaxy.historyOptionsMenu ) ){\n        Galaxy.historyOptionsMenu.findItemByHtml( "')
        # SOURCE LINE 286
        __M_writer(unicode("Include Deleted Datasets"))
        __M_writer(u'" ).checked =\n            Galaxy.currHistoryPanel.storage.get( \'show_deleted\' );\n        Galaxy.historyOptionsMenu.findItemByHtml( "')
        # SOURCE LINE 288
        __M_writer(unicode("Include Hidden Datasets"))
        __M_writer(u'" ).checked =\n            Galaxy.currHistoryPanel.storage.get( \'show_hidden\' );\n    }\n\n    return;\n});\n</script>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


