$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        }
    }
});

$(document).ready(function () {
    $('#email').on('input', function () {
        let email = $(this).val();

        $.ajax({
            type:'POST',
            url: 'verify_email',
            data: {
                'email': email
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    $('#email-feedback').text('*This email is already taken.');
                    
                } else {
                    $('#email-feedback').text('');
                }
            }
        });
    });
});