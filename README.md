django-gentype
==============

(NOTE: This tries to achieve something similar to django-polymorphic. Probably better off using django-polymorphic.)

Generic django model to be extended by a concrete model. A one-to-one between generic and concrete model. Generic object holds reference to concrete object. 


For example a generic Shape model:

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

    # creating Circle rec will automatically create Shape rec (1-to-1)
    # with the Shape rec holding reference to the concrete Circle rec 
    circle = Circle(radius=23)
    circle.save()

    # create Square 
    square = Square(x=12)
    square.save()

    for shape in Shape.filter.all():
        # we can reference concrete recs from Shape
        print shape.get_concrete_object().area()
