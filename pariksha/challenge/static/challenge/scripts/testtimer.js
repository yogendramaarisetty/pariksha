
  const status = window.navigator.onLine;
  if(status) online()
  else offline()
  window.addEventListener('online',online);
  window.addEventListener('offline',offline);
  function online(){
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
    toastr["success"]("you are online", "Online");
  }
  function offline(){
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

    toastr["warning"]("you are offline", "No Internet");
  }
  
window.addEventListener('offline', function(e) { 

 
 });

window.addEventListener('online', function(e) { 
  
});

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
    document.getElementById("timer").innerHTML = +hours + " h : " +
        minutes + " m : " + seconds + " s";

    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("timer").innerHTML = "EXPIRED";
        //submitTestFinal()
        
    }
}, 1000);

var left_down = document.getElementsByClassName('top_controller_bar')[0];
new ResizeSensor(left_down, function() {
    if(left_down.clientWidth < 434){
      $('.change_q')[0].innerHTML = "<i class=\"fas fa-list\"></i>";
      $('.q_navigator')[0].style.fontSize = "small";
      $('#q_title')[0].style.fontSize = "small";
    }
    else{
      $('.change_q')[0].innerHTML = "<i class=\"fas fa-list\"></i> Change Question";
      $('.q_navigator')[0].style.fontSize = "13px";
      $('#q_title')[0].style.fontSize = "13px";
    }
});

var right_pane = document.getElementById('right_pane');
new ResizeSensor(right_pane, function() {
    if(right_pane.clientWidth<760){
      $('.p').hide();
      if(right_pane.clientWidth<460)
    {
      $('.submit_button').css({'font-size':'12px','padding':'0px !important','width':'4rem'});
      $('.run_button').css({'font-size':'12px','padding':'0px !important','width':'4rem'});
      $('.nav_btns').css({'margin':'0 5px', 'font-size':'12px'});
    }
    else{
      $('.submit_button').css({'font-size':'14px','padding':'1px 6px','width':'5rem'});
      $('.run_button').css({'font-size':'14px','padding':'1px 6px','width':'5rem'});
      $('.nav_btns').css({'margin':'0 20px', 'font-size':'14px'});

    }
    }
    
    else{
      $('.p').show();
    }
});
var top_nav = document.getElementById('testpage_header');
new ResizeSensor(top_nav, function() {
    if( top_nav.clientWidth < 950){
      $('#candidate').hide();
      $('#candidate_name').hide();
      $('#testcases_pane').hide();
      $('#output_pane').hide();
      $('#q_title').hide();
    }
    else{
      $('#candidate').show();
      $('#candidate_name').show();
      $('#testcases_pane').show();
      $('#output_pane').show();
      $('#q_title').show();
    }
});