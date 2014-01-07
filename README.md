django-gentype
==============

Generic django model to be extended by a concrete model. A one-to-one between generic and concrete model. Generic object holds reference to concrete object. 

(NOTE: Similar but a lot more decoupled design could be achieved by using django contrib Content Types app and adding content_type and content_object references to your model.)


For example a generic model:

    from django.db import models
    from gentype.models import GenericType

    class Shape(GenericType):
        pass


Concrete models extending Shape:

    class Circle(Shape):
        radius = models.FloatField()

        def area(self):
            return (radius**2) * 3.14


    class Square(Shape):
        x = models.FloatField()

        def area(self):
            return x**2


Create some shapes:

    # this will create Shape and Circle db records (1-to-1)
    circle = Circle(radius=23)
    circle.save()

    # Shape and Square db recs 
    square = Square(x=12)
    square.save()

    for shape in Shape.filter.all():
        # we can get concrete recs from Shape
        print shape.get_concrete_object().area()
