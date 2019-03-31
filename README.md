# Introduction
This application allows the user to upload multiple images to the database. Also allows to view and download those images using Document Viewer.

# Installation

* Clone the Repo:
```
    $ git clone "https://github.com/yash-m-agarwal/task2_image_upload"
```

* Create the virtual environment and activate

```
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
```
* Change directory into the folder named task2_image_upload

* Install all the project dependencies
```
    $ pip install -r requirements.txt
```
* Make the database migrations
```
    $ python manage.py migrate
```

* Run the Server
```
    $ python manage.py runserver
```
* The above steps starts the development server on localhost:8000. Go to `http://localhost:8000/` in your browser.

# Configuring MySQL database:
The following segment guides how to use Mysql database

#### Configuring MySQL with the project(Linux)
* Install mysql and setup
```
    $ sudo apt-get update
    $ sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
    $ sudo mysql_secure_installation
``` 

* Install the django mysql depedencies(First activate the virtual environment)
```
    $ pip install mysqlclient
```

* Configure MySQL database
```
IN settings.py
Give appropriate values to the USER and PASSWORD fields, supply the ones you used to setup the mysql installation
Leave the NAME field as it is. This field is the name of the Database to use.
```

* Create the database of the same name as in the NAME field above. Assuming you left the field as it is with the name 'ImageUploadDb' type the following in the terminal :
```
    $ sudo service mysql start
    $ mysql -h 127.0.0.1 -u :username -p
```
:username is the username you provided during the mysql setup. If left as default it will be 'root'. The above command will prompt for a password as well. Provide the password used during the mysql setup

* To create the database (named ImageUploadDb)
```
    > CREATE DATABASE ImageUploadDb;
    > SHOW DATABASES;
```

Using SHOW DATABASES Command your created database will appear in the list of databases

* To use this database, again migrate
```
    $ python manage.py migrate
```

* Run the Server
```
    $ python manage.py runserver
```

# Views Implemented:

* Base Url: `http://localhost:8000`

* `/images`
    * GET Request
    * Retrieves all the data objects of the **Data Model**.
    * For each data object it displays the data **title**, **description**, **Uploaded date** and a link to a **Image** at the top. This details are displayed in a card.
    * When clicked on the **image link** a new window pops up. Which displays the image in the viewer. User can then accordingly **Download** and **View** the document
    * Also a link is present at the bottom named **View all images** which redirects to `/image/<pk>`. 

* `/image/<pk>`
    * GET REQUEST
    * It displays the all the image objects uploaded from the **Image Model** whose **Data Field** has primary key of :pk.
    * Since, every image object has a data model associated with it. So, it retrieves all the images with that **Data** Field as a **Foreign Key**. It implements using the reverse-relationship.
    * When clicked on a **Image object link** new window pops up. Which displays the image in the viewer. User can then accordingly **Download** and **View** the document
    * Two buttons are present at the bottom.
        * Add a new image this link redirects to `image/new`
        * All images this link redirects to `/images`

* `/image/new`
    
    ##### GET 
    * It renders a form.
    * In the form user can enter **title**, **description** an Can **upload images**.
    * A add_button (+) is provided which allows user to add more images from the local computer.
    * All the added images are appended at the bottom of the Added images Table.
    * When the user clicks on the **Create** button a POST request is generated to the same url which uploads all the images.
    
    ##### POST
    * It generates a **AJAX** call to the backend.
    * Every time user clicks on add_button(+) the image is appended to a list which is present in the frontend.
    * When the user clicks on CREATE, those list storing images is passed to the backend along with title and description.
    * For each image in the list a new image object is generated and a single Data object is generated which is passed as a foreign key to all the images object.
    
    * Button is present at the bottom named All images this link redirects to `/images` 
  
# Database Schema:

**There exists a one-to-many relationship between the Data Table and the Image Table**

#### Data(Table)

* Title
* Description
* Flagship image
* Uploaded at
* Reference to Image

#### image(Table)

* Image
* Data (Foreign Key)
