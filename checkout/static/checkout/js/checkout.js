let shipFullName = $('#id_ship_full_name');
let shipStreet1 = $('#id_ship_street_address1');
let shipStreet2 = $('#id_ship_street_address2');
let shipCity =  $('#id_ship_city');
let shipState =  $('#id_ship_state');
let shipZipCode = $('#id_ship_zipcode');
let shipPhone = $('#id_ship_phone_number');
let billFullName = $('#id_bill_full_name');
let billStreet1 = $('#id_bill_street_address1');
let billStreet2 = $('#id_bill_street_address2');
let billCity = $('#id_bill_city');
let billState = $('#id_bill_state');
let billZipCode = $('#id_bill_zipcode');
let billPhone = $('#id_bill_phone_number');
const $steps = $('.step'); 

$(document).ready(function () {
    console.log("function working");
    //MD Bootstrap payment stepper
    $('.stepper').mdbStepper();

    //Add gray to SelectState when page loads and change when selected
    $(shipState).css('color', '#c3ccd3');

    $(shipState).change(function () {
        $(shipState).css('color', '#47646f');
    });

    $(billState).css('color', '#c3ccd3');

    $(billState).change(function () {
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
    $('input[name=same-as-ship]:checkbox').change(
    function() {
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

