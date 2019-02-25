# -*- coding: utf-8 -*-
__filename = 'index_html'
__tokens = {}

from sys import exc_info as _exc_info

_static_4501478592 = {}

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x10c4f1cc0> name=None at 10c4f1f60> -> __attrs_4503365728
            __attrs_4503365728 = _static_4501478592

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html')
            __append('>')
            __append('\n')

            # <Static value=<_ast.Dict object at 0x10c4f1cc0> name=None at 10c4f1f60> -> __attrs_4503366456
            __attrs_4503366456 = _static_4501478592

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head')
            __append('>')
            __append('\n  ')

            # <Static value=<_ast.Dict object at 0x10c4f1cc0> name=None at 10c4f1f60> -> __attrs_4503367240
            __attrs_4503367240 = _static_4501478592

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title')
            __append('>')
            __append('Welcome to POLL!')
            __append('</title>')
            __append('\n')
            __append('</head>')
            __append('\n')

            # <Static value=<_ast.Dict object at 0x10c4f1cc0> name=None at 10c4f1f60> -> __attrs_4503413032
            __attrs_4503413032 = _static_4501478592

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')
            __append('>')
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x10c4f1cc0> name=None at 10c4f1f60> -> __attrs_4503413760
            __attrs_4503413760 = _static_4501478592

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2')
            __append('>')
            __append('Welcome to POLL!')
            __append('</h2>')
            __append('\n\n')
            __append('</body>')
            __append('\n')
            __append('</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }