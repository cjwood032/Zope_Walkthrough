# -*- coding: utf-8 -*-
__filename = '/index_html'
__tokens = {56: ('template/title', 4, 24), 170: ('context/title_or_id', 9, 27), 247: ('template/title', 10, 29), 290: ('template/title', 11, 27), 386: ('template/id', 13, 43)}

from Products.PageTemplates.expression import BoboAwareZopeTraverse as _BoboAwareZopeTraverse
from sys import exc_info as _exc_info

_static_4555803000 = {'charset': 'utf-8', }
_static_4553452624 = _BoboAwareZopeTraverse()
_static_4553449880 = {}

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
            __append('<!DOCTYPE html>')
            __append('\n')

            # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4554168976
            __attrs_4554168976 = _static_4553449880

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html')
            __append('>')
            __append('\n  ')

            # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4554169872
            __attrs_4554169872 = _static_4553449880

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4555802776
            __attrs_4555802776 = _static_4553449880

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title')
            __append('>')
            __default_4555803672 = '__default'

            # <Value 'template/title' (4:24)> -> __cache_4554299320
            __token = 56
            __cache_4554299320 = _static_4553452624(getitem('template'), econtext, True, ('title', ))

            # <Identity expression=<Value 'template/title' (4:24)> value=<_ast.Str object at 0x10f6fe390> at 10f6fedd8> -> __condition
            __expression = __cache_4554299320
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                __append('The title')
            else:
                __content = __cache_4554299320
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</title>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x10f8c0978> name=None at 10f8c0748> -> __attrs_4555800760
            __attrs_4555800760 = _static_4555803000

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta')
            __append(' charset="utf-8"')
            __append(' />')
            __append('\n  ')
            __append('</head>')
            __append('\n  ')

            # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4555801208
            __attrs_4555801208 = _static_4553449880

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')
            __append('>')
            __append('\n    \n    ')

            # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4555803504
            __attrs_4555803504 = _static_4553449880

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2')
            __append('>')
            __default_4553905768 = '__default'

            # <Value 'context/title_or_id' (9:27)> -> __cache_4553905824
            __token = 170
            __cache_4553905824 = _static_4553452624(getitem('context'), econtext, True, ('title_or_id', ))

            # <Identity expression=<Value 'context/title_or_id' (9:27)> value=<_ast.Str object at 0x10f6f1390> at 10f6f1f98> -> __condition
            __expression = __cache_4553905824
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:

                # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4555804232
                __attrs_4555804232 = _static_4553449880

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span')
                __append('>')
                __append('content title or id')
                __append('</span>')
            else:
                __content = __cache_4553905824
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Value 'template/title' (10:29)> -> __condition
            __token = 247
            __condition = _static_4553452624(getitem('template'), econtext, True, ('title', ))
            if __condition:
                __default_4553907616 = '__default'

                # <Value 'template/title' (11:27)> -> __cache_4553906272
                __token = 290
                __cache_4553906272 = _static_4553452624(getitem('template'), econtext, True, ('title', ))

                # <Identity expression=<Value 'template/title' (11:27)> value=<_ast.Str object at 0x10f6f19e8> at 10f6f19b0> -> __condition
                __expression = __cache_4553906272
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:

                    # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4553906104
                    __attrs_4553906104 = _static_4553449880

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')
                    __append('>')
                    __append('optional template title')
                    __append('</span>')
                else:
                    __content = __cache_4553906272
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append('</h2>')
            __append('\n\n    This is Page Template ')

            # <Static value=<_ast.Dict object at 0x10f682198> name=None at 10f6824e0> -> __attrs_4556084056
            __attrs_4556084056 = _static_4553449880

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em')
            __append('>')
            __default_4553907168 = '__default'

            # <Value 'template/id' (13:43)> -> __cache_4553907840
            __token = 386
            __cache_4553907840 = _static_4553452624(getitem('template'), econtext, True, ('id', ))

            # <Identity expression=<Value 'template/id' (13:43)> value=<_ast.Str object at 0x10f6f1978> at 10f6f1b70> -> __condition
            __expression = __cache_4553907840
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                __append('template id')
            else:
                __content = __cache_4553907840
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</em>')
            __append('.\n  ')
            __append('</body>')
            __append('\n')
            __append('</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }