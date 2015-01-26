# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399327083.137918
_template_filename='templates/webapps/galaxy/page/index.mako'
_template_uri='page/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['init', 'center_panel']


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
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        # SOURCE LINE 52
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="shared"
        self.message_box_visible=False
        
        
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        shared_by_others = context.get('shared_by_others', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        grid = context.get('grid', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n\n    <div style="overflow: auto; height: 100%;">\n        <div class="page-container" style="padding: 10px;">\n            ')
        # SOURCE LINE 16
        __M_writer(unicode(h.to_unicode( grid )))
        __M_writer(u'\n\n            <br><br>\n            <h2>Pages shared with you by others</h2>\n\n')
        # SOURCE LINE 21
        if shared_by_others:
            # SOURCE LINE 22
            __M_writer(u'                <table class="colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n                    <tr class="header">\n                        <th>Title</th>\n                        <th>Owner</th>\n                        <th></th>\n                    </tr>\n')
            # SOURCE LINE 28
            for i, association in enumerate( shared_by_others ):
                # SOURCE LINE 29
                __M_writer(u'                        ')
                page = association.page 
                
                __M_writer(u'\n                        <tr>\n                            <td>\n                                <a class="menubutton" id="shared-')
                # SOURCE LINE 32
                __M_writer(unicode(i))
                __M_writer(u'-popup" href="')
                __M_writer(unicode(h.url_for(controller='page', action='display_by_username_and_slug', username=page.user.username, slug=page.slug)))
                __M_writer(u'">')
                __M_writer(unicode(page.title))
                __M_writer(u'</a>\n                            </td>\n                            <td>')
                # SOURCE LINE 34
                __M_writer(unicode(page.user.username))
                __M_writer(u'</td>\n                            <td>\n                                <div popupmenu="shared-')
                # SOURCE LINE 36
                __M_writer(unicode(i))
                __M_writer(u'-popup">\n                                    <a class="action-button" href="')
                # SOURCE LINE 37
                __M_writer(unicode(h.url_for(controller='page', action='display_by_username_and_slug', username=page.user.username, slug=page.slug)))
                __M_writer(u'" target="_top">View</a>\n                                </div>\n                            </td>\n                        </tr>    \n')
                pass
            # SOURCE LINE 42
            __M_writer(u'                </table>\n')
            # SOURCE LINE 43
        else:
            # SOURCE LINE 44
            __M_writer(u'\n                No pages have been shared with you.\n\n')
            pass
        # SOURCE LINE 48
        __M_writer(u'\n        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


