/* eslint-disable no-unused-vars */
/* eslint-disable no-undef */
import { Telegraf } from "telegraf"; 
const TOKEN = '6497931798:AAGuwE4WJ26yrPy5uwSh5E_4NWPl_LTodZ8'
const bot = new Telegraf(TOKEN);


const web_link = 'https://tg-webapp-react-bot.netlify.app'



bot.start((ctx) =>
  ctx.reply('Welcome :))))))', {
    reply_markup: { keyboard: [[{ text: "3D Models", web_app: {url: web_link}}]] },
  })
);

bot.launch()