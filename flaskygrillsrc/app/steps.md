1. Create the venv. - Done
    - Install flask - Done

2. Create the Configurations(instance/config.py) as well as the config.py not meant for VERSION CONTROL
    - Done

3. Create the databases(flaskapi & testdb) & pip install flaskSqLalchemy, psycopg2, flask_migrate
    - Done

4. Create the App
    - requirements: pip install Flask-API(like Django Rest Framework)

5. Run the App
    - DONE

6. Create the Model
    -DONE

7. Make Migrations
    - requirements: install flask_migrate, flask_script for use in manage.py
    - DONE  
    - psql output  
    ```
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
     ```
     
    ### Image for Migration:  
    ![image](https://user-images.githubusercontent.com/16536231/62377272-2174fb00-b54b-11e9-81b9-fccb4a2ffb33.png)

8. Create your Tests
    - NOT DONE
    
    ### Image for Tests failing due to no functionality
    ![image](https://user-images.githubusercontent.com/16536231/62411524-d7e4e880-b5fc-11e9-8f91-0ab8bd405c2f.png)


9. API Functionality
    - route for both list & create
    - NOT DONE

    Image: Tests working for list & create
    ![image](https://user-images.githubusercontent.com/16536231/62412736-39ae4e00-b60f-11e9-8f54-2bbc4d11d0f9.png)
    Image 2:
    ![image](https://user-images.githubusercontent.com/16536231/62412907-58154900-b611-11e9-8a66-ba4959ab9025.png)



10. API Manipulation
    - route for GET, POST & DELETE requests. restaurant = Restaurant.query.filter(id=id)
    - NOT DONE

## git remove committed files
If you want to remove the file from the remote repo, first remove it from your project with --cache option and then push it:

git rm --cache /path/to/file eg git rm -r --cached **"C:\baronprojects\pythonprojects\flaskprojects\flaskygrill\flaskygrillsrc\instance"**  
git commit -am "Remove file"  
git push -u origin master  
(This works even if the file was added to the remote repo some commits ago) Remember to add to .gitignore the file extensions that you don't want to push.  
