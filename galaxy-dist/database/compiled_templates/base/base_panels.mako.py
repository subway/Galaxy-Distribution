# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1383768039.709843
_template_filename=u'templates/base/base_panels.mako'
_template_uri=u'/base/base_panels.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['overlay', 'late_javascripts', 'stylesheets', 'init', 'masthead', 'javascripts']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        app = context.get('app', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML>\n\n')
        # SOURCE LINE 3

        self.has_left_panel = hasattr( self, 'left_panel' )
        self.has_right_panel = hasattr( self, 'right_panel' )
        self.message_box_visible = app.config.message_box_visible
        self.show_inactivity_warning = False
        if trans.webapp.name == 'galaxy' and trans.user:
            self.show_inactivity_warning = ( ( trans.user.active is False ) and ( app.config.user_activation_on ) and ( app.config.inactivity_box_content is not None ) )
        self.overlay_visible=False
        self.active_view=None
        self.body_class=""
        self.require_javascript=False
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 14
        __M_writer(u'\n    \n')
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 113
        __M_writer(u'\n\n')
        # SOURCE LINE 226
        __M_writer(u'\n\n')
        # SOURCE LINE 231
        __M_writer(u'\n\n')
        # SOURCE LINE 263
        __M_writer(u'\n\n')
        # SOURCE LINE 266
        __M_writer(u'<html>\n    <!--base_panels.mako-->\n    ')
        # SOURCE LINE 268
        __M_writer(unicode(self.init()))
        __M_writer(u'    \n    <head>\n')
        # SOURCE LINE 270
        if app.config.brand:
            # SOURCE LINE 271
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u' / ')
            __M_writer(unicode(app.config.brand))
            __M_writer(u'</title>\n')
            # SOURCE LINE 272
        else:
            # SOURCE LINE 273
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u'</title>\n')
            pass
        # SOURCE LINE 275
        __M_writer(u'        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        # SOURCE LINE 277
        __M_writer(u'        <meta name = "viewport" content = "maximum-scale=1.0">\n')
        # SOURCE LINE 279
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n        ')
        # SOURCE LINE 280
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        # SOURCE LINE 281
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n    </head>\n    \n    ')
        # SOURCE LINE 284

        body_class = self.body_class
        if self.message_box_visible:
            body_class += " has-message-box"
        if self.show_inactivity_warning:
            body_class += " has-inactivity-box"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['body_class'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 290
        __M_writer(u'\n\n    <body scroll="no" class="full-content ')
        # SOURCE LINE 292
        __M_writer(unicode(body_class))
        __M_writer(u'">\n')
        # SOURCE LINE 293
        if self.require_javascript:
            # SOURCE LINE 294
            __M_writer(u'            <noscript>\n                <div class="overlay overlay-background">\n                    <div class="modal dialog-box" border="0">\n                        <div class="modal-header"><h3 class="title">Javascript Required</h3></div>\n                        <div class="modal-body">The Galaxy analysis interface requires a browser with Javascript enabled. <br> Please enable Javascript and refresh this page</div>\n                    </div>\n                </div>\n            </noscript>\n')
            pass
        # SOURCE LINE 303
        __M_writer(u'        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">\n')
        # SOURCE LINE 305
        __M_writer(u'            <div id="background"></div>\n')
        # SOURCE LINE 307
        __M_writer(u'            <div id="masthead" class="navbar navbar-fixed-top navbar-inverse">\n                ')
        # SOURCE LINE 308
        __M_writer(unicode(self.masthead()))
        __M_writer(u'\n            </div>\n            <div id="messagebox" class="panel-')
        # SOURCE LINE 310
        __M_writer(unicode(app.config.message_box_class))
        __M_writer(u'-message">\n                ')
        # SOURCE LINE 311
        __M_writer(unicode(app.config.message_box_content))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 313
        if self.show_inactivity_warning:
            # SOURCE LINE 314
            __M_writer(u'                <div id="inactivebox" class="panel-warning-message">\n                    ')
            # SOURCE LINE 315
            __M_writer(unicode(app.config.inactivity_box_content))
            __M_writer(u' <a href="')
            __M_writer(unicode(h.url_for( controller='user', action='resend_verification' )))
            __M_writer(u'">Resend verification.</a>\n                </div>\n')
            pass
        # SOURCE LINE 318
        __M_writer(u'            ')
        __M_writer(unicode(self.overlay(visible=self.overlay_visible)))
        __M_writer(u'\n')
        # SOURCE LINE 319
        if self.has_left_panel:
            # SOURCE LINE 320
            __M_writer(u'                <div id="left">\n                    ')
            # SOURCE LINE 321
            __M_writer(unicode(self.left_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse"></span></div>\n                        <div class="drag"></div>\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 328
        __M_writer(u'            <div id="center">\n                ')
        # SOURCE LINE 329
        __M_writer(unicode(self.center_panel()))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 331
        if self.has_right_panel:
            # SOURCE LINE 332
            __M_writer(u'                <div id="right">\n                    ')
            # SOURCE LINE 333
            __M_writer(unicode(self.right_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse right"></span></div>\n                        <div class="drag"></div>\n                    </div>\n                </div>\n')
            pass
        # SOURCE LINE 340
        __M_writer(u'        </div>\n')
        # SOURCE LINE 342
        __M_writer(u'    </body>\n')
        # SOURCE LINE 345
        __M_writer(u'    ')
        __M_writer(unicode(self.late_javascripts()))
        __M_writer(u'\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,title='',content='',visible=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 233
        __M_writer(u'\n    ')
        # SOURCE LINE 234
        __M_writer(u'\n    ')
        # SOURCE LINE 235
        __M_writer(u'\n\n    ')
        # SOURCE LINE 237

        if visible:
            display = "style='display: block;'"
            overlay_class = "in"
        else:
            display = "style='display: none;'"
            overlay_class = ""
        
        
        # SOURCE LINE 244
        __M_writer(u'\n\n    <div id="top-modal" class="modal fade ')
        # SOURCE LINE 246
        __M_writer(unicode(overlay_class))
        __M_writer(u'" ')
        __M_writer(unicode(display))
        __M_writer(u'>\n        <div id="top-modal-backdrop" class="modal-backdrop fade ')
        # SOURCE LINE 247
        __M_writer(unicode(overlay_class))
        __M_writer(u'" style="z-index: -1"></div>\n        <div id="top-modal-dialog" class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <button type=\'button\' class=\'close\' style="display: none;">&times;</button>\n                    <h4 class=\'title\'>')
        # SOURCE LINE 252
        __M_writer(unicode(title))
        __M_writer(u'</h4>\n                </div>\n                <div class="modal-body">')
        # SOURCE LINE 254
        __M_writer(unicode(content))
        __M_writer(u'</div>\n                <div class="modal-footer">\n                    <div class="buttons" style="float: right;"></div>\n                    <div class="extra_buttons" style=""></div>\n                    <div style="clear: both;"></div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 116
        __M_writer(u'\n')
        # SOURCE LINE 119
        __M_writer(u'    ')
        __M_writer(unicode(h.js( 'libs/jquery/jquery.event.drag', 'libs/jquery/jquery.event.hover', 'libs/jquery/jquery.form', 'libs/jquery/jquery.rating', 'galaxy.panels' )))
        __M_writer(u'\n    <script type="text/javascript">\n        \n    ensure_dd_helper();\n        \n')
        # SOURCE LINE 124
        if self.has_left_panel:
            # SOURCE LINE 125
            __M_writer(u'            var lp = new Panel( { panel: $("#left"), center: $("#center"), drag: $("#left > .unified-panel-footer > .drag" ), toggle: $("#left > .unified-panel-footer > .panel-collapse" ) } );\n            force_left_panel = function( x ) { lp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 128
        __M_writer(u'        \n')
        # SOURCE LINE 129
        if self.has_right_panel:
            # SOURCE LINE 130
            __M_writer(u'            var rp = new Panel( { panel: $("#right"), center: $("#center"), drag: $("#right > .unified-panel-footer > .drag" ), toggle: $("#right > .unified-panel-footer > .panel-collapse" ), right: true } );\n            window.handle_minwidth_hint = function( x ) { rp.handle_minwidth_hint( x ) };\n            force_right_panel = function( x ) { rp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 134
        __M_writer(u'    \n    </script>\n')
        # SOURCE LINE 137
        __M_writer(u'    <![if !IE]>\n    <script type="text/javascript">\n        var upload_form_error = function( msg ) {\n            if ( ! $("iframe#galaxy_main").contents().find("body").find("div[class=\'errormessage\']").size() ) {\n                $("iframe#galaxy_main").contents().find("body").prepend( \'<div class="errormessage" name="upload_error">\' + msg + \'</div><p/>\' );\n            } else {\n                $("iframe#galaxy_main").contents().find("body").find("div[class=\'errormessage\']").text( msg );\n            }\n        }\n        var uploads_in_progress = 0;\n        jQuery( function() {\n            $("iframe#galaxy_main").load( function() {\n                $(this).contents().find("form").each( function() { \n                    if ( $(this).find("input[galaxy-ajax-upload]").length > 0 ){\n                        $(this).submit( function() {\n                            // Only bother using a hidden iframe if there\'s a file (e.g. big data) upload\n                            var file_upload = false;\n                            $(this).find("input[galaxy-ajax-upload]").each( function() {\n                                if ( $(this).val() != \'\' ) {\n                                    file_upload = true;\n                                }\n                            });\n                            if ( ! file_upload ) {\n                                return true;\n                            }\n                            // Make a synchronous request to create the datasets first\n                            var async_datasets;\n                            var upload_error = false;\n                            $.ajax( {\n                                async:      false,\n                                type:       "POST",\n                                url:        "')
        # SOURCE LINE 168
        __M_writer(unicode(h.url_for(controller='/tool_runner', action='upload_async_create')))
        __M_writer(u'",\n                                data:       $(this).formSerialize(),\n                                dataType:   "json",\n                                success:    function(array_obj, status) {\n                                                if (array_obj.length > 0) {\n                                                    if (array_obj[0] == \'error\') {\n                                                        upload_error = true;\n                                                        upload_form_error(array_obj[1]);\n                                                    } else {\n                                                        async_datasets = array_obj.join();\n                                                    }\n                                                } else {\n                                                    // ( gvk 1/22/10 ) FIXME: this block is never entered, so there may be a bug somewhere\n                                                    // I\'ve done some debugging like checking to see if array_obj is undefined, but have not\n                                                    // tracked down the behavior that will result in this block being entered.  I believe the\n                                                    // intent was to have this block entered if the upload button is clicked on the upload\n                                                    // form but no file was selected.\n                                                    upload_error = true;\n                                                    upload_form_error( \'No data was entered in the upload form.  You may choose to upload a file, paste some data directly in the data box, or enter URL(s) to fetch data.\' );\n                                                }\n                                            }\n                            } );\n                            if (upload_error == true) {\n                                return false;\n                            } else {\n                                $(this).find("input[name=async_datasets]").val( async_datasets );\n                                $(this).append("<input type=\'hidden\' name=\'ajax_upload\' value=\'true\'>");\n                            }\n                            // iframe submit is required for nginx (otherwise the encoding is wrong)\n                            $(this).ajaxSubmit( { iframe:   true,\n                                                  complete: function (xhr, stat) {\n                                                                uploads_in_progress--;\n                                                                if (uploads_in_progress == 0) {\n                                                                    window.onbeforeunload = null;\n                                                                }\n                                                            }\n                                                 } );\n                            uploads_in_progress++;\n                            window.onbeforeunload = function() { return "Navigating away from the Galaxy analysis interface will interrupt the file upload(s) currently in progress.  Do you really want to do this?"; }\n                            if ( $(this).find("input[name=\'folder_id\']").val() != undefined ) {\n                                var library_id = $(this).find("input[name=\'library_id\']").val();\n                                var show_deleted = $(this).find("input[name=\'show_deleted\']").val();\n                                if ( location.pathname.indexOf( \'admin\' ) != -1 ) {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 211
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library_admin&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                } else {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 213
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                }\n                            } else {\n                                $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 216
        __M_writer(unicode(h.url_for(controller='tool_runner', action='upload_async_message')))
        __M_writer(u'");\n                            }\n                            return false;\n                        });\n                    }\n                });\n            });\n        });\n    </script>\n    <![endif]>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n    ')
        # SOURCE LINE 22
        __M_writer(unicode(h.css('base','jquery.rating')))
        __M_writer(u'\n    <style type="text/css">\n    #center {\n')
        # SOURCE LINE 25
        if not self.has_left_panel:
            # SOURCE LINE 26
            __M_writer(u'            left: 0 !important;\n')
            pass
        # SOURCE LINE 28
        if not self.has_right_panel:
            # SOURCE LINE 29
            __M_writer(u'            right: 0 !important;\n')
            pass
        # SOURCE LINE 31
        __M_writer(u'    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 229
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer(u'\n\n')
        # SOURCE LINE 39
        if app.config.sentry_dsn:
            # SOURCE LINE 40
            __M_writer(u'        ')
            __M_writer(unicode(h.js( "libs/tracekit", "libs/raven" )))
            __M_writer(u"\n        <script>\n            Raven.config('")
            # SOURCE LINE 42
            __M_writer(unicode(app.config.sentry_dsn_public))
            __M_writer(u"').install();\n")
            # SOURCE LINE 43
            if trans.user:
                # SOURCE LINE 44
                __M_writer(u'                Raven.setUser( { email: "')
                __M_writer(unicode(trans.user.email))
                __M_writer(u'" } );\n')
                pass
            # SOURCE LINE 46
            __M_writer(u'        </script>\n')
            pass
        # SOURCE LINE 48
        __M_writer(u'\n    ')
        # SOURCE LINE 49
        __M_writer(unicode(h.js(
        'libs/jquery/jquery',
        'libs/jquery/jquery.migrate',
        'libs/jquery/select2',
        'libs/bootstrap',
        'libs/underscore',
        'libs/backbone/backbone',
        'libs/backbone/backbone-relational',
        'libs/handlebars.runtime',
        'galaxy.base',
        'libs/require'
    )))
        # SOURCE LINE 60
        __M_writer(u'\n\n    ')
        # SOURCE LINE 62
        __M_writer(unicode(h.templates(
        "template-popupmenu-menu"
    )))
        # SOURCE LINE 64
        __M_writer(u'\n\n    ')
        # SOURCE LINE 66
        __M_writer(unicode(h.js(
        "mvc/ui"
    )))
        # SOURCE LINE 68
        __M_writer(u'\n\n    <script type="text/javascript">\n')
        # SOURCE LINE 72
        __M_writer(u"        var galaxy_config =\n        {\n            root: '")
        # SOURCE LINE 74
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u"'\n        };\n\n")
        # SOURCE LINE 78
        __M_writer(u'        if (window != window.top)\n            $(\'<link href="\' + galaxy_config.root + \'static/style/galaxy.frame.masthead.css" rel="stylesheet">\').appendTo(\'head\');\n\n        // start a Galaxy namespace for objects created\n        window.Galaxy = window.Galaxy || {};\n\n        // console protection\n        window.console = window.console || {\n            log     : function(){},\n            debug   : function(){},\n            info    : function(){},\n            warn    : function(){},\n            error   : function(){},\n            assert  : function(){}\n        };\n\n')
        # SOURCE LINE 95
        __M_writer(u'        require.config({\n            baseUrl: "')
        # SOURCE LINE 96
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n            shim: {\n                "libs/underscore": { exports: "_" },\n                "libs/backbone/backbone": { exports: "Backbone" },\n                "libs/backbone/backbone-relational": ["libs/backbone/backbone"]\n            }\n        });\n        \n')
        # SOURCE LINE 105
        __M_writer(u"        require(['galaxy.master', 'galaxy.frame', 'galaxy.modal', 'galaxy.upload'], function(master, frame, modal, upload)\n        {\n            Galaxy.master = new master.GalaxyMaster();\n            Galaxy.frame_manager = new frame.GalaxyFrameManager();\n            Galaxy.modal = new modal.GalaxyModal();\n")
        # SOURCE LINE 111
        __M_writer(u'        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


