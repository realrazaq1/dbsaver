#!/usr/bin/python3
import os


def backup_dbs(dbs, dbu, dbp, buf):
    for db in dbs:
        os.system(f"mysqldump -u {dbu} -p{dbp} {db} > {buf}/{db}.sql")


def push_to_gh(bud):
    os.system("git add .")
    os.system(f"git commit -m 'Databases backed up | Date: {bud}'")
    #os.system("git push origin main")


def save_log(bud, lf):
    os.system(f"echo 'Databases backed up | Date: {bud}' >> {lf}/dbsaver.log")
