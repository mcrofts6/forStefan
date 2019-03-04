# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550877240.1489487
_enable_loop = True
_template_filename = 'C:/Users/Madisyn Crofts/mysite/homepage/templates/index.html'
_template_uri = '/homepage/templates/index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'content', 'site_center', 'site_right']


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
        def site_center():
            return render_site_center(context._locals(__M_locals))
        now = context.get('now', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        now = context.get('now', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>Congratulations -- you\'ve successfully created a new django-mako-plus app!</h3>\r\n      <h4>Next Up: Go through the django-mako-plus tutorial and add Javascript, CSS, and urlparams to this page.</h4>\r\n      <p class="server-time">The current server time is ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( now ))
        __M_writer('.</p>\r\n      <button id="server-time-button">Refresh Server Time</button>\r\n      <p class="browser-time">The current browser time is .</p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<center>\r\nWelcome to our Website!  We specialize in python tips and tricks.  Hopefully you read latin ;)</center><br>\r\nLorem ipsum dolor, sit amet consectetur adipisicing elit. Expedita maxime, ex omnis incidunt fuga cumque. Consequatur aliquam aliquid vitae! Officiis omnis et laborum provident quidem autem molestiae delectus inventore molestias!\r\nLorem ipsum dolor sit amet consectetur adipisicing elit. Unde, temporibus? Corrupti at dolorem quam consequuntur voluptatum fuga debitis illum doloribus perferendis enim? Assumenda qui amet ducimus officia. Explicabo, quasi consectetur!\r\nLorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur natus, cumque quisquam ad quidem dolor sit hic possimus vitae minus sed vel facere autem ut aut explicabo atque ipsam? Harum.\r\nLorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, pariatur consectetur praesentium, cum qui fugiat perspiciatis deleniti, temporibus maxime fugit nihil delectus minus distinctio impedit incidunt sequi. Incidunt, debitis at!\r\nLorem ipsum dolor sit amet consectetur adipisicing elit. Similique sunt nostrum, neque mollitia vitae consectetur, officiis fuga adipisci laborum officia molestiae magnam enim culpa dignissimos magni excepturi laudantium deleniti harum?\r\nLorem ipsum dolor sit amet, consectetur adipisicing elit. Perspiciatis, deserunt! Dolores hic qui amet vitae voluptates cumque eos suscipit ratione consequatur recusandae natus dolorum officia, consequuntur harum? Sint, repellendus non.\r\nLorem ipsum, dolor sit amet consectetur adipisicing elit. Perferendis, a molestias, dolorem distinctio sed recusandae blanditiis beatae neque repellendus commodi, doloribus fuga at dicta error harum quo quis debitis dolorum.\r\nLorem ipsum dolor sit amet, consectetur adipisicing elit. Hic commodi ullam, quisquam sint doloremque laudantium aliquam provident. Exercitationem tenetur, blanditiis natus consectetur, non, consequatur rerum odit nesciunt enim quasi voluptatum?\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('Right side')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Madisyn Crofts/mysite/homepage/templates/index.html", "uri": "/homepage/templates/index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 3, "54": 13, "59": 27, "69": 3, "75": 3, "81": 5, "89": 5, "90": 9, "91": 9, "97": 16, "103": 16, "109": 29, "115": 29, "121": 115}}
__M_END_METADATA
"""
