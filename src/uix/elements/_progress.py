from ..core.element import Element
print("Imported: progress")
class progress(Element):
    def __init__(self,value = 0,id = None, max = 100):
        super().__init__(value, id = id)
        self.tag = "progress"
        self.max = max
        self.attrs["max"] = max



title = "Progress"

description = """
# progress(value,id,max)
1. Progress bir input elementidir.
| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Progress elementinin id'si                        |
| value         | Progress elementinin değeri                       |
| max           | Progress'in maksimum değeri                       |
"""

sample = """
def progress_example():
    main = progress(50, id="progress")
    return main
"""