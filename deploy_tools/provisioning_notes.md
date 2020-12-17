Provisioning a new site
========================

## Required packages:

* nginx
* Python3.8
* pipx + poetry
* Git

eg. on Ubuntu:
```
sudo apt-get install nginx python3.8 python3-pip git
pip3 install pipx
pipx install poetry
```

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:

assume we have a user account at /home/username
/home/username
└── sites
    └── SITENAME
	├── database
	├── source
        └── static
