const shipFullName = $('#id_ship_full_name');
const shipStreet1 = $('#id_ship_street_address1');
const shipStreet2 = $('#id_ship_street_address2');
const shipCity =  $('#id_ship_city');
const shipState =  $('#id_ship_state');
const shipZipCode = $('#id_ship_zipcode');
const shipPhone = $('#id_ship_phone_number');
const billFullName = $('#id_bill_full_name');
const billStreet1 = $('#id_bill_street_address1');
const billStreet2 = $('#id_bill_street_address2');
const billCity = $('#id_bill_city');
const billState = $('#id_bill_state');
const billZipCode = $('#id_bill_zipcode');
const billPhone = $('#id_bill_phone_number');
const $steps = $('.step'); 

$(document).ready(function() {
    console.log("function working");
    //MD Bootstrap payment stepper
    $('.stepper').mdbStepper();

    //Add gray to SelectState when page loads and change when selected
    $(shipState).css('color', '#c3ccd3');

    $(shipState).change(function() {
        $(shipState).css('color', '#47646f');
    });

    $(billState).css('color', '#c3ccd3');

    $(billState).change(function() {
        $(billState).css('color', '#47646f'); 
    });

    /*MD Bootstrap provided code to keep step 2 from collapsing after
    preloading */
    $("#step2-btn").change(function() { 
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
    });

    /* Load shipping address to billing address when requested */
    $('input[name=same-as-ship]:checkbox').change(function() {
        if ($(this).is(':checked')) {
            billFullName.val(shipFullName.val());
            billStreet1.val(shipStreet1.val());
            billStreet2.val(shipStreet2.val());
            billCity.val(shipCity.val());
            billState.val(shipState.val());
            billZipCode.val(shipZipCode.val());
            billPhone.val(shipPhone.val());
        } else {
            billFullName.val("");
            billStreet1.val("");
            billStreet2.val("");
            billCity.val("");
            billState.val("");
            billZipCode.val("");
            billPhone.val("");
        }
    });
});

