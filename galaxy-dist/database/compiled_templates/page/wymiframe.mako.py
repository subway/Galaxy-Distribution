# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1399385555.009608
_template_filename='templates/webapps/galaxy/page/wymiframe.mako'
_template_uri='page/wymiframe.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<!--\n * WYMeditor : what you see is What You Mean web-based editor\n * Copyright (c) 2005 - 2009 Jean-Francois Hovinne, http://www.wymeditor.org/\n * Dual licensed under the MIT (MIT-license.txt)\n * and GPL (GPL-license.txt) licenses.\n *\n * For further information visit:\n *        http://www.wymeditor.org/\n *\n * File Name:\n *        wymiframe.html\n *        Iframe used by designMode.\n *        See the documentation for more info.\n *\n * File Authors:\n *        Jean-Francois Hovinne (jf.hovinne a-t wymeditor dotorg)\n-->\n<html>\n    <head>\n        <title>WYMeditor iframe</title>\n        <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />\n        <link rel="stylesheet" type="text/css" media="screen" href="/static/wymeditor/iframe/galaxy/wymiframe.css" />\n        ')
        # SOURCE LINE 24
        __M_writer(unicode(h.css("base", "autocomplete_tagging", "embed_item")))
        __M_writer(u'\n    </head>\n    <body class="wym_iframe text-content"></body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


