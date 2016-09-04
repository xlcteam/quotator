$(document).on('submit', 'form.quote-schedule', function(){
    var selector = $(this);
    var q_pk = $(this).find('input[name="quote_pk"]').val();
    
    var sday = $(this).find('input[name="schedule_d"]').val();
    var smonth = $(this).find('input[name="schedule_m"]').val();
    var syear = $(this).find('input[name="schedule_y"]').val();
    var stime = $(this).find('input[name="schedule_time"]').val();

    if (q_pk == '' || sday == '' || smonth == '' || syear == '' || stime=='')
        return false;
    
    var request_url = "{% url 'quote_schedule' %}";
    $.ajax({
        url: request_url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            quote_pk: q_pk,
            day: sday,
            month: smonth,
            year: syear,
            time: stime
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


