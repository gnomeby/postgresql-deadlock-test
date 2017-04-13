# postgresql-deadlock-test
PostgreSQL deadlock test scripts. Aim is using in educational purposes.

## Install

* Create new virtualenv
* Install requirements
* Create empty DB in PostgreSQL
* Change credentials in db.py
* Create Table with data

```sql
CREATE TABLE public.users
(
  id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
  nickname text,
  balance numeric,
  CONSTRAINT "primary" PRIMARY KEY (id)
)
WITH (OIDS=FALSE);

INSERT INTO users (id, nickname, balance) VALUES (2, 'Beta', 160.0);
INSERT INTO users (id, nickname, balance) VALUES (1, 'Alpha', 260.0);
INSERT INTO users (id, nickname, balance) VALUES (3, 'Gamma', 510.50);
```

## Using

```bash
python deadlock_test.py
```
