# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1385061688.301363
_template_filename='templates/webapps/galaxy/workflow/list_for_run.mako'
_template_uri='workflow/list_for_run.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['title']


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
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        h = context.get('h', UNDEFINED)
        workflows = context.get('workflows', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        message = context.get('message', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        if message:
            # SOURCE LINE 6

            try:
                messagetype
            except:
                messagetype = "done"
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['messagetype'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 11
            __M_writer(u'\n<p />\n<div class="')
            # SOURCE LINE 13
            __M_writer(unicode(messagetype))
            __M_writer(u'message">\n    ')
            # SOURCE LINE 14
            __M_writer(unicode(message))
            __M_writer(u'\n</div>\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'\n<h2>Your workflows</h2>\n\n<ul class="manage-table-actions">\n    <li>\n        <a class="action-button" href="')
        # SOURCE LINE 22
        __M_writer(unicode(h.url_for( controller='workflow', action='index' )))
        __M_writer(u'" target="_parent">\n            <span>Switch to workflow management view</span>\n        </a>\n    </li>\n</ul>\n  \n')
        # SOURCE LINE 28
        if workflows:
            # SOURCE LINE 29
            __M_writer(u'    <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n        <tr class="header">\n            <th>Name</th>\n            <th># of Steps</th>\n')
            # SOURCE LINE 34
            __M_writer(u'            <th></th>\n        </tr>\n')
            # SOURCE LINE 36
            for i, workflow in enumerate( workflows ):
                # SOURCE LINE 37
                __M_writer(u'            <tr>\n                <td>\n                    <a href="')
                # SOURCE LINE 39
                __M_writer(unicode(h.url_for(controller='workflow', action='run', id=trans.security.encode_id(workflow.id) )))
                __M_writer(u'">')
                __M_writer(unicode(h.to_unicode( workflow.name )))
                __M_writer(u'</a>\n                    <a id="wf-')
                # SOURCE LINE 40
                __M_writer(unicode(i))
                __M_writer(u'-popup" class="popup-arrow" style="display: none;">&#9660;</a>\n                </td>\n                <td>')
                # SOURCE LINE 42
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n')
                # SOURCE LINE 44
                __M_writer(u'            </tr>    \n')
                pass
            # SOURCE LINE 46
            __M_writer(u'    </table>\n')
            # SOURCE LINE 47
        else:
            # SOURCE LINE 48
            __M_writer(u'\n    You have no workflows.\n\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'\n<h2>Workflows shared with you by others</h2>\n\n')
        # SOURCE LINE 55
        if shared_by_others:
            # SOURCE LINE 56
            __M_writer(u'    <table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n        <tr class="header">\n            <th>Name</th>\n            <th>Owner</th>\n            <th># of Steps</th>\n            <th></th>\n        </tr>\n')
            # SOURCE LINE 63
            for i, association in enumerate( shared_by_others ):
                # SOURCE LINE 64
                __M_writer(u'            ')
                workflow = association.stored_workflow 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['workflow'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n            <tr>\n                <td>\n                    <a href="')
                # SOURCE LINE 67
                __M_writer(unicode(h.url_for( controller='workflow', action='run', id=trans.security.encode_id(workflow.id) )))
                __M_writer(u'">')
                __M_writer(unicode(workflow.name))
                __M_writer(u'</a>\n                    <a id="shared-')
                # SOURCE LINE 68
                __M_writer(unicode(i))
                __M_writer(u'-popup" class="popup-arrow" style="display: none;">&#9660;</a>\n                </td>\n                <td>')
                # SOURCE LINE 70
                __M_writer(unicode(workflow.user.email))
                __M_writer(u'</td>\n                <td>')
                # SOURCE LINE 71
                __M_writer(unicode(len(workflow.latest_workflow.steps)))
                __M_writer(u'</td>\n            </tr>    \n')
                pass
            # SOURCE LINE 74
            __M_writer(u'    </table>\n')
            # SOURCE LINE 75
        else:
            # SOURCE LINE 76
            __M_writer(u'\n    No workflows have been shared with you.\n\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Workflow home')
        return ''
    finally:
        context.caller_stack._pop_frame()


