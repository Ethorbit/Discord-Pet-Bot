# Discord-Pet-Bot
Inspired by the Creators.TF Discord bot 'Pet Bot'
It uses the same website (Created by Moonly Days) so the gifs it returns are the same.

This is a Discord bot that can turn images (mentioned user's avatars, embedded links and attached content) into .gifs of them being patted by a hand.

<img src="https://i.imgur.com/jLeVDXK.gif"/>

## Config
The config.ini (in the same directory) has these settings under ['MAIN']
* Token = Discord bot's token
* Command = pet - The thing someone needs to type before the image/mention/link
* CommandPresets = ['?', '!', '/', '$'] - The symbols before the command that make the command valid
* URL = https://pet.moonlydays.com/pet.php - The website to send user content to and get a response from 
* URLParam = remote - The URL parameter to the URL to pass the user link to
