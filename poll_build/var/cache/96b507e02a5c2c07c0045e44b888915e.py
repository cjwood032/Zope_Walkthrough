# -*- coding: utf-8 -*-
__filename = 'manage_main'
__tokens = {31: ('here/manage_page_header', 1, 31), 89: ('here/manage_tabs', 3, 29), 229: ("python:getattr(here.aq_explicit, 'has_order_support', 0)", 8, 38), 309: (' modules/AccessControl/SecurityManagement/getSecurityManage', 9, 22), 402: ("t python: 'position' if has_order_support else 'i", 10, 31), 477: ("ey python:request.get('skey',default_so", 11, 22), 542: ("key python:request.get('rkey','a", 12, 21), 604: ("_alt python:'desc' if rkey=='asc' else ", 13, 24), 668: ('  obs python: here.manage_get_sortedObjects(sortkey = skey, revkey =', 14, 18), 796: ('string:${request/URL1}/', 16, 31), 805: ('request/URL1', 16, 40), 853: ('obs', 18, 30), 948: ('obs', 19, 89), 1011: ("python:'thead-light sorted_%s'%(request.get('rkey',''))", 20, 57), 1441: ("python:'Sort %s by Meta-Type'%( rkey_alt.upper() )", 28, 39), 1530: (" python:'?skey=meta_type&rkey=%s'%( rkey_alt ", 29, 37), 1615: ("s python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or No", 30, 37), 1985: ("python:'Sort %s by Name'%( rkey_alt.upper() )", 38, 39), 2069: (" python:'?skey=id&rkey=%s'%( rkey_alt ", 39, 37), 2147: ("s python:request.get('skey',None)=='id' and 'zmi-sort_key' or No", 40, 37), 2826: ("python:'Sort %s by File-Size'%( rkey_alt.upper() )", 51, 39), 2915: (" python:'?skey=get_size&rkey=%s'%( rkey_alt ", 52, 37), 2999: ("s python:request.get('skey',None)=='get_size' and 'zmi-sort_key' or No", 53, 37), 3431: ("python:'Sort %s by Modification Date'%( rkey_alt.upper() )", 62, 39), 3528: (" python:'?skey=_p_mtime&rkey=%s'%( rkey_alt ", 63, 37), 3612: ("s python:request.get('skey',None)=='_p_mtime' and 'zmi-sort_key' or No", 64, 37), 3914: ('obs', 73, 34), 3952: ('nocall:ob_dict/obj', 74, 32), 4186: ('ob_dict/id', 76, 104), 4530: (' ob/meta_type | defaul', 79, 122), 4502: ('ob/zmi_icon | default', 79, 94), 4609: ('ob/meta_type | default', 80, 53), 4776: ("python:'%s/manage_workspace'%(ob_dict['quoted_id'])", 84, 40), 4867: ('ob_dict/id', 85, 37), 5000: ('ob/wl_isLocked | nothing', 86, 111), 5174: ('ob/title|nothing', 89, 74), 5239: ('ob/title', 90, 46), 5401: ('python:here.compute_size(ob)', 94, 76), 5533: ('python:here.last_modified(ob)', 96, 81), 5734: ("python:sm.checkPermission('Delete objects', context)", 104, 21), 5803: ('obs', 104, 90), 5844: ('not:context/dontAllowCopyAndPaste|nothing', 105, 35), 5848: ('context/dontAllowCopyAndPaste|nothing', 105, 39), 6107: ('delete_allowed', 107, 114), 6348: ('here/cb_dataValid', 109, 118), 6511: ('delete_allowed', 111, 115), 6658: ("python:sm.checkPermission('Import/Export objects', context)", 112, 128), 6835: ("python: has_order_support and sm.checkPermission('Manage properties', context)", 115, 64), 7387: ('python:range(1,min(5,len(obs)))', 122, 38), 7433: ('val', 122, 84), 7479: ('python:range(5,len(obs),5)', 123, 38), 7520: ('val', 123, 79), 7960: ('not:obs', 132, 26), 7964: ('obs', 132, 30), 8074: ('here/title_or_id', 134, 57), 8178: ('not:context/dontAllowCopyAndPaste|nothing', 137, 35), 8182: ('context/dontAllowCopyAndPaste|nothing', 137, 39), 8340: ('here/cb_dataValid', 138, 118), 8516: ("python:sm.checkPermission('Import/Export objects', context)", 140, 128), 11448: ('here/manage_page_footer', 237, 31)}

from Products.PageTemplates.expression import BoboAwareZopeTraverse as _BoboAwareZopeTraverse
from sys import exc_info as _exc_info
from AccessControl.ZopeGuards import guarded_getitem as _guarded_getitem
from zope.location.interfaces import LocationError as _LocationError
from zExceptions.unauthorized import Unauthorized as _Unauthorized
from zExceptions import NotFound as _NotFound
from AccessControl.cAccessControl import guarded_getattr as _guarded_getattr

