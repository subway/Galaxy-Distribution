# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1395877554.750184
_template_filename='templates/webapps/galaxy/user/manage_info.mako'
_template_uri='/webapps/galaxy/user/manage_info.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x17538ed0', context._clean_inheritance_tokens(), templateuri=u'/user/info.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x17538ed0')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x2b27b4367290', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2b27b4367290')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x17538ed0')._populate(_import_ns, [u'render_user_info'])
        _mako_get_namespace(context, '__anon_0x2b27b4367290')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        user_info_forms = _import_ns.get('user_info_forms', context.get('user_info_forms', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        addresses = _import_ns.get('addresses', context.get('addresses', UNDEFINED))
        user_type_form_definition = _import_ns.get('user_type_form_definition', context.get('user_type_form_definition', UNDEFINED))
        render_user_info = _import_ns.get('render_user_info', context.get('render_user_info', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        show_filter = _import_ns.get('show_filter', context.get('show_filter', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        widgets = _import_ns.get('widgets', context.get('widgets', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        user_type_fd_id_select_field = _import_ns.get('user_type_fd_id_select_field', context.get('user_type_fd_id_select_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        if message:
            # SOURCE LINE 6
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(unicode(render_user_info()))
        __M_writer(u'\n\n')
        # SOURCE LINE 11
        if user.values or user_info_forms:
            # SOURCE LINE 12
            __M_writer(u'    <p></p>\n    <div class="toolForm">\n        <form name="user_info" id="user_info" action="')
            # SOURCE LINE 14
            __M_writer(unicode(h.url_for( controller='user', action='edit_info', cntrller=cntrller, user_id=trans.security.encode_id( user.id ) )))
            __M_writer(u'" method="post" >\n            <div class="toolFormTitle">User information</div>\n')
            # SOURCE LINE 16
            if user_type_fd_id_select_field and len( user_type_fd_id_select_field.options ) > 1:
                # SOURCE LINE 17
                __M_writer(u'                <div class="form-row">\n                    <label>User type:</label>\n                    ')
                # SOURCE LINE 19
                __M_writer(unicode(user_type_fd_id_select_field.get_html()))
                __M_writer(u'\n                </div>\n')
                # SOURCE LINE 21
            else:
                # SOURCE LINE 22
                __M_writer(u'                <input type="hidden" name="user_type_fd_id" value="')
                __M_writer(unicode(trans.security.encode_id( user_type_form_definition.id )))
                __M_writer(u'"/>\n')
                pass
            # SOURCE LINE 24
            for field in widgets:
                # SOURCE LINE 25
                __M_writer(u'                <div class="form-row">\n                    <label>')
                # SOURCE LINE 26
                __M_writer(unicode(field['label']))
                __M_writer(u':</label>\n                    ')
                # SOURCE LINE 27
                __M_writer(unicode(field['widget'].get_html()))
                __M_writer(u'\n                    <div class="toolParamHelp" style="clear: both;">\n                        ')
                # SOURCE LINE 29
                __M_writer(unicode(field['helptext']))
                __M_writer(u'\n                    </div>\n                    <div style="clear: both"></div>\n                </div>\n')
                pass
            # SOURCE LINE 34
            __M_writer(u'            <div class="form-row">\n                <input type="submit" name="edit_user_info_button" value="Save"/>\n            </div>\n        </form>\n    </div>\n    <p></p>\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'\n<p/>\n\n<div class="toolForm">\n    <form name="user_addresses" id="user_addresses" action="')
        # SOURCE LINE 45
        __M_writer(unicode(h.url_for( controller='user', action='new_address', cntrller=cntrller, user_id=trans.security.encode_id( user.id ) )))
        __M_writer(u'" method="post" >\n        <div class="toolFormTitle">User Addresses</div>\n        <div class="toolFormBody">\n')
        # SOURCE LINE 48
        if user.addresses:
            # SOURCE LINE 49
            __M_writer(u'                <div class="form-row">\n                <div class="grid-header">\n')
            # SOURCE LINE 51
            for i, filter in enumerate( ['Active', 'Deleted', 'All'] ):
                # SOURCE LINE 52
                if i > 0:    
                    # SOURCE LINE 53
                    __M_writer(u'                            <span>|</span>\n')
                    pass
                # SOURCE LINE 55
                if show_filter == filter:
                    # SOURCE LINE 56
                    __M_writer(u'                            <span class="filter"><a href="')
                    __M_writer(unicode(h.url_for( controller='user', action='manage_user_info', cntrller=cntrller, show_filter=filter, user_id=trans.security.encode_id( user.id ) )))
                    __M_writer(u'"><b>')
                    __M_writer(unicode(filter))
                    __M_writer(u'</b></a></span>\n')
                    # SOURCE LINE 57
                else:
                    # SOURCE LINE 58
                    __M_writer(u'                            <span class="filter"><a href="')
                    __M_writer(unicode(h.url_for( controller='user', action='manage_user_info', cntrller=cntrller, show_filter=filter, user_id=trans.security.encode_id( user.id ) )))
                    __M_writer(u'">')
                    __M_writer(unicode(filter))
                    __M_writer(u'</a></span>\n')
                    pass
                pass
            # SOURCE LINE 61
            __M_writer(u'                </div>\n                </div>\n                <table class="grid">\n                    <tbody>\n')
            # SOURCE LINE 65
            for index, address in enumerate(addresses):    
                # SOURCE LINE 66
                __M_writer(u'                            <tr class="libraryRow libraryOrFolderRow" id="libraryRow">\n                                <td>\n                                    <div class="form-row">   \n                                        <label>')
                # SOURCE LINE 69
                __M_writer(unicode(address.desc))
                __M_writer(u':</label>\n                                        ')
                # SOURCE LINE 70
                __M_writer(unicode(address.get_html()))
                __M_writer(u'\n                                    </div>\n                                    <div class="form-row">\n                                        <ul class="manage-table-actions">\n                                            <li>\n')
                # SOURCE LINE 75
                if not address.deleted:
                    # SOURCE LINE 76
                    __M_writer(u'                                                    <a class="action-button"  href="')
                    __M_writer(unicode(h.url_for( controller='user', action='edit_address', cntrller=cntrller, address_id=trans.security.encode_id( address.id ), user_id=trans.security.encode_id( user.id ) )))
                    __M_writer(u'">Edit</a>\n                                                    <a class="action-button"  href="')
                    # SOURCE LINE 77
                    __M_writer(unicode(h.url_for( controller='user', action='delete_address', cntrller=cntrller, address_id=trans.security.encode_id( address.id ), user_id=trans.security.encode_id( user.id ) )))
                    __M_writer(u'">Delete</a>\n')
                    # SOURCE LINE 78
                else:
                    # SOURCE LINE 79
                    __M_writer(u'                                                    <a class="action-button"  href="')
                    __M_writer(unicode(h.url_for( controller='user', action='undelete_address', cntrller=cntrller, address_id=trans.security.encode_id( address.id ), user_id=trans.security.encode_id( user.id ) )))
                    __M_writer(u'">Undelete</a>\n')
                    pass
                # SOURCE LINE 81
                __M_writer(u'                                            </li>\n                                        </ul>\n                                    </div>\n                                </td>\n                             </tr>             \n')
                pass
            # SOURCE LINE 87
            __M_writer(u'                    </tbody>\n                </table>\n')
            pass
        # SOURCE LINE 90
        __M_writer(u'            <div class="form-row">\n                <input type="submit" value="Add a new address">\n            </div>\n        </div>\n    </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


