#!/usr/bin/env python3
from os import listdir
from importlib import import_module
from random import choice as rchoice
from main import logger
from plugins.helper.themes import ebiza_candy

AVL_THEMES = {"candy": ebiza_candy}
for theme in listdir('plugins/helper/themes'):
    if theme.startswith('ebiza_') and theme.endswith('.py'):
        AVL_THEMES[theme[5:-3]] = import_module(f'plugins.helper.themes.{theme[:-3]}')

def BotTheme(var_name, **format_vars):
    text = None
    theme_ = "candy"

    if theme_ in AVL_THEMES:
        text = getattr(AVL_THEMES[theme_].EBIZAStyle(), var_name, None)
        if text is None:
            logger.error(f"{var_name} not Found in {theme_}. Please recheck with Official Repo")
    elif theme_ == 'random':
        rantheme = rchoice(list(AVL_THEMES.values()))
        logger.info(f"Random Theme Chosen: {rantheme}")
        text = getattr(rantheme.EBIZAStyle(), var_name, None)
        
    if text is None:
        text = getattr(ebiza_candy.EBIZAStyle(), var_name)

    return text.format_map(format_vars)
