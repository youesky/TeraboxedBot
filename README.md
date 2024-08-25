# TeraboxedBot ⚡

The TeraboxedBot is designed to help users get direct download links from TeraBox files on Telegram.

![icon.jpg](https://te.legra.ph/file/7680309a045c8063a08c7.jpg)

---

## Special Feature - Public Database

Results of the bypass is hosted on public database on [DBHub.io](https://dbhub.io/bipinkrish/link_bypass.db) so if the bot finds link alredy in database it uses the result from the same, time saved and so many problems will be solved.

Table is creted with the below command, if anyone wants to use it for thier own.

```sql
CREATE TABLE results (link TEXT PRIMARY KEY, result TEXT)
```

---

## Required Variables

- `TOKEN` Bot Token from @BotFather
- `HASH` API Hash from my.telegram.org
- `ID` API ID from my.telegram.org

## Optional Variables

you can also set these in `config.json` file

- `CRYPT` GDTot Crypt If you don't know how to get Crypt then [Learn Here](https://www.youtube.com/watch?v=EfZ29CotRSU)
- `XSRF_TOKEN` and `Laravel_Session` XSRF Token and Laravel Session cookies! If you don't know how to get then then watch [this Video](https://www.youtube.com/watch?v=EfZ29CotRSU) (for GDTOT) and do the same for sharer.pw
- `DRIVEFIRE_CRYPT` Drivefire Crypt
- `KOLOP_CRYPT`  Kolop Crypt!
- `HUBDRIVE_CRYPT` Hubdrive Crypt
- `KATDRIVE_CRYPT` Katdrive Crypt
- `UPTOBOX_TOKEN` Uptobox Token
- `CLOUDFLARE` Use `cf_clearance` cookie from and Cloudflare protected sites
- `PORT` Port to run the Bot Site on (defaults to 5000)

## Optinal Database Feature

You need set all three to work

- `DB_API` API KEY from [DBHub](https://dbhub.io/pref), make sure it has Read/Write permission
- `DB_OWNER` (defaults to `bipinkrish`)
- `DB_NAME` (defaults to `link_bypass.db`)

---

## Deploy on Heroku

**BEFORE YOU DEPLOY ON HEROKU, YOU SHOULD STAR AND FORK THE REPO AND CHANGE ITS NAME TO ANYTHING ELSE**<br>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/youesky/TeraboxedBot)<br>


---

## Commands

Everything is set programtically, nothing to work

```
/start - Welcome Message
/help - List of All Supported Sites
```

---

## Supported Sites

To see the list of supported sites see [texts.py](https://github.com/youesky/TeraboxedBot/blob/main/texts.py) file

---

## Help

* If you are deploying on VPS, watch videos on how to set/export Environment Variables. OR you can set these in `config.json` file
