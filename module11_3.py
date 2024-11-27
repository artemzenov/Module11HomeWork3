from pprint import pprint
from inspect import getmodule


def introspection_info(obj):
    result = dict()
    result['type'] = type(obj)
    result['module'] = getmodule(obj)
    result['methods'] = list()

    for i_elem in dir(obj):
        if callable(getattr(obj, i_elem)):
            result['methods'].append(i_elem)
    
    result['attributes'] = list(
        set(dir(obj)).difference(set(result['methods']))
        )
    result['attributes'].sort()
    
    return result


class Test:
  attr_class_1 = None
  attr_class_2 = None
  
  def __init__(self, attr1=None, attr2=None):
      self.attr1 = attr1
      self.attr2 = attr2
  
  def func1(self):
    pass
  
  def func2(self):
    pass


obj = Test()
pprint(introspection_info(obj))
