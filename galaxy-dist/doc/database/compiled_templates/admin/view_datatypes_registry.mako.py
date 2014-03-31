# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389957386.96649
_template_filename='templates/admin/view_datatypes_registry.mako'
_template_uri='admin/view_datatypes_registry.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x13ba1f50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x13ba1f50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x13ba1f50')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        if message:
            # SOURCE LINE 5
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8

        import galaxy.util
        from galaxy.web.base.controller import sort_by_attr, Datatype
        ctr = 0
        datatypes = []
        for elem in trans.app.datatypes_registry.datatype_elems:
            # Build a list of objects that can be sorted.
            extension = elem.get( 'extension', None )
            dtype = elem.get( 'type', None )
            type_extension = elem.get( 'type_extension', None )
            mimetype = elem.get( 'mimetype', None )
            display_in_upload = galaxy.util.string_as_bool( elem.get( 'display_in_upload', False ) )
            datatypes.append( Datatype( extension, dtype, type_extension, mimetype, display_in_upload ) )
        sorted_datatypes = sort_by_attr( datatypes, 'extension' )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['type_extension','mimetype','extension','ctr','Datatype','dtype','elem','display_in_upload','sorted_datatypes','sort_by_attr','datatypes','galaxy'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 22
        __M_writer(u'\n\n<div class="toolForm">\n    <div class="toolFormTitle">Current data types registry contains ')
        # SOURCE LINE 25
        __M_writer(unicode(len( sorted_datatypes )))
        __M_writer(u' data types</div>\n    <div class="toolFormBody">\n        <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n            <tr>\n                <th bgcolor="#D8D8D8">Extension</th>\n                <th bgcolor="#D8D8D8">Type</th>\n                <th bgcolor="#D8D8D8">Mimetype</th>\n                <th bgcolor="#D8D8D8">Display in upload</th>\n            </tr>\n')
        # SOURCE LINE 34
        for datatype in sorted_datatypes:
            # SOURCE LINE 35
            if ctr % 2 == 1:
                # SOURCE LINE 36
                __M_writer(u'                    <tr class="odd_row">\n')
                # SOURCE LINE 37
            else:
                # SOURCE LINE 38
                __M_writer(u'                    <tr class="tr">\n')
                pass
            # SOURCE LINE 40
            __M_writer(u'                    <td>')
            __M_writer(unicode(datatype.extension))
            __M_writer(u'</td>\n                    <td>')
            # SOURCE LINE 41
            __M_writer(unicode(datatype.dtype))
            __M_writer(u'</td>\n                    <td>\n')
            # SOURCE LINE 43
            if datatype.mimetype:
                # SOURCE LINE 44
                __M_writer(u'                            ')
                __M_writer(unicode(datatype.mimetype))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 46
            __M_writer(u'                    </td>\n                    <td>\n')
            # SOURCE LINE 48
            if datatype.display_in_upload:
                # SOURCE LINE 49
                __M_writer(u'                            ')
                __M_writer(unicode(datatype.display_in_upload))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 51
            __M_writer(u'                    </td>\n                </tr>\n                ')
            # SOURCE LINE 53
            ctr += 1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ctr'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 55
        __M_writer(u'        </table>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


