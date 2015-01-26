# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399385602.137405
_template_filename=u'templates/embed_base.mako'
_template_uri=u'/embed_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_summary_content', 'render_item_links', 'render_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 6
    ns = runtime.TemplateNamespace('__anon_0x2b80e42b6c50', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b80e42b6c50')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b80e42b6c50')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        item_data = _import_ns.get('item_data', context.get('item_data', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u"<div class='embedded-item display ")
        __M_writer(unicode(get_class_display_name( item.__class__ ).lower()))
        __M_writer(u"'>\n    <div class='title'>\n        ")
        # SOURCE LINE 11
        __M_writer(unicode(self.render_title( item )))
        __M_writer(u"\n    </div>\n    <div class='summary-content'>\n        ")
        # SOURCE LINE 14
        __M_writer(unicode(self.render_summary_content( item, item_data )))
        __M_writer(u"\n    </div>\n    <div class='expanded-content'>\n        <hr/>\n        <div class='item-content'></div>\n    </div>\n</div>\n\n")
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 60
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_summary_content(context,item,item_data):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b80e42b6c50')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 63
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b80e42b6c50')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        get_item_user = _import_ns.get('get_item_user', context.get('get_item_user', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        get_item_slug = _import_ns.get('get_item_slug', context.get('get_item_slug', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer(u'\n    ')
        # SOURCE LINE 24

        item_display_name = get_class_display_name( item.__class__ ).lower()
        item_controller = "/%s" % get_controller_name( item )
        item_user = get_item_user( item )
        item_slug = get_item_slug( item )
        display_href = h.url_for( controller=item_controller, action='display_by_username_and_slug', username=item_user.username, slug=item_slug )
            
        
        # SOURCE LINE 30
        __M_writer(u'\n    \n')
        # SOURCE LINE 33
        __M_writer(u'    <a href="')
        __M_writer(unicode(h.url_for( controller=item_controller, action='imp', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'" title="Import ')
        __M_writer(unicode(item_display_name))
        __M_writer(u'" class="icon-button import"></a>\n    <a class="icon-button go-to-full-screen" href="')
        # SOURCE LINE 34
        __M_writer(unicode(display_href))
        __M_writer(u'" title="Go to ')
        __M_writer(unicode(item_display_name))
        __M_writer(u'"></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_title(context,item):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2b80e42b6c50')._populate(_import_ns, [u'*'])
        get_item_user = _import_ns.get('get_item_user', context.get('get_item_user', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        get_item_slug = _import_ns.get('get_item_slug', context.get('get_item_slug', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n    ')
        # SOURCE LINE 38

        item_display_name = get_class_display_name( item.__class__ ).lower()
        item_controller = "/%s" % get_controller_name( item )
        item_user = get_item_user( item )
        item_slug = get_item_slug( item )
        display_href = h.url_for( controller=item_controller, action='display_by_username_and_slug', username=item_user.username, slug=item_slug )
            
        
        # SOURCE LINE 44
        __M_writer(u'\n    <div style="float: left">\n        <a class="display_in_embed icon-button toggle-expand" item_id="')
        # SOURCE LINE 46
        __M_writer(unicode(trans.security.encode_id( item.id )))
        __M_writer(u'" item_class="$item.__class__.__name__" href="')
        __M_writer(unicode(display_href))
        __M_writer(u'"\n            title="Show ')
        # SOURCE LINE 47
        __M_writer(unicode(item_display_name))
        __M_writer(u' content"></a>\n        <a class="toggle icon-button" href="')
        # SOURCE LINE 48
        __M_writer(unicode(display_href))
        __M_writer(u'" title="Hide ')
        __M_writer(unicode(item_display_name))
        __M_writer(u' content"></a>\n    </div>\n    <div style="float: right;">\n        ')
        # SOURCE LINE 51
        __M_writer(unicode(self.render_item_links( item )))
        __M_writer(u'\n    </div>\n    <h4><a class="toggle-embed" href="')
        # SOURCE LINE 53
        __M_writer(unicode(display_href))
        __M_writer(u'" title="Show or hide ')
        __M_writer(unicode(item_display_name))
        __M_writer(u' content">Galaxy ')
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u' | ')
        __M_writer(unicode(get_item_name( item )))
        __M_writer(u'</a></h4>\n')
        # SOURCE LINE 54
        if hasattr( item, "annotation") and item.annotation:
            # SOURCE LINE 55
            __M_writer(u'        <div class="annotation">')
            __M_writer(unicode(item.annotation))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 57
        __M_writer(u'    \n')
        # SOURCE LINE 59
        __M_writer(u'    <input type="hidden" name="ajax-item-content-url" value="')
        __M_writer(unicode(h.url_for( controller=item_controller, action='get_item_content_async', id=trans.security.encode_id( item.id ) )))
        __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


