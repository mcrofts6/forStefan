# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549423012.1463206
_enable_loop = True
_template_filename = 'C:/Users/Madisyn Crofts/mysite/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'header', 'menu_items', 'site_left', 'site_center', 'site_right']


import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n')
        __M_writer('        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" />\r\n\r\n        <title>Sprint 1 &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n\r\n        <script src="django_mako_plus/dmp-common.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.2.1-dist/js/bootstrap.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.2.1-dist/css/bootstrap.css"></link>\r\n\r\n')
        __M_writer('        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n        <div class="alert alert-info" role="alert">\r\n            This site is currently under maintenance.\r\n        </div>\r\n        <header id="header">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n        </header>\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n        <footer class="center">\r\n            &copy Copyright: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.datetime.today().year ))
        __M_writer('\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="python" />\r\n                <div class="title">Welcome to <br/> DMP!</div> <br><br>\r\n')
        __M_writer('                <nav class="navbar navbar-expand-lg navbar-light bg-light">\r\n                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n                        <span class="navbar-toggler-icon"></span>\r\n                    </button>\r\n\r\n                    <div class="collapse navbar-collapse" id="navbarSupportedContent">\r\n                        <ul class="navbar-nav mr-auto">\r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\r\n                        </ul>\r\n                    </div>\r\n                </nav>\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n                                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('">\r\n                                    <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>\r\n                                </li>\r\n                                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('">\r\n                                    <a class="nav-link " href="#">About</a>\r\n                                </li>\r\n                                <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('">\r\n                                    <a class="nav-link " href="#">Contact</a>\r\n                                </li>\r\n                                <li class="nav-item dropdown">\r\n                                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                        User\r\n                                    </a>\r\n                                    <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\r\n                                        <a class="dropdown-item" href="#">Account</a>\r\n                                        <a class="dropdown-item" href="#">Log Out</a>\r\n                                    </div>\r\n                                </li>\r\n                            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Madisyn Crofts/mysite/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 0, "40": 2, "41": 9, "42": 9, "43": 9, "48": 11, "49": 14, "50": 14, "51": 14, "52": 19, "53": 19, "54": 19, "55": 20, "56": 20, "57": 23, "58": 23, "59": 23, "64": 65, "69": 71, "74": 75, "79": 79, "80": 84, "81": 84, "87": 11, "98": 31, "109": 31, "110": 32, "111": 32, "112": 35, "117": 61, "123": 42, "131": 42, "132": 43, "133": 43, "134": 46, "135": 46, "136": 49, "137": 49, "143": 69, "149": 69, "155": 74, "161": 74, "167": 78, "173": 78, "179": 173}}
__M_END_METADATA
"""
