"""
Themes/Font definitions
=======================

.. seealso::

   `Material Design spec, The type system <https://material.io/design/typography/the-type-system.html>`_
"""
from functools import partial
from kivy.core.text import LabelBase
from kivy.metrics import sp

from kivymd import fonts_path

from kivy_garden.i18n.fontfinder import enum_pre_installed_fonts, can_render_lang

is_traditional_chinese = partial(can_render_lang, lang="zh_Hant")
fonts = [
    {
        "name": "zh_Hant",
        "fn_regular": str(next(filter(is_traditional_chinese, enum_pre_installed_fonts()))),
    },
    {
        "name": "Icons",
        "fn_regular": fonts_path + "materialdesignicons-webfont.ttf",
    },
]

for font in fonts:
    LabelBase.register(**font)

# TODO: Add `weight` properties.
theme_font_styles = {
    "Icon": {
        "large": {
            "line-height": 1,
            "font-name": "Icons",
            "font-size": sp(24),
        },
    },
    "Display": {
        "large": {
            "line-height": 1.64,
            "font-name": "zh_Hant",
            "font-size": sp(57),
        },
        "medium": {
            "line-height": 1.52,
            "font-name": "zh_Hant",
            "font-size": sp(45),
        },
        "small": {
            "line-height": 1.44,
            "font-name": "zh_Hant",
            "font-size": sp(36),
        },
    },
    "Headline": {
        "large": {
            "line-height": 1.40,
            "font-name": "zh_Hant",
            "font-size": sp(32),
        },
        "medium": {
            "line-height": 1.36,
            "font-name": "zh_Hant",
            "font-size": sp(28),
        },
        "small": {
            "line-height": 1.32,
            "font-name": "zh_Hant",
            "font-size": sp(24),
        },
    },
    "Title": {
        "large": {
            "line-height": 1.28,
            "font-name": "zh_Hant",
            "font-size": sp(22),
        },
        "medium": {
            "line-height": 1.24,
            "font-name": "zh_Hant",
            "font-size": sp(16),
        },
        "small": {
            "line-height": 1.20,
            "font-name": "zh_Hant",
            "font-size": sp(14),
        },
    },
    "Body": {
        "large": {
            "line-height": 1.24,
            "font-name": "zh_Hant",
            "font-size": sp(16),
        },
        "medium": {
            "line-height": 1.20,
            "font-name": "zh_Hant",
            "font-size": sp(14),
        },
        "small": {
            "line-height": 1.16,
            "font-name": "zh_Hant",
            "font-size": sp(12),
        },
    },
    "Label": {
        "large": {
            "line-height": 1.20,
            "font-name": "zh_Hant",
            "font-size": sp(14),
        },
        "medium": {
            "line-height": 1.16,
            "font-name": "zh_Hant",
            "font-size": sp(12),
        },
        "small": {
            "line-height": 1.16,
            "font-name": "zh_Hant",
            "font-size": sp(11),
        },
    },
}
"""
.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label-font-style-preview.png
    :align: center
"""
