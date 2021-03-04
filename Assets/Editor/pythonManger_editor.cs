using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEditor.Scripting.Python;

[CustomEditor(typeof(pythonManger))]
public class pythonManger_editor : Editor
{
    pythonManger targetManager;

    private void OnEnable()
    {
        targetManager = (pythonManger)target;
    }

    public override void OnInspectorGUI()
    {
        if (GUILayout.Button("Launch Python Script", GUILayout.Height(35)))
        {
            string path = Application.dataPath + "/Python/testPython.py";
            Debug.Log(path);
            PythonRunner.RunFile(path);
            
        }
    }
}
