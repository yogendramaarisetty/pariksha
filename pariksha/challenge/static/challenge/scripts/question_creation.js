
var c_editor,cpp_editor,csharp_editor,java_editor,python_editor;
c_editor = ace.edit("id_default_c_code");
c_editor.session.setMode("ace/mode/c_cpp");
c_editor.setTheme("ace/theme/textmate");
c_editor.renderer.setScrollMargin(10, 10);
// enable autocompletion and snippets
c_editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});

c_editor.on("change", function() {
    c_editor.resize();
});


cpp_editor = ace.edit("id_default_cpp_code");
cpp_editor.session.setMode("ace/mode/c_cpp");
cpp_editor.setTheme("ace/theme/textmate");
cpp_editor.renderer.setScrollMargin(10, 10);
// enable autocompletion and snippets
cpp_editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});
cpp_editor.on("change", function() {
    cpp_editor.resize();
});


csharp_editor = ace.edit("id_default_csharp_code");
csharp_editor.session.setMode("ace/mode/csharp");
csharp_editor.setTheme("ace/theme/textmate");
csharp_editor.renderer.setScrollMargin(10, 10);
// enable autocompletion and snippets
csharp_editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});
csharp_editor.on("change", function() {
    csharp_editor.resize();
});



java_editor = ace.edit("id_default_java_code");
java_editor.session.setMode("ace/mode/java");
java_editor.setTheme("ace/theme/textmate");
java_editor.renderer.setScrollMargin(10, 10);
// enable autocompletion and snippets
java_editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});
java_editor.on("change", function() {
    java_editor.resize();
});


python_editor = ace.edit("id_default_python_code");
python_editor.session.setMode("ace/mode/python");
python_editor.setTheme("ace/theme/textmate");
python_editor.renderer.setScrollMargin(10, 10);
// enable autocompletion and snippets
python_editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});
python_editor.on("change", function() {
    python_editor.resize();
});