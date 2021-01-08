//make state select placeholder gray
const stateSelected = $('#div_id_defaultship_state').val();

const profileDefaultShipFullName = $('#id_defaultship_full_name');
const profileDefaultShipCompName = $('#id_defaultship_comp_name');
const profileDefaultShipFullName = $('#id_ship_full_name');
const profileDefaultShipStreet1 = $('#id_defaultship_street_address1');
const profileDefaultShipStreet2 = $('#id_defaultship_street_address2');
const profileDefaultShipCity =  $('#id_defaultship_city');
const profileDefaultShipState =  $('#id_defaultship_state');
const profileDefaultShipZipCode = $('#id_defaultship_zipcode');
const profileDefaultShipPhone = $('#id_defaultship_phone_number');

$(document).ready(function() {
    if ($(profileDefaultShipFullName).val('')) {
        $(profileDefaultShipFullName).css('color', '#c3ccd3');
        $(profileDefaultShipCompName).css('color', '#c3ccd3');
        $(profileDefaultShipStreet1).css('color', '#c3ccd3');
        $(profileDefaultShipStreet2).css('color', '#c3ccd3');
        $(profileDefaultShipCity).css('color', '#c3ccd3');
        $(profileDefaultShipState).css('color', '#c3ccd3');
        $(profileDefaultShipZipCode).css('color', '#c3ccd3');
        $(profileDefaultShipPhone).css('color', '#c3ccd3');
    } else {
        $(profileDefaultShipFullName).css('color', '#47646f');
        $(profileDefaultShipCompName).css('color', '#47646f');
        $(profileDefaultShipStreet1).css('color', '#47646f');
        $(profileDefaultShipStreet2).css('color', '#47646f');
        $(profileDefaultShipCity).css('color', '#47646f');
        $(profileDefaultShipState).css('color', '#47646f');
        $(profileDefaultShipZipCode).css('color', '#47646f');
        $(profileDefaultShipPhone).css('color', '#47646f');
    }

    $(profileDefaultShipState).change(function() {
        $(this).css('color', '#47646f');
    });
});