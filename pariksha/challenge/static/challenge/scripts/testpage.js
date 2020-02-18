var java_code;
var c_code;
var cpp_code;
var python_code;
var csharp_code;
var active_question;
var first_q;
var req_question;
var testcases;
var admin_sidebar = document.getElementById('admin_sidebar');
admin_sidebar.style.display = 'none';
const myNotification = window.createNotification({
  
});


myNotification({
  // options here
  title: 'Title',
  message: 'Notification Message',
  closeOnClick: false,
  displayCloseButton: false,
  positionClass: 'nfc-top-right',
  onclick: false,
  showDuration: 13500,
  theme: 'success'
})
$(window).load(function() {
  $(function() {window.createNotification({
    closeOnClick: closeOnClick,
    displayCloseButton: displayClose,
    positionClass: position,
    showDuration: duration,
    theme: theme
  })({
    title: title,
    message: message
  });});
  document.getElementById("ovl").click();
  myNotification({ 


    
  });
});

// function for fullscreen overlay
$(function() {
  var $overlay = $('.overlay'),
      $overlayTrigger = $('.overlay-trigger button'),
      $overlayClose = $('.overlay-close'),
      openClass = 'is-open';

  $overlayTrigger.on('click', function() {
    var num = ('0' + ($(this).index() + 1)).slice(-2);
    $('.overlay' + num).addClass(openClass);
    $overlayClose.addClass(openClass);
  });

  $overlayClose.on('click', function() {
    $overlayClose.removeClass(openClass);
    $overlay.removeClass(openClass);
  });
});

//online offline status
$(function() {
const status = window.navigator.onLine;
if(status) online()
else offline()
window.addEventListener('online',online);
window.addEventListener('offline',offline);
function online(){
$('#internet').show();
$('#nointernet').hide();
}
function offline(){
$('#internet').hide();
$('#nointernet').show();
}
});
//fullscreen count call
function fullscreencount(){
  var action="fullscreen";
  var custom_json_data = {
        csrfmiddlewaretoken: CSRF_TOKEN,
        full_screen: 'yes',
      };
  ajax_call(custom_json_data,action)
  fullscreen();
}

if (r[3]=="testpage"){
  $("#logout").hide();
}
console.log(url_path);
function instructionPop() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
  }
  function instructionPop2() {
    var popup = document.getElementById("myPopup2");
    popup.classList.toggle("show");
  }
// Set the date we're counting down to
var countDownDate = new Date(end_time).getTime();
// Update the count down every 1 second
var x = setInterval(function() {
  // Get today's date and time
    var now = new Date().getTime();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;


    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
    document.getElementById("demo").innerHTML = +hours + " h : " +
        minutes + " m : " + seconds + " s";

    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "EXPIRED";
        submitTestFinal()
        
    }
}, 1000);

 function submitTestFinal(){
   submitTest();
        redirect();
 }
$(function() {
    var editor = ace.edit("codeeditor");
        session = editor.getSession();
        
});


var lang = "Java";
ace.require("ace/ext/language_tools");
var editor = ace.edit("codeeditor");
editor.session.setMode("ace/mode/c_cpp");
editor.setTheme("ace/theme/monokai");
editor.setFontSize("15px");
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
editor.setOptions({
    maxLines: Infinity
});

function redirect(){
 window.location.href = "{% url 'submittedpage' challenge_id=challenge.id c_id=candidate.id %}";
            
}
editor.commands.addCommand({
    name: 'save',
    bindKey: {win: "Ctrl-S", "mac": "Cmd-S"},
    exec: function(editor) {
      if($('#save').html()!='saved'){
        codeDraft();
      }
    }
})

function submitTest(){
  $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: CSRF_TOKEN,
                submit_test:'yes',
                c_id: candidate_id ,
            },
            success: function(json) {
                $('.loader').hide();
            },
        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;
            console.log(ajaxSecs2, " seconds");
        });
        
           


}

sidelist = document.getElementsByClassName("sidebar-link collapsed");
active_question= sidelist[0];
function openQuestion(evt, questionName, q_id) {
  fullscreen();
    var i, tabcontent, tablinks;
    active_question.className="sidebar-link collapsed";
    req_question = q_id;
    //var prev = document.getElementsByClassName("sidebar-link collapsed active");
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    getQuestions(q_id,questionName);
    
}
$(window).load(function() {
  
});
editor.getSession().on('change', function() {
  setTimeout(500);
  
  lang = document.getElementById("language").value;
    if (lang == "Java") {
      if(java_code!=editor.getValue()){
        $('#save').html('Ctrl + S');
        $('#saveico').hide();
      }
      else{
         $('#save').html('saved');
        $('#saveico').show();
      }
    }
    if (lang == "Python") {
      if(python_code!=editor.getValue()){
        $('#save').html('Ctrl + S');
        $('#saveico').hide();
      }
      else{
         $('#save').html('saved');
        $('#saveico').show();
      }
    }
    if (lang == "C") {
      if(c_code!=editor.getValue()){
        $('#save').html('Ctrl + S');
        $('#saveico').hide();
      }
      else{
         $('#save').html('saved');
        $('#saveico').show();
      }
    }
    if (lang == "C++") {
      if(cpp_code!=editor.getValue()){
        $('#save').html('Ctrl + S');
        $('#saveico').hide();
      }
      else{
         $('#save').html('saved');
        $('#saveico').show();
      }
    }
    if (lang == "C#") {
      if(csharp_code!=editor.getValue()){
        $('#save').html('Ctrl + S');
        $('#saveico').hide();
      }
      else{
         $('#save').html('saved');
        $('#saveico').show();
      }
    }
  
});
function codeDraft(){
  var ajaxMins = new Date().getMinutes();
        var ajaxSecs = new Date().getSeconds();
        var ajaxMS = new Date().getMilliseconds();
  $('#save').html('saving..');
  $('#saveico').hide();
   lang = document.getElementById("language").value;
        updateVariables(lang);
        $('#output').html("");
        $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: CSRF_TOKEN,
                code_draft: 'yes',
                code: editor.getValue(),
                input: $('#input').val(),
                language: document.getElementById("language").value,
                q_id: req_question,
            },
            success: function(json) {
                 $('#save').html('saved');
                 $('#saveico').show();
                  $('#internet').show();
                  
            $('#nointernet').hide();

            },
            
            statusCode: {
            500: function() {
             $('#internet').hide();
             $('#nointernet').show();
              $('#save').html('offline');
        }},
        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;
            console.log(ajaxSecs2, " seconds");
            $('.loader').hide();
        });

}
function getQuestions(q_id,questionName){
  
      var sample_input ="{{q.sample_inputs|safe}}";
      document.getElementById("input").value = sample_input;
        var ajaxMins = new Date().getMinutes();
        var ajaxSecs = new Date().getSeconds();
        var ajaxMS = new Date().getMilliseconds();
        $('#testcase-table').hide();

    $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: CSRF_TOKEN,
                question:'yes',
                q_id: q_id,
            },
            success: function(json) {
                $('.loader').hide();
                java_code=json.java;
                python_code=json.python;
                c_code=json.c;
                csharp_code=json.csharp;
                cpp_code=json.cpp;
                document.getElementById("input").value = json.sample_input;
                selectLang();
                document.getElementById(questionName).style.display = "block";
                active_question = document.getElementById(q_id);
                active_question.className = "sidebar-link collapsed active";
            },
            statusCode: {
            500: function() {
            $('.loader').hide();
            $('#testcase-table').hide();
            alert("Server is not responding");
        }},
        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;
            $('.loader').hide();
            console.log(ajaxSecs2, " seconds");
        });
}


function selectLang() {

    lang = document.getElementById("language").value;
 
    if (lang == "Java") {
      editor = ace.edit("codeeditor");
        editor.getSession().setMode("ace/mode/java");
        if(editor.getValue()==java_code){
          $('#save').html('saved');
          $('#saveico').show();
        }
        else{
        editor.setValue(java_code);
        }
    } else if (lang == "C" ) {
      editor = ace.edit("codeeditor");
        editor.getSession().setMode("ace/mode/c_cpp"); 
         if(editor.getValue()==c_code){
          $('#save').html('saved');
          $('#saveico').show();
        }
        else{
        editor.setValue(c_code);
        }
    }
      else if(lang == "C++" ){
        editor = ace.edit("codeeditor");
        editor.getSession().setMode("ace/mode/c_cpp");
          if(editor.getValue()==cpp_code){
          $('#save').html('saved');
          $('#saveico').show();
        }
        else{
        editor.setValue(cpp_code);
        }
      } 
    else if (lang == "C#") {
      editor = ace.edit("codeeditor");
        editor.getSession().setMode("ace/mode/csharp");
         if(editor.getValue()==csharp_code){
          $('#save').html('saved');
          $('#saveico').show();
        }
        else{
        editor.setValue(csharp_code);
        }
    } else if (lang == "Python") {
      editor = ace.edit("codeeditor");
        editor.getSession().setMode("ace/mode/python");
          if(editor.getValue()==python_code){
          $('#save').html('saved');
          $('#saveico').show();
        }
        else{
        editor.setValue(python_code);
        }

    }
    
}
function runCode() {

    if (editor.getValue() != "") {
        $('.loader').show();
        var ajaxMins = new Date().getMinutes();
        var ajaxSecs = new Date().getSeconds();
        var ajaxMS = new Date().getMilliseconds();
        lang = document.getElementById("language").value;
        updateVariables(lang);
        $('#output').html("");
        $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: CSRF_TOKEN,
                compile_run: 'yes',
                code: editor.getValue(),
                input: $('#input').val(),
                language: document.getElementById("language").value,
                q_id: req_question,
            },
            success: function(json) {
                $('.loader').hide();
                $('#output').html(json.msg);
            },
            
            statusCode: {
            500: function() {
            $('.loader').hide();
            $('#testcase-table').hide();
        }},
        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;
            console.log(ajaxSecs2, " seconds");
            $('.loader').hide();
            $('#save').html('saved');
            $('#saveico').show();
        });
    } else {
        $('#output').html("Don't submit empty code");
    }
}

