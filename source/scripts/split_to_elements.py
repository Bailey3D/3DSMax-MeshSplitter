"""
:script
:type tool
:desc Splits all selected meshes into unique meshes for each of the sub-elements it contains
"""
import pymxs


class MeshSplitter(object):
    def __init__(self):
        split_meshes = []
        for i in self.selection:
            for j in self.run(i):
                split_meshes.append(j)
        self.set_selection(split_meshes)

    @property
    def selection(self):
        output = []
        for i in pymxs.runtime.selection:
            output.append(i)
        return output

    def set_selection(self, nodes):
        split_objects_mxs_array = pymxs.runtime.array()
        for i in nodes:
            pymxs.runtime.append(split_objects_mxs_array, i)
        pymxs.runtime.select(split_objects_mxs_array)

    def validate_geometry(self, node):
        pymxs.runtime.convertToPoly(node)
        pymxs.runtime.resetXForm(node)
        pymxs.runtime.resetTransform(node)
        pymxs.runtime.resetScale(node)
        pymxs.runtime.resetPivot(node)
        pymxs.runtime.centerPivot(node)

    # ------------------------------------------------------

    def run(self, node):
        output = []
        node_superclass = pymxs.runtime.superClassOf(node)
        if(node_superclass == pymxs.runtime.GeometryClass):
            temp_copy = pymxs.runtime.copy(node)
            temp_copy_name = node.name
            pymxs.runtime.convertToPoly(temp_copy)
            for i in range(temp_copy.getNumFaces()):
                if(temp_copy.getNumFaces() != 0):
                    pymxs.runtime.polyOp.setFaceSelection(temp_copy, pymxs.runtime.array(1))
                    temp_copy.selectElement()
                    elem = pymxs.runtime.polyOp.getFaceSelection(temp_copy)
                    elem_name = pymxs.runtime.uniqueName(temp_copy_name + "_elem_")
                    pymxs.runtime.polyOp.detachFaces(
                        temp_copy,
                        elem,
                        asNode=True,
                        name=elem_name
                    )
                    geo = pymxs.runtime.getNodeByName(elem_name)
                    output.append(geo)
                    self.validate_geometry(geo)
                else:
                    break
            pymxs.runtime.delete(temp_copy)
        self.set_selection(output)
        return output


tool = MeshSplitter()
