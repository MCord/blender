import bpy
import mathutils
import math


# get the template object to copy from
original_object = bpy.data.objects.get("Cube")
# get original object location
original_location = original_object.location

# for 10 elements
for x in range(1,11):
    # clone the template to create a new object
    cloned_object = original_object.copy()
    
    # move the object to new location
    cloned_object.location = original_location + mathutils.Vector((x * 5,0,0))
    
    # rotate the object around all 3 axies
    cloned_object.rotation_euler[0] = math.radians(45)
    cloned_object.rotation_euler[1] = math.radians(20)
    cloned_object.rotation_euler[2n] = math.radians(10)

    # add the object to the scene
    bpy.data.collections["Collection"].objects.link(cloned_object)    


