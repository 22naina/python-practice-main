#program for cuboid:
cuboid_length=int(input("enter any value:"))
cuboid_breadth=int(input("enter any value:"))
cuboid_height=int(input("enter any value:"))

#finding volume of cuboid:
volume_cuboid=(cuboid_length*cuboid_breadth*cuboid_height)

#Finding lateral surface area of cuboid:
lateral_surface_area=2*cuboid_height*(cuboid_length+cuboid_breadth)

#finding surface area of cuboid:
surface_area=2*(cuboid_length*cuboid_breadth+cuboid_length*cuboid_height+cuboid_breadth*cuboid_height)

print(volume_cuboid)
print(lateral_surface_area)
print(surface_area)