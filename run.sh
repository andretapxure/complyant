#!/bin/bash
export PGPASSWORD="Mcpjst22p"
pg_dump -h 127.0.0.1 -U postgres -f "bkp/complyant_$(date +'%Y-%m-%d_%H%M%S')_backup.sql" complyant
pg_dump -h 127.0.0.1 -U postgres -f "bkp/metabase_$(date +'%Y-%m-%d_%H%M%S')_backup.sql" metabase
./manage.py makemigrations
./manage.py migrate
./manage.py runserver