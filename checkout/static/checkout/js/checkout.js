
/*const $steps = $('.step'); */

$(document).ready(function() {
    console.log("function working");
    //MD Bootstrap payment stepper
    $('.stepper').mdbStepper();

    //Add gray to SelectState when page loads and change when selected
    /*$(shipState).css('color', '#c3ccd3');

    $(shipState).change(function() {
        $(shipState).css('color', '#47646f');
    });

    $(billState).css('color', '#c3ccd3');

    $(billState).change(function() {
        $(billState).css('color', '#47646f'); 
    });

    /*MD Bootstrap provided code to keep step 2 from collapsing after
    preloading 
    $("").change(function() { 
        console.log("listener working");
        $steps.each(function(index, step) { 
            let $stepContent = $(step).children('.step-new-content'); 
            if(index < 1 ) {
                console.log("0");
                $stepContent.css('display', 'none'); 
                $(step).attr("class","step done"); 
            } else if(index === 1 ) {
                console.log("1"); 
                $stepContent.css('display', 'block'); 
                $(step).attr("class","step active"); 
            } else {
                console.log("2"); 
                $stepContent.css('display', 'none'); 
                $(step).attr("class","step"); 
            } 
        });
    });*/

    /* Load shipping address to billing address when requested */
});

