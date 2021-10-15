import os
from discord_webhook import DiscordWebhook, DiscordEmbed

def hello_world(request):
  
    # The webhook used to send messages to discord
    webhook = DiscordWebhook(url=os.environ.get('discord_webhook'))

    request_json = request.get_json(silent=True)


    description = f"""\n**Offer Type**: {request_json['offer_type']}
**Degree**: {request_json['degree']}
**Product Area**: {request_json['product_area']}
**Position**: {request_json['position']}
**Date of Offer**: {request_json['date_of_offer']}
**Location**: {request_json['location']}
**Base Salary**: {request_json['base_salary']}
**Equity**: {request_json['equity']}
**Relocation/Housing**: {request_json['relocation_housing']}
**Signing**: {request_json['signing']}
**Yearly Bonus**: {request_json['yearly_bonus']}
**Negotiated**: {request_json['negotiated']}
**Additional Info**: {request_json['additional_info']}

Reminder: please contribute to this channel if you've received an offer by filling out this form: https://forms.gle/HALoA2deGWEUqi9q8
    """
    # create embed object for webhook
    embed = DiscordEmbed(title=f"{request_json['position']} {request_json['offer_type']}", description=description, color='03b2f8')

    # set footer
    embed.set_author(name="Google Form Response", url="https://forms.gle/HALoA2deGWEUqi9q8", icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Google_Forms_2020_Logo.svg/1200px-Google_Forms_2020_Logo.svg.png')

    # set timestamp (default is now)
    embed.set_timestamp()

    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()

    return "success"
