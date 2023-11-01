# suricata-block-alert
a little suricata script to send webhooks when new ip is blocked

# How to install
## Before

Edit `suricata.yaml` (`find / -iname suricata.yaml` to locate the file) and enable `eve-log`.

Restart suricata.


## Download and edit files

Create the folder and cd into it `mkdir /etc/suricata-discord && cd /etc/suricata-discord`

Clone the project `git clone https://github.com/boomerangBS/suricata-block-alert.git .`

Install dependicies `pip install -r requirements.txt`

Enter in the full file path of the eve.json file (`find / -iname eve.json` to locate the file) on the line **55** of the suricata-discord.py file.

Enter the Ip Range of the Destination ip (not source ip) (like 192.168.1 **not 192.168.1.0/24**) on the line **65** of  suricata-discord.py.

Enter the discord webhook url on line 9 of suricata-discord.py.

Run the script by using `python suricata-discord.py`, you can also create a cron to automaticly start the script on boot


## Others

Based on the [Mody404 project](https://github.com/Mody404/Suricata-to-Discord)
