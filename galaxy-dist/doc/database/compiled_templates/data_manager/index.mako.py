# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389957383.884296
_template_filename='templates/webapps/galaxy/data_manager/index.mako'
_template_uri='data_manager/index.mako'
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
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x13b8af10', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x13b8af10')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x13b8af10')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        data_managers = _import_ns.get('data_managers', context.get('data_managers', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        view_only = _import_ns.get('view_only', context.get('view_only', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        if message:
            # SOURCE LINE 7
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 9
        __M_writer(u'\n<h2>Data Manager</h2>\n\n')
        # SOURCE LINE 12
        if view_only:
            # SOURCE LINE 13
            __M_writer(u'    <p>Not implemented</p>\n')
            # SOURCE LINE 14
        else:
            # SOURCE LINE 15
            __M_writer(u'    <p>Choose your data managing option from below.</p>\n    <ul>\n        <li><strong>Access data managers</strong> - get data, build indexes, etc\n            <p/>\n            <ul>\n')
            # SOURCE LINE 20
            for data_manager_id, data_manager in data_managers.data_managers.iteritems():
                # SOURCE LINE 21
                __M_writer(u'                <li>\n                    <a href="')
                # SOURCE LINE 22
                __M_writer(unicode( h.url_for( 'tool_runner?tool_id=%s' % ( data_manager.tool.id ) ) ))
                __M_writer(u'"><strong>')
                __M_writer(filters.html_escape(unicode( data_manager.name )))
                __M_writer(u'</strong></a> - ')
                __M_writer(filters.html_escape(unicode( data_manager.description )))
                __M_writer(u'\n                </li>\n                <p/>\n')
                pass
            # SOURCE LINE 26
            __M_writer(u'            </ul>\n        </li>\n        <p/>\n        <li><strong>View managed data by manager</strong>\n            <p/>\n            <ul>\n')
            # SOURCE LINE 32
            for data_manager_id, data_manager in data_managers.data_managers.iteritems():
                # SOURCE LINE 33
                __M_writer(u'                    <li>\n                        <a href="')
                # SOURCE LINE 34
                __M_writer(unicode(h.url_for( controller='data_manager', action='manage_data_manager', id=data_manager_id)))
                __M_writer(u'" target="galaxy_main"><strong>')
                __M_writer(filters.html_escape(unicode( data_manager.name )))
                __M_writer(u'</strong></a> - ')
                __M_writer(filters.html_escape(unicode( data_manager.description )))
                __M_writer(u'</a>\n                    </li>\n                    <p/>\n')
                pass
            # SOURCE LINE 38
            __M_writer(u'            </ul>\n        </li>\n        <p/>\n        <p/>\n        <li><strong>View managed data by Tool Data Table</strong>\n            <p/>\n            <ul>\n')
            # SOURCE LINE 45
            for table_name, managers in data_managers.managed_data_tables.iteritems():
                # SOURCE LINE 46
                __M_writer(u'                    <li>\n                        <a href="')
                # SOURCE LINE 47
                __M_writer(unicode(h.url_for( controller='data_manager', action='manage_data_table', table_name=table_name)))
                __M_writer(u'" target="galaxy_main"><strong>')
                __M_writer(filters.html_escape(unicode( table_name )))
                __M_writer(u'</strong></a>\n                    </li>\n                    <p/>\n')
                pass
            # SOURCE LINE 51
            __M_writer(u'            </ul>\n        </li>\n        <p/>\n    </ul>\n    <p/>\n    <br/>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x13b8af10')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Data Manager')
        return ''
    finally:
        context.caller_stack._pop_frame()