function submitCode(){
   $('#testcase-table').show();
  if (editor.getValue() != "") {
        $('.loader').show();
        var ajaxMins = new Date().getMinutes();
        var ajaxSecs = new Date().getSeconds();
        var ajaxMS = new Date().getMilliseconds();
        lang = document.getElementById("language").value;
        updateVariables(lang);
        $('#output').html("");
        
        htmlloader="<img class='status-icon' src='/static/img/spinner.gif' alt='Loading...'>"
        $('#tcdescription1').html(htmlloader);
                $('#tcdescription2').html(htmlloader);
                $('#tcdescription3').html(htmlloader);
                $('#tcdescription4').html(htmlloader);
                $('#tcdescription5').html(htmlloader);
                $('#tcstatus1').html(htmlloader);
                $('#tcstatus2').html(htmlloader);
                $('#tcstatus3').html(htmlloader);
                $('#tcstatus4').html(htmlloader);
                $('#tcstatus5').html(htmlloader);
                $('#tcscore1').html(htmlloader);
                $('#tcscore2').html(htmlloader);
                $('#tcscore3').html(htmlloader);
                $('#tcscore4').html(htmlloader);
                $('#tcscore5').html(htmlloader);
                
        $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: CSRF_TOKEN,
                submit_code: 'yes',
                code: editor.getValue(),
                language: document.getElementById("language").value,
                q_id: req_question,
            },

            success: function(json) {
                $('.loader').hide();
                $('#tcdescription1').html(json.tcdescription1);
                $('#tcdescription2').html(json.tcdescription2);
                $('#tcdescription3').html(json.tcdescription3);
                $('#tcdescription4').html(json.tcdescription4);
                $('#tcdescription5').html(json.tcdescription5);
                $('#tcstatus1').html(json.tcstatus1);
                $('#tcstatus2').html(json.tcstatus2);
                $('#tcstatus3').html(json.tcstatus3);
                $('#tcstatus4').html(json.tcstatus4);
                $('#tcstatus5').html(json.tcstatus5);
                $('#tcscore1').html(json.tcscore1);
                $('#tcscore2').html(json.tcscore2);
                $('#tcscore3').html(json.tcscore3);
                $('#tcscore4').html(json.tcscore4);
                $('#tcscore5').html(json.tcscore5);
                
            },
            
            statusCode: {
            500: function() {
            $('.loader').hide();
            $('#testcase-table').hide();
        }},
        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;
            console.log(ajaxSecs2, " seconds",ajaxMS2, " milli seconds");
            $('.loader').hide();
            $('#save').html('saved');
            $('#saveico').show();
        });
    } else {
        $('#output').html("Don't submit empty code");
    }

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


function ajax_call(custom_json_data,action){
  var ajaxMins = new Date().getMinutes();
  var ajaxSecs = new Date().getSeconds();
  var ajaxMS = new Date().getMilliseconds();
  $.ajax({
    type: 'POST',
    url: '',
    dataType: 'json',
    cache: false,
    async: true,
    data: custom_json_data,

    success: function(json) {
        
    },
    
    statusCode: {
    500: function() {
    $('.loader').hide();
    $('#testcase-table').hide();
}},
}).done(function() {
    var ajaxMins2 = new Date().getMinutes() - ajaxMins;
    var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
    var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;
    console.log(ajaxSecs2, " seconds",ajaxMS2, " milli seconds");
    $('.loader').hide();
    $('#save').html('saved');
    $('#saveico').show();
});
}