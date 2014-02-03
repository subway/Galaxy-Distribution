# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389704087.422702
_template_filename='templates/webapps/galaxy/history/options.mako'
_template_uri='/history/options.mako'
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
        len = context.get('len', UNDEFINED)
        user = context.get('user', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        history = context.get('history', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n    \n<h2>')
        # SOURCE LINE 5
        __M_writer(unicode(_('History Options')))
        __M_writer(u'</h2>\n\n')
        # SOURCE LINE 7
        if not user:
            # SOURCE LINE 8
            __M_writer(u'<div class="infomessage">\n    <div>')
            # SOURCE LINE 9
            __M_writer(unicode(_('You must be ')))
            __M_writer(u'<a target="galaxy_main" href="')
            __M_writer(unicode(h.url_for( controller='user', action='login' )))
            __M_writer(u'">')
            __M_writer(unicode(_('logged in')))
            __M_writer(u'</a>')
            __M_writer(unicode(_(' to store or switch histories.')))
            __M_writer(u'</div>\n</div>\n')
            pass
        # SOURCE LINE 12
        __M_writer(u'\n<ul>\n')
        # SOURCE LINE 14
        if user:
            # SOURCE LINE 15
            __M_writer(u'        <li><a href="')
            __M_writer(unicode(h.url_for( controller='history', action='list')))
            __M_writer(u'" target="galaxy_main">Previously</a> stored histories</li>\n')
            # SOURCE LINE 16
            if len( history.active_datasets ) > 0:
                # SOURCE LINE 17
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(h.url_for( controller='root', action='history_new' )))
                __M_writer(u'">Create</a> a new empty history</li>\n            <li><a href="')
                # SOURCE LINE 18
                __M_writer(unicode(h.url_for( controller='workflow', action='build_from_current_history' )))
                __M_writer(u'">Construct workflow</a> from current history</li>\n            <li><a href="')
                # SOURCE LINE 19
                __M_writer(unicode(h.url_for( controller='history', action='copy', id=trans.security.encode_id( history.id ) )))
                __M_writer(u'">Copy</a> current history</li>\n')
                pass
            # SOURCE LINE 21
            __M_writer(u'        <li><a href="')
            __M_writer(unicode(h.url_for( controller='history', action='share' )))
            __M_writer(u'" target="galaxy_main">Share</a> current history</div>\n        <li><a href="')
            # SOURCE LINE 22
            __M_writer(unicode(h.url_for( controller='root', action='history_set_default_permissions' )))
            __M_writer(u'">Change default permissions</a> for current history</li>\n')
            pass
        # SOURCE LINE 24
        if len( history.activatable_datasets ) > 0:
            # SOURCE LINE 25
            __M_writer(u'        <li><a href="')
            __M_writer(unicode(h.url_for( controller='root', action='history', show_deleted=True)))
            __M_writer(u'" target="galaxy_history">Show deleted</a> datasets in current history</li>\n')
            pass
        # SOURCE LINE 27
        __M_writer(u'    <li><a href="')
        __M_writer(unicode(h.url_for( controller='history', action='rename', id=trans.security.encode_id( history.id ) )))
        __M_writer(u'" target="galaxy_main">Rename</a> current history (stored as "')
        __M_writer(unicode(history.name))
        __M_writer(u'")</li>\n    <li><a href="')
        # SOURCE LINE 28
        __M_writer(unicode(h.url_for( controller='history', action='delete_current' )))
        __M_writer(u'" confirm="Are you sure you want to delete the current history?">Delete</a> current history</div>\n')
        # SOURCE LINE 29
        if user and user.histories_shared_by_others:
            # SOURCE LINE 30
            __M_writer(u'        <li><a href="')
            __M_writer(unicode(h.url_for( controller='history', action='list_shared')))
            __M_writer(u'" target="galaxy_main">Histories</a> shared with you by others</li>\n')
            pass
        # SOURCE LINE 32
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'History options')
        return ''
    finally:
        context.caller_stack._pop_frame()


