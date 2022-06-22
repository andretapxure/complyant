# Database stuff

## First create the complyant database
```
#Complyant
drop database complyant with(force);
create role complyant_user with password 'ABC@123@';
alter role complyant_user with login;
create database complyant with owner complyant_user;
grant connect on database complyant to complyant_user;
grant all privileges on all tables in schema public to complyant_user;
grant usage on schema public to complyant_user;
grant all privileges on all sequences in schema public to complyant_user;
grant all privileges on all functions in schema public to complyant_user;
grant update, insert, select, delete on all tables in schema public to complyant_user;
alter default privileges in schema public grant update, insert, select, delete on tables to complyant_user;
```
## Then Metabase's
```
create role metabase_user with password 'ABC@123@';
alter role metabase_user with login;
create database metabase with owner metabase_user;
grant connect on database metabase to metabase_user;
grant all privileges on all tables in schema public to metabase_user;
grant usage on schema public to metabase_user;
grant all privileges on all sequences in schema public to metabase_user;
grant all privileges on all functions in schema public to metabase_user;
grant update, insert, select, delete on all tables in schema public to metabase_user;
alter default privileges in schema public grant update, insert, select, delete on tables to metabase_user;
```

## Trigger to insert all assessment items after an assessment is created
```
CREATE OR REPLACE FUNCTION insert_assessment_items_function()
  RETURNS trigger AS
$$
BEGIN
    INSERT INTO "assessmentitems" ("assessment_id", "item_id", "compliance_level_id") (SELECT NEW."id", item_id, 0 FROM template_items where template_id = NEW."template_id");
    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE  TRIGGER insert_assessment_items_trigger
  AFTER INSERT
  ON assessment
  FOR EACH ROW
  EXECUTE PROCEDURE insert_assessment_items_function();
```

## Trigger to insert in all assessments all assessment items after an assessment is created
```
CREATE OR REPLACE FUNCTION insert_new_items_on_assessment_items_function()
  RETURNS trigger AS
$$
declare assessment record;
BEGIN
    for assessment in select id from assessment where template_id = NEW.template_id
    loop
      INSERT INTO "assessmentitems" ("assessment_id", "item_id", "compliance_level") values (assessment.id, NEW.item_id, 0);
    end loop;
    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE  TRIGGER insert_new_items_on_assessment_items_trigger
  AFTER INSERT
  ON template_items
  FOR EACH ROW
  EXECUTE PROCEDURE insert_new_items_on_assessment_items_function();
```