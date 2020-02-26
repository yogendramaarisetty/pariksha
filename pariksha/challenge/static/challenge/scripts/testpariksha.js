var lang = "Java";
ace.require("ace/ext/language_tools");
var editor = ace.edit("codeeditor");
editor.session.setMode("ace/mode/c_cpp");
editor.setTheme("ace/theme/xcode");
editor.setFontSize("14px");
editor.renderer.setScrollMargin(10, 10);
// enable autocompletion and snippets
editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});
![
    "dragenter", "dragover", "dragend", "dragstart", "dragleave", "drop"
].forEach(function(eventName) {
    editor.container.addEventListener(eventName, function(e) {
        e.stopPropagation()
    }, true)
});
editor.setOption("dragEnabled", false)