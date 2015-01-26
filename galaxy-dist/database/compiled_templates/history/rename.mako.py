# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402887598.295486
_template_filename='templates/webapps/galaxy/history/rename.mako'
_template_uri='/history/rename.mako'
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
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        histories = context.get('histories', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n<div class="toolForm">\n  <div class="toolFormTitle">')
        # SOURCE LINE 5
        __M_writer(unicode(_('Rename')))
        __M_writer(u'</div>\n    <div class="toolFormBody">\n        <form action="')
        # SOURCE LINE 7
        __M_writer(unicode(h.url_for( controller='history', action='rename' )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n            <table>\n                <thead>\n                    <tr>\n                        <th>')
        # SOURCE LINE 12
        __M_writer(unicode(_('Current Name')))
        __M_writer(u'</th>\n                        <th>')
        # SOURCE LINE 13
        __M_writer(unicode(_('New Name')))
        __M_writer(u'</th>\n                    </tr>\n                </thead>\n                <tbody>\n')
        # SOURCE LINE 17
        for history in histories:
            # SOURCE LINE 18
            __M_writer(u'                    <tr>\n                        <td>\n                            <input type="hidden" name="id" value="')
            # SOURCE LINE 20
            __M_writer(unicode(trans.security.encode_id( history.id )))
            __M_writer(u'">\n                            ')
            # SOURCE LINE 21
            __M_writer(filters.html_escape(unicode(history.get_display_name() )))
            __M_writer(u'\n                        </td>\n                        <td>\n                            <input type="text" name="name" value="')
            # SOURCE LINE 24
            __M_writer(filters.html_escape(unicode(history.get_display_name() )))
            __M_writer(u'" size="40">\n                        </td>\n                    </tr>\n')
            pass
        # SOURCE LINE 28
        __M_writer(u'                </tbody>\n                <tr>\n                    <td colspan="2">\n                        <input type="submit" name="history_rename_btn" value="')
        # SOURCE LINE 31
        __M_writer(unicode(_('Rename Histories')))
        __M_writer(u'">\n                    </td>\n                </tr>\n            </table>\n            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(unicode(_('Rename History')))
        return ''
    finally:
        context.caller_stack._pop_frame()


