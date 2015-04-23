import maya.cmds as cmds

weight = 1.0

selectedObjects = cmds.ls(sl=True)

currentParent = selectedObjects[0]
currentChild = selectedObjects[1]

#COPY POSITION DATA
pointConstrainName = str(currentChild) + "_pointConstrain1"
cmds.pointConstraint( currentParent, currentChild, w = weight, name = pointConstrainName)

cmds.delete(pointConstrainName)

#COPY ROTATION DATA
orientConstrainName = str(currentChild) + "_orientConstrain1"
cmds.orientConstraint( currentParent, currentChild, w = weight, name = orientConstrainName)

cmds.delete(orientConstrainName)


'''
# Set keyframes

cmds.setKeyframe(currentChild, at='translateX')
cmds.setKeyframe(currentChild, at='translateY')
cmds.setKeyframe(currentChild, at='translateZ')

cmds.setKeyframe(currentChild, at='rotateX')
cmds.setKeyframe(currentChild, at='rotateY')
cmds.setKeyframe(currentChild, at='rotateZ')
'''