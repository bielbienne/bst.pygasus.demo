from bb.extjs.core import ext

from js.extjs.theme import themes

from fanstatic import Library
from fanstatic import Resource


library = Library('demo', 'app')
styles = Resource(library, 'resources/css/styles.css')
clearButtonStyle = Resource(library, 'resources/css/ClearButton.css')
favicon = Resource(library, 'resources/images/phone.ico')

class DemoContext(ext.ApplicationContext):

    title = 'Demo'
    application = 'bb.extjs.demo.Application'
    namespace = 'bb.extjs.demo'
    resources = Resource(library, 'application.js',
                         depends=[ext.extjs_resources_skinless, themes['neptune'], styles, clearButtonStyle, favicon])

class ViewClassPathMapping(ext.ClassPathMapping):
    namespace='bb.extjs.demo.view'
    path='fanstatic/demo/view'


class ControllerClassPathMapping(ext.ClassPathMapping):
    namespace='bb.extjs.demo.controller'
    path='fanstatic/demo/controller'