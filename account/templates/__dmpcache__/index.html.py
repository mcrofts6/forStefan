# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550877770.8867464
_enable_loop = True
_template_filename = 'C:/Users/Madisyn Crofts/mysite/account/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['sit_center']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def sit_center():
            return render_sit_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sit_center'):
            context['self'].sit_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sit_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sit_center():
            return render_sit_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Congratulations -- you\'ve successfully logged out!</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Madisyn Crofts/mysite/account/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "41": 7, "47": 3, "53": 3, "59": 53}}
__M_END_METADATA
"""
