# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552489001.9484901
_enable_loop = True
_template_filename = 'C:/Users/Madisyn Crofts/mysite/catalog/templates/product.html'
_template_uri = 'product.html'
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
    return runtime._inherit_from(context, '/catalog/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1 class="text-center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Product' if product is None else product.name ))
        __M_writer('</h1>\r\n    <div id="catalog">\r\n            <span class="product-tile, text-center" >\r\n                <div><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.image_url() ))
        __M_writer('" /></div>\r\n                <div>Name: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        __M_writer('</div>\r\n                <div>Description: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.description ))
        __M_writer('</div>\r\n                <div>Price: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.price ))
        __M_writer('</div>\r\n                <div>Quantity: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.quantity ))
        __M_writer('</div>\r\n                <div>Reorder Trigger: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.reorder_trigger ))
        __M_writer('</div>\r\n                <div>Reorder Quantity: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.reorder_quantity ))
        __M_writer('</div>\r\n            </span>\r\n    </div>\r\n    <div>\r\n')
        for url in product.images_urls():
            __M_writer('            <a><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( url ))
            __M_writer('" class="img-thumbnail, thumbnail"/></a><br><br>\r\n')
        __M_writer('    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Madisyn Crofts/mysite/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 4, "58": 4, "59": 7, "60": 7, "61": 8, "62": 8, "63": 9, "64": 9, "65": 10, "66": 10, "67": 11, "68": 11, "69": 12, "70": 12, "71": 13, "72": 13, "73": 17, "74": 18, "75": 18, "76": 18, "77": 20, "83": 77}}
__M_END_METADATA
"""
