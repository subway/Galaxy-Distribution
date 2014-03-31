# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1393458778.424883
_template_filename='templates/webapps/galaxy/requests/common/find_samples.mako'
_template_uri='/requests/common/find_samples.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x1a92c4d0', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1a92c4d0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1a92c4d0')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        request_states = _import_ns.get('request_states', context.get('request_states', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        search_box = _import_ns.get('search_box', context.get('search_box', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        results = _import_ns.get('results', context.get('results', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        search_type = _import_ns.get('search_type', context.get('search_type', UNDEFINED))
        samples = _import_ns.get('samples', context.get('samples', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        is_admin = cntrller == 'requests_admin' and trans.user_is_admin() 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_admin'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<br/>\n<br/>\n<ul class="manage-table-actions">\n    <li>\n        <a class="action-button"  href="')
        # SOURCE LINE 20
        __M_writer(unicode(h.url_for( controller=cntrller, action='browse_requests' )))
        __M_writer(u'">Browse requests</a>\n    </li>\n</ul>\n\n')
        # SOURCE LINE 24
        if message:
            # SOURCE LINE 25
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 27
        __M_writer(u'\n<div class="toolForm">\n    <div class="toolFormTitle">Find samples</div>\n    <div class="toolFormBody">\n        <form name="find_request" id="find_request" action="')
        # SOURCE LINE 31
        __M_writer(unicode(h.url_for( controller='requests_common', action='find_samples', cntrller=cntrller )))
        __M_writer(u'" method="post" >\n            <div class="form-row">\n                <label>Find samples using:</label>\n                ')
        # SOURCE LINE 34
        __M_writer(unicode(search_type.get_html()))
        __M_writer(u'\n                <div class="toolParamHelp" style="clear: both;">\n                    Select a sample attribute for searching.  To search <br/>\n                    for a sample with a dataset name, select the dataset <br/>\n                    option above. This will return all the samples that <br/>\n                    are associated with a dataset with that name. <br/> \n                </div>\n            </div>\n            <div class="form-row">\n                <label>Show only sequencing requests in state:</label>\n                ')
        # SOURCE LINE 44
        __M_writer(unicode(request_states.get_html()))
        __M_writer(u'\n            </div>\n            <div class="form-row">\n                ')
        # SOURCE LINE 47
        __M_writer(unicode(search_box.get_html()))
        __M_writer(u'\n                <input type="submit" name="find_samples_button" value="Find"/>  \n                <div class="toolParamHelp" style="clear: both;">\n                   <p>\n                   Wildcard search (%) can be used as placeholder for any sequence of characters or words.<br/> \n                   For example, to search for samples starting with \'mysample\' use \'mysample%\' as the search string.\n                   </p>\n                   <p>\n                   When \'form value\' search type is selected, then enter the search string in \'field label=value\' format.\n                   <br/>For example, when searching for all samples whose \'Volume\' field is 1.3mL, then the search string\n                   should be \'Volume=1.3mL\' (without qoutes).\n                   </p>\n                </div>\n            </div>\n')
        # SOURCE LINE 61
        if results:
            # SOURCE LINE 62
            __M_writer(u'                <div class="form-row">\n                    <label><i>')
            # SOURCE LINE 63
            __M_writer(unicode(results))
            __M_writer(u'</i></label>\n')
            # SOURCE LINE 64
            if samples:
                # SOURCE LINE 65
                __M_writer(u'                        <div class="toolParamHelp" style="clear: both;">\n                           The search results are sorted by the date the samples where created. \n                        </div>\n')
                pass
            # SOURCE LINE 69
            __M_writer(u'                </div>\n')
            pass
        # SOURCE LINE 71
        __M_writer(u'            <div class="form-row">\n')
        # SOURCE LINE 72
        if samples:
            # SOURCE LINE 73
            for sample in samples:
                # SOURCE LINE 74
                __M_writer(u'                        <div class="form-row">\n                            Sample: <b>')
                # SOURCE LINE 75
                __M_writer(unicode(sample.name))
                __M_writer(u'</b> | Barcode: ')
                __M_writer(unicode(sample.bar_code))
                __M_writer(u'<br/>\n')
                # SOURCE LINE 76
                if sample.request.is_new or not sample.state:
                    # SOURCE LINE 77
                    __M_writer(u'                                State: Unsubmitted<br/>\n')
                    # SOURCE LINE 78
                else:
                    # SOURCE LINE 79
                    __M_writer(u'                                State: ')
                    __M_writer(unicode(sample.state.name))
                    __M_writer(u'<br/>\n')
                    pass
                # SOURCE LINE 81
                __M_writer(u'                            ')

                                # Get an external_service from one of the sample datasets.  This assumes all sample datasets are associated with
                                # the same external service - hopefully this is a good assumption.
                external_service = sample.datasets[0].external_service
                                            
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['external_service'] if __M_key in __M_locals_builtin_stored]))
                # SOURCE LINE 85
                __M_writer(u'\n                            Datasets: <a href="')
                # SOURCE LINE 86
                __M_writer(unicode(h.url_for( controller='requests_common', action='view_sample_datasets', cntrller=cntrller, external_service_id=trans.security.encode_id( external_service.id ), sample_id=trans.security.encode_id( sample.id ) )))
                __M_writer(u'">')
                __M_writer(unicode(len( sample.datasets )))
                __M_writer(u'</a><br/>\n')
                # SOURCE LINE 87
                if is_admin:
                    # SOURCE LINE 88
                    __M_writer(u'                               <i>User: ')
                    __M_writer(unicode(sample.request.user.email))
                    __M_writer(u'</i>\n')
                    pass
                # SOURCE LINE 90
                __M_writer(u'                            <div class="toolParamHelp" style="clear: both;">\n                                <a href="')
                # SOURCE LINE 91
                __M_writer(unicode(h.url_for( controller='requests_common', action='view_request', cntrller=cntrller, id=trans.security.encode_id( sample.request.id ) )))
                __M_writer(u'">Sequencing request: ')
                __M_writer(unicode(sample.request.name))
                __M_writer(u' | Type: ')
                __M_writer(unicode(sample.request.type.name))
                __M_writer(u' | State: ')
                __M_writer(unicode(sample.request.state))
                __M_writer(u'</a>\n                            </div>\n                        </div>\n                        <br/>\n')
                pass
            pass
        # SOURCE LINE 97
        __M_writer(u'            </div>\n        </form>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1a92c4d0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n    ')
        # SOURCE LINE 10
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(h.css( "autocomplete_tagging" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1a92c4d0')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n   ')
        # SOURCE LINE 5
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n   ')
        # SOURCE LINE 6
        __M_writer(unicode(h.js("libs/jquery/jquery.autocomplete", "galaxy.autocom_tagging" )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


