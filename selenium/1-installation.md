# Selenium Installattion

## Step 1:  Install Firefox

Make sure that the firefox browser is installed.

## Step 2: Downlaod Geckodriver for your platform

You can find the latest here: https://github.com/mozilla/geckodriver/releases

 * [Linux](https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz)
 * [MacOS](https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-macos.tar.gz)
 * [Windows](https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-win64.zip)

Mac users also need to run the followin:


## Step 3: Perform the Install for your Platform

#### Mac

```bash
tar -xvzf geckodriver*
chmod +x geckodriver*
sudo mv geckodriver /usr/local/bin
xattr -r -d com.apple.quarantine geckodriver
```

#### Linux

```bash
tar -xvzf geckodriver*
chmod +x geckodriver*
sudo mv geckodriver /usr/local/bin

```


## Step 4: Install pip package

```bash
pip instal selenium
```
