// ace editor*******************************

//ace_editor##############################3

//splitjs*************
Split(['#left_pane', '#right_pane'], {
    gutterSize: 7,
    sizes: [40, 60],
    minSize: [200, 600]
});

var sizes = localStorage.getItem('split-sizes')

if (sizes) {
    sizes = JSON.parse(sizes)
} else {
    sizes = [50, 50] // default sizes
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

var active_question_id = "";
// cosole buttons*******************************
var current_active = "";
$(document).ready(function() {
    // executes when HTML-Document is loaded and DOM is ready
    $('#loader').hide();
    $('.question_content_wrapper').hide();
    
    $('.left_section').hide();
    $('.response_cards').hide();
});
var initial_output_state = document.getElementById('output_card');
//###########################################################################
//window load
$(window).load(function() {
  

    // executes when complete page is fully loaded, including all frames, objects and images
    $('#loader').hide();
    $('.question_content_wrapper').hide();
    
    $('.left_section').hide();
    $('.response_cards').hide();
    $(".nav_btns")[2].click();
    var sizes = splitV.getSizes();
    if (sizes[1] < 20) {
        var icon = $('#up_down');
        icon = icon[0];
        icon.innerText = "keyboard_arrow_up";
    }
   
    $('.ql_item')[0].click();
});

function createEditor(){
    ace.require("ace/ext/language_tools");
    editor = ace.edit("codeeditor");
    editor.session.setMode("ace/mode/c_cpp");
    if($('#mode')[0].checked){
    editor.setTheme("ace/theme/monokai");
    }
    else{
    editor.setTheme("ace/theme/textmate");
    }
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
    /*editor.commands.addCommand({
        name: "breakTheEditor", 
        bindKey: "ctrl-c|ctrl-v|ctrl-x|ctrl-shift-v|shift-del|cmd-c|cmd-v|cmd-x", 
        exec: function() {} 
    });*/
    // editor.setOptions({
    //     maxLines: Infinity
    // });]
    editor.setOptions({
        fontSize: "11pt"
    });
    editor.addEventListener('click', function(){ editor.resize(); console.log('clicked');}); 
    editor.commands.addCommand({
        name: 'save',
        bindKey: {win: "Ctrl-S", "mac": "Cmd-S"},
        exec: function(editor) {

            codeDraft();
        }
    })
    editor.commands.addCommand({
        name: 'run',
        bindKey: {win: "Ctrl-L", mac: "Command-Option-F"},
        exec: function(editor) {
            runCode();
        }
    })
    editor.addEventListener("keydown", function(event) {
        event.preventDefault();
        switch (event.which) {
          case 120:
            runCode();
            break;
        }
      })
editor.getSession().on('change', function() {
    // setTimeout(500);
    lang = document.getElementById("languages").value;
      if (lang == "Java") {
        if(java_code!=editor.getValue()){
            $('#save_btn')[0].setAttribute('status','unsaved');
        }
        else{
            $('#save_btn')[0].setAttribute('status','saved');
        }
      }
      if (lang == "Python") {
        if(python_code!=editor.getValue()){
            $('#save_btn')[0].setAttribute('status','unsaved');
        }
        else{
            $('#save_btn')[0].setAttribute('status','saved');
        }
      }
      if (lang == "C") {
        if(c_code!=editor.getValue()){
            $('#save_btn')[0].setAttribute('status','unsaved');
        }
        else{
            $('#save_btn')[0].setAttribute('status','saved');
        }
      }
      if (lang == "C++") {
        if(cpp_code!=editor.getValue()){
            $('#save_btn')[0].setAttribute('status','unsaved');
        }
        else{
            $('#save_btn')[0].setAttribute('status','saved');
        }
      }
      if (lang == "C#") {
        if(csharp_code!=editor.getValue()){
            $('#save_btn')[0].setAttribute('status','unsaved');
        }
        else{
            $('#save_btn')[0].setAttribute('status','saved');
        }
      }
    
  });
  return editor;
}

function updateVariables(lang){
    if(lang=="C"){
            c_code = editor.getValue()
          }
          else if(lang=="C++"){
            cpp_code = editor.getValue()
          }
          else if(lang=="Python"){
            python_code = editor.getValue()
          }
          else if(lang=="C#"){
            csharp_code = editor.getValue()
          }
          else if(lang=="Java"){
            java_code = editor.getValue()
          }
  }

function codeDraft(){
    if($('#save_btn')[0].getAttribute('status') !="saved"){
     var lang = document.getElementById("languages").value;
          $.ajax({
              type: 'POST',
              url: '',
              dataType: 'json',
              cache: false,
              async: true,
              data: {
                  csrfmiddlewaretoken: csrf_token,
                  code_draft: 'yes',
                  code: editor.getValue(),
                  language: document.getElementById("languages").value,
                  q_id: active_question_id,
              },
              success: function(json) {
                
                     updateVariables(lang);
                     $('#save_btn')[0].setAttribute('status','saved');
              },
              error: function ( xhr, status, error) {
                // console.log( " xhr.responseText: " + xhr.responseText + " //status: " + status + " //Error: "+error );
      
              }
          }).done(function() {
          });
        }
  }
 
$('#finish_button').on('click', function() {
  $.confirm({
    title: 'Finish Test',
    content: 'Are you sure you want to Finish the Test?',
    buttons: {
        Finish: function() {
            submitTest();
        },
        cancel: function() {
        },
    }
});
});

function submitTest(){
    $.ajax({
              type: 'POST',
              url: '',
              dataType: 'json',
              cache: false,
              async: true,
              data: {
                  csrfmiddlewaretoken: csrf_token,
                  submit_test:'yes',
              },
              success: function(json) {
                window.location.href =submission_page_url;
              },
          }).done(function() {
          });
  }

$('.ql_item').click(function(){
    
    $('#q_list').hide();
    editor = createEditor();
    
    $('.left_section').show();
    if(active_question_id != this.id){
        fetchCandidateCodes(this.id);
        active_question_id = this.id;
    }
    $('#status_message')[0].setAttribute('status','');
    $('#status_message')[0].innerHTML= "";

        $('#status_message')[0].innerText= "Click on run to see the output";
        $('#input')[0].innerText="";
        $('#type_msg')[0].innerHTML = "";
        $('#tc_body')[0].innerHTML = "";
        $('#time_elapsed')[0].innerHTML = "";
        $('#output_result_pre')[0].innerHTML = "";
    $('.question_content_wrapper').hide();
    var id = this.id;
    id = "question_"+id+"_id";
    question_desc = document.getElementById(id);
    question_desc.style.display = 'block';
});

var java_code;
var c_code;
var cpp_code;
var python_code;
var csharp_code;
var ace_modes = {
    'Java': ['ace/mode/java',java_code],
    'C': ['ace/mode/c_cpp', c_code],
    'Python': ['ace/mode/python', python_code],
    'C++':['ace/mode/c_cpp', cpp_code ],
    'C#': ['ace/mode/csharp',csharp_code],
}
  

function fetchCandidateCodes(id){
   
    $.ajax({
        type: 'POST',
        url: '',
        dataType: 'json',
        cache: false,
        async: true,
        data: {
            csrfmiddlewaretoken: csrf_token,
            msg : 'fetch_current_question_codes',
            current_question_id : id,
        },
        success: function(json) {
            $('.loader').hide();
            java_code=json.java;
            python_code=json.python;
            c_code=json.c;
            csharp_code=json.csharp;
            cpp_code=json.cpp;
            // document.getElementById("input").value = json.sample_input;
            update_editor_mode_and_code();

            $('#status_message')[0].innerHTML = initial_output_state.innerHTML;
            $('#input')[0].innerText="";
            $('#output_result_pre').innerText="";
            $('#type_msg').innerHTML = "";
            $('#tc_body').innerHTML = "";
        },
        error: function ( xhr, status, error) {
            // console.log( " xhr.responseText: " + xhr.responseText + " //status: " + status + " //Error: "+error );
  
          }
    }).done(function() {
        $('#status_message')[0].innerHTML= "";
        $('#status_message')[0].innerText= "Click on run to see the output";
        $('#input')[0].innerText="";
        $('#type_msg').innerHTML = "";
        $('#tc_body').innerHTML = "";
        $('#time_elapsed').innerHTML = "";
    });

}

function selectLang(){
    update_editor_mode_and_code();
}

function update_editor_mode_and_code(){
    var ace_modes = {
        'Java': ['ace/mode/java',java_code],
        'C': ['ace/mode/c_cpp', c_code],
        'Python': ['ace/mode/python', python_code],
        'C++':['ace/mode/c_cpp', cpp_code ],
        'C#': ['ace/mode/csharp',csharp_code],
    };
    var active_lang = $('#languages')[0].value;
    editor.getSession().setMode(ace_modes[active_lang][0]);
    editor.setValue(ace_modes[active_lang][1]);
}

function viewQuestionList(){
    $('.question_content_wrapper').hide();
    $('#q_list').show();
}

var draggerV = $(".gutter-vertical")[0];
draggerV.addEventListener("click", function(event) {
    editor.resize();
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

function runCode() {
    if(!$('.run_button')[0].disabled){
    $('#output_pane').click();
    $('#time_elapsed')[0].innerHTML = "";
    $('#output_card').hide();
    $('#loader').show();
    $('.run_button')[0].disabled = true;
    $('.submit_button')[0].disabled = true;
    if (editor.getValue() != "") {
        lang = document.getElementById("languages").value;
        updateVariables(lang);
        $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: csrf_token,
                compile_run: 'yes',
                code: editor.getValue(),
                input: $('#input').val(),
                language: document.getElementById("languages").value,
                q_id: active_question_id,
            },
            success: function(json) {
                $('#output_pane').click();
                $('.run_button')[0].disabled = false;
                $('.submit_button')[0].disabled = false;
                $('#save_btn')[0].setAttribute('status','saved');
                if(json.status == "Successfully ran"){
                    renderSuccessOutput(json.output,json.Timetaken);
                }
                else if(json.status == "Compilation Errors"){
                    renderErrorMsg(json.error);
                }
                else if (json.status == "Run Time Errors"){
                    renderRuntimeError(json.error,json.Timetaken);
                }
                else if(json.status == "Timelimit exception"){
                    renderTLE(json.error,json.Timetaken);
                }
                // $('#output_card').show();   
            $('#loader').hide();
            },
            
            error: function ( xhr, status, error) {
                // console.log( " xhr.responseText: " + xhr.responseText + " //status: " + status + " //Error: "+error );
                
            $('#loader').hide();
              }
        }).done(function() {
            $('#loader').hide();
        });
    } else {
        $('#output').html("Don't submit empty code");
    }
    
    }
}
function submitCode(){
    if(!$('.submit_button')[0].disabled){
        $('#testcases_pane').click();
    $('#testcases_card').hide();
    $('#output_card').hide();
    $('#loader').show();
    $('.run_button')[0].disabled = true;
    $('.submit_button')[0].disabled = true;
   if (editor.getValue() != "") {
         $.ajax({
             type: 'POST',
             url: '',
             dataType: 'json',
             cache: false,
             async: true,
             data: {
                 csrfmiddlewaretoken: csrf_token,
                 submit_code: 'yes',
                 code: editor.getValue(),
                 language: document.getElementById("languages").value,
                 q_id: active_question_id,
             },
 
             success: function(json) {
                $('#testcases_pane').click();
                $('.run_button')[0].disabled = false;
                $('.submit_button')[0].disabled = false;
                $('#save_btn')[0].setAttribute('status','saved');
                 if(json.status == "Compilation Errors"){
                    $('#output_pane').click();
                    renderErrorMsg(json.error);
                    
                }
                else{
                    
                    $('#tc_body')[0].innerHTML = "";
                    var result = json;
                    var numberOfTestCases = Object.keys(result).length;
                    $('#testcases_card').show();
                    for(var i =0;i<numberOfTestCases;i++){
                        var testCase = result[i];
                        addRow(testCase,i+1);
                    }
                    $('#testcase-table').show();
                }
                 
             },
             
         }).done(function() {
     $('#loader').hide();
         });
     } else {
     }
    }
 }

function addRow(json,num){
    var tc_body = $('#tc_body')[0];
    var row = document.createElement('tr');
    var time_val = ""+json['Time_taken'];
    time_val = time_val.substring(0,6);
    row.className = "tc_record";
    var testCaseNumber = document.createElement('td');
    var description = document.createElement('td');
    var status = document.createElement('td');
    var time = document.createElement('td');
    var status_icon = document.createElement('td');
    var score = document.createElement('td');
    testCaseNumber.innerText = "Testcase "+num;
    description.innerText = json['description'];
    status.innerText = json['status'];
    time.innerText = time_val;
    status.setAttribute('status',json['status']);
    status_icon.setAttribute('status',json['status']);
    score.innerText = json['score'];
 
    if(json['status'] == "Timelimit exception"){
        status_icon.innerHTML = "<div icon='status_icon' status='Timelimit exception'></div>";
    }
    else if(json['status'] == "Run Time Errors"){
        status_icon.innerHTML = "<div icon='status_icon' status='Run Time Errors'></div>";
    }
    else if(json['status'] == "Passed"){
        status_icon.innerHTML = "<div icon='status_icon' status='Passed'></div>";
    }
    else if(json['status'] == "Failed"){
        status_icon.innerHTML = "<div icon='status_icon' status='Failed'></div>";
    }
    row.appendChild(testCaseNumber);
    row.appendChild(description);
    row.appendChild(status);
    row.appendChild(status_icon);
    row.appendChild(time);
    row.appendChild(score);
    tc_body.appendChild(row);
}
 
function renderSuccessOutput(output, time){
    $('#status_message')[0].innerHTML = "";
    $('#status_message')[0].innerText = "Successfully ran";
    $('#status_message')[0].setAttribute('status','success');
    $('#output_result_pre')[0].innerText = output;
    $('#output_result_pre')[0].setAttribute('status','success');
    $('#type_msg')[0].innerText = 'Output';
     
    var time_elapsed = document.createElement('div');
    time_elapsed.id = "timetaken";
    var s = "" +time+"";
     s= s.substring(0, 6)
    time_elapsed.innerHTML = "<i id=\"time_icon\" class=\"material-icons\">access_time</i> <b>Time Taken</b> : "+ s +" Seconds" ;
    $('#time_elapsed')[0].appendChild(time_elapsed);
}
function renderErrorMsg(error){
    $('#status_message')[0].innerHTML = "";
    $('#status_message')[0].innerText = "Compilation Error";
    $('#status_message')[0].setAttribute('status','Error');
    $('#output_result_pre')[0].innerText = error;
    $('#output_result_pre')[0].setAttribute('status','Error');
}

function renderRuntimeError(error, time){
    $('#status_message')[0].innerHTML = "";
    $('#status_message')[0].innerText = "Runtime Error";
    $('#status_message')[0].setAttribute('status','rterror');
    $('#output_result_pre')[0].innerText = error;
    $('#output_result_pre')[0].setAttribute('status','rtrror');
    var time_elapsed = document.createElement('div');
    time_elapsed.id = "timetaken";
    var s = "" +time+"";
     s= s.substring(0, 6)
    time_elapsed.innerHTML = "<i id=\"time_icon\" class=\"material-icons\">access_time</i> <b>Time Taken</b> : "+ s +" Seconds" ;
    $('#time_elapsed')[0].appendChild(time_elapsed);
}
function renderTLE(msg, time){
    $('#status_message')[0].innerHTML = "<i id=\"tleico\"class=\"material-icons\">timer_off</i> <b> TLE (Time Limit Exception)</b>";
    $('#status_message')[0].setAttribute('status','tle');
    $('#output_result_pre')[0].innerText = msg;
    $('#output_result_pre')[0].setAttribute('status','tle');
    var time_elapsed = document.createElement('div');
    time_elapsed.id = "timetaken";
    var s = "" +time+"";
     s= s.substring(0, 6)
    time_elapsed.innerHTML = "<i id=\"time_icon\" class=\"material-icons\">access_time</i> <b>Time Taken</b> : "+ s +" Seconds" ;
    $('#time_elapsed')[0].appendChild(time_elapsed);

}



$(".nav_btns").click(function() {
    $('.response_cards').hide();
    document.getElementById(this.getAttribute('data')).style.display="block";
    if (current_active != this) {
        this.className = "nav_btns_active";
        console.log(this.getAttribute('data'));
        current_active.className = "nav_btns";
        current_active = this;
    }
});


// $('#ew').bind('resize', function(){
//     alert( 'Height changed to' + $(this).height() );
// });
$('#console_collapse').click(function() {
    editor.resize();
    var icon = $('#up_down');
    icon = icon[0];
    if (icon.innerText == "keyboard_arrow_down") {
        splitV.setSizes([100, 0]);
        editor.resize();
        icon.innerText = "keyboard_arrow_up";
    } else if (icon.innerText == "keyboard_arrow_up") {
        splitV.setSizes([70, 30]);
        editor.resize();
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
        $('link[title=darkmode]')[0].disabled = false;
    } else if (mode == "light") {
        editor.setTheme("ace/theme/textmate");
        $('.ace_gutter')[0].setAttribute('style', '');
        $('link[title=darkmode]')[0].disabled = true;
    }
}