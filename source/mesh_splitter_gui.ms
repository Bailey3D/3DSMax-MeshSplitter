(
    global g_rolloutMeshSplitter
    try(destroyDialog g_rolloutMeshSplitter)catch()

    function this_script_path =
    (
        return getFileNamePath (getThisScriptFileName())
    )

    rollout g_rolloutMeshSplitter "Bailey3D - MeshSplitter" width:250
    (
        group "Mesh Splitter"
        (
            button btnSplitToElements "Split To Elements" width:200 tooltip:"Splits the selected meshes to one unique mesh per element"
            button btnSplitByMaterialID "Split By Material ID" width:200 tooltip:"Splits the selected meshes to one unique mesh per material ID"
            button btnSplitBySmoothingGroup "Split By Smoothing Group" width:200 tooltip:"Splits the selected meshes to one unique mesh per smoothing group"
            button btnSplitByFaceColour "Split By Face Color" width:200 tooltip:"Splits the selected meshes to one unique mesh per face colour"
        )

        group "Extras.."
        (
            button btnArtstation "More by Bailey3D" width:200
        )



        on btnSplitToElements pressed do
        (
            split_by_face_color_path = this_script_path() + "scripts/split_to_elements.py"
            python.executeFile split_by_face_color_path
        )

        on btnSplitByMaterialID pressed do
        (
            split_by_face_color_path = this_script_path() + "scripts/split_by_material_id.py"
            python.executeFile split_by_face_color_path
        )

        on btnSplitBySmoothingGroup pressed do
        (
            split_by_face_color_path = this_script_path() + "scripts/split_by_smoothing_group.py"
            python.executeFile split_by_face_color_path
        )

        on btnSplitByFaceColour pressed do
        (
            split_by_face_color_path = this_script_path() + "scripts/split_by_face_color.py"
            python.executeFile split_by_face_color_path
        )

        on btnArtstation pressed do
        (
            ShellLaunch "http://bailey3d.com/" ""
        )
    )

    createDialog g_rolloutMeshSplitter
)