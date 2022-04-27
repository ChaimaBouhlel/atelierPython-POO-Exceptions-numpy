class Dog:
	"classe dog"
	kind = 'canine' # class variable (static) shared by all instances
	def __init__(self, name):
		self.name = name # instance variable unique to each instance
	def modify_kind(self, name):
		Dog.kind=name

d = Dog('Fido')
e = Dog('Buddy')
d.kind # shared by all dogs 'canine'
e.kind # shared by all dogs 'canine'
d.name # unique to d 'Fido'
e.name # unique to e 'Buddy'
e.kind="pitbull"
print(Dog.kind)
Dog.kind="caniche"
print(Dog.kind)
print(e.kind)
print(e.__doc__)
e.couleur="marron"
print(Dog.__dict__)
print(e.__dict__)
print(d.__dict__)
print(d.__module__)
print(d.__class__)