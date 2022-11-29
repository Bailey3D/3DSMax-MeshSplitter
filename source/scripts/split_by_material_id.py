"""
:script
:type tool
:desc Splits all selected meshes into unique meshes depending on their given material IDs
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
            pymxs.runtime.setFaceSelection(temp_copy, pymxs.runtime.array(1))

            ids_grouped = {}

            for i in range(1, temp_copy.getNumFaces()):
                face_id = i

                face_mat_id = pymxs.runtime.polyOp.getFaceMatID(temp_copy, face_id)
                if(face_mat_id not in ids_grouped):
                    ids_grouped[face_mat_id] = [face_id]
                else:
                    ids_grouped[face_mat_id].append(face_id)

            for mat_id in ids_grouped:
                pymxs.runtime.polyOp.setFaceSelection(temp_copy, ids_grouped[mat_id])
                split_name = temp_copy_name + "_mat_" + str(mat_id)
                pymxs.runtime.polyOp.detachFaces(
                    temp_copy,
                    ids_grouped[mat_id],
                    asNode=True,
                    name=split_name,
                    delete=False
                )
                geo = pymxs.runtime.getNodeByName(split_name)
                output.append(geo)
                self.validate_geometry(geo)

            pymxs.runtime.delete(temp_copy)

        return output


tool = MeshSplitter()
