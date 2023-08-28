# Car Review Blog Site
Here you can post your car and get reviews.

The game is hosted on heroku.

The aim of the blog site is to get a review,ideas etc on your car.

Check out [Car Reviews]()

### **Disclaimer if you would like to open any links in a new tab use `Ctrl` and click the link.**

# Table of Contents
  
  - <p><a href="#wireframes">Wireframes</a></p>
  - <p><a href="#ux">UX</a></p>
  - <p><a href="#features">Features</a></p>
  - <p><a href="#manual-testing">Manual Testing</a></p>
  - <p><a href="#frameworks"> Framework / Programs Used / Technologies</a></p>
  - <p><a href="#bugs-and-fixes">Bugs and Fixes</a></p>
  - <p><a href="#creation">Creation</a></p>
  - <p><a href="#deployment">Deployment</a></p>
  - <p><a href="#cloning">Cloning</a></p>
  - <p><a href="#forking">Forking</a></p>
  - <p><a href="#git-commits">Git Commits</a></p>
  - <p><a href="#credits">Credits</a></p>

# Wireframes

-[Wireframes](https://docs.google.com/presentation/d/e/2PACX-1vRhU0RHyYE-rQnc9Cna2TQW-rw12e_NPvrMDmPYpEMdQJLLMqwbAtvmh44Aj96I4yb24vrJ8p4Nvxx_/pub?start=false&loop=true&delayms=5000) (Google Slides) 

  # UX
### **User Goals**
- As a ***user*** I can view the page so that I can get the required information
- As a ***user*** I can register an account so that I can like the images/posts 
- As a ***user*** I can login to the account so that I can view the information that is required to be logged in for
- As a ***user*** I can logout from the website so that the information (Logged in information) isn't visible when you are logged out
- As a ***user*** I can create a post so that other users can view what I post
- As a ***user*** I can Create/Read/Update/Delete the posts I make.
- As a ***user*** I can click on a post so that I can read the information
- As a ***user*** I can view posts and select one and get the information I want
- As a ***user*** I can like/unlike posts so that so I can interact with the posts/images
- As a ***user*** I can see the numbers of likes so that I can see what other users liked most
- As a ***user*** I can comment on posts to give my feedback.
- As a ***user*** I can contact the page so that I can get updates



### **Owner Goals**
- As a  ***Site Admin*** I can install libraries so that the required libraries are installed and ready to use
- As a ***Site Admin*** I can deploy the website early so that the site can be tested early
- As a ***Site Admin*** I can Create/Read/Update/Delete posts so that the posts/images can be managed
- As a ***Site Admin*** I can view the contact information provided so that the user can be replied to


### **Returning User**
- As a ***returning user*** I can view/ my created post to see how its doing.

# Features
## **Exisiting Features**
* Login
* Regisiter
* View Posts
* Create Post
* Edit Post 
* Delete Post
* Favourite Post
* Comment on Post
* Edit Profile
* Change Password
* Contact
| Feature        |      |
   | -------------  |:-------------:| 
   | Login | ![Login](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693158863/PP4%20Readme/Screenshot_2023-08-27_185410_ncp5rh.jpg) |
   | Registration | ![Registration](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693158938/PP4%20Readme/Screenshot_2023-08-27_185529_s7ku3n.jpg) |
   | View Posts | ![View Posts](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693159012/PP4%20Readme/Screenshot_2023-08-27_185643_ccmiym.jpg) |
   | Create Post | ![Create Post](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693159591/PP4%20Readme/Screenshot_2023-08-27_190614_inf8f1.jpg) |
   | Edit Post | ![Edit Post](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693159667/PP4%20Readme/Screenshot_2023-08-27_190736_smedce.jpg) |
   | Delete Post | ![Delete Post](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693159727/PP4%20Readme/Screenshot_2023-08-27_190836_n2yzzq.jpg) |
   | Favourite | ![Favourite](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693159817/PP4%20Readme/Screenshot_2023-08-27_190950_ezzzdc.jpg) |
   | Comment on Post | ![Comment on Post](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693159890/PP4%20Readme/Screenshot_2023-08-27_191123_qxfe19.jpg) |
   | Edit Profile | ![Edit Profile](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693159967/PP4%20Readme/Screenshot_2023-08-27_191232_qnvzfx.jpg) |
   | Change Password | ![Change Password](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693160084/PP4%20Readme/Screenshot_2023-08-27_191435_jtctri.jpg) |
   | Contact | ![Contact](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693160133/PP4%20Readme/Screenshot_2023-08-27_191521_s4pker.jpg) |
## Features to be added
* Send an email through the contact form.

# Manual Testing
   | Feature        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | Login | Logs the user in | The user is logged in correctly. | Try logging in with username and password |
   | Register   | Registers the user to the site    | The user is registered to the site correctly. | Fill in the required fields. |
   | View Post   | The post details shows   | Post details are shown | Click a created post |
   | Create Post | Post is created for the site  | Post is created on the site | Filled in the required fields for a post |
   | Edit Post | Change information on the post   | The information changed. | Change information on the created post |
   | Delete Post   | Post deletes from the site | Post deleted from the site | Use the delete function on the post |
   | Favourite Post  |The post gains a favourite| Post gained a favourite| Click the favourite button |
   | Comment on Post  | Comment appears under the post | Comment appeared under the post | Used the comment form |
   | Edit Profile  |User info updates | User info updated | Used the edit profile form |
   | Change Password  | Users password gets change | Password changed | Use the password change form |
   | Contact  | Contact form is saved | Form saved | Used the contact form |

   | Testing        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | HTML Validation (W3C) | Pass | Errors caused by django forms | -[Validation](https://docs.google.com/presentation/d/e/2PACX-1vRhU0RHyYE-rQnc9Cna2TQW-rw12e_NPvrMDmPYpEMdQJLLMqwbAtvmh44Aj96I4yb24vrJ8p4Nvxx_/pub?start=false&loop=true&delayms=5000) (Google Slides)  |
   | CSS Validation  | Pass | Pass | ![Contact](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693162287/PP4%20Readme/css_rhhson.jpg) |
   | Browsers | Works as normal. | No issues. | Use Chrome, Safari, Edge and Firefox |

   # Frameworks
  - [Django](https://www.djangoproject.com/)
    - Django was used as the framework and logic of the project.
  - [Bootstrap](https://getbootstrap.com/)
    - Bootstrap was used for the styling of the site.
  - [Git](https://git-scm.com/)
    - Git was used for version control
  - [Github](https://github.com/)
    - Github was used for storing the code.
  - [Gitpod](https://gitpod.io/workspaces)
    - Gitpod was used for coding.
  - [Heroku](https://id.heroku.com/)
    - Heroku was used for live deployment.
  - [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used for wireframes.
  - [Google Slides](https://www.google.com/slides/about/)
    - Google Slides was used for storing large images.
  - [Gunicorn](https://gunicorn.org/)
    - Gunicorn was used for the server for heroku
  - [Cloudinary](https://cloudinary.com/)
    - Cloudinary was used for image storage.
  - [Pillow](https://pypi.org/project/Pillow/)
    - Pillow was used for an image libary
  - [HTML](https://en.wikipedia.org/wiki/HTML/)
    - HTML was used for the templates.
  - [JavaScript](https://www.javascript.com/)
    - Javascript was used to get users info.
  - [Python](https://www.python.org/)
    - Python was used for functionality of the site.
  - [CSS](https://en.wikipedia.org/wiki/CSS)
    - CSS was used for extra styling.

    # Bugs and Fixes
  | Bugs/Errors        |   Explain   | Fix |
   | -------------  |:-------------:| -----: |
   | Password Redirect  | I was having issues with being directed to the password change site | I got help from [Stack Overflow](https://stackoverflow.com/questions/52445694/the-current-path-account-login-didnt-match-any-of-these) I solved this by using ``<int:uid>``  |
   | Category Admin Panel Issues | I was having issues with category not showing in the admin panel | I fixed this by adding category to my admin.py file |
   | Images Showing | I was having issues with the images showing up | I got help from slack and added `` enctype="multipart/form-data`` to my form |
   | Deployment | I was having issues with deployment caused by cloudinary | I added cloudinary cloud_name, api_key and api_secret to heroku config vard |
   |  |  | |

   # Creation
   1. Head over to [CI Template](https://github.com/Code-Institute-Org/gitpod-full-template)
   2. Press 'Use this template'
   3. Create a new repository.
   4. Select a name.
   5. Click create.
   6. Click gitpod.
   7. In the terminal install Django and Gunicorn
      -  pip3 install django gunicorn
   8. Install the required libaries
      - pip3 install dj_database_url==0.5.0 psycopg2
   9. Install Cloudinary libaries
      - pip3 install dj3-cloudinary-storage
pip3 install urllib3==1.26.15
  10. Create requirements file
      - pip3 freeze --local > requirements.txt
  11. Create Project
      - django-admin startproject your_project_name .
  12. Create App
      - python3 manage.py startapp your_app
  13. In settings.py add your app name inside 'Installed apps' and save the file
  14.  Migrate your changes 
       - python3 manage.py migrate
  15. To run the server use 'python3 manage.py runserver'
  16. Inside of settings.py in the 'Allowed hosts' field add your server address

  ### DataBase
  1. Head over to [Elephantsql](https://www.elephantsql.com/)
  2. Create an account
  3. Click create new instance
  4. Set up your free plan
  5. Select your region
  6. Press review
  7. Copy your databse url

  ### Heroku
  1. Head over to [Heroku](https://dashboard.heroku.com/)
  2. Create an app (your_app_name) and location.
  3. Head to settings and click reveal config vars.
  4. Create a new one called 'DATABASE_URL' (Copy in your database url)
  5. In gitpod create a file called 'env.py'
  6. Import 'os'
  7. Paste `os.environ["DATABASE_URL"]` (Replace 'DATABASE_URL) with your URL
  8. Add a secret key `os.environ["SECRET_KEY"] = "create_your_own"`
  9. Head back to heroku config vars and add 'SECRET_KEY' and input your key.
  10. In settings.py add 
      - `import os`
      `import dj_database_url`
      `if os.path.isfile("env.py):`
      `import env`
  11. Remove the secret key and replace it with `SECRET_KEY = os.environ.get('SECRET_KEY')` (This links with env.py)
  12. Comment out the database content
  13. Paste in: `DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}`
14. Save all files and in the terminal paste `python3 manage.py migrate`
### Static Files
 1. Head to [Cloudinary](Cloudinary.com)
 2. Head to dashboard and copy your CLOUDINARY_URL
 3. In env.py add `os.environ["CLOUDINARY_URL"] = "cloudinary://your_link`
 4. Add cloudinary url to heroku confic vars.
 5. Add a confic var `DISABLE_COLLECTSTATIC, 1` 
 6. In settings.py add Cloudinary to 'Installed apps'`  'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',`
  7. Under STATIC_URL add: `STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`
  8. Change the template directory to `'DIRS': [TEMPLATES_DIR],`
  9. In allowed hosts add heroku ["your_project_name.herokuapp.com", "YOUR_HOSTNAME"]
  10. In gitpod create 3 folder 'media, static and templates'
  11. Create a 'Procfile'
  12. Inside the Procfile add `web: gunicorn your_project_name.wsgi`
  13. In the terminal add, commit and push.


   # Deployment

1. Open up [Heroku.](https://dashboard.heroku.com/apps)
2. Click Deploy
3. Set deployment method as GitHub
4. Click Manual Deploy
5. Watch the build log
6. When complete it will say 'Your App Was Successfully Deployed'

# Cloning
1. Open up the repository [Car Reviews](https://github.com/CliveC99/car-rating)
2. Above the list of files click "Code".
3. Click if you would like to clone as "HTTPS", "SSH", or "GitHub CLI".
4. Once selected press copy.
5. Open Git Bash.
6. Change the directory to where you want the clone to appear.
7. Paste in the link you copied in step 4. (This is the line for my repository): <br>
  `$ git clone https://github.com/CliveC99/car-rating.git`
8. Press enter and the clone will happen.

# Forking
1. Open up the repository [Car Reviews](https://github.com/CliveC99/car-rating)
2. Locate the fork button at the top right.
3. Select an owner and repository name.
4. Add a description (optional).
5. Click "Create fork".
6. The repository should appear in your repositories now.

# **Git Commits**
   - I structured my git commits whenever I would add, change or update code.
   - I did this by using:
   1. git status
   2. git add (file name)
   3. git commit -m (message)
   4. git push.
  ![Git Commits](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1693167118/PP4%20Readme/commits_eaetxp.jpg)

# Credits

  - I got help and inspiration from [Youtube](https://www.youtube.com/)
    - [Tutorial 1](https://www.youtube.com/watch?v=OBsLgCm-Ayo&list=PL_KegS2ON4s580mS3nPt5x_eu6kO2cvOc&ab_channel=Desphixs)
    - [Tutorial 2](https://www.youtube.com/watch?v=oU9kN13-Xbs&t=1178s&ab_channel=BekBrace)
    - [Tutorial 3](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&ab_channel=Codemy.com)
    - [Tutorial 4](https://www.youtube.com/watch?v=I8TRkEcw9Mg&ab_channel=CodeWithStein)
    - [Tutorial 5](https://www.youtube.com/watch?v=3aVqWaLjqS4&ab_channel=CoreySchafer)
  - I got help with urls.py path from [Stack Overflow](https://stackoverflow.com/questions/52445694/the-current-path-account-login-didnt-match-any-of-these)
  - I got help with form succession page from [Django docs](https://docs.djangoproject.com/en/4.2/topics/forms/)
  - This project would not be possible without the help of my mentor (Rory_Patrick), my friends, and my facilitator (Chris Quinn).
  - I would also like to thank the private "Novemeber 2022-UCD" group on slack for the all the support.


 <p><a href="#table-of-contents">Back to table of contents.</a></p>