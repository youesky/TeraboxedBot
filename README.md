# TeraboxedBot ⚡

The TeraboxedBot is designed to help users get direct download links from TeraBox files on Telegram.

![icon.jpg](https://te.legra.ph/file/7680309a045c8063a08c7.jpg)


### **Features:**

1. **Start Command:**
   - `/start`: Initiates communication with the bot, presenting users with a refined introduction and clear usage instructions.

2. **Link Handling:**
   - Automatically detects TeraBox links in messages, ensuring a polished user experience.
   - Validates URLs, fetching direct download links with a commitment to precision.
   - Presents file details such as title, size, and download link in a structured and professional manner.

3. **Access Control:**
   - Restricts usage to private chats or specified groups, prioritizing privacy and controlled access.
   - Issues a courteous warning when accessed from unauthorized groups.

---

### **How to Use:**

1. **Start a Chat:**
   - Initiate a private chat with the bot, ensuring a discreet and personalized experience.

2. **Send TeraBox Links:**
   - Share TeraBox links with the bot, guaranteeing a streamlined interaction.

3. **Receive Download Links:**
   - Experience the bot's efficiency as it provides direct download links and comprehensive file information.

---

## Deployment
Deployment is easy, you can deploy Terabox Bypass on Heroku or Railway.
1. Star and fork this repository.
2. Deploy:

    <details>
    <summary>Deploy to Heroku</summary>
    
    <br>[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/youesky/TeraboxedBot)
    </details>
    
    <details>
    <summary>Deploy to Koyeb</summary>
    
    <br>[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/youesky/TeraboxedBot&env[SET_COMMANDS]=True&env[WEBHOOK_URL]=True&env[BOT_TOKEN]&env[API_ID]&env[API_HASH]&env[ADMINS]&env[IMAGES]&run_command=python%20bot.py&branch=main&name=TeraboxedBot)              
    </details>
    
    <details>
    <summary>Deploy to Railway</summary>
    
    <br>[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/_l3iQY?referralCode=IEUhZ-)
    </details>

3. In environment variable section, add the following variables:

    <details>
    <summary><b>Variables</b></summary>
      
      <b>Required Variable</b>
    * `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
        
      <b>Optional Variables</b>
    * `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
    * `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
    * `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
    * `IMAGES`: Telegraph links of images to show in start message.( Multiple images can be used seperated by space )
    * `WEBHOOK_URL`: True/False if your server is web support required? the value is True else False
    </details>
    
4. Click on Deploy.
5. Restart the app and enjoy.

---

### TELAGRAM SUPPORT 

* [![EBIZA SUPPORT](https://img.shields.io/static/v1?label=EBIZA&message=SUPPORT&color=critical)](https://t.me/EbizaSupport)

### Credit 💞

* [![EBIZA](https://img.shields.io/static/v1?label=OWNER&message=EBIZA&color=yellow)](https://t.me/ebiza)

* [![BASE REPO](https://img.shields.io/static/v1?label=BASE&message=REPO&color=green)](https://github.com/bakamono12/Terabox-Bypass)

### Disclaimer

[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)<br>
<b>Licensed under <a href="https://github.com/MrMKN/PROFESSOR-BOT/blob/main/LICENSE">GNU AGPL 2.0.</a></b>
<b>This bot is intended for educational and personal use only, upholding the highest standards of ethical use.</b><br>
<b>Selling The Codes To Other People For Money Is Strictly Prohibited.</b>
