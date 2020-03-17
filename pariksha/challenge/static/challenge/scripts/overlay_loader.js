
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
// Hide it after 3 seconds
setTimeout(function(){
    $.LoadingOverlay("hide");
}, 1000);