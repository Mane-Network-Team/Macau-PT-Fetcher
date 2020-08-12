# Mane-Macau-PT-Fetcher
 Using Selenium and Chrome to Fetch the part-time job information

## Environment

- Install Selenium Environment
- Install Google Chrome
- Install Webdriver for Google Chrome
- Install npm
- Install [markdown-styles](https://github.com/mixu/markdown-styles)

```bash
sudo apt install npm
sudo npm install -g markdown-styles
```

## Usage

```bash
python3 main.py
```

A file is generated call *output.pdf* after it finish

## Module

- facebook_mptjs.py : Facebook @MacauPartTimeJobsStation and Visitors leave a message.
- hellojob.py : 隨心搵好工 – WeCare Happy Jobs隨心好工
- macauhr.py : 澳門筍工網
- suncareer.py : 澳門首選搵工網站
- um.py : 澳门大学 職位空缺
- N_fastfindjob.py : In preparation may possible to give up.

## Issue

- Some module do not support background running, so they require Linux with a graphical desktop.

## History

**V1.0.4 Alpha**

- Insert Statistical code, goto manesec server and jump.
- Remove URL and Program Version.

**V1.0.3 Alpha**

- Support output pdf using google chrome command line.
- Change output Readme file and convert to html.
- Patch html for word wrap.
- Fix terminal message.
- Fix word wrap in macauhr module.

**v1.0.2 Alpha**

- Fix header text and replace \n to \r\n.

**v1.0.1 Alpha**

- Fix display error and save title error.

