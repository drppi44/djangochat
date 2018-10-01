$(document).on('submit', 'form#message', function(){
    var form = $(this);
    $.ajax({
        url: '/ajax/chat/add/',
        type: 'post',
        dataType: "JSON",
        data: new FormData(this),
        processData: false,
        contentType: false,
        success: function(){
            $(form).find('#id_text').val('');
            var control = $("#id_file");
            control.replaceWith( control = control.clone( true ) );
        },
        error: function (err){
            console.log(err)
        }
    });

    return false
});

function show_chat(data){
    $('.chat#container').html(data);

    $('.js-auto-scroll-down .js-message').each(function (i, elem) {
        let time = Date.parse($(elem).find('.js-time').text()),
            now = new Date(),
            millis = now.getTime() + (now.getTimezoneOffset() * 60000),
            delta = millis - time;

        if (delta <= 5*1000){
            $(elem).css('background-color', 'orange');
            setTimeout(function(elem){$(elem).css('background-color', 'white')}, 5000 - delta)
        }

    })
}

function scroll_bottom(target){
    if (!$('.js-auto-scroll-down').is(":hover")){
        target.animate({scrollTop: target[0].scrollHeight}, 1000)
    }
}


function load_chat(){
    $.get('/ajax/chat/get')
        .done(function(data){
            show_chat(data);
            scroll_bottom($('.js-auto-scroll-down'));
        })
        .fail(function(err){
            console.log(err.error_msg)
        })
}

$(document).ready(function(){
    load_chat();
    setInterval(load_chat, 1000);
});