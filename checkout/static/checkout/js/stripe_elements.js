/*
    Core logic/payment flow and css for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment-synchronously#web-collect-card-details
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#1e383c',
        fontFamily: '"Roboto", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '12px',
        '::placeholder': {
            color: '#c3ccd3'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert"> 
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `
        $(errorDiv).html(html);
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

   var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.bill_full_name.value),
                    phone: $.trim(form.bill_phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.bill_street_address1.value),
                        line2: $.trim(form.bill_street_address2.value),
                        city: $.trim(form.bill_city.value),
                        state: $.trim(form.bill_state.value),
                        postal_code: $.trim(form.bill_zipcode.value),
                    }
                }    
            },
            shipping: {
                name: $.trim(form.ship_full_name.value),
                phone: $.trim(form.ship_phone_number.value),
                address: {
                    line1: $.trim(form.ship_street_address1.value),
                    line2: $.trim(form.ship_street_address2.value),
                    city: $.trim(form.ship_city.value),
                    state: $.trim(form.ship_state.value),
                    postal_code: $.trim(form.ship_zipcode.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })   
});

//make state select placeholder gray
//let stateSelected = $('#id_ship_state').val();
//if(!stateSelected) {
//    $('#id_ship_state').css('color', '#c3ccd3');
//};

//$('#id_ship_state').change(function() {
//     stateSelected = $(this).val();
//    if(! stateSelected) {
//        $(this).css('color', '#c3ccd3');
//    } else {
//        $(this).css('color', '#47646f');
//    }
//});

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

$(document).ready(function () {
    //MD Bootstrap payment stepper
    $('.stepper').mdbStepper();

    //Add gray to SelectState when page loads and change when selected
    $(shipState).css('color', '#c3ccd3');

    $(shipState).change(function () {
       $(shipState).css('color', '#47646f'); 
    })

    $(billState).css('color', '#c3ccd3');

    $(billState).change(function () {
       $(billState).css('color', '#47646f'); 
    })
    
})

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
        $
    })


