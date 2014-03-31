# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1395666515.746073
_template_filename='templates/webapps/galaxy/history/copy.mako'
_template_uri='/history/copy.mako'
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
        id_argument = context.get('id_argument', UNDEFINED)
        h = context.get('h', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n<div class="toolForm">\n  <div class="toolFormTitle">Copy History</div>\n    <div class="toolFormBody">\n        <form action="')
        # SOURCE LINE 8
        __M_writer(unicode(h.url_for( controller='history', action='copy' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n')
        # SOURCE LINE 10
        if id_argument is not None:
            # SOURCE LINE 11
            __M_writer(u'                  <input type="hidden" name="id" value="')
            __M_writer(unicode(id_argument))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 13
        __M_writer(u'                You can make a copy of the history that includes all datasets in the original history or just the active \n                (not deleted) datasets.\n            </div>\n            <div class="form-row">\n                <input type="radio" name="copy_choice" value="activatable"> Copy all datasets, including deleted ones\n            </div>\n            <div class="form-row">\n                <input type="radio" name="copy_choice" value="active"> Copy only active (not deleted) datasets\n            </div>\n            <div class="form-row">\n                <input type="submit" name="copy_choice_button" value="Copy">\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Copy History')
        return ''
    finally:
        context.caller_stack._pop_frame()


