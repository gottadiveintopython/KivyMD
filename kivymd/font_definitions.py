"""
Font Definitions
================

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

`Material Design spec, The type system <https://material.io/design/typography/the-type-system.html>`_
"""

from kivy.core.text import LabelBase
from kivymd import fonts_path

fonts = [
    {
        "name": "DefaultJapaneseFont",
        "fn_regular": fonts_path + "yomogifont.otf",
    },
    {
        "name": "Icons",
        "fn_regular": fonts_path + "materialdesignicons-webfont.ttf",
    },
]

for font in fonts:
    LabelBase.register(**font)

theme_font_styles = [
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Subtitle1",
    "Subtitle2",
    "Body1",
    "Body2",
    "Button",
    "Caption",
    "Overline",
    "Icon",
]
