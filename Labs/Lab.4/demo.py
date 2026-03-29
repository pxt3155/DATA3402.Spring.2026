from paint import canvas, rectangle, circle, triangle, CompoundShape, paint_shape

c =canvas(40, 20, ".")

r=rectangle(6, 4, 2, 2)
ci=circle(3, 15, 8)
t=triangle(5, 4, 25, 5)

group=CompoundShape()
group.add(r)
group.add(ci)
group.add(t)

group.paint(c, "*")

c.show()