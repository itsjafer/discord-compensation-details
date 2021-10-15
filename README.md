# discord-compensation-details

Google Cloud Function that takes results from a Google Form and posts them to a discord channel.

In particular, we use this to keep an active compensation channel on the Google Interns + Nooglers discord.

## How it Works

Whenever a google form response is submitted, we run a custom script (this is written using the built-in script-editor in Google forms):

```
function onSubmitForm(e) {
  Logger.log("onSubmitForm Running");
  var itemResponses = e.response.getItemResponses();

  var data = {
  'offer_type': itemResponses[0] ? itemResponses[0].getResponse() : "",
  'degree': itemResponses[1] ? itemResponses[1].getResponse() : "",
  'product_area': itemResponses[2] ? itemResponses[2].getResponse() || "N/A" : "N/A",
  'position': itemResponses[3] ? itemResponses[3].getResponse() : "",
  'date_of_offer': itemResponses[4] ? itemResponses[4].getResponse() : "",
  'location': itemResponses[5] ? itemResponses[5].getResponse() : "",
  'base_salary': itemResponses[6] ? itemResponses[6].getResponse() : "",
  'equity': itemResponses[7] ? itemResponses[7].getResponse() || "N/A" : "",
  'relocation_housing': itemResponses[8] ? itemResponses[8].getResponse() || "N/A" : "N/A",
  'signing': itemResponses[9] ? itemResponses[9].getResponse() || "N/A" : "N/A",
  'yearly_bonus': itemResponses[10] ? itemResponses[10].getResponse() || "N/A" : "N/A",
  'negotiated': itemResponses[11] ? itemResponses[11].getResponse() || "N/A": "N/A",
  'additional_info': itemResponses[12] ? itemResponses[12].getResponse() || "N/A" : "N/A"
  };
  var options = {
    'method' : 'post',
    'contentType': 'application/json',
    // Convert the JavaScript object to a JSON string.
    'payload' : JSON.stringify(data)
  };
  var url = "https://example.com"; // this is the endpoint where we host our cloud function (main.py) as a lambda function
  var response = UrlFetchApp.fetch(url, options);
  Logger.log(response)
}

```
