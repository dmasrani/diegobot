const Discord = require('discord.js')
const client = new Discord.Client()

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)
})

// Get your bot's secret token from:
// https://discordapp.com/developers/applications/
// Click on your application -> Bot -> Token -> "Click to Reveal Token"
bot_secret_token = "NDgzMTU5NDU2MzI3NDAxNDgy.D3vzZg.jHfWovXQFv6ouH_HasnjQU1gMjM"

client.login(bot_secret_token)
