# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389957408.055567
_template_filename='templates/admin/jobs.mako'
_template_uri='/admin/jobs.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['javascripts', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x139b4b90', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x139b4b90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x139b4b90')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        cutoff = _import_ns.get('cutoff', context.get('cutoff', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        jobs = _import_ns.get('jobs', context.get('jobs', UNDEFINED))
        last_updated = _import_ns.get('last_updated', context.get('last_updated', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        __M_writer(u'\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n<h2>Jobs</h2>\n\n')
        # SOURCE LINE 20
        if message:
            # SOURCE LINE 21
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 23
        __M_writer(u'\n<p>\n    All unfinished jobs are displayed here.  To display only jobs that have not\n    had their job state updated recently, set a cutoff value in the \'cutoff\'\n    box below.\n</p>\n<p>\n    If any jobs are displayed, you may choose to stop them.  Your stop message\n    will be displayed to the user as: "This job was stopped by an\n    administrator: <b>&lt;YOUR MESSAGE&gt;</b>  For more information or help,\n    report this error".\n</p>\n\n\n<p/>\n\n')
        # SOURCE LINE 39
        if jobs:
            # SOURCE LINE 40
            __M_writer(u'<form name="jobs" action="')
            __M_writer(unicode(h.url_for(controller='admin', action='jobs')))
            __M_writer(u'" method="POST">\n    <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n        <tr class="header">\n            <td><input type="checkbox" onClick="toggle_all(this)"/></td>\n            <td>Job ID</td>\n            <td>User</td>\n            <td>Last Update</td>\n            <td>Tool</td>\n            <td>State</td>\n            <td>Inputs</td>\n            <td>Command Line</td>\n            <td>Job Runner</td>\n            <td>PID/Cluster ID</td>\n        </tr>\n')
            # SOURCE LINE 54
            for job in jobs:
                # SOURCE LINE 55
                __M_writer(u'                <td>\n')
                # SOURCE LINE 56
                if job.state == 'upload':
                    # SOURCE LINE 57
                    __M_writer(u'                        &nbsp;\n')
                    # SOURCE LINE 58
                else:
                    # SOURCE LINE 59
                    __M_writer(u'                        <input type="checkbox" name="stop" value="')
                    __M_writer(unicode(job.id))
                    __M_writer(u'"/>\n')
                    pass
                # SOURCE LINE 61
                __M_writer(u'                </td>\n                <td>')
                # SOURCE LINE 62
                __M_writer(unicode(job.id))
                __M_writer(u'</td>\n')
                # SOURCE LINE 63
                if job.history and job.history.user:
                    # SOURCE LINE 64
                    __M_writer(u'                    <td>')
                    __M_writer(unicode(job.history.user.email))
                    __M_writer(u'</td>\n')
                    # SOURCE LINE 65
                else:
                    # SOURCE LINE 66
                    __M_writer(u'                    <td>anonymous</td>\n')
                    pass
                # SOURCE LINE 68
                __M_writer(u'                <td>')
                __M_writer(unicode(last_updated[job.id]))
                __M_writer(u' ago</td>\n                <td>')
                # SOURCE LINE 69
                __M_writer(unicode(job.tool_id))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 70
                __M_writer(unicode(job.state))
                __M_writer(u'</td>\n                ')
                # SOURCE LINE 71

                try:
                    inputs = ", ".join( [ '%s&nbsp;%s' % ( da.dataset.id, da.dataset.state ) for da in job.input_datasets ] )
                except:
                    inputs = 'Unable to determine inputs'
                                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['inputs','da'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 76
                __M_writer(u'\n                <td>')
                # SOURCE LINE 77
                __M_writer(unicode(inputs))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 78
                __M_writer(unicode(job.command_line))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 79
                __M_writer(unicode(job.job_runner_name))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 80
                __M_writer(unicode(job.job_runner_external_id))
                __M_writer(u'</td>\n            </tr>\n')
                pass
            # SOURCE LINE 83
            __M_writer(u'    </table>\n    <p/>\n    <div class="toolForm">\n        <div class="toolFormTitle">\n            Stop Jobs\n        </div>\n        <div class="toolFormBody">\n            <div class="form-row">\n                <label>\n                    Stop message:\n                </label>\n                <div class="form-row-input">\n                    <input type="text" name="stop_msg" size="40"/>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    to be displayed to the user\n                </div>\n            </div>\n            <div class="form-row">\n                <input type="submit" class="primary-button" name="submit" value="Submit">\n            </div>\n        </div>\n    </div>\n    <p/>\n</form>\n')
            # SOURCE LINE 108
        else:
            # SOURCE LINE 109
            __M_writer(u'    <div class="infomessage">There are no unfinished jobs to show with current cutoff time.</div>\n    <p/>\n')
            pass
        # SOURCE LINE 112
        __M_writer(u'<form name="jobs" action="')
        __M_writer(unicode(h.url_for(controller='admin', action='jobs')))
        __M_writer(u'" method="POST">\n    <div class="toolForm">\n        <div class="toolFormTitle">\n            Update Jobs\n        </div>\n        <div class="toolFormBody">\n\n            <div class="form-row">\n                <label>\n                    Cutoff:\n                </label>\n                <div class="form-row-input">\n                    <input type="text" name="cutoff" size="4" value="')
        # SOURCE LINE 124
        __M_writer(unicode(cutoff))
        __M_writer(u'"/>\n                </div>\n                <div class="toolParamHelp" style="clear: both;">\n                    In seconds\n                </div>\n            </div>\n            <div class="form-row">\n                <input type="submit" class="primary-button" name="submit" value="Refresh">\n            </div>\n        </div>\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x139b4b90')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n        function toggle_all(source) {\n            // sets all checkboxes in source\'s parent form to match source element.\n            $.each($(source).closest("form").find(":checkbox"), function(i, v){\n                v.checked = source.checked;\n            });\n        }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x139b4b90')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'Jobs')
        return ''
    finally:
        context.caller_stack._pop_frame()


