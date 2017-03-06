#!/bin/bash
DB_NAME=appointments.db
DB_TABLE=app
sqlite3 $DB_NAME <<EOF 

CREATE TABLE $DB_TABLE (
      "date" TEXT, "time" TEXT, "description" TEXT
);

EOF
