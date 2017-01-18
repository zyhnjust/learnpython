commands = {}


def get_commands_list():
    return [
    {"cmd":"db-dump", "label":"Dump database using database utility", "param":"[Local folder] [s3://BUCKET]", "func":"cmd_db_dump", "argc":0},
    {"cmd":"db-restore", "label":"Restore database using database utility from dump file", "param":"<Dump file URL>", "func":"cmd_db_restore", "argc":1},
    {"cmd":"cms-copy", "label":"Extract database data to files, and upload them to AWS S3", "param":"[Local folder] [s3://BUCKET]", "func":"cmd_cms_db_copy", "argc":0},
    # {"cmd":"s3-copy", "label":"Upload/download files between local and AWS S3", "param":"<Local folder> s3://BUCKET | s3://BUCKET <local folder>", "func":cmd_s3_copy, "argc":2},
    # {"cmd":"rs-load", "label":"Load data into RedShift database from files on S3", "param":"s3://BUCKET", "func":cmd_rs_restore, "argc":1},
    # {"cmd":"schema-gen", "label":"Generate database schema script file", "param":"<File Location>", "func":cmd_gen_ddl, "argc":1},
    # {"cmd":"sql-run", "label":"Execute SQL scripts from file", "param":"<File path>", "func":cmd_run_sql, "argc":1},
    # {"cmd":"upgrade", "label":"Upgrade cc-tool and its dependencies", "param":"<File URL>", "func":cmd_install, "argc":1},
    ]
commands_list = get_commands_list()

for cmd in commands_list:
    if cmd.has_key("cmd"):
        commands[cmd["cmd"]] = cmd

print commands_list
print commands
for co in commands.keys():
    print co
    print commands.get(co)
    # print "\n"

