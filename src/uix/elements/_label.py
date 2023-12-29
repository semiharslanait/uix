from ..core.element import Element
print("Imported: label")

class label(Element):
    def __init__(self,value= None,id = None, tabindex = -1, usefor = None):
        super().__init__(value, id = id)
        self.classes.append("label")
        self.usefor = usefor
        self.tag = "label"
        self.attrs["tabindex"] = tabindex
        self.attrs["for"] = usefor
        self.has_content = True

title = "Label"
description = '''
Label elementi. Bir input elementine ait label elementi için kullanılır.
value : Label içeriği
id : Labelin id'si
attributes : Labela ait attribute'lar
attrs["tabindex"] : Labelin tabindex'i. Varsayılan değer: -1. Değer -1 ise tab ile focuslanamaz.
usefor : Labelin kullanıldığı input elementinin id'si
'''
sample = """
    with parent:
        label("Label",id="label1",usefor="input1")
        input(id="input1", type="text", placeholder="Label için input")
        
"""