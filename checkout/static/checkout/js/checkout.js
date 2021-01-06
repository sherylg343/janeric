$(document).ready(function() {
    console.log("function working");
    //MD Bootstrap payment stepper
    $('.stepper').mdbStepper();
debugger;
    /* Add gray to SelectState when page loads and change when selected */
    $('#id_ship_state').on('change', function() {
        $('#id_ship_state').css('color', '#47646f');
    });

    $('#id_bill_state').css('color', '#c3ccd3');

    $('#id_bill_state').on('change', function() {
        $('#id_bill_state').css('color', '#47646f'); 
    });
});

