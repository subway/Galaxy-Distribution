# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1395666684.144276
_template_filename='templates/tool_shed_rating.mako'
_template_uri='tool_shed_rating.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        num_ratings = context.get('num_ratings', UNDEFINED)
        item_id = context.get('item_id', UNDEFINED)
        ave_item_rating = context.get('ave_item_rating', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        label = "ratings"
        if num_ratings == 1:
            label = "rating"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['label'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 5
        __M_writer(u'\n<div>\n    <input name="star1-')
        # SOURCE LINE 7
        __M_writer(unicode(item_id))
        __M_writer(u'" type="radio" class="community_rating_star star" disabled="disabled" value="1"\n')
        # SOURCE LINE 8
        if ave_item_rating > 0 and ave_item_rating <= 1.5:
            # SOURCE LINE 9
            __M_writer(u'        checked="checked"\n')
            pass
        # SOURCE LINE 11
        __M_writer(u'    \n    />\n    <input name="star1-')
        # SOURCE LINE 13
        __M_writer(unicode(item_id))
        __M_writer(u'" type="radio" class="community_rating_star star" disabled="disabled" value="2"\n')
        # SOURCE LINE 14
        if ave_item_rating > 1.5 and ave_item_rating <= 2.5:
            # SOURCE LINE 15
            __M_writer(u'        checked="checked"\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'    />\n    <input name="star1-')
        # SOURCE LINE 18
        __M_writer(unicode(item_id))
        __M_writer(u'" type="radio" class="community_rating_star star" disabled="disabled" value="3"\n')
        # SOURCE LINE 19
        if ave_item_rating > 2.5 and ave_item_rating <= 3.5:
            # SOURCE LINE 20
            __M_writer(u'        checked="checked"\n')
            pass
        # SOURCE LINE 22
        __M_writer(u'    />\n    <input name="star1-')
        # SOURCE LINE 23
        __M_writer(unicode(item_id))
        __M_writer(u'" type="radio" class="community_rating_star star" disabled="disabled" value="4"\n')
        # SOURCE LINE 24
        if ave_item_rating > 3.5 and ave_item_rating <= 4.5:
            # SOURCE LINE 25
            __M_writer(u'        checked="checked"\n')
            pass
        # SOURCE LINE 27
        __M_writer(u'    />\n    <input name="star1-')
        # SOURCE LINE 28
        __M_writer(unicode(item_id))
        __M_writer(u'" type="radio" class="community_rating_star star" disabled="disabled" value="5"\n')
        # SOURCE LINE 29
        if ave_item_rating > 4.5:
            # SOURCE LINE 30
            __M_writer(u'        checked="checked"\n')
            pass
        # SOURCE LINE 32
        __M_writer(u'    />\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


