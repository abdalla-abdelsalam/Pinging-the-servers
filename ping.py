import csv
import slack
import os
from dotenv import load_dotenv
from pathlib import Path

def load_env_variables():
    env_path=str(Path('.')/'.env')
    load_dotenv(dotenv_path=env_path)


def slack_connection(servers_status):
    try:
        client=slack.WebClient(token=os.environ['SLACK_TOKEN'])
        client.chat_postMessage(channel='#general',text=servers_status)
    except:
        print("your SLACK TOKEN is not valid")


def ping_the_servers():
    try:
        with open('ips_list.txt') as ipsfile:
            if(os.stat("ips_list.txt").st_size == 0):
                raise Exception()

            ip_list = str.splitlines(ipsfile.read())
            servers_status = ""
            for ip in ip_list:
                # ping the ip
                response = os.system("ping -c 2 -t 100 "+ip)
                if(response == 0):
                    servers_status += ip+" is up !!\n"
                else:
                    servers_status += ip+" is down !!\n"

        return servers_status
    except FileNotFoundError:
        print("sorry, the ips_list.txt file not found ")
        exit()
    except Exception:
        print("sorry, the ips_list.txt file is empty")
        exit()



def output_file(servers_status):
    with open('output.txt', 'w') as output:
        output.write(servers_status)


if __name__=="__main__":
    servers_status=ping_the_servers()
    output_file(servers_status)
    load_env_variables()
    slack_connection(servers_status)

