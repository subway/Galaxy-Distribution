# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399385602.205022
_template_filename='templates/webapps/galaxy/dataset/embed.mako'
_template_uri='dataset/embed.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_item_links', 'render_summary_content']


# SOURCE LINE 2

from galaxy.web.framework.helpers import iff


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
    return runtime._inherit_from(context, u'/embed_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,dataset):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    <a href="')
        # SOURCE LINE 7
        __M_writer(unicode(h.url_for( controller='/dataset', action='display', dataset_id=trans.security.encode_id( dataset.id ), to_ext=dataset.ext )))
        __M_writer(u'" title="Save dataset" class="icon-button disk tooltip"></a>\n')
        # SOURCE LINE 9
        __M_writer(u'    <a href="')
        __M_writer(unicode(h.url_for( controller='/dataset', action='imp', dataset_id=trans.security.encode_id( item.id ) )))
        __M_writer(u'" title="Import dataset" class="icon-button import tooltip"></a>\n    <a class="icon-button go-to-full-screen tooltip" href="')
        # SOURCE LINE 10
        __M_writer(unicode(h.url_for( controller='/dataset', action='display_by_username_and_slug', username=dataset.history.user.username, slug=trans.security.encode_id( dataset.id ) )))
        __M_writer(u'" title="Go to dataset"></a>\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_summary_content(context,dataset,data):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


