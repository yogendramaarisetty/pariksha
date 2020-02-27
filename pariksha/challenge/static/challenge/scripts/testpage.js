var lang = "Java";
ace.require("ace/ext/language_tools");
var editor = ace.edit("codeeditor");
editor.session.setMode("ace/mode/c_cpp");
editor.setTheme("ace/theme/textmate");
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
// editor.setOption("dragEnabled", false)
/*editor.commands.addCommand({
    name: "breakTheEditor", 
    bindKey: "ctrl-c|ctrl-v|ctrl-x|ctrl-shift-v|shift-del|cmd-c|cmd-v|cmd-x", 
    exec: function() {} 
});*/
// editor.setOptions({
//     maxLines: Infinity
// });
editor.setOptions({
    fontSize: "11pt"
});

$(document).ready(function() {
    // executes when HTML-Document is loaded and DOM is ready
   });
   
   var current_active = "";
   $(window).load(function() {
    // executes when complete page is fully loaded, including all frames, objects and images
   $(".nav_btns")[2].click();
   });
$(".nav_btns").click(function(){
    if(current_active != this){
    
    this.className = "nav_btns_active";
    console.log(this.getAttribute('data'));
    current_active.className = "nav_btns";
    current_active = this;
    }
  });

  