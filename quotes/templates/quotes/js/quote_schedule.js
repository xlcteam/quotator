$(document).on('submit', 'form.quote-schedule', function(){
    var selector = $(this);
    var q_pk = $(this).find('input[name="quote_pk"]').val();
    var schedule_time = $(this).find('input[name="schedule_time"]').val();

    if (schedule_time == '')
        return false;
    
    var request_url = "{% url 'quote_schedule' %}";
    $.ajax({
        url: request_url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            quote_pk: q_pk,
            stime: schedule_time,
        },

        success: function(response) {
            if (response['result'] == 'OK') {
                selector.slideToggle('slow', function() {
                    selector.siblings('.quote-author')
                        .find('.quote-scheduled span').text(response.time);

                    selector.siblings('.quote-author')
                        .find('.quote-scheduled').show();  
                });
            }
        }
    });
        
    return false;
});

/* initialize datetimepicker */
$('.datetimepicker').datetimepicker({
    format: 'd.m.Y H:i'
});
