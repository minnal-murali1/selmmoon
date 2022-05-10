<p><a href="https://heroku.com/deploy"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>


# Extras

## Bot commands to be set in [@BotFather](https://t.me/BotFather)

```
mirror8 - Mirror
zipmirror8 - Mirror and upload as zip
unzipmirror8 - Mirror and extract files
qbmirror8 - Mirror torrent using qBittorrent
qbzipmirror8 - Mirror torrent and upload as zip using qb
qbunzipmirror8 - Mirror torrent and extract files using qb
leech8 - Leech
zipleech8 - Leech and upload as zip
unzipleech8 - Leech and extract files
qbleech8 - Leech torrent using qBittorrent
qbzipleech8 - Leech torrent and upload as zip using qb
qbunzipleech8 - Leech torrent and extract using qb
clone8 - Copy file/folder to Drive
count8 - Count file/folder of Drive
watch8 - Mirror yt-dlp supported link
zipwatch8 - Mirror yt-dlp supported link as zip
leechwatch8 - Leech through yt-dlp supported link
leechzipwatch8 - Leech yt-dlp support link as zip
leechset8 - Leech settings
setthumb8 - Set thumbnail
status8 - Get Mirror Status message
rsslist8 - List all subscribed rss feed info
rssget8 - Get specific No. of links from specific rss feed
rsssub8 - Subscribe new rss feed
rssunsub8 - Unsubscribe rss feed by title
rssset8 - Rss Settings
list8 - Search files in Drive
search8 - Search for torrents with API
cancel8 - Cancel a task
cancelall8 - Cancel all tasks
del8 - Delete file/folder from Drive
log8 - Get the Bot Log
shell8 - Run commands in Shell
restart8 - Restart the Bot
stats8 - Bot Usage Stats
ping8 - Ping the Bot
help8 - All cmds with description
```
------

## UPSTREAM REPO (Recommended)

- `UPSTREAM_REPO` variable can be used for edit/add any file in repository.
- You can add private/public repository link to grab/overwrite all files from it.
- You can skip adding the privates files like token.pickle or accounts folder before deploying, also no need to add variables direct links except **config.env**, simply fill `UPSTREAM_REPO` private one in case you want to grab all files including private files.
- If you added private files while deploying and you have added private `UPSTREAM_REPO` and your private files in this private repository, so your private files will be overwritten from this repository. Also if you are using URL variables like `TOKEN_PICKLE_URL` then all files from those variables will override the private files that added before deploying or from private `UPSTREAM_REPO`.
- If you filled `UPSTREAM_REPO` with the official repository link then be carefull incase any change in requirements.txt your bot will not start after restart. In this case you need to deploy again with updated code to install the new requirements or simply by changing the `UPSTREAM_REPO` to you fork link with that old updates or make it empty if deployed master branch.
- In case you you filled `UPSTREAM_REPO` with your fork link be carefull also if you fetched the commits from the official repository.
- The changes in your `UPSTREAM_REPO` will take affect only after restart.
- `UPSTREAM_BRANCH` don't ever fill heroku here.

------

## Using Service Accounts for uploading to avoid user rate limit
>For Service Account to work, you must set `USE_SERVICE_ACCOUNTS` = "True" in config file or environment variables.
>**NOTE**: Using Service Accounts is only recommended while uploading to a Team Drive.

### 1. Generate Service Accounts. [What is Service Account?](https://cloud.google.com/iam/docs/service-accounts)
Let us create only the Service Accounts that we need.

**Warning**: Abuse of this feature is not the aim of this project and we do **NOT** recommend that you make a lot of projects, just one project and 100 SAs allow you plenty of use, its also possible that over abuse might get your projects banned by Google.

>**NOTE**: If you have created SAs in past from this script, you can also just re download the keys by running:
```
python3 gen_sa_accounts.py --download-keys $PROJECTID
```
>**NOTE:** 1 Service Account can upload/copy around 750 GB a day, 1 project can make 100 Service Accounts so you can upload 75 TB a day or clone 2 TB from each file creator (uploader email).

#### Two methods to create service accounts
Choose one of these methods

##### 1. Create Service Accounts in existed Project (Recommended Method)
- List your projects ids
```
python3 gen_sa_accounts.py --list-projects
```
- Enable services automatically by this command
```
python3 gen_sa_accounts.py --enable-services $PROJECTID
```
- Create Sevice Accounts to current project
```
python3 gen_sa_accounts.py --create-sas $PROJECTID
```
- Download Sevice Accounts as accounts folder
```
python3 gen_sa_accounts.py --download-keys $PROJECTID
```

