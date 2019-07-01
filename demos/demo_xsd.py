# ./demo_xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-02-12 17:36:20.708769 by PyXB version 1.2.6 using Python 3.6.7.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:53e4ff2e-2ee4-11e9-ba23-080027144eb6')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vendor'), 'vendor', '__AbsentNamespace0_CTD_ANON_vendor', False, pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 6, 4), )

    
    vendor = property(__vendor.value, __vendor.set, None, None)

    
    # Element model uses Python identifier model
    __model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'model'), 'model', '__AbsentNamespace0_CTD_ANON_model', False, pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 7, 4), )

    
    model = property(__model.value, __model.set, None, None)

    
    # Element osver uses Python identifier osver
    __osver = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osver'), 'osver', '__AbsentNamespace0_CTD_ANON_osver', False, pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 8, 4), )

    
    osver = property(__osver.value, __osver.set, None, None)

    _ElementMap.update({
        __vendor.name() : __vendor,
        __model.name() : __model,
        __osver.name() : __osver
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


device = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'device'), CTD_ANON, location=pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 3, 1))
Namespace.addCategoryObject('elementBinding', device.name().localName(), device)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vendor'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 6, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'model'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 7, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osver'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 8, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'vendor')), pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 6, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'model')), pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 7, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'osver')), pyxb.utils.utility.Location('/media/sf_caumont/Dropbox/EigeneDateien/7_Professional/ExperTeach/ET_Courses/PRPN/prpn_latest/Kapitel/Kap1_Python_Grundlagen/demo_xsd.xsd', 8, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

