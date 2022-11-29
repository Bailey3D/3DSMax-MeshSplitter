"""
Installs the scripts as macros to 3DS Max
"""
import os
import pymxs


def create_a_macro(name, tooltip, script_path, maxscript=False):
    macro_category = "Bailey3D"
    auto_undo_enabled = True
    script_path = script_path.replace("\\", "/")

    if(maxscript):
        command = "fileIn"
    else:
        command = "python.executeFile"

    macro_text = """
        macroScript {} category:"{}" toolTip:"{}" autoUndoEnabled:{}
        (
            script_path = "{}"
            {} script_path
        )
    """.format(
        name, macro_category, tooltip, str(auto_undo_enabled), script_path, command
    )
    pymxs.runtime.execute(macro_text)


create_a_macro(
    "SplitToElements",
    "Split To Elements",
    os.path.join(os.path.dirname(__file__), "scripts\\split_to_elements.py")
)

create_a_macro(
    "SplitByFaceColor",
    "Split By Face Color",
    os.path.join(os.path.dirname(__file__), "scripts\\split_by_face_color.py")
)

create_a_macro(
    "SplitBySmoothingGroup",
    "Split By Smoothing Group",
    os.path.join(os.path.dirname(__file__), "scripts\\split_by_smoothing_group.py")
)

create_a_macro(
    "SplitByMaterialID",
    "Split By Material ID",
    os.path.join(os.path.dirname(__file__), "scripts\\split_by_material_id.py")
)

create_a_macro(
    "MeshSplitterGUI",
    "Mesh Splitter (GUI)",
    os.path.join(os.path.dirname(__file__), "mesh_splitter_gui.ms"),
    maxscript=True
)
