1. Create the venv. - Done
    - Install flask - NOT Done

2. Create the Configurations(instance/config.py) as well as the config.py not meant for VERSION CONTROL
    - Done

3. Create the databases(flaskapi & testdb) & pip install flaskSqLalchemy, psycopg2, flask_migrate
    - Done

4. Create the App
    - requirements: pip install Flask-API(like Django Rest Framework)

5. Run the App
    - NOT DONE

6. Craete the Model
    -Not DONE

7. Make Migrations
    - requirements: install flask_migrate, flask_script for use in manage.py
    - NOT DONE
    -psql output
        flaskapi=# \d
                        List of relations
        Schema |        Name        |   Type   |  Owner
        --------+--------------------+----------+----------
        public | alembic_version    | table    | postgres
        public | restaurants        | table    | postgres
        public | restaurants_id_seq | sequence | postgres

        flaskapi=# \d restaurants
                                            Table "public.restaurants"
            Column    |            Type             |                        Modifiers
        --------------+-----------------------------+----------------------------------------------------------
        id           | integer                     | not null default nextval('restaurants_id_seq'::regclass)
        name         | character varying(255)      |
        date_created | timestamp without time zone |
        date_updated | timestamp without time zone |
        Indexes:
            "restaurants_pkey" PRIMARY KEY, btree (id)

        Image for markdown: ![image](https://user-images.githubusercontent.com/16536231/62377272-2174fb00-b54b-11e9-81b9-fccb4a2ffb33.png)

8. Create your Tests
    - NOT DONE

9. API Functionality
    - route for both list & create
    - NOT DONE

10. API Manipulation
    - route for GET, POST & DELETE requests. restaurant = Restaurant.query.filter(id=id)
    - NOT DONE
