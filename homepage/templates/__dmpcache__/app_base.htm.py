# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549420766.615816
_enable_loop = True
_template_filename = 'C:/Users/Madisyn Crofts/mysite/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['menu_items', 'site_left']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('">\r\n        <a class="nav-link" href="/homepage/index">Home <span class="sr-only">(current)</span></a>\r\n    </li>\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('">\r\n        <a class="nav-link " href="#">About</a>\r\n    </li>\r\n    <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('">\r\n        <a class="nav-link " href="/homepage/contact">Contact</a>\r\n    </li>\r\n    <li class="nav-item dropdown">\r\n        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n            User\r\n        </a>\r\n        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\r\n            <a class="dropdown-item" href="#">Account</a>\r\n            <a class="dropdown-item" href="#">Log Out</a>\r\n        </div>\r\n    </li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <ul>\r\n            <li>\r\n                <a class="white" href="/homepage/index">Home</a>\r\n            </li>\r\n            <li>\r\n                <a class="white" href="/homepage/contact">Contact</a>\r\n            </li>\r\n        </ul>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Madisyn Crofts/mysite/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 22, "50": 35, "56": 3, "64": 3, "65": 4, "66": 4, "67": 7, "68": 7, "69": 10, "70": 10, "76": 24, "82": 24, "88": 82}}
__M_END_METADATA
"""
