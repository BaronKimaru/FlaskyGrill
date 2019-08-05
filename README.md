# FlaskyGrill
A Flask App that takes full advantage of all the features Flask &amp; FLaskAPI has to Offer.

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
    - DONE
    
    ### Image for Tests failing due to no functionality
    ![image](https://user-images.githubusercontent.com/16536231/62411524-d7e4e880-b5fc-11e9-8f91-0ab8bd405c2f.png)


9. API Functionality
    - route for both list & create
    - DONE

    Image: Tests working for list & create
    ![image](https://user-images.githubusercontent.com/16536231/62412736-39ae4e00-b60f-11e9-8f54-2bbc4d11d0f9.png)
    Image 2:
    ![image](https://user-images.githubusercontent.com/16536231/62412907-58154900-b611-11e9-8a66-ba4959ab9025.png)



10. API Manipulation
    - route for GET, POST & DELETE requests. restaurant = Restaurant.query.filter_by(id=id) OR query.get(id)
    - DONE

## git remove committed files
If you want to remove the file from the remote repo, first remove it from your project with --cache option and then push it:

git rm --cache /path/to/file eg git rm -r --cached **"C:\baronprojects\pythonprojects\flaskprojects\flaskygrill\flaskygrillsrc\instance"**  
git commit -am "Remove file"  
git push -u origin master  
(This works even if the file was added to the remote repo some commits ago) Remember to add to .gitignore the file extensions that you don't want to push.  

## How to Add a New Remote to your Git Repo  
To add a new remote, use the ```git remote add command``` on the terminal, in the directory your repository is stored at.  

The git remote add command takes two arguments:

* A remote name, for example, “origin”
* A remote URL, which you can find on the Source sub-tab of your Git repo

#### For example:

```
git remote add origin git@git.assembla.com:portfolio/space.space_name.git
#set a new remote
git remote -v
#Verify new remote
origin  git@git.assembla.com:portfolio/space.space_name.git (fetch) ie, git fetch --all
origin  git@git.assembla.com:portfolio/space.space_name.git (push)  git push 
```
FULL TUTORIAL:
When collaborating with colleagues, or even when you're just using an open source library, you'll often need to fetch a branch from a remote repository using Git.

The "base case" to fetch a branch is fairly simple, but like with many other Git operations, it can become quite confusing when other constraints are introduced and you need to start using one of the many options available. In this article I'll try and shed some light on the commands that need to be run and options that are commonly used.

Generally, you'll want to run this sequence:

$ git fetch <remote-repo> <remote-branch>:<local-branch>
$ git checkout <local-branch>
The fetch command will retrieve the remote branch you're interested in and all related objects and references, storing it in a new local branch that you specified by the argument <local-branch>.

Once everything has been downloaded from the remote repo you can then check it out to actually inspect and play around with the code.

If you only have one remote repo then you can omit all of the arguments to git fetch, which will retrieve all branches and updates, and then run git checkout <branch-name> since all remote branches are already on your system.

Given how fetch works, the example command above will retrieve all of the code in the branch you're interested in but it won't affect any of your local branches since nothing is merged with fetch.

Often times you'll want your new local branch to track the remote one, which is helpful for easily pulling and pushing changes. To do this, you should use the --track option with the checkout command, which simultaneously checks out the branch and tracks it with the remote branch. Here is what that would look like:

$ git checkout --track <remote-repo>/<remote-branch>
This will create a local branch of the same name as the remote one.

If you want to checkout the remote branch to a local one, but with a different name, then you need to include the -b option to create the new local branch:

$ git checkout --track -b <local-branch> <remote-repo>/<remote-branch>
In practice, it'll look something like this:

$ git checkout --track -b fix-144 origin/bug-144
Branch fix-144 set up to track remote branch bug-144 from origin.
Switched to a new branch 'fix-144'
To verify your new branch is tracking the remote branch, run the branch command with the -vv option:

$ git branch -vv
* fix-144 0774548 [origin/bug-144] Fix #144
  master  dc538f6 [origin/master] 4.16.4
