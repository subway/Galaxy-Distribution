# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1384451543.685127
_template_filename='templates/webapps/galaxy/library/index.mako'
_template_uri='/library/index.mako'
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
        # SOURCE LINE 9
        __M_writer(u'\n\n')
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
        
        
        # SOURCE LINE 8
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        default_action = context.get('default_action', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n\n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 100%; height: 100%;" src="')
        # SOURCE LINE 13
        __M_writer(unicode(h.url_for( controller="library", action="browse_libraries", default_action=default_action )))
        __M_writer(u'"> </iframe>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


