FS30��uáf       �      initial database creation        ��uáf                        @�cpersistent.mapping
PersistentMapping
q .�}qX   dataq}qs.       ���w-��      �               ��w-��       4       �         ��cpersistent.mapping
PersistentMapping
q .�}qX   dataq}qX   ApplicationqC       qcOFS.Application
Application
q�qQss.       ��w-��               �         ʀcOFS.Application
Application
q .�}q(X   __allow_groups__qC       qcOFS.userfolder
UserFolder
q�qQX   _objectsq}q(X   idqX	   acl_usersq	X	   meta_typeq
X   User Folderqu�qh	hh�qQu.       ��w-��               �         ��cOFS.userfolder
UserFolder
q .�}q(X   dataqC       qcPersistence.mapping
PersistentMapping
q�qQX   _ofs_migratedq�u.       ��w-��               �         A�cPersistence.mapping
PersistentMapping
q .�}qX   dataq}qs.      ���w/""      �      Created initial user       ��w/""            {         z�cPersistence.mapping
PersistentMapping
q .�}qX   dataq}qX   chrisqC       qcAccessControl.users
User
q�qQss.       ��w/""              {         ��cAccessControl.users
User
q .�}q(X   nameqX   chrisqX   __qC!{SHA}52f7mZ+bdUmK02BroIE9LSMtygA=qX   rolesqX   Managerq�qX   domainsq	]q
u.      ���wD`�      =      Added virtual_hosting       ��wD`�      i              W�cOFS.Application
Application
q .�}q(X   __allow_groups__qC       qcOFS.userfolder
UserFolder
q�qQX   _objectsq}q(X   idqX	   acl_usersq	X	   meta_typeq
X   User Folderqu}q(hX   virtual_hostingqh
X   Virtual Host Monsterqu�qh	hh�qQhC       qcProducts.SiteAccess.VirtualHostMonster
VirtualHostMonster
q�qQX   __before_traverse__q}qKh�qcZPublisher.BeforeTraverse
NameCaller
q)�q}qX   nameqhsbsX   __before_publishing_traverse__qcZPublisher.BeforeTraverse
MultiHook
q)�q}q(X	   _hooknameqhX   _priorq NX   _defined_in_classq!�X   _listq"]q#haubu.       ��wD`�                       f�cProducts.SiteAccess.VirtualHostMonster
VirtualHostMonster
q .�}qX   idqX   virtual_hostingqs.      =��wX�      �    "  Added default view for root object       ��wX�      B      [        ӀcOFS.Application
Application
q .�}q(X   __allow_groups__qC       qcOFS.userfolder
UserFolder
q�qQX   _objectsq}q(X   idqX	   acl_usersq	X	   meta_typeq
X   User Folderqu}q(hX   virtual_hostingqh
X   Virtual Host Monsterqu}q(hX
   index_htmlqh
X   Page Templatequ�qh	hh�qQhC       qcProducts.SiteAccess.VirtualHostMonster
VirtualHostMonster
q�qQX   __before_traverse__q}qKh�qcZPublisher.BeforeTraverse
NameCaller
q)�q}qX   nameqhsbsX   __before_publishing_traverse__qcZPublisher.BeforeTraverse
MultiHook
q)�q }q!(X	   _hooknameq"hX   _priorq#NX   _defined_in_classq$�X   _listq%]q&haubhC       q'cProducts.PageTemplates.ZopePageTemplate
ZopePageTemplate
q(�q)Qu.       ��wX�              [        ,�cProducts.PageTemplates.ZopePageTemplate
ZopePageTemplate
q .�}q(X   idqX
   index_htmlqX   expandqK X   _bind_namesqcShared.DC.Scripts.Bindings
NameAssignments
q)�q}qX   _asgnsq	}q
X   name_subpathqX   traverse_subpathqssbX   output_encodingqX   utf-8qX   content_typeqX	   text/htmlqX   _textqX�  <!DOCTYPE html>
<html>
  <head>
    <title tal:content="template/title">The title</title>
    <meta charset="utf-8" />
  </head>
  <body>
    
    <h2><span tal:replace="context/title_or_id">content title or id</span>
        <span tal:condition="template/title"
              tal:replace="template/title">optional template title</span></h2>

    This is Page Template <em tal:content="template/id">template id</em>.
  </body>
</html>qX   titleqX   Auto-generated default pagequ.      ��氵e�f      �      chris/addPollMain       �氵e�f      �      �        ��cOFS.Application
Application
q .�}q(X   __allow_groups__qC       qcOFS.userfolder
UserFolder
q�qQX   _objectsq(}q(X   idqX	   acl_usersq	X	   meta_typeq
X   User Folderqu}q(hX   virtual_hostingqh
X   Virtual Host Monsterqu}q(hX
   index_htmlqh
X   Page Templatequ}q(X   idqX   pollqX	   meta_typeqX   POLLqutqX	   acl_usersqhh�qQX   virtual_hostingqC       qcProducts.SiteAccess.VirtualHostMonster
VirtualHostMonster
q�qQX   __before_traverse__q}qKh�q cZPublisher.BeforeTraverse
NameCaller
q!)�q"}q#X   nameq$hsbsX   __before_publishing_traverse__q%cZPublisher.BeforeTraverse
MultiHook
q&)�q'}q((X	   _hooknameq)X   __before_publishing_traverse__q*X   _priorq+NX   _defined_in_classq,�X   _listq-]q.h"aubX
   index_htmlq/C       q0cProducts.PageTemplates.ZopePageTemplate
ZopePageTemplate
q1�q2QX   pollq3C       q4cpoll.main.app
PollMain
q5�q6Qu.       �氵e�f              �         ��cpoll.main.app
PollMain
q .�}q(X   idqX   pollqX   _ownerq]qX	   acl_usersqaX   chrisq�qX   __ac_local_roles__q	}q
h]qX   Ownerqasu.      