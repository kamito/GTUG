/**
 * GTUG #0
 */

goog.provide("Gtug.Gtug0");


goog.require("goog.dom");
goog.require("goog.events");
goog.require("goog.json");
goog.require("goog.net.XhrIo");
goog.require("goog.structs.Map");
goog.require("goog.Uri.QueryData");
goog.require('goog.ui.CustomButton');
goog.require('goog.ui.Css3ButtonRenderer');


goog.require("Gtug");
goog.require("Gtug.Base");


;(function() {

    Gtug.Gtug0 = function() {
        this.initialize();
    };
    goog.addSingletonGetter(Gtug.Gtug0);


    Gtug.Gtug0.prototype = {
        initialize: function() {
            this.initChannel();
            this.initForm();
        },

        initChannel: function() {
            // alert("initChannel: " + window.channel_token);

            this.channel = new goog.appengine.Channel(window.channel_token);
            this.socket  = this.channel.open();
            this.socket.onopen    = goog.bind(this.onOpened, this);
            this.socket.onmessage = goog.bind(this.onMessage, this);
            this.socket.onerror   = goog.bind(this.onError, this);
            this.socket.onclose   = goog.bind(this.onClose, this);
        },

        onOpened: function() {
            Gtug.log("Opened");
            this.refleshMessageArea();
        },

        onMessage: function(response) {
            // Gtug.log("Message");
            var json = goog.json.parse(response.data);
            var data = json.data;
            this.updateMessage(data);
        },

        onError: function() {

        },

        onClose: function() {

        },



        initForm: function() {
            // make Request
            this.request = new goog.net.XhrIo();
            // goog.events.listen(this.request, "complete", goog.bind(function() {
            //     Gtug.log("Complete");
            //     var json = this.request.getResponseJson();
            //     var data = json.data;
            //     Gtug.log(data);
            //     this.updateMessage(data);
            // }, this));


            // field
            var message_field = goog.dom.getElement("message_field");


            // build button
            var send_button = new goog.ui.CustomButton("Send", goog.ui.Css3ButtonRenderer.getInstance());
            send_button.render(goog.dom.getElement("buttons"));
            goog.events.listen(send_button, goog.ui.Component.EventType.ACTION, goog.bind(function(e) {
                var message = message_field.value;
                var data = goog.Uri.QueryData.createFromMap(new goog.structs.Map({
                    message: message
                }));
                this.request.send("/gtug0/update", "POST", data.toString());
            }, this));

            var form = goog.dom.getElement("form");
            
        },


        updateMessage: function(data) {
            Gtug.log(data);
            var name_txt    = data.user + " : ";
            var message_txt = data.message + " (" + data.updated_at +  ")";

            var tbody = goog.dom.getElement("messages");
            var th_name    = goog.dom.createDom("th", {style:"text-align:right;"}, name_txt);
            var td_message = goog.dom.createDom("td", {}, message_txt);
            var tr = goog.dom.createDom("tr", {}, [th_name, td_message]);
            tbody.insertBefore(tr, tbody.childNodes[0]);

            this.refleshMessageArea();
        },


        refleshMessageArea: function() {
            var message_field = goog.dom.getElement("message_field");
            message_field.value = "";
            message_field.focus();
        },


        none: null
    };


    Gtug.Gtug0.getInstance();

})();

