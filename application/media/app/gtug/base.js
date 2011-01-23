/* GTUG */


goog.provide("Gtug");
goog.provide("Gtug.Base");


Gtug.Base = function() {};
Gtug.Base.prototype.log = function(message) { Gtug.log(message); };

// static method
Gtug.log = function(message) { console.log(message); };

