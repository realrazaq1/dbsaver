#!/usr/bin/python3

# This Python script will automatically backup a list of MySQL Databases on a Linux server
# locally and remotely to a GitHub repository on a daily basis

import os
import schedule
from dotenv import load_dotenv
from utils import backup_dbs, push_to_gh, save_log


def run_script():
    load_dotenv()

    bud = os.popen("date").read().strip()
    dbs = ["hr", "inventory", "invoicing", "store"]
    dbp = os.getenv("DB_PASS")
    dbu = os.getenv("DB_USER")
    buf = "/home/razaq/db-backup"
    lf = "~/logs"

    backup_dbs(dbs, dbu, dbp, buf)
    os.chdir(buf)
    push_to_gh(bud)
    save_log(bud, lf)


schedule.every().day.do(run_script)

while True:
    schedule.run_pending()
