$(function() {
    // When we're using HTTPS, use WSS too.
 
var ws = window.location.protocol == "https:" ? "wss" : "ws";
var newsoc = new WebSocket(ws + '://' + window.location.host + "/main");
 

newsoc.onmessage = function(message) {
alert("new post");
};
    $("#MessageForm").on("submit", function(event) {
        var messages = {
            created_date: $('#created_date').val(),
            author: $('#author').val(),
            text: $('#text').val(),
        }
        sock.send(JSON.stringify(messages));
        $("#messages").val('').focus();
        return false;
    });
});


