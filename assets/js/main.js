$(document).on('submit', 'form#message', function(){
    $.post('/ajax/chat/add/', $(this).serialize())
        .fail(function(err){console.log(err)});

    return false
});

function show_chat(data){
    var msg, container='';
    for (var i=0; msg=data[i]; i++)
        container += msg.fields.name + ': '+ msg.fields.text + '\n'
    $('textarea#container').html(container)
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