##### 2. Create Service Accounts in New Project
```
python3 gen_sa_accounts.py --quick-setup 1 --new-only
```
A folder named accounts will be created which will contain keys for the Service Accounts.

### 2. Add Service Accounts

#### Two methods to add service accounts
Choose one of these methods

##### 1. Add Them To Google Group then to Team Drive (Recommended)
- Mount accounts folder
```
cd accounts
```
- Grab emails form all accounts to emails.txt file that would be created in accounts folder
- `For Windows using PowerShell`
```
$emails = Get-ChildItem .\**.json |Get-Content -Raw |ConvertFrom-Json |Select -ExpandProperty client_email >>emails.txt
```
- `For Linux / MacOs`
```
grep -oPh '"client_email": "\K[^"]+' *.json > emails.txt
```
- Unmount acounts folder
```
cd ..
```
Then add emails from emails.txt to Google Group, after that add this Google Group to your Shared Drive and promote it to manager and delete email.txt file from accounts folder

##### 2. Add Them To Team Drive Directly
- Run:
```
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```
------

### Generate Database

**1. Using Railway**
- Go to [railway](https://railway.app) and create account
- Start new project
- Press on `Provision PostgreSQL`
- After creating database press on `PostgresSQL`
- Go to `Connect` column
- Copy `Postgres Connection URL` and fill `DATABASE_URL` variable with it

**2. Using Heroku PostgreSQL**
<p><a href="https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1"> <img src="https://img.shields.io/badge/See%20Dev.to-black?style=for-the-badge&logo=dev.to" width="160""/></a></p>

**3. Using ElephantSQL**
- Go to [elephantsql](https://elephantsql.com) and create account
- Hit `Create New Instance`
- Follow the further instructions in the screen
- Hit `Select Region`
- Hit `Review`
- Hit `Create instance`
- Select your database name
- Copy your database url, and fill `DATABASE_URL` variable with it

------

## Multi Search IDs
To use list from multi TD/folder. Run driveid.py in your terminal and follow it. It will generate **drive_folder** file or u can simply create `drive_folder` file in working directory and fill it, check below format:
```
MyTdName folderID/tdID IndexLink(if available)
MyTdName2 folderID/tdID IndexLink(if available)
```
-----

## Yt-dlp and Aria2c Authentication Using .netrc File
For using your premium accounts in yt-dlp or for protected Index Links, create .netrc file according to following format:

**Note**: Create .netrc and not netrc, this file will be hidden, so view hidden files to edit it after creation.

Format:
```
machine host login username password my_password
```
Example:
```
machine instagram login anas.tayyar password mypassword
```
**Instagram Note**: You must login even if you want to download public posts and after first try you must confirm that this was you logged in from different ip(you can confirm from phone app).

**Youtube Note**: For `youtube` authentication use [cookies.txt](https://github.com/ytdl-org/youtube-dl#how-do-i-pass-cookies-to-youtube-dl) file.

Using Aria2c you can also use built in feature from bot with or without username. Here example for index link without username.
```
machine example.workers.dev password index_password
```
Where host is the name of extractor (eg. instagram, Twitch). Multiple accounts of different hosts can be added each separated by a new line.

-----

## Gdtot Cookies
To Clone or Leech gdtot link follow these steps:
1. Login/Register to [gdtot](https://new.gdtot.top).
2. Copy this script and paste it in browser address bar.
   - **Note**: After pasting it check at the beginning of the script in broswer address bar if `javascript:` exists or not, if not so write it as shown below.
   ```javascript
   javascript:(function () {
    const input = document.createElement('input');
    COOKIE = JSON.parse(JSON.stringify({cookie : document.cookie}));
    input.value = COOKIE['cookie'].split('crypt=')[1];
    document.body.appendChild(input);
    input.focus();
    input.select();
    var result = document.execCommand('copy');
    document.body.removeChild(input);
     if(result)
       alert('Crypt copied to clipboard');
     else
       prompt('Failed to copy Crypt. Manually copy below Crypt\n\n', input.value);
   })();
   ```
   - After pressing enter your browser will prompt a alert.
3. Now you'll get Crypt value in your clipboard
   ```
   NGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxWdSVT0%3D
   ```
4. From this you have to paste value for **CRYPT** in config.env file.

-----
