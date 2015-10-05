$(document).ready(function(){
    window.setInterval(
        function(){
            get_requests();
            get_request_count();
        },
        1000);
});


function get_requests(){
    $.ajax({
        url:'request/ajax/getrequests/',
        type:'GET',
        dataType: 'json',
        success: show_requests,
        error:function(data){console.error(data)}
    });
}


function get_request_count(){
    $.ajax({
        url:'request/ajax/getrequestscount/',
        type:'GET',
        dataType: 'json',
        success: show_request_count,
        error:function(data){console.error(data)}
    });
}


var show_requests = function(requests){
    var table_data='';

    for (var i in requests){
        var request = requests[i];
        table_data += '<tr><td>'+request.fields.uri+'</td><td>'+request.fields.time+'</td></tr>';
    }

    var table=$('table#example');
    var thead = '<<thead><tr><th>URI</th><th>TIME</th></tr></thead>';
    var tbody = '<tbody>'+table_data+'</tbody>';

    table.html(thead+tbody);
};


function show_request_count(count){
    $('.container h1').html('('+count+') 42 Coffee Cups Test Assignment. Midleware.');
    $('title').html('('+count+') 42 Coffee Cups Test Assignment')
}