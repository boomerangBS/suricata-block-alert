#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By Mody404 made with <3
# Fixed and adapted by BoomerangBS with <3
# SCRIPT UNDER GNU General Public License v3.0 LICENSE
import json
import time
import requests

WEBHOOK_URL = "Put Your Webhook Url Here"  # Put Your Webhook Url Here
IP_THRESHOLD = 10  # Do not edit this
counter = 0 # Do not edit this
ip_log = {} # Do not edit this
ip_sended = {} # Do not edit this

def send_to_discord(ip_events):
    # Create the Discord message data
    data = {
        "content": f":shield: New Problem Detected",
        #"username": "Suricata Logs",  # Webhook Name ,disabled because not working
        #"avatar_url": "https://imgur.com/5KXvYZo",  # avatar,disabled because not working, edit it in the webhook details
        "embeds": []
    }

    # Create an embed for each destination IP
    for ip, event in ip_events.items():
        fields = []
        alert = event[0]['alert']['signature']
        dest_ip = event[0]['dest_ip']
        dest_port = event[0]['dest_port']
        protocol = event[0]['proto']
        timestamp = event[0]['timestamp']
        src_ip = event[0]['src_ip']
            #paquets = event['flow']
        fields.append({
            "name": f":warning: Detected anomaly Possible Attack ",
            "value": f"  **Source IP:** {src_ip} | **Server IP:** {dest_ip} | **Port:** {dest_port} |**Alert**: {alert}| **Protocol:** {protocol}| **Timestamp:** {timestamp}",
            "inline": False
        })

        embed = {
            "title": f"Source IP : {src_ip}",
            "color": 0xff0000,
            "fields": fields
        }
        data["embeds"].append(embed)

    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)
    if response.status_code == 200 or response.status_code == 204:
        print(f"Message sent successfully")
    else:
        print(f"Error sending message: {response.status_code} {response.reason}")

while True:
    with open("CHANGE THIS TO YOU eve.json PATH", "r") as f: # CHANGE THIS TO YOU eve.json PATH
        for line in f:
            log = json.loads(line.strip())

            # Check if the log contains the necessary information for an alert
            if "alert" in log and "dest_ip" in log and "dest_port" in log and "proto" in log and "src_ip" in log:
                dest_ip = log['dest_ip']
                src_ip = log['src_ip']

                # Check if the destination IP starts with 'Your ip range'
                if not dest_ip.startswith('Put your ip range like this 192.168.1. **NOT 192.168.1.0/24**'):
                    continue

                # If this is the first log for this IP, add it to the log dictionary
                if src_ip not in ip_log and src_ip not in ip_sended:
                    ip_log[src_ip] = {"events": [log], "last_sent": time.time()}
                    ip_sended[src_ip] = {"events": [log], "last_sent": time.time()}
                else:
                    continue

        # Send an alert for each IP if 50 seconds have passed since the last one
        for ip, data in ip_log.items():
            c=ip_log.items()
            if 1==1:
                events = data["events"][-4:]
                events.sort(key=lambda x: x['timestamp'])
                send_to_discord({ip: events})
                data["last_sent"] = time.time()
                ip_log[ip] = data
        ip_log = {}

    time.sleep(1)
