# Getting Started

1. Install Python3
2. Install the script's dependecies
	```bash
		cd dbsaverpy
		pip install requirements.txt
	```
3. Install Nodejs
4. Install PM2 globally
	```bash
		npm install pm2 -g
	```
5. Create a backup folder 
6. Create a logs folder
7. Change the backup and logs folder in run.py
8. Setup a github repo and link it to the backup folder (for remote backup)
5. Use PM2 to run the script
	```bash
		pm2 start run.py --interpreter python3
	```
	
# Script variables
bud: backup date
dbs: list of databases (replace with yours)
buf: backup folder (replace with yours)
lf: logs folder (replace with yours)

# Environment variables
- Create a .env file and add the values for your database password and user
- Check .env.example for example


