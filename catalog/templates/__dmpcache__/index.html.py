# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552515488.3223307
_enable_loop = True
_template_filename = 'C:/Users/Madisyn Crofts/mysite/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
        numpages = context.get('numpages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        page = context.get('page', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('                 \r\n            \r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        numpages = context.get('numpages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        page = context.get('page', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_center():
            return render_site_center(context)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1 class="text-center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Products' if category is None else category.name ))
        __M_writer('</h1>\r\n    <div id="catalog">\r\n')
        for product in products:
            __M_writer('            <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
            __M_writer('">\r\n            </span>\r\n')
        __M_writer('    </div>\r\n\r\n    <div id="paginator" class="text-right">\r\n')
        if page <= numpages:
            __M_writer('            <a class="btn btn-secondary" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 1 if page == 1 else page - 1 ))
            __M_writer('">Previous</a>\r\n')
        if page < 5:
            __M_writer('            <a class="btn btn-secondary" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 2 if page == 1  else page + 1  ))
            __M_writer('">Next</a>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Madisyn Crofts/mysite/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 20, "52": 3, "63": 3, "64": 4, "65": 4, "66": 6, "67": 7, "68": 7, "69": 7, "70": 10, "71": 13, "72": 14, "73": 14, "74": 14, "75": 14, "76": 14, "77": 16, "78": 17, "79": 17, "80": 17, "81": 17, "82": 17, "83": 19, "89": 83}}
__M_END_METADATA
"""
