$(document).ready(function() {
    console.log("function working");
    //MD Bootstrap payment stepper
    $('.stepper').mdbStepper();

    /* Add gray to SelectState when page loads and change when selected */
    /* if statement handles preload */
    if ($('#id_ship_city').val() != '' ) {
        $('#id_ship_state').css('color', '#47646f');
    } else {
        $('#id_ship_state').css('color', '#c3ccd3');
    }

    $('#id_ship_state').on('change', function() {
        $('#id_ship_state').css('color', '#47646f');
    });

    $('#id_bill_state').css('color', '#c3ccd3');
    /* .on('change') didn't work for bill_state */
    $('#id_bill_state').change(function() {
        $('#id_bill_state').css('color', '#47646f'); 
    });
});

