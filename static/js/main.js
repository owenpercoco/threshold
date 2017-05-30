function customShow(show){
    console.log(show);
    $(show).toggle();

}
$( document ).ready(function() {
    fadeIn();
    slideIn();
});

$( window ).resize(function() {
    fadeIn();
    slideIn();
});

function fadeIn(){
    var fading = $(".fade-in");
    var cf = 0;
    var ht = $(window).height() * .75;
        while (cf < fading.length && $(this).scrollTop() > $(fading[cf]).offset().top - ht  ){
        	$(fading[cf]).animate({opacity: '1'});
        	var cf=cf + 1;

        }
}

function slideIn(){
    var sn = $(".slide-in-now");

    for(var cs = 0; cs < sn.length; cs++){
    	var time = $($(sn[cs]).data().time);
    	$(sn[cs]).delay(time[0]).animate({left: '0px', opacity: '1'});
    }

}

