// ace editor*******************************

//ace_editor##############################3

//splitjs*************
Split(['#left_pane', '#right_pane'], {
    gutterSize: 13,
    sizes: [40, 60],
    minSize: [200, 600]
});

var sizes = localStorage.getItem('split-sizes')

if (sizes) {
    sizes = JSON.parse(sizes)
} else {
    sizes = [90, 10] // default sizes
}

var splitV = Split(['#top_section', '#bottom_section'], {
    gutterSize: 7,
    sizes: [90, 10],
    direction: 'vertical',
    minSize: 40,
    sizes: sizes,
    onDragEnd: function(sizes) {
        localStorage.setItem('split-sizes', JSON.stringify(sizes))
    },
});
//splitjs###################

var lang = "Java";
var editor;

// cosole buttons*******************************
var current_active = "";
$(window).load(function() {
    // executes when complete page is fully loaded, including all frames, objects and images
    $(".nav_btns")[2].click();
    var sizes = splitV.getSizes();
    if (sizes[1] < 20) {
        var icon = $('#up_down');
        icon = icon[0];
        icon.innerText = "keyboard_arrow_up";
    }
    ace.require("ace/ext/language_tools");
    editor = ace.edit("codeeditor");
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
});

var draggerV = $(".gutter-vertical")[0];
draggerV.addEventListener("click", function(event) {
    var s = splitV.getSizes();
    console.log("dragged");
    if (s[1] < 25) {
        var icon = $('#up_down');
        icon = icon[0];
        icon.innerText = "keyboard_arrow_up";
    } else if (s[1] > 25) {
        var icon = $('#up_down');
        icon = icon[0];
        icon.innerText = "keyboard_arrow_down";
    }
});

$(".nav_btns").click(function() {
    if (current_active != this) {

        this.className = "nav_btns_active";
        console.log(this.getAttribute('data'));
        current_active.className = "nav_btns";
        current_active = this;
    }
});
$('#console_collapse').click(function() {
    var icon = $('#up_down');
    icon = icon[0];
    if (icon.innerText == "keyboard_arrow_down") {
        splitV.setSizes([100, 0]);
        icon.innerText = "keyboard_arrow_up";
    } else if (icon.innerText == "keyboard_arrow_up") {
        splitV.setSizes([70, 30]);
        icon.innerText = "keyboard_arrow_down";
    }


})

// cosole buttons#########################3333
$('#mode').change(function() {
    if (this.checked) {
        set_ace_editor_mode("dark");
    } else {
        set_ace_editor_mode("light");
    }
});

function set_ace_editor_mode(mode) {
    if (mode == "dark") {
        editor.setTheme("ace/theme/monokai");
        $('.ace_gutter')[0].setAttribute('style', 'background:#272822 !important');
        $(".ace_gutter-active-line")[0].style.color = "#00a8cc";
        $('link[title=darkmode]')[0].disabled = false;
    } else if (mode == "light") {
        editor.setTheme("ace/theme/textmate");
        $('.ace_gutter')[0].setAttribute('style', '');
        $(".ace_gutter-active-line")[0].style.color = "#0056a8";
        $('link[title=darkmode]')[0].disabled = true;
    }
}