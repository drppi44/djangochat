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
    $('.chat#container').html(data)
}

function load_chat(){
    $.get('/ajax/chat/get')
        .done(function(data){
            show_chat(data)
        })
        .fail(function(err){
            console.log(err.error_msg)
        })
}

$(document).ready(function(){
    load_chat();
    setInterval(load_chat, 5000);

});