# -*- coding: utf-8 -*-
__filename = 'manage_addPollMain_form'
__tokens = {}

from sys import exc_info as _exc_info

_static_4605077600 = {'type': 'submit', 'value': 'Add', }
_static_4605077376 = {'type': 'text', 'name': 'title', }
_static_4605076200 = {'type': 'text', 'name': 'id', }
_static_4603535488 = {'action': 'addPollMain', 'method': 'post', }
_static_4603194560 = {}
_static_4604891320 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<_ast.Dict object at 0x1127910b8> name=None at 112791240> -> __attrs_4604894120
            __attrs_4604894120 = _static_4604891320

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html')
            __append(' xmlns="http://www.w3.org/1999/xhtml"')
            __append('>')
            __append('\n  ')

            # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4603626160
            __attrs_4603626160 = _static_4603194560

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')
            __append('>')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4603745840
            __attrs_4603745840 = _static_4603194560

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2')
            __append('>')
            __append('Add POLL')
            __append('</h2>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x112646080> name=None at 112646278> -> __attrs_4604845808
            __attrs_4604845808 = _static_4603535488

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')
            __append(' action="addPollMain"')
            __append(' method="post"')
            __append('>')
            __append('\n      Id: ')

            # <Static value=<_ast.Dict object at 0x1127be2e8> name=None at 112785588> -> __attrs_4605076032
            __attrs_4605076032 = _static_4605076200

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')
            __append(' type="text"')
            __append(' name="id"')
            __append(' />')

            # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605076648
            __attrs_4605076648 = _static_4603194560

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br')
            __append(' />')
            __append('\n      Title: ')

            # <Static value=<_ast.Dict object at 0x1127be780> name=None at 1127be710> -> __attrs_4605078664
            __attrs_4605078664 = _static_4605077376

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')
            __append(' type="text"')
            __append(' name="title"')
            __append(' />')

            # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605079168
            __attrs_4605079168 = _static_4603194560

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br')
            __append(' />')
            __append('\n      ')

            # <Static value=<_ast.Dict object at 0x1127be860> name=None at 1127be898> -> __attrs_4605419872
            __attrs_4605419872 = _static_4605077600

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')
            __append(' type="submit"')
            __append(' value="Add"')
            __append(' />')
            __append('\n    ')
            __append('</form>')
            __append('\n  ')
            __append('</body>')
            __append('\n')
            __append('</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }