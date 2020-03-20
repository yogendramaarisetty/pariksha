
Split(['#left_pane', '#right_pane'], {
    gutterSize: 7,
    sizes: [36, 64],
    minSize: [200, 600]
});
setTimeout(function(){
    
    fullScreenOverlay();
    $(window).focus(function() {
        //do something
        $.LoadingOverlay("hide");
    });
    
    $(window).blur(function() {
       fullScreenOverlay();
    });
  
}, 2900);

var customElement = $("<span>", {
    "css"   : {
        "animation-duration":"5s",
        "color":"#0084ec",
    },
    "class" : "cogs slow-ani",
});

customElement[0].innerHTML = "<i class=\"fas fa-cog fa-4x fa-spin\" data-fa-transform=\"down-5  right-5\"></i><i class=\"fas fa-cog fa-3x fa-spin\" data-fa-transform=\"down-17 right-3\"></i><i class=\"fas fa-cog fa-5x fa-spin\" data-fa-transform=\"left-7\"></i>"
$.LoadingOverlay("show", {
    image       : "",
    fontawesome : "",                              // String/Boolean
fontawesomeAnimation    : ""  ,                              // String/Boolean
fontawesomeAutoResize   : true               ,               // Boolean
fontawesomeResizeFactor : 1                   ,              // Float
fontawesomeColor        : "#0084ec"            ,             // String/Boolean
fontawesomeOrder        : 2  ,
custom : customElement,
size                    : 50   ,                             // Float/String/Boolean
minSize                 : 20    ,                            // Integer/String
maxSize                 : 120    ,                           // Integer/String
// Misc
direction               : "column",                          // String
fade                    : [400, 200],                        // Array/Boolean/Integer/String
resizeInterval          : 50         ,                       // Integer
zIndex                  : 2147483647                        // Integer

});
var current_question_index;
// Hide it after 3 seconds
setTimeout(function(){
    $.LoadingOverlay("hide");
    $('.ql_item')[0].click();
    current_question_index=0;
}, 2500);

document.onfullscreenchange = function ( event ) { 
    if (!document.fullscreenElement) {
        fullScreenOverlay();
    } else {
        $.LoadingOverlay("hide");
    }
  }; 
  $(document).on("keydown",function(ev){
	// console.log(ev.keyCode);
	if(ev.keyCode===27||ev.keyCode===122) return false
});

function fullscreencount(){
        $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: csrf_token,
                full_screen: 'yes',
              },
        
            success: function(json) {
                
            },
            
            statusCode: {
            500: function() {
        }},
        }).done(function() {
        });
  }

function fullScreenOverlay(){
    var customElement2 = $("<button>", {
        "css"   : {
            "color":"#0084ec",
        },
        "class" : "full_screen_button",
        "id":"full_screen_button"
    });
    customElement2[0].innerHTML = "Full Screen"
    $.LoadingOverlay("show", {
        image       : "",
        fontawesome : "",                              // String/Boolean
    fontawesomeAnimation    : ""  ,                              // String/Boolean
    fontawesomeAutoResize   : true               ,               // Boolean
    fontawesomeResizeFactor : 1                   ,              // Float
    fontawesomeColor        : "#0084ec"            ,             // String/Boolean
    fontawesomeOrder        : 2  ,
    custom : customElement2,
    background: "#242d38cc",
    size                    : 50   ,                             // Float/String/Boolean
    minSize                 : 20    ,                            // Integer/String
    maxSize                 : 120    ,                           // Integer/String
    // Misc
    direction               : "column",                          // String
    fade                    : [400, 200],                        // Array/Boolean/Integer/String
    resizeInterval          : 50         ,                       // Integer
    zIndex                  : 2147483647                        // Integer
    
    });
    customElement2.on('click',function(){

        document.documentElement.requestFullscreen();
        $.LoadingOverlay("hide");
    });
    fullscreencount();
}

//ace_editor##############################3



//splitjs*************


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
    editor.addEventListener('click', function(){ editor.resize(); 
        // console.log('clicked');
    }); 
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
                $('#loader').hide();
               errorNotify(status);
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

  function InvokeLoader(){
    if($('link[title=darkmode]')[0].disabled ==  false){
        $("#top_section").LoadingOverlay("show",{
            image       : "",
            fontawesome : "fas fa-cog fa-spin",                              // String/Boolean
        fontawesomeAnimation    : ""  ,                              // String/Boolean
        fontawesomeAutoResize   : true               ,               // Boolean
        fontawesomeResizeFactor : 1                   ,              // Float
        fontawesomeColor        : "#0084ec"            ,             // String/Boolean
        fontawesomeOrder        : 2  ,
        background  : "#242d38cc",
        size                    : 30   ,                             // Float/String/Boolean
        minSize                 : 20    ,                            // Integer/String
        maxSize                 : 50    , 
        });
        
    }
    else{
        $("#top_section").LoadingOverlay("show",{
            image       : "",
            fontawesome : "fas fa-cog fa-spin",                              // String/Boolean
        fontawesomeAnimation    : ""  ,                              // String/Boolean
        fontawesomeAutoResize   : true               ,               // Boolean
        fontawesomeResizeFactor : 1                   ,              // Float
        fontawesomeColor        : "#4e4e4e"            ,             // String/Boolean
        fontawesomeOrder        : 2  ,
        background  : "#ffffffc2",
        
        size                    : 30   ,                             // Float/String/Boolean
        minSize                 : 20    ,                            // Integer/String
        maxSize                 : 50    , 
        });

    }

  }
  $('.prev_q').click(function(){
    if(current_question_index == 0){
        $('.ql_item')[$('.ql_item').size()-1].click();
    }
    else{
    $('.ql_item')[current_question_index-1].click();
    }
  });
  $('.next_q').click(function(){
    if(current_question_index == $('.ql_item').size()-1){
        $('.ql_item')[0].click();
    }
    else{
    $('.ql_item')[current_question_index+1].click();
    }
  });
$('.ql_item').click(function(){
    $('#input')[0].value = "";
    $('#sample_case_wrap')[0].innerHTML = "Click on run to see the output";
//   console.log("qustion item number = "+ a);
    $('#q_list').hide();
    editor = createEditor();
    InvokeLoader();
    $('.left_section').show();
    if(active_question_id != this.id){
        fetchCandidateCodes(this.id);
        active_question_id = this.id;
    }
    $('#sample_case_wrap')[0].innerHTML = "click on run to see the output"
    $('.question_content_wrapper').hide();
    var id = this.id;
    id = "question_"+id+"_id";
    question_desc = document.getElementById(id);
    question_desc.style.display = 'block';
    
   current_question_index = parseInt( $( "li" ).index( this ));
   $('#q_title').text(current_question_index+1 +". " +this.innerText);
    setTimeout(function(){
        $("#top_section").LoadingOverlay("hide");
    }, 900);
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
   
    $(".run_button").attr("disabled", true);
  $(".submit_button").attr("disabled", true);

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

           
        },
        error: function ( xhr, status, error) {
            $('#loader').hide();
            errorNotify(status);
          }
    }).done(function() {
        
    $(".run_button").attr("disabled", false);
  $(".submit_button").attr("disabled", false);

        $('#sample_case_wrap')[0].innerHTML = "Click on run to see the output";
        
    });

}

function selectLang(){
    InvokeLoader()
    update_editor_mode_and_code();
    $("#top_section").LoadingOverlay("hide");
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
    // console.log("dragged");
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
    $(".run_button").attr("disabled", true);
  $(".submit_button").attr("disabled", true);

    if($(".run_button").attr("disabled") == "disabled"){
   
    $('#output_card').hide();
    $('#loader').show();
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
                
                $(".run_button").attr("disabled", false);
  $(".submit_button").attr("disabled", false);

                $('#save_btn')[0].setAttribute('status','saved');
                
                if(json['status'] == "Compilation Errors"){
                    renderErrorMsg(json);
                }
                else if(json['sample_cases'] == "yes"){
                    renderSampleCases(json);
                }
                else if(json == {}){
                    var a = json;
                }
                else if(json['custom_output']['status'] == "Successfully ran" ||json['custom_output']['status'] == "Run Time Errors" || json['custom_output']['status'] == "Timelimit exception"){
                    renderSuccessOutput(json['custom_output']);
                }
                
                // $('#output_card').show();   
            $('#loader').hide();
            
    $(".run_button").attr("disabled", false);
  $(".submit_button").attr("disabled", false);

            },
            
            error: function ( xhr, status, error) {
                $('#loader').hide();
            errorNotify(status);
              }
        }).done(function() {
            
    $(".run_button").attr("disabled", false);
  $(".submit_button").attr("disabled", false);

        });
    } else {
        $('#output').html("Don't submit empty code");
    }
    
    }
}
function renderSampleCases(json){
    $('#sample_case_wrap')[0].innerHTML="";
    $('#sample_case_wrap');
    for(var i =0 ; i<Object.keys(json).length-1;i++){
        var msg=json[i];
        var resp="";
        if(msg['status'] == 'Passed' || msg['status'] == 'Failed'){
            resp = msg['Your Output']['output'];
        }
        else if(msg['status'] == 'Timelimit exception' || msg['status'] == 'Run Time Errors'){
            resp = msg['Your Output']['error'];
        }
        var card = "<div class=\"item\"></div>"
        var status = "<h4 status=\""+msg['status']+"\">"+msg['status']+"</h4>"
        var st_label_input = "<div class='label_input_wrap'><label class='sample_label' for=\"tc_input\">Input</label>"
        var tc_input = "<pre  class='sample_pre' name=\"tc_input\" id=\"tc_input\" disabled>"+msg['Input']+"</pre></div>"
        var st_label_output =  "<div class='label_input_wrap'><label class='sample_label' for=\"your_output\">Your Output</label>"
        var your_output = "<pre class='sample_pre' name=\"your_output\" id=\"your_output\" disabled>"+resp+"</pre></div>"
        var st_label_exp_output = "<div class='label_input_wrap'><label class='sample_label' for=\"expected_output\">Expected Output</label>"
        var expected_output = "<pre class='sample_pre' name=\"expected_output\" id=\"expected_output\" disabled>"+msg['Expected Output']+"</pre></div>"
        $('#sample_case_wrap')[0].innerHTML += status+st_label_input+tc_input+st_label_output+your_output+st_label_exp_output+expected_output;
    }
    $('#output_result_pre')[0].innerText = json;
}
function submitCode(){
    
    $(".run_button").attr("disabled", true);
  $(".submit_button").attr("disabled", true);

    if($('.submit_button').attr('disabled') == "disabled") {
        $('#testcases_pane').click();
    $('#testcases_card').hide();
    $('#output_card').hide();
    $('#loader').show();
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
                
             $(".run_button").attr("disabled", false);
  $(".submit_button").attr("disabled", false);

                 
             },
             error: function ( xhr, status, error) {
                $('#loader').hide();
                errorNotify(status);
                  },
             
         }).done(function() {
     $('#loader').hide();
         });
     } else {
     }
    }
 }

function errorNotify(status){
    toastr.options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
      }
    toastr["error"]("Something went wrong", "Server Error");

    toastr.options = {
      "closeButton": false,
      "debug": false,
      "newestOnTop": false,
      "progressBar": false,
      "positionClass": "toast-top-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
    };
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
 
function renderSuccessOutput(msg){
    $('#sample_case_wrap')[0].innerHTML="";
    var resp="";
    if(msg['status'] == 'Passed' || msg['status'] == 'Failed'|| msg['status'] =="Successfully ran"){
        resp = msg['output'];
    }
    else if(msg['status'] == 'Timelimit exception' || msg['status'] == 'Run Time Errors'){
        resp = msg['error'];
    }
    var status = "<h4 status=\""+msg['status']+"\">"+msg['status']+"</h4>"
    var st_label_input = "<div class='label_input_wrap'><label class='sample_label' for=\"tc_input\">Custom Input</label>"
    var tc_input = "<pre  class='sample_pre' name=\"tc_input\" id=\"tc_input\" disabled>"+msg['custom_input']+"</pre></div>"
    var st_label_output =  "<div class='label_input_wrap'><label class='sample_label' for=\"your_output\">Your Output</label>"
    var your_output = "<pre class='sample_pre' name=\"your_output\" id=\"your_output\" disabled>"+resp+"</pre></div>"

    var note="<p class='small_note'>Expected output will not be shown for Custom inputs</p><br><small>Remove Custom input to see sample testcases</small>"
    var s = "" +msg['Timetaken']+"";
     s= s.substring(0, 6)
    var time_elapsed = "<div id=\"time_elapsed\"><i id=\"time_icon\" class=\"material-icons\">access_time</i> <b>Time Taken</b> : "+ s +" Seconds</div>" ;
    $('#sample_case_wrap')[0].innerHTML += status+time_elapsed+st_label_input+tc_input+st_label_output+your_output+note;
}
function renderErrorMsg(msg){
    $('#sample_case_wrap')[0].innerHTML ="";
    var status = "<h4 status=\""+msg['status']+"\">"+msg['status']+"</h4>"
    var error_msg = "<pre  class='sample_pre err' name=\"error_msg\" id=\"tc_input\" disabled>"+msg['error']+"</pre></div>"
    $('#sample_case_wrap')[0].innerHTML += status+error_msg;
}

// function renderRuntimeError(error, time){
//     $('#status_message')[0].innerHTML = "";
//     $('#status_message')[0].innerText = "Runtime Error";
//     $('#status_message')[0].setAttribute('status','rterror');
//     $('#output_result_pre')[0].innerText = error;
//     $('#output_result_pre')[0].setAttribute('status','rtrror');
//     var time_elapsed = document.createElement('div');
//     time_elapsed.id = "timetaken";
//     var s = "" +time+"";
//      s= s.substring(0, 6)
//     time_elapsed.innerHTML = "<i id=\"time_icon\" class=\"material-icons\">access_time</i> <b>Time Taken</b> : "+ s +" Seconds" ;
//     $('#time_elapsed')[0].appendChild(time_elapsed);
// }
// function renderTLE(msg, time){
//     $('#status_message')[0].innerHTML = "<i id=\"tleico\"class=\"material-icons\">timer_off</i> <b> TLE (Time Limit Exception)</b>";
//     $('#status_message')[0].setAttribute('status','tle');
//     $('#output_result_pre')[0].innerText = msg;
//     $('#output_result_pre')[0].setAttribute('status','tle');
//     var time_elapsed = document.createElement('div');
//     time_elapsed.id = "timetaken";
//     var s = "" +time+"";
//      s= s.substring(0, 6)
//     time_elapsed.innerHTML = "<i id=\"time_icon\" class=\"material-icons\">access_time</i> <b>Time Taken</b> : "+ s +" Seconds" ;
//     $('#time_elapsed')[0].appendChild(time_elapsed);

// }



$(".nav_btns").click(function() {
    $('.response_cards').hide();
    document.getElementById(this.getAttribute('data')).style.display="block";
    if (current_active != this) {
        this.className = "nav_btns_active";
        // console.log(this.getAttribute('data'));
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