_static_4605802648 = {'class': 'zmi-typename_show', }
_static_4605800520 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_4605786432 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_4605784304 = {'class': 'form-group', }
_static_4605777792 = {'class': 'alert alert-info mt-4 mb-4', }
_static_4605758936 = {'type': 'submit', 'name': 'manage_move_objects_to_bottom:method', 'value': 'Move to bottom', 'class': 'btn btn-primary', 'title': 'Move selected items to bottom', }
_static_4605756584 = {'type': 'submit', 'name': 'manage_move_objects_to_top:method', 'value': 'Move to top', 'class': 'btn btn-primary', 'title': 'Move selected items to top', }
_static_4605744352 = {'class': 'form-control', 'name': 'delta:int', }
_static_4605730768 = {'class': 'col-xs-2', }
_static_4605727968 = {'type': 'submit', 'name': 'manage_move_objects_down:method', 'value': 'Move down', 'title': 'Move selected items down', 'class': 'btn btn-primary', }
_static_4605720728 = {'type': 'submit', 'name': 'manage_move_objects_up:method', 'value': 'Move up', 'title': 'Move selected items up', 'class': 'btn btn-primary', }
_static_4605719104 = {'class': 'form-group row zmi-controls', }
_static_4605705576 = {'class': 'container-fluid', }
_static_4605703672 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_4605693288 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_delObjects:method', 'value': 'Delete', }
_static_4605691496 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_4605681168 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_copyObjects:method', 'value': 'Copy', }
_static_4605678984 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_cutObjects:method', 'value': 'Cut', }
_static_4605672752 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_renameForm:method', 'value': 'Rename', }
_static_4605598016 = {'class': 'form-group zmi-controls', }
_static_4605669504 = {'class': 'text-right zmi-object-date hidden-xs pl-3', }
_static_4605655472 = {'class': 'text-right zmi-object-size hidden-xs', }
_static_4605065032 = {'class': 'zmi-object-title hidden-xs', }
_static_4603626160 = {'class': 'fa fa-lock', }
_static_4605644696 = {'class': 'badge badge-warning', 'title': 'This item has been locked by WebDAV', }
_static_4605642008 = {'href': "python:'%s/manage_workspace'%(ob_dict['quoted_id'])", }
_static_4605640888 = {'class': 'zmi-object-id', }
_static_4605623264 = {'class': 'sr-only', }
_static_4605620744 = {'title': 'Broken object', 'class': 'fas fa-ban text-danger', }
_static_4605607048 = {'class': 'zmi-object-type', 'onclick': "$(this).prev().children('input').trigger('click')", }
_static_4605604864 = {'type': 'checkbox', 'class': 'checkbox-list-item', 'name': 'ids:list', 'onclick': "event.stopPropagation();$(this).parent().parent().toggleClass('checked');", 'value': 'ob_dict/id', }
_static_4605599024 = {'class': 'zmi-object-check text-right', 'onclick': "$(this).children('input').trigger('click');", }
_static_4605583144 = {'class': 'fa fa-sort', }
_static_4605581016 = {'title': 'Sort Ascending by Modification Date', 'href': '?skey=_p_mtime&rkey=asc', 'class': "python:request.get('skey',None)=='_p_mtime' and 'zmi-sort_key' or None", }
_static_4605579504 = {'scope': 'col', 'class': 'zmi-object-date text-right hidden-xs', }
_static_4605565976 = {'class': 'fa fa-sort', }
_static_4605563792 = {'title': 'Sort Ascending by File-Size', 'href': '?skey=get_size&rkey=asc', 'class': "python:request.get('skey',None)=='get_size' and 'zmi-sort_key' or None", }
_static_4605562160 = {'scope': 'col', 'class': 'zmi-object-size text-right hidden-xs', }
_static_4605560256 = {'id': 'tablefilter', 'name': 'obj_ids:tokens', 'type': 'text', 'title': 'Filter object list by entering a name. Pressing the Enter key starts recursive search.', }
_static_4604984680 = {'class': 'fa fa-search tablefilter', 'onclick': "$('#tablefilter').focus()", }
_static_4604983280 = {'class': 'fa fa-sort', }
_static_4605066880 = {'title': 'Sort Ascending by Name', 'href': '?skey=id&rkey=asc', 'class': "python:request.get('skey',None)=='id' and 'zmi-sort_key' or None", }
_static_4605065088 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_4605029400 = {'class': 'fa fa-sort', }
_static_4605028056 = {'title': 'Sort Ascending by Meta-Type', 'href': '?skey=meta_type&rkey=asc', 'class': "python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None", }
_static_4605026824 = {'scope': 'col', 'class': 'zmi-object-type', }
_static_4605022560 = {'type': 'checkbox', 'id': 'checkAll', 'onclick': 'checkbox_all();', }
_static_4605024408 = {'scope': 'col', 'class': 'zmi-object-check text-right', }
_static_4603194560 = {}
_static_4604990520 = {'class': 'thead-light', }
_static_4604989680 = {'class': 'table table-striped table-hover table-sm objectItems', }
_static_4604931320 = {'name': 'objectItems', 'method': 'post', 'action': 'string:${request/URL1}/', }
_static_4604928744 = {'class': 'container-fluid', }
_static_4603321424 = _BoboAwareZopeTraverse()

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
            __default_4604928296 = '__default'

            # <Value 'here/manage_page_header' (1:31)> -> __cache_4604878744
            __token = 31
            __cache_4604878744 = _static_4603321424(getitem('here'), econtext, True, ('manage_page_header', ))

            # <Identity expression=<Value 'here/manage_page_header' (1:31)> value=<_ast.Str object at 0x11278dfd0> at 11278df28> -> __condition
            __expression = __cache_4604878744
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4604878744
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')
            __default_4604929304 = '__default'

            # <Value 'here/manage_tabs' (3:29)> -> __cache_4604928800
            __token = 89
            __cache_4604928800 = _static_4603321424(getitem('here'), econtext, True, ('manage_tabs', ))

            # <Identity expression=<Value 'here/manage_tabs' (3:29)> value=<_ast.Str object at 0x11279a3c8> at 11279a240> -> __condition
            __expression = __cache_4604928800
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4604928800
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x11279a2e8> name=None at 11279a0b8> -> __attrs_4604930648
            __attrs_4604930648 = _static_4604928744

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main')
            __append(' class="container-fluid"')
            __append('>')
            __append('\n  ')
            __backup_has_order_support_4604878128 = get('has_order_support', __marker)

            # <Value "python:getattr(here.aq_explicit, 'has_order_support', 0)" (8:38)> -> __value
            __token = 229
            __value = get('getattr', getattr)(_guarded_getattr(getitem('here'), 'aq_explicit'), 'has_order_support', 0)
            econtext['has_order_support'] = __value
            __backup_sm_4604877904 = get('sm', __marker)

            # <Value 'modules/AccessControl/SecurityManagement/getSecurityManager' (9:22)> -> __value
            __token = 309
            __value = _static_4603321424(get('modules', modules), econtext, True, ('AccessControl', 'SecurityManagement', 'getSecurityManager', ))
            econtext['sm'] = __value
            __backup_default_sort_4604878408 = get('default_sort', __marker)

            # <Value "python: 'position' if has_order_support else 'id'" (10:31)> -> __value
            __token = 402
            __value = ('position' if getitem('has_order_support') else 'id')
            econtext['default_sort'] = __value
            __backup_skey_4604892384 = get('skey', __marker)

            # <Value "python:request.get('skey',default_sort)" (11:22)> -> __value
            __token = 477
            __value = _guarded_getattr(getitem('request'), 'get')('skey', getitem('default_sort'))
            econtext['skey'] = __value
            __backup_rkey_4604892160 = get('rkey', __marker)

            # <Value "python:request.get('rkey','asc')" (12:21)> -> __value
            __token = 542
            __value = _guarded_getattr(getitem('request'), 'get')('rkey', 'asc')
            econtext['rkey'] = __value
            __backup_rkey_alt_4604892552 = get('rkey_alt', __marker)

            # <Value "python:'desc' if rkey=='asc' else 'asc'" (13:24)> -> __value
            __token = 604
            __value = ('desc' if (getitem('rkey') == 'asc') else 'asc')
            econtext['rkey_alt'] = __value
            __backup_obs_4604891992 = get('obs', __marker)

            # <Value 'python: here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)' (14:18)> -> __value
            __token = 668
            __value = _guarded_getattr(getitem('here'), 'manage_get_sortedObjects')(sortkey=getitem('skey'), revkey=getitem('rkey'))
            econtext['obs'] = __value

            # <Static value=<_ast.Dict object at 0x11279acf8> name=None at 11279add8> -> __attrs_4604892104
            __attrs_4604892104 = _static_4604931320

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')
            __append(' name="objectItems"')
            __append(' method="post"')
            __default_4604891432 = '__default__'

            # <Substitution 'string:${request/URL1}/' (16:31)> -> __attr_action
            __token = 796
            __token = 805
            __attr_action = _static_4603321424(getitem('request'), econtext, True, ('URL1', ))
            if (__attr_action is None):
                pass
            else:
                if (__attr_action is '__default__'):
                    __attr_action = None
                else:
                    __tt = type(__attr_action)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_action = str(__attr_action)
                    else:
                        if (__tt is bytes):
                            __attr_action = decode(__attr_action)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_action = __attr_action.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_action)
                                    __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                else:
                                    __attr_action = __attr_action()
            __attr_action = ('%s%s' % ((__attr_action if (__attr_action is not None) else ''), '/', ))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, '__default__')
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>')
            __append('\n\n    ')

            # <Value 'obs' (18:30)> -> __condition
            __token = 853
            __condition = _static_4603321424(getitem('obs'), econtext, True, ())
            if __condition:
                __append('\n      ')

                # <Value 'obs' (19:89)> -> __condition
                __token = 948
                __condition = _static_4603321424(getitem('obs'), econtext, True, ())
                if __condition:

                    # <Static value=<_ast.Dict object at 0x1127a90f0> name=None at 1127a9048> -> __attrs_4604992312
                    __attrs_4604992312 = _static_4604989680

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table')
                    __append(' class="table table-striped table-hover table-sm objectItems"')
                    __append('>')
                    __append('\n        ')

                    # <Static value=<_ast.Dict object at 0x1127a9438> name=None at 1127a9358> -> __attrs_4604993264
                    __attrs_4604993264 = _static_4604990520

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead')
                    __default_4604992760 = 'thead-light'

                    # <Substitution "python:'thead-light sorted_%s'%(request.get('rkey',''))" (20:57)> -> __attr_class
                    __token = 1011
                    __attr_class = ('thead-light sorted_%s' % _guarded_getattr(getitem('request'), 'get')('rkey', ''))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'thead-light', '__default__')
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605024632
                    __attrs_4605024632 = _static_4603194560

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr')
                    __append('>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x1127b1898> name=None at 1127b18d0> -> __attrs_4605022728
                    __attrs_4605022728 = _static_4605024408

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th')
                    __append(' scope="col"')
                    __append(' class="zmi-object-check text-right"')
                    __append('>')
                    __append('\n              ')

                    # <Static value=<_ast.Dict object at 0x1127b1160> name=None at 1127b1358> -> __attrs_4605025304
                    __attrs_4605025304 = _static_4605022560

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input')
                    __append(' type="checkbox"')
                    __append(' id="checkAll"')
                    __append(' onclick="checkbox_all();"')
                    __append(' />')
                    __append('\n            ')
                    __append('</th>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x1127b2208> name=None at 1127b2198> -> __attrs_4605028336
                    __attrs_4605028336 = _static_4605026824

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th')
                    __append(' scope="col"')
                    __append(' class="zmi-object-type"')
                    __append('>')
                    __append('\n              ')

                    # <Static value=<_ast.Dict object at 0x1127b26d8> name=None at 1127b29b0> -> __attrs_4605029904
                    __attrs_4605029904 = _static_4605028056

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')
                    __default_4605028952 = 'Sort Ascending by Meta-Type'

                    # <Substitution "python:'Sort %s by Meta-Type'%( rkey_alt.upper() )" (28:39)> -> __attr_title
                    __token = 1441
                    __attr_title = ('Sort %s by Meta-Type' % _guarded_getattr(getitem('rkey_alt'), 'upper')())
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Meta-Type', '__default__')
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __default_4605029288 = '?skey=meta_type&rkey=asc'

                    # <Substitution "python:'?skey=meta_type&rkey=%s'%( rkey_alt )" (29:37)> -> __attr_href
                    __token = 1530
                    __attr_href = ('?skey=meta_type&rkey=%s' % getitem('rkey_alt'))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=meta_type&rkey=asc', '__default__')
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __default_4605029736 = '__default__'

                    # <Substitution "python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None" (30:37)> -> __attr_class
                    __token = 1615
                    __attr_class = (((_guarded_getattr(getitem('request'), 'get')('skey', None) == 'meta_type') and 'zmi-sort_key') or None)
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, '__default__')
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x1127b2c18> name=None at 1127b2f60> -> __attrs_4605064640
                    __attrs_4605064640 = _static_4605029400

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i')
                    __append(' class="fa fa-sort"')
                    __append('>')
                    __append('</i>')
                    __append('\n              ')
                    __append('</a>')
                    __append('\n            ')
                    __append('</th>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x1127bb780> name=None at 1127bb860> -> __attrs_4605067160
                    __attrs_4605067160 = _static_4605065088

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th')
                    __append(' scope="col"')
                    __append(' class="zmi-object-id"')
                    __append('>')
                    __append('\n              ')

                    # <Static value=<_ast.Dict object at 0x1127bbe80> name=None at 1127bbef0> -> __attrs_4604982552
                    __attrs_4604982552 = _static_4605066880

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')
                    __default_4604981824 = 'Sort Ascending by Name'

                    # <Substitution "python:'Sort %s by Name'%( rkey_alt.upper() )" (38:39)> -> __attr_title
                    __token = 1985
                    __attr_title = ('Sort %s by Name' % _guarded_getattr(getitem('rkey_alt'), 'upper')())
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Name', '__default__')
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __default_4604982104 = '?skey=id&rkey=asc'

                    # <Substitution "python:'?skey=id&rkey=%s'%( rkey_alt )" (39:37)> -> __attr_href
                    __token = 2069
                    __attr_href = ('?skey=id&rkey=%s' % getitem('rkey_alt'))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=id&rkey=asc', '__default__')
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __default_4604982384 = '__default__'

                    # <Substitution "python:request.get('skey',None)=='id' and 'zmi-sort_key' or None" (40:37)> -> __attr_class
                    __token = 2147
                    __attr_class = (((_guarded_getattr(getitem('request'), 'get')('skey', None) == 'id') and 'zmi-sort_key') or None)
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, '__default__')
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>')
                    __append('\n                Name\n                ')

                    # <Static value=<_ast.Dict object at 0x1127a77f0> name=None at 1127a7588> -> __attrs_4604984792
                    __attrs_4604984792 = _static_4604983280

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i')
                    __append(' class="fa fa-sort"')
                    __append('>')
                    __append('</i>')
                    __append('\n              ')
                    __append('</a>')
                    __append('\n              ')

                    # <Static value=<_ast.Dict object at 0x1127a7d68> name=None at 1127a7e10> -> __attrs_4605559696
                    __attrs_4605559696 = _static_4604984680

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i')
                    __append(' class="fa fa-search tablefilter"')
                    __append(' onclick="$(\'#tablefilter\').focus()"')
                    __append('>')
                    __append('</i>')
                    __append('\n              ')

                    # <Static value=<_ast.Dict object at 0x1128345c0> name=None at 112834588> -> __attrs_4605561712
                    __attrs_4605561712 = _static_4605560256

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input')
                    __append(' id="tablefilter"')
                    __append(' name="obj_ids:tokens"')
                    __append(' type="text"')
                    __append(' title="Filter object list by entering a name. Pressing the Enter key starts recursive search."')
                    __append(' />')
                    __append('\n            ')
                    __append('</th>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x112834d30> name=None at 112834cf8> -> __attrs_4605563288
                    __attrs_4605563288 = _static_4605562160

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th')
                    __append(' scope="col"')
                    __append(' class="zmi-object-size text-right hidden-xs"')
                    __append('>')
                    __append('\n              ')

                    # <Static value=<_ast.Dict object at 0x112835390> name=None at 1128352b0> -> __attrs_4605565584
                    __attrs_4605565584 = _static_4605563792

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')
                    __default_4605564576 = 'Sort Ascending by File-Size'

                    # <Substitution "python:'Sort %s by File-Size'%( rkey_alt.upper() )" (51:39)> -> __attr_title
                    __token = 2826
                    __attr_title = ('Sort %s by File-Size' % _guarded_getattr(getitem('rkey_alt'), 'upper')())
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by File-Size', '__default__')
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __default_4605564856 = '?skey=get_size&rkey=asc'

                    # <Substitution "python:'?skey=get_size&rkey=%s'%( rkey_alt )" (52:37)> -> __attr_href
                    __token = 2915
                    __attr_href = ('?skey=get_size&rkey=%s' % getitem('rkey_alt'))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=get_size&rkey=asc', '__default__')
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __default_4605565080 = '__default__'

                    # <Substitution "python:request.get('skey',None)=='get_size' and 'zmi-sort_key' or None" (53:37)> -> __attr_class
                    __token = 2999
                    __attr_class = (((_guarded_getattr(getitem('request'), 'get')('skey', None) == 'get_size') and 'zmi-sort_key') or None)
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, '__default__')
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>')
                    __append('\n                Size\n                ')

                    # <Static value=<_ast.Dict object at 0x112835c18> name=None at 112835be0> -> __attrs_4605566760
                    __attrs_4605566760 = _static_4605565976

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i')
                    __append(' class="fa fa-sort"')
                    __append('>')
                    __append('</i>')
                    __append('\n              ')
                    __append('</a>')
                    __append('\n            ')
                    __append('</th>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x1128390f0> name=None at 1128390b8> -> __attrs_4605580568
                    __attrs_4605580568 = _static_4605579504

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th')
                    __append(' scope="col"')
                    __append(' class="zmi-object-date text-right hidden-xs"')
                    __append('>')
                    __append('\n              ')

                    # <Static value=<_ast.Dict object at 0x1128396d8> name=None at 112839630> -> __attrs_4605582752
                    __attrs_4605582752 = _static_4605581016

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')
                    __default_4605581744 = 'Sort Ascending by Modification Date'

                    # <Substitution "python:'Sort %s by Modification Date'%( rkey_alt.upper() )" (62:39)> -> __attr_title
                    __token = 3431
                    __attr_title = ('Sort %s by Modification Date' % _guarded_getattr(getitem('rkey_alt'), 'upper')())
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Modification Date', '__default__')
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __default_4605582024 = '?skey=_p_mtime&rkey=asc'

                    # <Substitution "python:'?skey=_p_mtime&rkey=%s'%( rkey_alt )" (63:37)> -> __attr_href
                    __token = 3528
                    __attr_href = ('?skey=_p_mtime&rkey=%s' % getitem('rkey_alt'))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=_p_mtime&rkey=asc', '__default__')
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __default_4605582248 = '__default__'

                    # <Substitution "python:request.get('skey',None)=='_p_mtime' and 'zmi-sort_key' or None" (64:37)> -> __attr_class
                    __token = 3612
                    __attr_class = (((_guarded_getattr(getitem('request'), 'get')('skey', None) == '_p_mtime') and 'zmi-sort_key') or None)
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, '__default__')
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>')
                    __append('\n                Last Modified\n                ')

                    # <Static value=<_ast.Dict object at 0x112839f28> name=None at 112839ef0> -> __attrs_4605596280
                    __attrs_4605596280 = _static_4605583144

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i')
                    __append(' class="fa fa-sort"')
                    __append('>')
                    __append('</i>')
                    __append('\n              ')
                    __append('</a>')
                    __append('\n            ')
                    __append('</th>')
                    __append('\n          ')
                    __append('</tr>')
                    __append('\n        ')
                    __append('</thead>')
                    __append('\n        ')

                    # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605596896
                    __attrs_4605596896 = _static_4603194560

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody')
                    __append('>')
                    __append('\n          ')
                    __backup_ob_dict_4604894344 = get('ob_dict', __marker)

                    # <Value 'obs' (73:34)> -> __iterator
                    __token = 3914
                    __iterator = _static_4603321424(getitem('obs'), econtext, True, ())
                    (__iterator, ____index_4605597904, ) = getitem('repeat')('ob_dict', __iterator)
                    econtext['ob_dict'] = None
                    for __item in __iterator:
                        econtext['ob_dict'] = __item

                        # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605597624
                        __attrs_4605597624 = _static_4603194560

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr')
                        __append('>')
                        __append('\n            ')
                        __backup_ob_4604990408 = get('ob', __marker)

                        # <Value 'nocall:ob_dict/obj' (74:32)> -> __value
                        __token = 3952
                        __value = _static_4603321424(getitem('ob_dict'), econtext, False, ('obj', ))
                        econtext['ob'] = __value
                        __append('\n              ')

                        # <Static value=<_ast.Dict object at 0x11283dd30> name=None at 11283dc88> -> __attrs_4605604248
                        __attrs_4605604248 = _static_4605599024

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td')
                        __append(' class="zmi-object-check text-right"')
                        __append(' onclick="$(this).children(\'input\').trigger(\'click\');"')
                        __append('>')
                        __append('\n                ')

                        # <Static value=<_ast.Dict object at 0x11283f400> name=None at 11283f2b0> -> __attrs_4605606656
                        __attrs_4605606656 = _static_4605604864

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')
                        __append(' type="checkbox"')
                        __append(' class="checkbox-list-item"')
                        __append(' name="ids:list"')
                        __append(' onclick="event.stopPropagation();$(this).parent().parent().toggleClass(\'checked\');"')
                        __default_4605606320 = '__default__'

                        # <Substitution 'ob_dict/id' (76:104)> -> __attr_value
                        __token = 4186
                        __attr_value = _static_4603321424(getitem('ob_dict'), econtext, True, ('id', ))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, '__default__')
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />')
                        __append('\n              ')
                        __append('</td>')
                        __append('\n              ')

                        # <Static value=<_ast.Dict object at 0x11283fc88> name=None at 11283fc50> -> __attrs_4605620464
                        __attrs_4605620464 = _static_4605607048

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td')
                        __append(' class="zmi-object-type"')
                        __append(' onclick="$(this).prev().children(\'input\').trigger(\'click\')"')
                        __append('>')
                        __append('\n                ')

                        # <Static value=<_ast.Dict object at 0x112843208> name=None at 112843240> -> __attrs_4605622312
                        __attrs_4605622312 = _static_4605620744

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i')
                        __default_4605621472 = 'Broken object'

                        # <Substitution 'ob/meta_type | default' (79:122)> -> __attr_title
                        __token = 4530
                        try:
                            __attr_title = _static_4603321424(getitem('ob'), econtext, True, ('meta_type', ))
                        except (AttributeError, LookupError, NameError, TypeError, ValueError, _NotFound, _Unauthorized, _LocationError, ):
                            __attr_title = _static_4603321424(__default_4605621472, econtext, True, ())

                        __attr_title = __quote(__attr_title, '"', '&quot;', 'Broken object', '__default__')
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __default_4605621808 = 'fas fa-ban text-danger'

                        # <Substitution 'ob/zmi_icon | default' (79:94)> -> __attr_class
                        __token = 4502
                        try:
                            __attr_class = _static_4603321424(getitem('ob'), econtext, True, ('zmi_icon', ))
                        except (AttributeError, LookupError, NameError, TypeError, ValueError, _NotFound, _Unauthorized, _LocationError, ):
                            __attr_class = _static_4603321424(__default_4605621808, econtext, True, ())

                        __attr_class = __quote(__attr_class, '"', '&quot;', 'fas fa-ban text-danger', '__default__')
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>')
                        __append('\n                  ')

                        # <Static value=<_ast.Dict object at 0x112843be0> name=None at 112843ba8> -> __attrs_4605624048
                        __attrs_4605624048 = _static_4605623264

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span')
                        __append(' class="sr-only"')
                        __append('>')
                        __default_4605622984 = '__default'

                        # <Value 'ob/meta_type | default' (80:53)> -> __cache_4605622592
                        __token = 4609
                        try:
                            __cache_4605622592 = _static_4603321424(getitem('ob'), econtext, True, ('meta_type', ))
                        except (AttributeError, LookupError, NameError, TypeError, ValueError, _NotFound, _Unauthorized, _LocationError, ):
                            __cache_4605622592 = _static_4603321424(__default_4605622984, econtext, True, ())


                        # <Identity expression=<Value 'ob/meta_type | default' (80:53)> value=<_ast.Str object at 0x1128439b0> at 1128439e8> -> __condition
                        __expression = __cache_4605622592
                        __value = '__default'
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Broken object')
                        else:
                            __content = __cache_4605622592
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>')
                        __append('\n                ')
                        __append('</i>')
                        __append('\n              ')
                        __append('</td>')
                        __append('\n              ')

                        # <Static value=<_ast.Dict object at 0x1128480b8> name=None at 112848080> -> __attrs_4605641672
                        __attrs_4605641672 = _static_4605640888

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td')
                        __append(' class="zmi-object-id"')
                        __append('>')
                        __append('\n                ')

                        # <Static value=<_ast.Dict object at 0x112848518> name=None at 1128484e0> -> __attrs_4605643016
                        __attrs_4605643016 = _static_4605642008

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')
                        __default_4605642512 = '__default__'

                        # <Substitution "python:'%s/manage_workspace'%(ob_dict['quoted_id'])" (84:40)> -> __attr_href
                        __token = 4776
                        __attr_href = ('%s/manage_workspace' % _guarded_getitem(getitem('ob_dict'), 'quoted_id'))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, '__default__')
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>')
                        __append('\n                  ')
                        __default_4605644248 = '__default'

                        # <Value 'ob_dict/id' (85:37)> -> __cache_4605643856
                        __token = 4867
                        __cache_4605643856 = _static_4603321424(getitem('ob_dict'), econtext, True, ('id', ))

                        # <Identity expression=<Value 'ob_dict/id' (85:37)> value=<_ast.Str object at 0x112848cc0> at 112848cf8> -> __condition
                        __expression = __cache_4605643856
                        __value = '__default'
                        __condition = (__expression is __value)
                        if __condition:

                            # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605643744
                            __attrs_4605643744 = _static_4603194560

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span')
                            __append('>')
                            __append('Id')
                            __append('</span>')
                        else:
                            __content = __cache_4605643856
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                  ')

                        # <Value 'ob/wl_isLocked | nothing' (86:111)> -> __condition
                        __token = 5000
                        try:
                            __condition = _static_4603321424(getitem('ob'), econtext, True, ('wl_isLocked', ))
                        except (AttributeError, LookupError, NameError, TypeError, ValueError, _NotFound, _Unauthorized, _LocationError, ):
                            __condition = _static_4603321424(get('nothing', nothing), econtext, True, ())

                        if __condition:

                            # <Static value=<_ast.Dict object at 0x112848f98> name=None at 112848ef0> -> __attrs_4604846032
                            __attrs_4604846032 = _static_4605644696

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span')
                            __append(' class="badge badge-warning"')
                            __append(' title="This item has been locked by WebDAV"')
                            __append('>')
                            __append('\n                    ')

                            # <Static value=<_ast.Dict object at 0x11265c2b0> name=None at 11267d550> -> __attrs_4605064080
                            __attrs_4605064080 = _static_4603626160

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append('<i')
                            __append(' class="fa fa-lock"')
                            __append('>')
                            __append('</i>')
                            __append('\n                  ')
                            __append('</span>')
                        __append('\n                  ')

                        # <Value 'ob/title|nothing' (89:74)> -> __condition
                        __token = 5174
                        try:
                            __condition = _static_4603321424(getitem('ob'), econtext, True, ('title', ))
                        except (AttributeError, LookupError, NameError, TypeError, ValueError, _NotFound, _Unauthorized, _LocationError, ):
                            __condition = _static_4603321424(get('nothing', nothing), econtext, True, ())

                        if __condition:

                            # <Static value=<_ast.Dict object at 0x1127bb748> name=None at 1127bb828> -> __attrs_4605653344
                            __attrs_4605653344 = _static_4605065032

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span')
                            __append(' class="zmi-object-title hidden-xs"')
                            __append('>')
                            __append('\n                    &nbsp;(')
                            __default_4605654688 = '__default'

                            # <Value 'ob/title' (90:46)> -> __cache_4605654296
                            __token = 5239
                            __cache_4605654296 = _static_4603321424(getitem('ob'), econtext, True, ('title', ))

                            # <Identity expression=<Value 'ob/title' (90:46)> value=<_ast.Str object at 0x11284b588> at 11284b5c0> -> __condition
                            __expression = __cache_4605654296
                            __value = '__default'
                            __condition = (__expression is __value)
                            if __condition:

                                # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605654184
                                __attrs_4605654184 = _static_4603194560

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span')
                                __append('>')
                                __append('</span>')
                            else:
                                __content = __cache_4605654296
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(')\n                  ')
                            __append('</span>')
                        __append('\n                ')
                        __append('</a>')
                        __append('\n              ')
                        __append('</td>')
                        __append('\n              ')

                        # <Static value=<_ast.Dict object at 0x11284b9b0> name=None at 11284b978> -> __attrs_4605656256
                        __attrs_4605656256 = _static_4605655472

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td')
                        __append(' class="text-right zmi-object-size hidden-xs"')
                        __append('>')
                        __default_4605655248 = '__default'

                        # <Value 'python:here.compute_size(ob)' (94:76)> -> __cache_4605654856
                        __token = 5401
                        __cache_4605654856 = _guarded_getattr(getitem('here'), 'compute_size')(getitem('ob'))

                        # <Identity expression=<Value 'python:here.compute_size(ob)' (94:76)> value=<_ast.Str object at 0x11284b7b8> at 11284b7f0> -> __condition
                        __expression = __cache_4605654856
                        __value = '__default'
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_4605654856
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>')
                        __append('\n              ')

                        # <Static value=<_ast.Dict object at 0x11284f080> name=None at 11284f048> -> __attrs_4605670288
                        __attrs_4605670288 = _static_4605669504

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td')
                        __append(' class="text-right zmi-object-date hidden-xs pl-3"')
                        __append('>')
                        __default_4605656928 = '__default'

                        # <Value 'python:here.last_modified(ob)' (96:81)> -> __cache_4605656536
                        __token = 5533
                        __cache_4605656536 = _guarded_getattr(getitem('here'), 'last_modified')(getitem('ob'))

                        # <Identity expression=<Value 'python:here.last_modified(ob)' (96:81)> value=<_ast.Str object at 0x11284be48> at 11284be80> -> __condition
                        __expression = __cache_4605656536
                        __value = '__default'
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_4605656536
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>')
                        __append('\n            ')
                        if (__backup_ob_4604990408 is __marker):
                            del econtext['ob']
                        else:
                            econtext['ob'] = __backup_ob_4604990408
                        __append('\n          ')
                        __append('</tr>')
                        ____index_4605597904 -= 1
                        if (____index_4605597904 > 0):
                            __append('\n          ')
                    if (__backup_ob_dict_4604894344 is __marker):
                        del econtext['ob_dict']
                    else:
                        econtext['ob_dict'] = __backup_ob_dict_4604894344
                    __append('\n        ')
                    __append('</tbody>')
                    __append('\n      ')
                    __append('</table>')
                __append('\n\n      ')
                __backup_delete_allowed_4604892888 = get('delete_allowed', __marker)

                # <Value "python:sm.checkPermission('Delete objects', context)" (104:21)> -> __value
                __token = 5734
                __value = _guarded_getattr(getitem('sm'), 'checkPermission')('Delete objects', getitem('context'))
                econtext['delete_allowed'] = __value

                # <Value 'obs' (104:90)> -> __condition
                __token = 5803
                __condition = _static_4603321424(getitem('obs'), econtext, True, ())
                if __condition:

                    # <Static value=<_ast.Dict object at 0x11283d940> name=None at 11283d9e8> -> __attrs_4605671072
                    __attrs_4605671072 = _static_4605598016

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')
                    __append(' class="form-group zmi-controls"')
                    __append('>')
                    __append('\n        ')

                    # <Value 'not:context/dontAllowCopyAndPaste|nothing' (105:35)> -> __condition
                    __token = 5844
                    __token = 5848
                    try:
                        __condition = _static_4603321424(getitem('context'), econtext, True, ('dontAllowCopyAndPaste', ))
                    except (AttributeError, LookupError, NameError, TypeError, ValueError, _NotFound, _Unauthorized, _LocationError, ):
                        __condition = _static_4603321424(get('nothing', nothing), econtext, True, ())

                    __condition = not __condition
                    if __condition:
                        __append('\n          ')

                        # <Static value=<_ast.Dict object at 0x11284fd30> name=None at 11284fcf8> -> __attrs_4605678368
                        __attrs_4605678368 = _static_4605672752

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')
                        __append(' class="btn btn-primary"')
                        __append(' type="submit"')
                        __append(' name="manage_renameForm:method"')
                        __append(' value="Rename"')
                        __append(' />')
                        __append('\n          ')

                        # <Value 'delete_allowed' (107:114)> -> __condition
                        __token = 6107
                        __condition = _static_4603321424(getitem('delete_allowed'), econtext, True, ())
                        if __condition:

                            # <Static value=<_ast.Dict object at 0x112851588> name=None at 112851550> -> __attrs_4605680440
                            __attrs_4605680440 = _static_4605678984

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input')
                            __append(' class="btn btn-primary"')
                            __append(' type="submit"')
                            __append(' name="manage_cutObjects:method"')
                            __append(' value="Cut"')
                            __append(' />')
                        __append('\n          ')

                        # <Static value=<_ast.Dict object at 0x112851e10> name=None at 112851dd8> -> __attrs_4605690880
                        __attrs_4605690880 = _static_4605681168

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')
                        __append(' class="btn btn-primary"')
                        __append(' type="submit"')
                        __append(' name="manage_copyObjects:method"')
                        __append(' value="Copy"')
                        __append(' />')
                        __append('\n          ')

                        # <Value 'here/cb_dataValid' (109:118)> -> __condition
                        __token = 6348
                        __condition = _static_4603321424(getitem('here'), econtext, True, ('cb_dataValid', ))
                        if __condition:

                            # <Static value=<_ast.Dict object at 0x112854668> name=None at 112854630> -> __attrs_4605692952
                            __attrs_4605692952 = _static_4605691496

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input')
                            __append(' class="btn btn-primary"')
                            __append(' type="submit"')
                            __append(' name="manage_pasteObjects:method"')
                            __append(' value="Paste"')
                            __append(' />')
                        __append('\n        ')
                    __append('\n        ')

                    # <Value 'delete_allowed' (111:115)> -> __condition
                    __token = 6511
                    __condition = _static_4603321424(getitem('delete_allowed'), econtext, True, ())
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x112854d68> name=None at 112854d30> -> __attrs_4605703000
                        __attrs_4605703000 = _static_4605693288

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')
                        __append(' class="btn btn-primary"')
                        __append(' type="submit"')
                        __append(' name="manage_delObjects:method"')
                        __append(' value="Delete"')
                        __append(' />')
                    __append('\n        ')

                    # <Value "python:sm.checkPermission('Import/Export objects', context)" (112:128)> -> __condition
                    __token = 6658
                    __condition = _guarded_getattr(getitem('sm'), 'checkPermission')('Import/Export objects', getitem('context'))
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x1128575f8> name=None at 1128575c0> -> __attrs_4605705128
                        __attrs_4605705128 = _static_4605703672

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')
                        __append(' class="btn btn-primary"')
                        __append(' type="submit"')
                        __append(' name="manage_importExportForm:method"')
                        __append(' value="Import/Export"')
                        __append(' />')
                    __append('\n      ')
                    __append('</div>')
                if (__backup_delete_allowed_4604892888 is __marker):
                    del econtext['delete_allowed']
                else:
                    econtext['delete_allowed'] = __backup_delete_allowed_4604892888
                __append('\n      ')

                # <Static value=<_ast.Dict object at 0x112857d68> name=None at 112857d30> -> __attrs_4605718712
                __attrs_4605718712 = _static_4605705576

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="container-fluid"')
                __append('>')
                __append('\n        ')

                # <Value "python: has_order_support and sm.checkPermission('Manage properties', context)" (115:64)> -> __condition
                __token = 6835
                __condition = (getitem('has_order_support') and _guarded_getattr(getitem('sm'), 'checkPermission')('Manage properties', getitem('context')))
                if __condition:

                    # <Static value=<_ast.Dict object at 0x11285b240> name=None at 11285b208> -> __attrs_4605719888
                    __attrs_4605719888 = _static_4605719104

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')
                    __append(' class="form-group row zmi-controls"')
                    __append('>')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x11285b898> name=None at 11285b860> -> __attrs_4605722464
                    __attrs_4605722464 = _static_4605720728

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input')
                    __append(' type="submit"')
                    __append(' name="manage_move_objects_up:method"')
                    __append(' value="Move up"')
                    __append(' title="Move selected items up"')
                    __append(' class="btn btn-primary"')
                    __append(' />')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605727296
                    __attrs_4605727296 = _static_4603194560

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')
                    __append('>')
                    __append('/')
                    __append('</span>')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x11285d4e0> name=None at 11285d4a8> -> __attrs_4605729704
                    __attrs_4605729704 = _static_4605727968

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input')
                    __append(' type="submit"')
                    __append(' name="manage_move_objects_down:method"')
                    __append(' value="Move down"')
                    __append(' title="Move selected items down"')
                    __append(' class="btn btn-primary"')
                    __append(' />')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605730376
                    __attrs_4605730376 = _static_4603194560

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')
                    __append('>')
                    __append('by')
                    __append('</span>')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x11285dfd0> name=None at 11285df98> -> __attrs_4605743904
                    __attrs_4605743904 = _static_4605730768

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')
                    __append(' class="col-xs-2"')
                    __append('>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x1128614e0> name=None at 112861438> -> __attrs_4605745416
                    __attrs_4605745416 = _static_4605744352

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append('<select')
                    __append(' class="form-control"')
                    __append(' name="delta:int"')
                    __append('>')
                    __append('\n              ')
                    __backup_val_4604845920 = get('val', __marker)

                    # <Value 'python:range(1,min(5,len(obs)))' (122:38)> -> __iterator
                    __token = 7387
                    __iterator = get('range', range)(1, get('min', min)(5, len(getitem('obs'))))
                    (__iterator, ____index_4605746648, ) = getitem('repeat')('val', __iterator)
                    econtext['val'] = None
                    for __item in __iterator:
                        econtext['val'] = __item

                        # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605746480
                        __attrs_4605746480 = _static_4603194560

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append('<option')
                        __append('>')
                        __default_4605746088 = '__default'

                        # <Value 'val' (122:84)> -> __cache_4605745696
                        __token = 7433
                        __cache_4605745696 = _static_4603321424(getitem('val'), econtext, True, ())

                        # <Identity expression=<Value 'val' (122:84)> value=<_ast.Str object at 0x112861a90> at 112861ac8> -> __condition
                        __expression = __cache_4605745696
                        __value = '__default'
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4605745696
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</option>')
                        ____index_4605746648 -= 1
                        if (____index_4605746648 > 0):
                            __append('\n              ')
                    if (__backup_val_4604845920 is __marker):
                        del econtext['val']
                    else:
                        econtext['val'] = __backup_val_4604845920
                    __append('\n              ')
                    __backup_val_4605598464 = get('val', __marker)

                    # <Value 'python:range(5,len(obs),5)' (123:38)> -> __iterator
                    __token = 7479
                    __iterator = get('range', range)(5, len(getitem('obs')), 5)
                    (__iterator, ____index_4605756024, ) = getitem('repeat')('val', __iterator)
                    econtext['val'] = None
                    for __item in __iterator:
                        econtext['val'] = __item

                        # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605755856
                        __attrs_4605755856 = _static_4603194560

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append('<option')
                        __append('>')
                        __default_4605755464 = '__default'

                        # <Value 'val' (123:79)> -> __cache_4605746816
                        __token = 7520
                        __cache_4605746816 = _static_4603321424(getitem('val'), econtext, True, ())

                        # <Identity expression=<Value 'val' (123:79)> value=<_ast.Str object at 0x112861ef0> at 112861f28> -> __condition
                        __expression = __cache_4605746816
                        __value = '__default'
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4605746816
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</option>')
                        ____index_4605756024 -= 1
                        if (____index_4605756024 > 0):
                            __append('\n              ')
                    if (__backup_val_4605598464 is __marker):
                        del econtext['val']
                    else:
                        econtext['val'] = __backup_val_4605598464
                    __append('\n            ')
                    __append('</select>')
                    __append('\n          ')
                    __append('</div>')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x1128644a8> name=None at 112864470> -> __attrs_4605758320
                    __attrs_4605758320 = _static_4605756584

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input')
                    __append(' type="submit"')
                    __append(' name="manage_move_objects_to_top:method"')
                    __append(' value="Move to top"')
                    __append(' class="btn btn-primary"')
                    __append(' title="Move selected items to top"')
                    __append(' />')
                    __append('\n          ')

                    # <Static value=<_ast.Dict object at 0x112864dd8> name=None at 112864da0> -> __attrs_4605777120
                    __attrs_4605777120 = _static_4605758936

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input')
                    __append(' type="submit"')
                    __append(' name="manage_move_objects_to_bottom:method"')
                    __append(' value="Move to bottom"')
                    __append(' class="btn btn-primary"')
                    __append(' title="Move selected items to bottom"')
                    __append(' />')
                    __append('\n        ')
                    __append('</div>')
                __append('\n      ')
                __append('</div>')
                __append('\n    ')
            __append('\n\n    ')

            # <Value 'not:obs' (132:26)> -> __condition
            __token = 7960
            __token = 7964
            __condition = _static_4603321424(getitem('obs'), econtext, True, ())
            __condition = not __condition
            if __condition:
                __append('\n      ')

                # <Static value=<_ast.Dict object at 0x112869780> name=None at 112869748> -> __attrs_4605778576
                __attrs_4605778576 = _static_4605777792

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="alert alert-info mt-4 mb-4"')
                __append('>')
                __append('\n        There are currently no items in ')

                # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605779808
                __attrs_4605779808 = _static_4603194560

                # <em ... (0:0)
                # --------------------------------------------------------
                __append('<em')
                __append('>')
                __default_4605779248 = '__default'

                # <Value 'here/title_or_id' (134:57)> -> __cache_4605778856
                __token = 8074
                __cache_4605778856 = _static_4603321424(getitem('here'), econtext, True, ('title_or_id', ))

                # <Identity expression=<Value 'here/title_or_id' (134:57)> value=<_ast.Str object at 0x112869c18> at 112869c50> -> __condition
                __expression = __cache_4605778856
                __value = '__default'
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4605778856
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</em>')
                __append('.\n      ')
                __append('</div>')
                __append('\n      ')

                # <Static value=<_ast.Dict object at 0x11286b0f0> name=None at 11286b0b8> -> __attrs_4605785088
                __attrs_4605785088 = _static_4605784304

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="form-group"')
                __append('>')
                __append('\n        ')

                # <Value 'not:context/dontAllowCopyAndPaste|nothing' (137:35)> -> __condition
                __token = 8178
                __token = 8182
                try:
                    __condition = _static_4603321424(getitem('context'), econtext, True, ('dontAllowCopyAndPaste', ))
                except (AttributeError, LookupError, NameError, TypeError, ValueError, _NotFound, _Unauthorized, _LocationError, ):
                    __condition = _static_4603321424(get('nothing', nothing), econtext, True, ())

                __condition = not __condition
                if __condition:
                    __append('\n          ')

                    # <Value 'here/cb_dataValid' (138:118)> -> __condition
                    __token = 8340
                    __condition = _static_4603321424(getitem('here'), econtext, True, ('cb_dataValid', ))
                    if __condition:

                        # <Static value=<_ast.Dict object at 0x11286b940> name=None at 11286b908> -> __attrs_4605787888
                        __attrs_4605787888 = _static_4605786432

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')
                        __append(' class="btn btn-primary"')
                        __append(' type="submit"')
                        __append(' name="manage_pasteObjects:method"')
                        __append(' value="Paste"')
                        __append(' />')
                    __append('\n        ')
                __append('\n        ')

                # <Value "python:sm.checkPermission('Import/Export objects', context)" (140:128)> -> __condition
                __token = 8516
                __condition = _guarded_getattr(getitem('sm'), 'checkPermission')('Import/Export objects', getitem('context'))
                if __condition:

                    # <Static value=<_ast.Dict object at 0x11286f048> name=None at 11286b6d8> -> __attrs_4605801976
                    __attrs_4605801976 = _static_4605800520

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input')
                    __append(' class="btn btn-primary"')
                    __append(' type="submit"')
                    __append(' name="manage_importExportForm:method"')
                    __append(' value="Import/Export"')
                    __append(' />')
                __append('\n      ')
                __append('</div>')
                __append('\n    ')
            __append('\n  ')
            __append('</form>')
            if (__backup_has_order_support_4604878128 is __marker):
                del econtext['has_order_support']
            else:
                econtext['has_order_support'] = __backup_has_order_support_4604878128
            if (__backup_sm_4604877904 is __marker):
                del econtext['sm']
            else:
                econtext['sm'] = __backup_sm_4604877904
            if (__backup_default_sort_4604878408 is __marker):
                del econtext['default_sort']
            else:
                econtext['default_sort'] = __backup_default_sort_4604878408
            if (__backup_skey_4604892384 is __marker):
                del econtext['skey']
            else:
                econtext['skey'] = __backup_skey_4604892384
            if (__backup_rkey_4604892160 is __marker):
                del econtext['rkey']
            else:
                econtext['rkey'] = __backup_rkey_4604892160
            if (__backup_rkey_alt_4604892552 is __marker):
                del econtext['rkey_alt']
            else:
                econtext['rkey_alt'] = __backup_rkey_alt_4604892552
            if (__backup_obs_4604891992 is __marker):
                del econtext['obs']
            else:
                econtext['obs'] = __backup_obs_4604891992
            __append('\n')
            __append('</main>')
            __append('\n\n\n')

            # <Static value=<_ast.Dict object at 0x1125f2cc0> name=None at 1125f2f60> -> __attrs_4605777400
            __attrs_4605777400 = _static_4603194560

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')
            __append('>')
            __append("\n  // +++++++++++++++++++++++++++\n  // checkbox_all: Item  Selection\n  // +++++++++++++++++++++++++++\n  function checkbox_all() {\n    var checkboxes = document.getElementsByClassName('checkbox-list-item');\n    // Toggle Highlighting CSS-Class\n    if (document.getElementById('checkAll').checked) {\n      $('table.objectItems tbody tr').addClass('checked');\n    } else {\n      $('table.objectItems tbody tr').removeClass('checked');\n    };\n    // Set Checkbox like checkAll-Box\n    for (i = 0; i ")
            __append('<')
            __append(' checkboxes.length; i++) {\n      checkboxes[i].checked = document.getElementById(\'checkAll\').checked;\n    }\n  };\n\n\n  $(function () {\n\n    // +++++++++++++++++++++++++++\n    // Icon Tooltips\n    // +++++++++++++++++++++++++++\n    $(\'td.zmi-object-type i\').tooltip({\n      \'placement\': \'top\'\n    });\n\n    // +++++++++++++++++++++++++++\n    // Tablefilter/Search Element\n    // +++++++++++++++++++++++++++\n\n    function isModifierKeyPressed(event) {\n      return event.altKey ||\n        event.ctrlKey ||\n        event.metaKey;\n    }\n\n    $(document).keypress(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      // Set Focus to Tablefilter only when Modal Dialog is not Shown\n      if (!$(\'#zmi-modal\').hasClass(\'show\')) {\n        $(\'#tablefilter\').focus();\n        // Prevent Submitting a form by hitting Enter\n        // https://stackoverflow.com/questions/895171/prevent-users-from-submitting-a-form-by-hitting-enter\n        if (event.which == 13) {\n          event.preventDefault();\n          return false;\n        };\n      };\n    })\n\n    $(\'#tablefilter\').keyup(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      var tablefilter = $(this).val();\n      if (event.which == 13) {\n        if (1 === $(\'tbody tr:visible\').length) {\n          window.location.href = $(\'tbody tr:visible a\').attr(\'href\');\n        } else {\n          window.location.href = \'manage_findForm?btn_submit=Find&search_sub:int=1&obj_ids%3Atokens=\' + tablefilter;\n        }\n        event.preventDefault();\n      };\n      $(\'table.objectItems\').find("tbody tr").hide();\n      $(\'table.objectItems\').find("tbody tr td.zmi-object-id a:contains(" + tablefilter + ")").closest(\'tbody tr\').show();\n    });\n\n    // +++++++++++++++++++++++++++\n    // OBJECTIST SORTING: Show skey=meta_type\n    // +++++++++++++++++++++++++++\n    let searchParams = new URLSearchParams(window.location.search);\n    if (searchParams.get(\'skey\') == \'meta_type\') {\n      $(\'td.zmi-object-type i\').each(function () {\n        $(this).parent().parent().find(\'td.zmi-object-id\').prepend(\'')

            # <Static value=<_ast.Dict object at 0x11286f898> name=None at 11286f860> -> __attrs_4605803432
            __attrs_4605803432 = _static_4605802648

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')
            __append(' class="zmi-typename_show"')
            __append('>')
            __append("' + $(this).text() + '")
            __append('</span>')
            __append("')\n      });\n      $('th.zmi-object-id').addClass('zmi-typename_show');\n    }\n\n  });\n\n")
            __append('</script>')
            __append('\n\n')
            __default_4605804328 = '__default'

            # <Value 'here/manage_page_footer' (237:31)> -> __cache_4605803936
            __token = 11448
            __cache_4605803936 = _static_4603321424(getitem('here'), econtext, True, ('manage_page_footer', ))

            # <Identity expression=<Value 'here/manage_page_footer' (237:31)> value=<_ast.Str object at 0x11286fe10> at 11286fe48> -> __condition
            __expression = __cache_4605803936
            __value = '__default'
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4605803936
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }