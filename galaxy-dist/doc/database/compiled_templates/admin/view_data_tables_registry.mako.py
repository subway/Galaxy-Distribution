# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1389957390.761553
_template_filename='templates/admin/view_data_tables_registry.mako'
_template_uri='admin/view_data_tables_registry.mako'
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
    ns = runtime.TemplateNamespace('__anon_0x13b8ac50', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x13b8ac50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x13b8ac50')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
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

        ctr = 0
        sorted_data_tables = sorted( trans.app.tool_data_tables.get_tables().items() )
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sorted_data_tables','ctr'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 11
        __M_writer(u'\n\n<div class="toolForm">\n    <div class="toolFormTitle">Current data table registry contains ')
        # SOURCE LINE 14
        __M_writer(unicode(len( sorted_data_tables )))
        __M_writer(u' data tables</div>\n    <div class="toolFormBody">\n        <table class="manage-table colored" border="0" cellspacing="0" cellpadding="0" width="100%">\n            <tr>\n                <th bgcolor="#D8D8D8">Name</th>\n                <th bgcolor="#D8D8D8">Filename</th>\n                <th bgcolor="#D8D8D8">Tool data path</th>\n                <th bgcolor="#D8D8D8">Missing index file</th>\n            </tr>\n')
        # SOURCE LINE 23
        for data_table_elem_name, data_table in sorted_data_tables:
            # SOURCE LINE 24
            if ctr % 2 == 1:
                # SOURCE LINE 25
                __M_writer(u'                    <tr class="odd_row">\n')
                # SOURCE LINE 26
            else:
                # SOURCE LINE 27
                __M_writer(u'                    <tr class="tr">\n')
                pass
            # SOURCE LINE 29
            __M_writer(u'                    <td>')
            __M_writer(unicode(data_table.name))
            __M_writer(u'</td>\n')
            # SOURCE LINE 30
            for i, ( filename, file_dict ) in enumerate( data_table.filenames.iteritems() ):
                # SOURCE LINE 31
                if i > 0:
                    # SOURCE LINE 32
                    __M_writer(u'                            <tr><td></td>\n')
                    pass
                # SOURCE LINE 34
                __M_writer(u'                        <td>')
                __M_writer(filters.html_escape(unicode( filename )))
                __M_writer(u'</td>\n                        <td>')
                # SOURCE LINE 35
                __M_writer(filters.html_escape(unicode( file_dict.get( 'tool_data_path' ) )))
                __M_writer(u'</td>\n                        <td>\n')
                # SOURCE LINE 37
                if not file_dict.get( 'found' ):
                    # SOURCE LINE 38
                    __M_writer(u'                                missing\n')
                    pass
                # SOURCE LINE 40
                __M_writer(u'                        </td>\n                        </tr>\n')
                pass
            # SOURCE LINE 43
            __M_writer(u'                ')
            ctr += 1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ctr'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 45
        __M_writer(u'        </table>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


