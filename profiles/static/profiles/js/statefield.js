//make state select placeholder gray
const stateSelected = $('#div_id_defaultship_state').val();

const defaultShipFullName = $('#id_defaultship_full_name');
const defaultShipCompName = $('#id_defaultship_comp_name');
const defaultShipFullName = $('#id_ship_full_name');
const defaultShipStreet1 = $('#id_defaultship_street_address1');
const defaultShipStreet2 = $('#id_defaultship_street_address2');
const defaultShipCity =  $('#id_defaultship_city');
const defaultShipState =  $('#id_defaultship_state');
const defaultShipZipCode = $('#id_defaultship_zipcode');
const defaultShipPhone = $('#id_defaultship_phone_number');

$(document).ready(function() {
    if ($(defaultShipFullName).val('')) {
        $(defaultShipFullName).css('color', '#c3ccd3');
        $(defaultShipCompName).css('color', '#c3ccd3');
        $(defaultShipStreet1).css('color', '#c3ccd3');
        $(defaultShipStreet2).css('color', '#c3ccd3');
        $(defaultShipCity).css('color', '#c3ccd3');
        $(defaultShipState).css('color', '#c3ccd3');
        $(defaultShipZipCode).css('color', '#c3ccd3');
        $(defaultShipPhone).css('color', '#c3ccd3');
    } else {
        $(defaultShipFullName).css('color', '#47646f');
        $(defaultShipCompName).css('color', '#47646f');
        $(defaultShipStreet1).css('color', '#47646f');
        $(defaultShipStreet2).css('color', '#47646f');
        $(defaultShipCity).css('color', '#47646f');
        $(defaultShipState).css('color', '#47646f');
        $(defaultShipZipCode).css('color', '#47646f');
        $(defaultShipPhone).css('color', '#47646f');
    }

    $(defaultShipState).change(function() {
        $(this).css('color', '#47646f');
    });
});