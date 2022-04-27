import numpy as np
"""
a = np.array([1.2, 2.5, 3.2, 1.8])
print(type(a))
print(a.dtype)
print(a.ndim)
print(a.shape)
print(a.size)
"""
"""#création et typage implicite
a = np.array([1,2,4])
print(a.dtype) #int32
#création et typage explicite - préférable !
a = np.array([1,2,4],dtype=float)
print(a.dtype) #float64
print(a) #[1.  2.  4.]
#un vecteur de booléens est tout à fait possible
b = np.array([True,False,True,True], dtype=bool)
print(b) #[True  False  True True]
# la donnée peut être un objet python
a = np.array([{"Toto":(45,2000)},{"Tata":(34,1500)}])
print(a.dtype) #object"""

a = np.arange(start=0,stop=10)
print(a)

a = np.append(a,10)
print(a)
b = np.delete(a,4)
print(b)
b.resize(5)
print(b)
b.resize(15)
print(b)