//make state select placeholder gray
const stateSelected = $('#div_id_defaultship_state').val();

const profileShipFullName = $('#id_defaultship_full_name');
const profileShipCompName = $('#id_defaultship_comp_name');
const profileShipFullName = $('#id_ship_full_name');
const profileShipStreet1 = $('#id_defaultship_street_address1');
const profileShipStreet2 = $('#id_defaultship_street_address2');
const profileShipCity =  $('#id_defaultship_city');
const profileShipState =  $('#id_defaultship_state');
const profileShipZipCode = $('#id_defaultship_zipcode');
const profileShipPhone = $('#id_defaultship_phone_number');

$(document).ready(function() {
    if ($(profileShipFullName).val('')) {
        $(profileShipFullName).css('color', '#c3ccd3');
        $(profileShipCompName).css('color', '#c3ccd3');
        $(profileShipStreet1).css('color', '#c3ccd3');
        $(profileShipStreet2).css('color', '#c3ccd3');
        $(profileShipCity).css('color', '#c3ccd3');
        $(profileShipState).css('color', '#c3ccd3');
        $(profileShipZipCode).css('color', '#c3ccd3');
        $(profileShipPhone).css('color', '#c3ccd3');
    } else {
        $(profileShipFullName).css('color', '#47646f');
        $(profileShipCompName).css('color', '#47646f');
        $(profileShipStreet1).css('color', '#47646f');
        $(profileShipStreet2).css('color', '#47646f');
        $(profileShipCity).css('color', '#47646f');
        $(profileShipState).css('color', '#47646f');
        $(profileShipZipCode).css('color', '#47646f');
        $(profileShipPhone).css('color', '#47646f');
    }

    $(profileShipState).change(function() {
        $(this).css('color', '#47646f');
    });
});