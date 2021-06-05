# Pinging the Servers 

## Description 

python script for automating the proccess of pinging a cluster of servers.
<br>
the script will take ips-list file that contains the ips and it will send the results to slack ( a messgeing platform ) <br>
for more info about slack api visit [slack api](https://api.slack.com/).
also it will generates output.txt file containting the results



## installation 🚀

1. Modify ips-file.txt with your IP address(es)
1. You will need to modify .env with your slack access token
1. Install requisite python packages and modules then you can use the command
```bash
pip install -r requirements.txt
```
4. Run the script
```bash
python ping.py
```

