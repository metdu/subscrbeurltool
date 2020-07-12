#!/usr/bin/env bash
cd /var/local
rm -rf subscrbeurltool
git clone https://github.com/available2099/subscrbeurltool.git
cd  subscrbeurltool
chmod 777 subtool.sh
pip install --no-cache-dir -r requirements.txt
cp -f subtool.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable subtool
systemctl start subtool

