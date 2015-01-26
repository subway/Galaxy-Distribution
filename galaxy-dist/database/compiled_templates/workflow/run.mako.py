# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399324967.49742
_template_filename='templates/webapps/galaxy/workflow/run.mako'
_template_uri='workflow/run.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts', 'do_inputs', 'row_for_param']


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
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        isinstance = context.get('isinstance', UNDEFINED)
        missing_tools = context.get('missing_tools', UNDEFINED)
        basestring = context.get('basestring', UNDEFINED)
        errors = context.get('errors', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        workflow = context.get('workflow', UNDEFINED)
        def do_inputs(inputs,values,errors,prefix,step,other_values=None,already_used=None):
            return render_do_inputs(context.locals_(__M_locals),inputs,values,errors,prefix,step,other_values,already_used)
        len = context.get('len', UNDEFINED)
        step_version_changes = context.get('step_version_changes', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        t = context.get('t', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        has_upgrade_messages = context.get('has_upgrade_messages', UNDEFINED)
        steps = context.get('steps', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        history_id = context.get('history_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 182
        __M_writer(u'\n\n')
        # SOURCE LINE 221
        __M_writer(u'\n\n')
        # SOURCE LINE 223

        from galaxy.tools.parameters import DataToolParameter, RuntimeValue
        from galaxy.jobs.actions.post import ActionBox
        import re
        import colorsys
        import random
        
        used_accumulator = []
        
        wf_parms = {}
        for step in steps:
            for v in [ActionBox.get_short_str(pja) for pja in step.post_job_actions] + step.state.inputs.values():
                if isinstance(v, basestring):
                    for rematch in re.findall('\$\{.+?\}', v):
                        if rematch[2:-1] not in wf_parms:
                            wf_parms[rematch[2:-1]] = ""
        if wf_parms:
            hue_offset = 1.0 / len(wf_parms)
            hue = 0.0
            for k in wf_parms.iterkeys():
                wf_parms[k] = "#%X%X%X" % tuple([int(x * 255) for x in colorsys.hsv_to_rgb(hue, .1, .9)])
                hue += hue_offset
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['hue','hue_offset','wf_parms','ActionBox','DataToolParameter','rematch','used_accumulator','k','random','pja','re','step','RuntimeValue','colorsys','v','x'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 245
        __M_writer(u'\n\n')
        # SOURCE LINE 282
        __M_writer(u'\n\n')
        # SOURCE LINE 370
        __M_writer(u'\n\n<div id=\'ec_button_container\'>\n    <span class="action-button" id="show_all_tool_body">Expand All</span>\n    <span class="action-button" id="hide_all_tool_body">Collapse</span>\n</div>\n\n<h2>Running workflow "')
        # SOURCE LINE 377
        __M_writer(unicode(h.to_unicode( workflow.name )))
        __M_writer(u'"</h2>\n\n')
        # SOURCE LINE 379
        if has_upgrade_messages:
            # SOURCE LINE 380
            __M_writer(u'<div class="warningmessage">\n    Problems were encountered when loading this workflow, likely due to tool\n    version changes. Missing parameter values have been replaced with default.\n    Please review the parameter values below.\n</div>\n')
            pass
        # SOURCE LINE 386
        __M_writer(u'\n')
        # SOURCE LINE 387
        if step_version_changes:
            # SOURCE LINE 388
            __M_writer(u'    <div class="infomessage">\n        The following tools are beinge executed with a different version from\n        what was available when this workflow was last saved because the\n        previous version is no longer available for use on this galaxy\n        instance.\n        To upgrade your workflow and dismiss this message simply edit the\n        workflow and re-save it to update the stored tool version.\n        <ul>\n')
            # SOURCE LINE 396
            for vc in step_version_changes:
                # SOURCE LINE 397
                __M_writer(u'                <li>')
                __M_writer(unicode(vc))
                __M_writer(u'</li>\n')
                pass
            # SOURCE LINE 399
            __M_writer(u'        </ul>\n    </div>\n')
            pass
        # SOURCE LINE 402
        __M_writer(u'\n')
        # SOURCE LINE 403
        if workflow.annotation:
            # SOURCE LINE 404
            __M_writer(u'    <div class="workflow-annotation">')
            __M_writer(unicode(workflow.annotation))
            __M_writer(u'</div>\n    <hr/>\n')
            pass
        # SOURCE LINE 407
        __M_writer(u'\n<form id="tool_form" name="tool_form" method="POST">\n')
        # SOURCE LINE 410
        __M_writer(u'\n')
        # SOURCE LINE 411
        if wf_parms:
            # SOURCE LINE 412
            __M_writer(u'<div class="metadataForm">\n    <div class="metadataFormTitle">Workflow Parameters</div>\n    <div class="metadataFormBody">\n')
            # SOURCE LINE 415
            for parm in wf_parms:
                # SOURCE LINE 416
                __M_writer(u"        <div class='form-row'><label style='width:100px;'>")
                __M_writer(unicode(parm))
                __M_writer(u'<input style="border:2px solid ')
                __M_writer(unicode(wf_parms[parm]))
                __M_writer(u';border-left-width:8px;" type="text" class=\'wf_parm_input ptag_')
                __M_writer(unicode(parm))
                __M_writer(u'\' name="wf_parm|')
                __M_writer(unicode(parm))
                __M_writer(u'" value=""/></label></div>\n')
                pass
            # SOURCE LINE 418
            __M_writer(u'    </div>\n</div>\n    <script type="text/javascript">\n    // Set the change hooks for workflow parameters.\n    $(document).ready(function () {\n        $(\'.wf_parm_input\').bind(\'change keypress keyup\', function(event){\n            // DBTODO This is probably not reliable.  Ensure we have the right class.\n            var new_text = $(this).val();\n            if (new_text === \'\'){\n                var tag_id = $(this).attr("class").split(\' \')[1].substring(5);\n                // Set text properly.\n                $(\'.wfpspan.wf_parm__\'+tag_id).text(tag_id);\n            }else{\n                var tag_id = $(this).attr("class").split(\' \')[1].substring(5);\n                // Set text properly.\n                $(\'.wfpspan.wf_parm__\'+tag_id).text(new_text);\n                // Now set the hidden input to the generated text.\n                $(\'.wfpspan.wf_parm__\'+tag_id).not(\'.pja_wfp\').each(function(){\n                    var new_text = $(this).parent().text();\n                    $(this).parent().siblings().children().val(new_text);\n                });\n            }\n        });\n    });\n    </script>\n')
            pass
        # SOURCE LINE 444
        for i, step in enumerate( steps ):
            # SOURCE LINE 445
            if step.type == 'tool' or step.type is None:
                # SOURCE LINE 446
                __M_writer(u'      ')

                tool = trans.app.toolbox.get_tool( step.tool_id )
                      
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 448
                __M_writer(u'\n      <input type="hidden" name="')
                # SOURCE LINE 449
                __M_writer(unicode(step.id))
                __M_writer(u'|tool_state" value="')
                __M_writer(unicode(step.state.encode( tool, app )))
                __M_writer(u'">\n      <div class="toolForm">\n          <div class="toolFormTitle">\n              <span class=\'title_ul_text\'>Step ')
                # SOURCE LINE 452
                __M_writer(unicode(int(step.order_index)+1))
                __M_writer(u': ')
                __M_writer(unicode(tool.name))
                __M_writer(u'</span>\n')
                # SOURCE LINE 453
                if tool.version:
                    # SOURCE LINE 454
                    __M_writer(u'                  (version ')
                    __M_writer(unicode(tool.version))
                    __M_writer(u')\n')
                    pass
                # SOURCE LINE 456
                if step.annotations:
                    # SOURCE LINE 457
                    __M_writer(u'                <div class="step-annotation">')
                    __M_writer(unicode(h.to_unicode( step.annotations[0].annotation )))
                    __M_writer(u'</div>\n')
                    pass
                # SOURCE LINE 459
                __M_writer(u'          </div>\n          <div class="toolFormBody">\n                ')
                # SOURCE LINE 461
                __M_writer(unicode(do_inputs( tool.inputs, step.state.inputs, errors.get( step.id, dict() ), "", step, None, used_accumulator )))
                __M_writer(u'\n')
                # SOURCE LINE 462
                if step.post_job_actions:
                    # SOURCE LINE 463
                    __M_writer(u"                    <hr/>\n                    <div class='form-row'>\n")
                    # SOURCE LINE 465
                    if len(step.post_job_actions) > 1:
                        # SOURCE LINE 466
                        __M_writer(u'                        <label>Actions:</label>\n')
                        # SOURCE LINE 467
                    else:
                        # SOURCE LINE 468
                        __M_writer(u'                        <label>Action:</label>\n')
                        pass
                    # SOURCE LINE 470
                    __M_writer(u'                    ')

                    pja_ss_all = []
                    for pja_ss in [ActionBox.get_short_str(pja) for pja in step.post_job_actions]:
                        for rematch in re.findall('\$\{.+?\}', pja_ss):
                            pja_ss = pja_ss.replace(rematch, '<span style="background-color:%s" class="wfpspan wf_parm__%s pja_wfp">%s</span>' % (wf_parms[rematch[2:-1]], rematch[2:-1], rematch[2:-1]))
                        pja_ss_all.append(pja_ss)
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['rematch','pja_ss_all','pja','pja_ss'] if __M_key in __M_locals_builtin_stored]))
                    # SOURCE LINE 476
                    __M_writer(u'\n                    ')
                    # SOURCE LINE 477
                    __M_writer(unicode('<br/>'.join(pja_ss_all)))
                    __M_writer(u'\n                    </div>\n')
                    pass
                # SOURCE LINE 480
                __M_writer(u'              </div>\n          </div>\n')
                # SOURCE LINE 482
            else:
                # SOURCE LINE 483
                __M_writer(u'        ')
                module = step.module 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['module'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n          <input type="hidden" name="')
                # SOURCE LINE 484
                __M_writer(unicode(step.id))
                __M_writer(u'|tool_state" value="')
                __M_writer(unicode(module.encode_runtime_state( t, step.state )))
                __M_writer(u'">\n          <div class="toolForm">\n              <div class="toolFormTitle">\n                  <span class=\'title_ul_text\'>Step ')
                # SOURCE LINE 487
                __M_writer(unicode(int(step.order_index)+1))
                __M_writer(u': ')
                __M_writer(unicode(module.name))
                __M_writer(u'</span>\n')
                # SOURCE LINE 488
                if step.annotations:
                    # SOURCE LINE 489
                    __M_writer(u'                    <div class="step-annotation">')
                    __M_writer(unicode(step.annotations[0].annotation))
                    __M_writer(u'</div>\n')
                    pass
                # SOURCE LINE 491
                __M_writer(u'          </div>\n          <div class="toolFormBody">\n              ')
                # SOURCE LINE 493

              # Filter possible inputs to data types that are valid for subsequent steps
                type_filter = []
                for oc in step.output_connections:
                    for ic in oc.input_step.module.get_data_inputs():
                        if 'extensions' in ic and ic['name'] == oc.input_name:
                            type_filter += ic['extensions']
                if not type_filter:
                    type_filter = ['data']
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ic','oc','type_filter'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 502
                __M_writer(u'\n              ')
                # SOURCE LINE 503
                __M_writer(unicode(do_inputs( module.get_runtime_inputs(type_filter), step.state.inputs, errors.get( step.id, dict() ), "", step, None, used_accumulator )))
                __M_writer(u'\n          </div>\n      </div>\n')
                pass
            pass
        # SOURCE LINE 508
        if missing_tools:
            # SOURCE LINE 509
            __M_writer(u'    <div class=\'errormessage\'>\n    <strong>This workflow utilizes tools which are unavailable, and cannot be run.  Enable the tools listed below, or <a href="')
            # SOURCE LINE 510
            __M_writer(unicode(h.url_for(controller='workflow', action='editor', id=trans.security.encode_id(workflow.id) )))
            __M_writer(u'" target="_parent">edit the workflow</a> to correct these errors.</strong><br/>\n    <ul>\n')
            # SOURCE LINE 512
            for i, tool in enumerate( missing_tools ):
                # SOURCE LINE 513
                __M_writer(u'        <li>')
                __M_writer(unicode(tool))
                __M_writer(u'</li>\n')
                pass
            # SOURCE LINE 515
            __M_writer(u'    </ul>\n')
            # SOURCE LINE 516
        else:
            # SOURCE LINE 517
            if history_id is None:
                # SOURCE LINE 518
                __M_writer(u'<p id=\'new_history_p\'>\n    <input type="checkbox" name=\'new_history\' value="true" id=\'new_history_cbx\'/><label for=\'new_history_cbx\'>Send results to a new history </label>\n    <span id="new_history_input">named: <input type=\'text\' name=\'new_history_name\' value=\'')
                # SOURCE LINE 520
                __M_writer(unicode(h.to_unicode( workflow.name )))
                __M_writer(u"'/></span>\n</p>\n")
                pass
            # SOURCE LINE 523
            __M_writer(u'<input type="submit" class="btn btn-primary" name="run_workflow" value="Run workflow" />\n</form>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 184
        __M_writer(u'\n    ')
        # SOURCE LINE 185
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 186
        __M_writer(unicode(h.css( "autocomplete_tagging" )))
        __M_writer(u'\n    <style type="text/css">\n    #new_history_p{\n        line-height:2.5em;\n        margin:0em 0em .5em 0em;\n    }\n    #new_history_cbx{\n        margin-right:.5em;\n    }\n    #new_history_input{\n        display:none;\n        line-height:1em;\n    }\n    #ec_button_container{\n        float:right;\n    }\n    div.toolForm{\n        margin-top: 10px;\n        margin-bottom: 10px;\n    }\n    div.toolFormTitle{\n        cursor:pointer;\n    }\n    .title_ul_text{\n        text-decoration:underline;\n    }\n    .step-annotation {\n        margin-top: 0.25em;\n        font-weight: normal;\n        font-size: 97%;\n    }\n    .workflow-annotation {\n        margin-bottom: 1em;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        hide_fixed_params = context.get('hide_fixed_params', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    ')
        # SOURCE LINE 4
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        $( function() {\n            function show_tool_body(title){\n                title.parent().show().css(\'border-bottom-width\', \'1px\');\n                title.next().show(\'fast\');\n                if (\'')
        # SOURCE LINE 10
        __M_writer(unicode(hide_fixed_params))
        __M_writer(u'\'.toLowerCase() == \'true\') {\n                    // show previously hidden parameters\n                    title.next().children(".form-row").show();\n                }\n            }\n            function hide_tool_body(title){\n                title.parent().css(\'border-bottom-width\', \'0px\');\n                title.next().hide(\'fast\');\n            }\n            function toggle_tool_body(title) {\n                if (title.next().is(\':visible\')){\n                    hide_tool_body(title);\n                }else{\n                    show_tool_body(title);\n                }\n            }\n            function toggle_multiinput(select) {\n                var placeholder;\n                if (select.attr(\'multiple\')) {\n                    $(\'.multiinput\').removeClass(\'disabled\');\n                    if (select.val()) {\n                        select.val(select.val()[0]);\n                    } else {\n                        select.val($(\'option:last\', select).val());\n                    }\n                    select.closest(\'.form-row\').children(\'label\').children(\'span.mode-icon\').hide();\n                    select.removeAttr(\'multiple\').removeAttr(\'size\');\n                    placeholder = \'type to filter\';\n                } else {\n                    $(\'.multiinput\', select.closest(\'.form-row\')).removeClass(\'disabled\');\n                    select.closest(\'.form-row\').children(\'label\').children(\'span.mode-icon\').show();\n                    select.attr(\'multiple\', \'multiple\').attr(\'size\', 8);\n                    placeholder = \'type to filter, [enter] to select all\';\n                }\n                $(\'input.multiinput-filter\', select.parent()).attr(\n                    \'placeholder\', placeholder);\n            }\n            $( "select[refresh_on_change=\'true\']").change( function() {\n                $( "#tool_form" ).submit();\n            });\n            $("div.toolFormTitle").click(function(){\n                toggle_tool_body($(this));\n            });\n            if (\'')
        # SOURCE LINE 53
        __M_writer(unicode(hide_fixed_params))
        __M_writer(u'\'.toLowerCase() == \'true\') {\n                // hide parameters that are not runtime inputs\n                $("div.form-row:not(:has(select, textarea, input[type!=hidden], .wfpspan))").hide();\n                $("div.toolForm:not(:has(select, textarea, input[type!=hidden], .wfpspan))").hide();\n            }\n            else {\n                // Collapse non-interactive run-workflow panels by default.\n                $("div.toolFormBody:not(:has(select, textarea, input[type!=hidden], .wfpspan))").hide().parent().css(\'border-bottom-width\', \'0px\');\n            }\n            $("#show_all_tool_body").click(function(){\n                $("div.toolFormTitle").each(function(){\n                    show_tool_body($(this));\n                });\n            });\n            $("#hide_all_tool_body").click(function(){\n                $("div.toolFormTitle").each(function(){\n                    hide_tool_body($(this));\n                });\n            });\n            $("#new_history_cbx").click(function(){\n                $("#new_history_input").toggle(this.checked);\n            });\n            $(\'span.multiinput_wrap select[name*="|input"]\').removeAttr(\'multiple\').each(function(i, s) {\n                var select = $(s);\n                // The destroy on the following line is temporary and prevents\n                // select2 use on Input Dataset Steps, but allows elsewhere.  We\n                // need a new widget to better handle pairwise matching.\n                select.select2("destroy");\n                var new_width = Math.max(200, select.width()) + 20;\n                // Find the label for this element.\n                select.closest(\'.form-row\').children(\'label\').append(\n                    $(\'<span class="icon-button multiinput"></span>\').click(function() {\n                        if ($(this).hasClass(\'disabled\')) return;\n                        toggle_multiinput(select);\n                        select.focus();\n                    }).attr(\'title\',\n                            \'Enable/disable selection of multiple input \' +\n                            \'files. Each selected file will have an \' +\n                            \'instance of the workflow.\').tooltip({placement: \'bottom\'})\n                );\n                var filter = $(\'<input type="text" class="multiinput-filter" \' +\n                               \'placeholder="type to filter">\');\n                var filter_timeout = false;\n                var original_rows = select.find(\'option\');\n                var previous_filter = \'\';\n                // Todo: might have to choose keypress, depending on browser\n                filter.keydown(function(e) {\n                    var filter_select = function() {\n                        var f = $.trim(filter.val());\n                        var filtered_rows = original_rows;\n                        if (f.length >= 1) {\n                            filtered_rows = original_rows.filter(function() {\n                                return new RegExp(f, \'ig\').test($(this).text());\n                            });\n                        }\n                        select.html(\'\');\n                        select.html(filtered_rows);\n                    };\n                    if (e.which == 13) { // 13 = enter key\n                        e.preventDefault();\n                        multi = select.attr(\'multiple\');\n                        if (typeof multi !== \'undefined\' && multi !== false) {\n                            if (!select.find(\'option:not(:selected)\').length) {\n                                select.find(\'option\').removeAttr(\'selected\');\n                            } else {\n                                select.find(\'option\').attr(\'selected\', \'selected\');\n                            }\n                        }\n                        return;\n                    }\n                    if (filter.val() != previous_filter) {\n                        if (filter_timeout) clearTimeout(filter_timeout);\n                        timeout = setTimeout(filter_select, 300);\n                        previous_filter = filter.val();\n                    }\n                }).width(new_width).css(\'display\', \'block\');\n                select.after(filter);\n                select.width(new_width);\n            });\n\n            // Augment hidden fields with icons.\n            // http://stackoverflow.com/a/2088430\n            $(function(){\n                $(".multi-mode").each(function(){\n                    if($(this).val() == "matched") { \n                        $(this).closest(\'.form-row\').children(\'label\').append($(\'<span class="icon-button link mode-icon" title="This input is linked and will be run in matched order with other input datasets (ex: use this for matching forward and reverse reads)."></span>\')\n                            .attr({id:$(this).attr("id")})\n                            .css("display", $(this).css("display"))\n                            .tooltip({placement: \'bottom\'}));\n                    } else {\n                        $(this).closest(\'.form-row\').children(\'label\').append($(\'<span class="icon-button link-broken mode-icon" title="This input is not linked and each selection will be run against *all* other inputs."></span>\')\n                            .attr({id:$(this).attr("id")})\n                            .css("display", $(this).css("display"))\n                            .tooltip({placement: \'bottom\'}));\n                    }\n                });\n                $("span.mode-icon").click(function(){\n                    i= $(this).closest(\'.form-row\').find("input[type=hidden]");\n                    if($(this).hasClass("link")) {\n                        $(this).removeClass("link").addClass("link-broken");\n                        $(i).val("product");\n                    } else {\n                        $(this).removeClass("link-broken").addClass("link");\n                        $(i).val("matched");\n                    }\n                });\n            });\n            $("#tool_form").submit(function(e) {\n                var matchLength = -1;\n                $(\'span.multiinput_wrap select[name*="|input"]\').each(function() {\n                    var value = $(this).val();\n                    if(value instanceof Array) {\n                        // Multi-value\n                        if($(this).siblings("input[type=hidden]").val() == "matched") {\n                            var length = $(this).val().length;\n                            if(matchLength == -1) {\n                                matchLength = length;\n                            } else if(length != matchLength) {\n                                e.preventDefault();\n                                alert("Linked inputs must be submitted in equal number.");\n                                return false;\n                            }\n                        }\n                    }\n                });\n                return true;\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_do_inputs(context,inputs,values,errors,prefix,step,other_values=None,already_used=None):
    context.caller_stack._push_frame()
    try:
        def row_for_param(param,value,other_values,error_dict,prefix,step,already_used):
            return render_row_for_param(context,param,value,other_values,error_dict,prefix,step,already_used)
        def do_inputs(inputs,values,errors,prefix,step,other_values=None,already_used=None):
            return render_do_inputs(context,inputs,values,errors,prefix,step,other_values,already_used)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 247
        __M_writer(u'\n')
        # SOURCE LINE 248
        if other_values is None:
            # SOURCE LINE 249
            __M_writer(u'      ')
            other_values = values 
            
            __M_writer(u'\n')
            pass
        # SOURCE LINE 251
        for input_index, input in enumerate( inputs.itervalues() ):
            # SOURCE LINE 252
            if input.type == "repeat":
                # SOURCE LINE 253
                __M_writer(u'      <div class="repeat-group">\n          <div class="form-title-row"><b>')
                # SOURCE LINE 254
                __M_writer(unicode(input.title_plural))
                __M_writer(u'</b></div>\n          ')
                # SOURCE LINE 255
                repeat_values = values[input.name] 
                
                __M_writer(u'\n')
                # SOURCE LINE 256
                for i in range( len( repeat_values ) ):
                    # SOURCE LINE 257
                    if input.name in errors:
                        # SOURCE LINE 258
                        __M_writer(u'                ')
                        rep_errors = errors[input.name][i] 
                        
                        __M_writer(u'\n')
                        # SOURCE LINE 259
                    else:
                        # SOURCE LINE 260
                        __M_writer(u'                ')
                        rep_errors = dict() 
                        
                        __M_writer(u'\n')
                        pass
                    # SOURCE LINE 262
                    __M_writer(u'            <div class="repeat-group-item">\n            ')
                    # SOURCE LINE 263
                    index = repeat_values[i]['__index__'] 
                    
                    __M_writer(u'\n            <div class="form-title-row"><b>')
                    # SOURCE LINE 264
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i + 1))
                    __M_writer(u'</b></div>\n            ')
                    # SOURCE LINE 265
                    __M_writer(unicode(do_inputs( input.inputs, repeat_values[ i ], rep_errors,  prefix + input.name + "_" + str(index) + "|", step, other_values, already_used )))
                    __M_writer(u'\n')
                    # SOURCE LINE 267
                    __M_writer(u'            </div>\n')
                    pass
                # SOURCE LINE 270
                __M_writer(u'      </div>\n')
                # SOURCE LINE 271
            elif input.type == "conditional":
                # SOURCE LINE 272
                __M_writer(u'      ')
                group_values = values[input.name] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 273
                current_case = group_values['__current_case__'] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 274
                new_prefix = prefix + input.name + "|" 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 275
                group_errors = errors.get( input.name, {} ) 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 276
                __M_writer(unicode(row_for_param( input.test_param, group_values[ input.test_param.name ], other_values, group_errors, prefix, step, already_used )))
                __M_writer(u'\n      ')
                # SOURCE LINE 277
                __M_writer(unicode(do_inputs( input.cases[ current_case ].inputs, group_values, group_errors, new_prefix, step, other_values, already_used )))
                __M_writer(u'\n')
                # SOURCE LINE 278
            else:
                # SOURCE LINE 279
                __M_writer(u'      ')
                __M_writer(unicode(row_for_param( input, values[ input.name ], other_values, errors, prefix, step, already_used )))
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_param(context,param,value,other_values,error_dict,prefix,step,already_used):
    context.caller_stack._push_frame()
    try:
        basestring = context.get('basestring', UNDEFINED)
        wf_parms = context.get('wf_parms', UNDEFINED)
        incoming = context.get('incoming', UNDEFINED)
        DataToolParameter = context.get('DataToolParameter', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        list = context.get('list', UNDEFINED)
        enable_unique_defaults = context.get('enable_unique_defaults', UNDEFINED)
        re = context.get('re', UNDEFINED)
        RuntimeValue = context.get('RuntimeValue', UNDEFINED)
        t = context.get('t', UNDEFINED)
        str = context.get('str', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 284
        __M_writer(u'\n')
        # SOURCE LINE 286
        if error_dict.has_key( param.name ):
            # SOURCE LINE 287
            __M_writer(u'        ')
            cls = "form-row form-row-error" 
            
            __M_writer(u'\n')
            # SOURCE LINE 288
        else:
            # SOURCE LINE 289
            __M_writer(u'        ')
            cls = "form-row" 
            
            __M_writer(u'\n')
            pass
        # SOURCE LINE 291
        __M_writer(u'    <div class="')
        __M_writer(unicode(cls))
        __M_writer(u'">\n        <label>')
        # SOURCE LINE 292
        __M_writer(unicode(param.get_label()))
        __M_writer(u'</label>\n        <div>\n')
        # SOURCE LINE 294
        if isinstance( param, DataToolParameter ):
            # SOURCE LINE 295
            if ( prefix + param.name ) in step.input_connections_by_name:
                # SOURCE LINE 296
                __M_writer(u'                    ')

                conns = step.input_connections_by_name[ prefix + param.name ]
                if not isinstance(conns, list):
                    conns = [conns]
                vals = ["Output dataset '%s' from step %d" % (conn.output_name, int(conn.output_step.order_index)+1) for conn in conns]
                                    
                
                # SOURCE LINE 301
                __M_writer(u'\n                    ')
                # SOURCE LINE 302
                __M_writer(unicode(",".join(vals)))
                __M_writer(u'\n')
                # SOURCE LINE 303
            else:
                # SOURCE LINE 305
                __M_writer(u'                    ')

                if value is None:
                    value = other_values[ param.name ] = param.get_initial_value_from_history_prevent_repeats( t, other_values, already_used )
                    if not enable_unique_defaults:
                        del already_used[:]
                
                
                # SOURCE LINE 310
                __M_writer(u'\n')
                # SOURCE LINE 311
                if step.type == 'data_input':
                    # SOURCE LINE 313
                    __M_writer(u'                        <span class=\'multiinput_wrap\'>\n                        <input class="multi-mode" type="hidden" name="')
                    # SOURCE LINE 314
                    __M_writer(unicode(str(step.id)))
                    __M_writer(u'|multi_mode" id="')
                    __M_writer(unicode(str(step.id)))
                    __M_writer(u'|multi_mode" value="matched" />\n                        ')
                    # SOURCE LINE 315
                    __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                    __M_writer(u'\n                        </span>\n')
                    # SOURCE LINE 317
                else:
                    # SOURCE LINE 318
                    __M_writer(u'                        ')
                    __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 320
                __M_writer(u'\n                    <input type="hidden" name="')
                # SOURCE LINE 321
                __M_writer(unicode(step.id))
                __M_writer(u'|__force_update__')
                __M_writer(unicode(prefix))
                __M_writer(unicode(param.name))
                __M_writer(u'" value="true" />\n')
                pass
            # SOURCE LINE 323
        elif isinstance( value, RuntimeValue ) or ( str(step.id) + '|__runtime__' + prefix + param.name ) in incoming:
            # SOURCE LINE 333
            __M_writer(u'                ')

            value = other_values[ param.name ] = param.get_initial_value_from_history_prevent_repeats( t, other_values, already_used )
            if not enable_unique_defaults:
                del already_used[:]
                            
            
            # SOURCE LINE 337
            __M_writer(u'\n                ')
            # SOURCE LINE 338
            __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
            __M_writer(u'\n                <input type="hidden" name="')
            # SOURCE LINE 339
            __M_writer(unicode(step.id))
            __M_writer(u'|__runtime__')
            __M_writer(unicode(prefix))
            __M_writer(unicode(param.name))
            __M_writer(u'" value="true" />\n')
            # SOURCE LINE 340
        else:
            # SOURCE LINE 341
            __M_writer(u'                ')

            p_text = param.value_to_display_text( value, app )
            replacements = []
            if isinstance(p_text, basestring):
                for rematch in re.findall('\$\{.+?\}', p_text):
                    replacements.append('wf_parm__%s' % rematch[2:-1])
                    p_text = p_text.replace(rematch, '<span style="background-color:%s" class="wfpspan wf_parm__%s">%s</span>' % (wf_parms[rematch[2:-1]], rematch[2:-1], rematch[2:-1]))
            
            
            # SOURCE LINE 348
            __M_writer(u'\n')
            # SOURCE LINE 349
            if replacements:
                # SOURCE LINE 350
                __M_writer(u'                    <span style="display:none" class="parm_wrap ')
                __M_writer(unicode(' '.join(replacements)))
                __M_writer(u'">\n                    ')
                # SOURCE LINE 351
                __M_writer(unicode(param.get_html_field( t, value, other_values ).get_html( str(step.id) + "|" + prefix )))
                __M_writer(u'\n                    </span>\n                    <span class="p_text_wrapper">')
                # SOURCE LINE 353
                __M_writer(unicode(p_text))
                __M_writer(u'</span>\n                    <input type="hidden" name="')
                # SOURCE LINE 354
                __M_writer(unicode(step.id))
                __M_writer(u'|__runtime__')
                __M_writer(unicode(prefix))
                __M_writer(unicode(param.name))
                __M_writer(u'" value="true" />\n')
                # SOURCE LINE 355
            else:
                # SOURCE LINE 356
                __M_writer(u'                    ')
                __M_writer(unicode(param.value_to_display_text( value, app )))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 359
        __M_writer(u'        </div>\n')
        # SOURCE LINE 360
        if step.upgrade_messages and param.name in step.upgrade_messages:
            # SOURCE LINE 361
            __M_writer(u'        <div class="warningmark">')
            __M_writer(unicode(step.upgrade_messages[param.name]))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 363
        if error_dict.has_key( param.name ):
            # SOURCE LINE 364
            __M_writer(u'        <div style="color: red; font-weight: bold; padding-top: 1px; padding-bottom: 3px;">\n            <div style="width: 300px;"><img style="vertical-align: middle;" src="')
            # SOURCE LINE 365
            __M_writer(unicode(h.url_for('/static/style/error_small.png')))
            __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
            __M_writer(unicode(error_dict[param.name]))
            __M_writer(u'</span></div>\n        </div>\n')
            pass
        # SOURCE LINE 368
        __M_writer(u'        <div style="clear: both"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


