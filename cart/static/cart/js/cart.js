$(document).ready(function() {
    //Update link updates quantity on click
    $('.update-link').click(function(e) {
        const form = $(this).closest('.update-form');
        form.submit();
    });

    //Remove item and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        const productId = $(this).attr('id').split('remove_')[1];
        const url = `/cart/remove/${productId}/`;
        const data = {'csrfmiddlewaretoken': csrfToken};

        $.post(url, data)
        .done(function() {
            location.reload();
        });
    });
});