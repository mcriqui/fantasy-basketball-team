
// Node module dependencies
var app = require('gopher'),
    twilio = require('twilio');

// Pull in Twilio config from the BlueMix environment
// The VCAP_SERVICES environment variable contains a JSON string with all your
// BlueMix environment data
var config = JSON.parse(process.env.VCAP_SERVICES);

// Loop through user-provided config info and pull out our Twilio credentials
var twilioSid, twilioToken;
config['user-provided'].forEach(function(service) {
    if (service.name == 'Twilio') {
        twilioSid = service.credentials.accountSID;
        twilioToken = service.credentials.authToken;
    }
});

// Define a URL that will send a message, and display the message ID in the
// browser. View the numbers you own and can text from here:
// https://www.twilio.com/user/account/phone-numbers/incoming
app.get('/', function(request, response) {
    var client = new twilio.RestClient(twilioSid, twilioToken);

    client.sendMessage({
        to:'+12014638287',
        from:'+12017625745',
        body:'go big blue!'
    }, function(err, message) {
        response.send('Message sent! ID: '+message.sid);
    });
});