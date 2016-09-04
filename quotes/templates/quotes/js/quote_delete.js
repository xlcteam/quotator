$(document).on('submit', 'form.quote-delete', function(){
    var selector = $(this);
    var q_pk = $(this).find('input[name="quote_pk"]').val();

    if (q_pk == '')
        return false;

    var request_url = "{% url 'quote_delete' %}";
    $.ajax({
        url: request_url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            quote_pk: q_pk,
        },

        success: function(response) {
            if (response['result'] == 'OK') {
                selector.parent().slideToggle("slow", function() {
                    selector.parent().remove();
                });
            }
        }
    });
        
    return false;
});


