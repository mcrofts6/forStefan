# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552494961.3434362
_enable_loop = True
_template_filename = 'C:/Users/Madisyn Crofts/mysite/catalog/templates/base.htm'
_template_uri = '/catalog/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_left']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <ul class="ul">\r\n            <li>\r\n                <a class="white" href="/catalog/index/1">Piano</a>\r\n            </li>\r\n            <li>\r\n                <a class="white" href="/catalog/index/2">Guitar</a>\r\n            </li>\r\n            <li>\r\n                <a class="white" href="/catalog/index/3">Bagpipes</a>\r\n            </li>\r\n            <li>\r\n                <a class="white" href="/catalog/index">All Products</a>\r\n            </li>\r\n        </ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Madisyn Crofts/mysite/catalog/templates/base.htm", "uri": "/catalog/templates/base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 2, "41": 22, "47": 5, "53": 5, "59": 53}}
__M_END_METADATA
"""
