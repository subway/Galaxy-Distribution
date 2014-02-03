# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389698477.501421
_template_filename='templates/webapps/galaxy/dataset/copy_view.mako'
_template_uri='/dataset/copy_view.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x158c48d0', context._clean_inheritance_tokens(), templateuri=u'/refresh_frames.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x158c48d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x158c48d0')._populate(_import_ns, [u'handle_refresh_frames'])
        done_msg = _import_ns.get('done_msg', context.get('done_msg', UNDEFINED))
        source_dataset_ids = _import_ns.get('source_dataset_ids', context.get('source_dataset_ids', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        target_history_ids = _import_ns.get('target_history_ids', context.get('target_history_ids', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        error_msg = _import_ns.get('error_msg', context.get('error_msg', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        target_histories = _import_ns.get('target_histories', context.get('target_histories', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        source_datasets = _import_ns.get('source_datasets', context.get('source_datasets', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        source_history = _import_ns.get('source_history', context.get('source_history', UNDEFINED))
        current_history = _import_ns.get('current_history', context.get('current_history', UNDEFINED))
        target_history_id = _import_ns.get('target_history_id', context.get('target_history_id', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        if error_msg:
            # SOURCE LINE 25
            __M_writer(u'    <p>\n        <div class="errormessage">')
            # SOURCE LINE 26
            __M_writer(unicode(error_msg))
            __M_writer(u'</div>\n        <div style="clear: both"></div>\n    </p>\n')
            pass
        # SOURCE LINE 30
        if done_msg:
            # SOURCE LINE 31
            __M_writer(u'    <p>\n        <div class="donemessage">')
            # SOURCE LINE 32
            __M_writer(unicode(done_msg))
            __M_writer(u'</div>\n        <div style="clear: both"></div>\n    </p>\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'<p>\n    <div class="infomessage">Copy any number of history items from one history to another.</div>\n    <div style="clear: both"></div>\n</p>\n<p>\n    <form method="post">\n        <div class="toolForm" style="float: left; width: 45%; padding: 0px;">\n            <div class="toolFormTitle">Source History:<br />\n                <select id="source_history" name="source_history" refresh_on_change="true" style="font-weight: normal;">\n')
        # SOURCE LINE 45
        for i, hist in enumerate(target_histories):
            # SOURCE LINE 46
            __M_writer(u'                        ')

            selected = ""
            current_history_text = ""
            if hist == source_history:
                selected = "selected='selected'"
            if hist == current_history:
                current_history_text = " (current history)"
            
                                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['current_history_text','selected'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 54
            __M_writer(u'\n                        <option value="')
            # SOURCE LINE 55
            __M_writer(unicode(trans.security.encode_id(hist.id)))
            __M_writer(u'" ')
            __M_writer(unicode(selected))
            __M_writer(u'>\n                            ')
            # SOURCE LINE 56
            __M_writer(unicode(i + 1))
            __M_writer(u': ')
            __M_writer(unicode(h.truncate(util.unicodify( hist.name ), 30)))
            __M_writer(unicode(current_history_text))
            __M_writer(u'\n                        </option>\n')
            pass
        # SOURCE LINE 59
        __M_writer(u'                </select>\n            </div>\n            <div class="toolFormBody">\n')
        # SOURCE LINE 62
        if len(source_datasets) > 0:
            # SOURCE LINE 63
            for data in source_datasets:
                # SOURCE LINE 64
                __M_writer(u'                        ')

                checked = ""
                encoded_id = trans.security.encode_id(data.id)
                if data.id in source_dataset_ids:
                    checked = " checked='checked'"
                                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['encoded_id','checked'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 69
                __M_writer(u'\n                        <div class="form-row">\n                            <input type="checkbox" name="source_dataset_ids" id="dataset_')
                # SOURCE LINE 71
                __M_writer(unicode(encoded_id))
                __M_writer(u'" value="')
                __M_writer(unicode(encoded_id))
                __M_writer(u'"')
                __M_writer(unicode(checked))
                __M_writer(u'/>\n                            <label for="dataset_')
                # SOURCE LINE 72
                __M_writer(unicode(encoded_id))
                __M_writer(u'" style="display: inline;font-weight:normal;"> ')
                __M_writer(unicode(data.hid))
                __M_writer(u': ')
                __M_writer(unicode(h.to_unicode(data.name)))
                __M_writer(u'</label>\n                        </div>\n')
                pass
            # SOURCE LINE 75
        else:
            # SOURCE LINE 76
            __M_writer(u'                    <div class="form-row">This history has no datasets.</div>\n')
            pass
        # SOURCE LINE 78
        __M_writer(u'            </div>\n        </div>\n        <div style="float: left; padding-left: 10px; font-size: 36px;">&rarr;</div>\n        <div class="toolForm" style="float: right; width: 45%; padding: 0px;">\n            <div class="toolFormTitle">Destination History:</div>\n            <div class="toolFormBody">\n                <div class="form-row" id="single-destination">\n                    <select id="single-dest-select" name="target_history_id">\n                        <option value=""></option>\n')
        # SOURCE LINE 87
        for i, hist in enumerate(target_histories):
            # SOURCE LINE 88
            __M_writer(u'                            ')

            encoded_id = trans.security.encode_id(hist.id)
            source_history_text = ""
            selected = ""
            if hist == source_history:
                source_history_text = " (source history)"
            if encoded_id == target_history_id:
                selected = " selected='selected'"
                                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['selected','encoded_id','source_history_text'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 96
            __M_writer(u'\n                            <option value="')
            # SOURCE LINE 97
            __M_writer(unicode(encoded_id))
            __M_writer(u'"')
            __M_writer(unicode(selected))
            __M_writer(u'>')
            __M_writer(unicode(i + 1))
            __M_writer(u': ')
            __M_writer(unicode(h.truncate( util.unicodify( hist.name ), 30)))
            __M_writer(unicode(source_history_text))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 99
        __M_writer(u'                    </select><br /><br />\n                    <a style="margin-left: 10px;" href="javascript:void(0);" id="select-multiple">Choose multiple histories</a>\n                </div>\n                <div id="multiple-destination" style="display: none;">\n')
        # SOURCE LINE 103
        for i, hist in enumerate( target_histories ):
            # SOURCE LINE 104
            __M_writer(u'                        ')

            cur_history_text = ""
            encoded_id = trans.security.encode_id(hist.id)
            if hist == source_history:
                cur_history_text = " <strong>(source history)</strong>"
                                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['cur_history_text','encoded_id'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 109
            __M_writer(u'\n                        <div class="form-row">\n                            <input type="checkbox" name="target_history_ids" id="hist_')
            # SOURCE LINE 111
            __M_writer(unicode(encoded_id))
            __M_writer(u'" value="')
            __M_writer(unicode(encoded_id))
            __M_writer(u'"/>\n                            <label for="hist_')
            # SOURCE LINE 112
            __M_writer(unicode(encoded_id))
            __M_writer(u'" style="display: inline; font-weight:normal;">')
            __M_writer(unicode(i + 1))
            __M_writer(u': ')
            __M_writer(unicode( util.unicodify( hist.name ) ))
            __M_writer(unicode(cur_history_text))
            __M_writer(u'</label>\n                        </div>\n')
            pass
        # SOURCE LINE 115
        __M_writer(u'                </div>\n')
        # SOURCE LINE 116
        if trans.get_user():
            # SOURCE LINE 117
            __M_writer(u'                    ')

            checked = ""
            if "create_new_history" in target_history_ids:
                checked = " checked='checked'"
                                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['checked'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 121
            __M_writer(u'\n                    <hr />\n                    <div style="text-align: center; color: #888;">&mdash; OR &mdash;</div>\n                    <div class="form-row">\n                        <label for="new_history_name" style="display: inline; font-weight:normal;">New history named:</label>\n                        <input type="textbox" name="new_history_name" />\n                    </div>\n')
            pass
        # SOURCE LINE 129
        __M_writer(u'            </div>\n        </div>\n            <div style="clear: both"></div>\n            <div class="form-row" align="center">\n                <input type="submit" class="primary-button" name="do_copy" value="Copy History Items"/>\n            </div>\n        </form>\n    </div>\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x158c48d0')._populate(_import_ns, [u'handle_refresh_frames'])
        handle_refresh_frames = _import_ns.get('handle_refresh_frames', context.get('handle_refresh_frames', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n    ')
        # SOURCE LINE 10
        __M_writer(unicode(handle_refresh_frames))
        __M_writer(u'\n    \n    <script type="text/javascript">\n        $(function() {\n            $("#select-multiple").click(function() {\n                $("#single-dest-select").val("");\n                $("#single-destination").hide();\n                $("#multiple-destination").show();\n            });\n        });\n    </script>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x158c48d0')._populate(_import_ns, [u'handle_refresh_frames'])
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Copy History Items')
        return ''
    finally:
        context.caller_stack._pop_frame()


