/**
 * GTUG #0
 */

goog.require("goog.dom");

log = function(message) { console.log(message); };

onOpened = function() {
    // alert("Opened");
    log("Opened");
};

onMessage = function() {
    log(arguments);
};

var main = function() {
    // alert("GTUG #0");

    window.channel = new goog.appengine.Channel(window.channel_token);
    socket = channel.open();
    socket.onopen = onOpened;
    socket.onmessage = onMessage;
    // socket.onerror = onError;
    // socket.onclose = onClose;
};

google.setOnLoadCallback(function() {
    main();
});