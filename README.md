# TeraboxedBot ⚡

The *TeraboxedBot* is designed to help users get direct download links from TeraBox files on Telegram.

![icon.jpg](https://te.legra.ph/file/7680309a045c8063a08c7.jpg)

## Features

- **Media Liberation:** Bypass anti-forward/copy restrictions and transfer media files, including photos and videos.
- **Account Integration:** Securely connect GhostForwarder with your Telegram account for a personalized experience.
- **Selective Transfer:** Choose specific media items to transfer, providing you with control and flexibility.
- **Stealth Mode:** Operate discreetly, minimizing disruption and maintaining the privacy of your interactions.

## How to Use

1. **Authentication:**
   - Authenticate GhostForwarder with your Telegram account.
   - Use the `auth` file to authenticate the app or ...
   - Use [![Run on Repl.it](https://replit.com/badge/github/bakamono12/GhostForwarder)](https://replit.com/@baka1432/PyroGramAuth) to get the `session string`.

2. **Source Chat Specification:**
   - Specify the source chat ID with anti-forward/copy restrictions, use the `/help` command to know more.

3. **Destination Chat Selection:**
   - Saved Message will be used for the transferred media or any update error.

4. **Media Transfer:**
   - Now media items can be transferred from the sources chat IDs once you request anyfile or receive any video files in  mentioned chats.

5. **Enjoy:**
   - Sit back and enjoy hassle-free media transfer while preserving the privacy of your communications.

## Getting Started

To get started with GhostForwarder, follow these steps to run the application locally:

1. Clone the repository.
2. Set up the necessary environment variables.
3. Install dependencies using `pip install` [requirements.txt](requirements.txt).
4. Run the application using `python -m main.py`.
5. This Will run your app locally.

## Deployment
Deployment is easy, you can deploy GhostForwarder on Heroku or Railway.\
1. Fork this repository.
2. [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/qHge9_?referralCode=IEUhZ-)
3. [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
4. And Wait for the build to start..
5. In environment variable section, add the following variables:
   - `SESSION_STRING` : Get it from [![Run on Repl.it](https://replit.com/badge/github/bakamono12/GhostForwarder)](https://replit.com/@baka1432/PyroGramAuth).
6. Restart the app and enjoy.
7. To check if app is live or not, use `/boomer` command in Saved Messages or Any Chat.

## Contributing

- **Bot Developer:**
  - [EBIZA](https://t.me/ebiza)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.