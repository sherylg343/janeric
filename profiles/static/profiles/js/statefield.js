//make state select placeholder gray
const stateSelected = $('#id_ship_state').val();
if(!stateSelected) {
    $('#id_ship_state').css('color', '#c3ccd3');
};
$('#id_ship_state').change(function() {
     stateSelected = $(this).val();
    if(! stateSelected) {
        $(this).css('color', '#c3ccd3');
    } else {
        $(this).css('color', '#47646f');
    }
});