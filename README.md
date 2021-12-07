# Instagram
### 7th Dec. 2021
## Author 
[Ian Seme](https://github.com/devseme)
# Description 
This is the famous Instagram clone app that enables users to see the different pictures posted by other users. Here,they can view, like, follow and unfollow other users.They can also view user stories.
##  Live Link 
 

## User Story 
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Click a single image to expand it and view the details of that photo
* Search for images by image name.
* Copy a link to the photo.
* Like a picture and leave a comment on it.
* Follow other users and see their pictures on my timeline..


## Setup and Installation 
##### Clone the repository: 
 ```bash
https://github.com/devseme/Instagram.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd Instagram, pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations insta
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.
## Technology used 
* [Python3.8](https://www.python.org/)
* [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)
## Known Bugs 
* There are no known bugs
## Support and Contact Information
To make a contribution to the code used or for any queries feel free to contact me via my email addresses ian.ochenge@student.moringaschool.com or semeochenge@gmail.com or @devseme
## License
### MIT LICENCE
#### Copyright (c) 2021 **Ian ochenge** ~ Moringa School
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

