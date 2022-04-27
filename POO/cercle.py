class Cercle:
    def __init__(self, radius):
        self.__radius=radius

    def _get_radius(self):
        return self.__radius

    def _set_radius(self, radius):
        self.__radius=radius

    def _del_radius(self):
        del self.__radius
        print("attribut supprimé")

    radius = property(fget=_get_radius, fset=_set_radius, fdel=_del_radius)

c = Cercle(15);

c.radius=20;
print(c.radius)
#del c.radius
print(c.radius)
print(dir(c))
print(c.__str__())
