import anywidget
import traitlets

from custom_widget_test123.config import JS_PATH, CSS_PATH

class CustomWidget(anywidget.AnyWidget):
    _esm = JS_PATH
    _css = CSS_PATH
    value = traitlets.Int(0).tag(sync=True)

