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
  - <p><a href="#imported-modules">Imported Modules</a></p>
  - <p><a href="#bugs-and-fixes">Bugs and Fixes</a></p>
  - <p><a href="#deployment">Deployment</a></p>
  - <p><a href="#cloning">Cloning</a></p>
  - <p><a href="#forking">Forking</a></p>
  - <p><a href="#git-commits">Git Commits</a></p>
  - <p><a href="#tools-used">Tools Used</a></p>
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
   | User input verifaction | Show error message and let the user input the right data. | If the user input the wrong data, an error shows. If the user inputs the correct data, it moves to the next step. | Input correct data and input incorrect data. |
   | Python sleep   | Pause the next step from showing up.    | There was a pause of the next step showing where required. | Input data to move to the next step. |
   | Players turns   | Switch from 'X' to 'O'.   | Switched correctly | Input data on the board. |
   | Win or Draw | Show who won or the game was a draw.  | Printed the winner or if the game was a draw. | Played the game to see if it would give the right output. |
   | Play again | Start the game again.   | The game started. | Restart the game. |
   | Reset score   | Score either is reset or continues | When selected the score reset, when not selected the score kept counting. | Reset the score, play without resetting the score. |


   | Testing        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | Pep8 Linter | Pass. | No Errors. | ![test](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681679398/p3-tic-tac-toe/pep8_leax3w.jpg) |
   | Local Terminal | Game to function without issues. | Game functioned. | Play the game. |
   | CI Heroku Terminal | Game to function without issues. | Game functions. | Play the game. |

   # Imported Modules
  - [OS](https://www.scaler.com/topics/how-to-clear-screen-in-python/)
    - I used `os.system('clear')` to clear the terminal so it wouldn't be clogged up.
  - [Time](https://www.digitalocean.com/community/tutorials/python-time-sleep)
    - I used `time.sleep(3)` so it would give the user time to read the information.

    # Bugs and Fixes
  | Bugs/Errors        |   Explain   | Fix |
   | -------------  |:-------------:| -----: |
   | User input  | I was having issues with user input if the wrong data was entered. | I got help from [Stack Overflow.](https://stackoverflow.com/questions/49496609/user-input-being-incorrectly-appended-to-python-list) |
   | Index errors | I was having issues with index errors being one off. | I fixed this by adding `int(position) - 1` where needed. |
   | Score counter | I was having issues with the score counter adding for a win. |  I solved this by adding `player_one += 1` I got help from [Stack Overflow](https://stackoverflow.com/questions/26514438/python-how-to-keep-score-in-a-tic-tac-toe-game)|
   | Reset score counter | I was having issues with the score counter resetting. | I solved this by adding `player_one = 0 player_two = 0` |
   | User input for play again/reset score | I was having issues that allowed the user to continue to the next step if the data was wrong. | I solved this by adding `valid = False` and then placing `input(f"\nYou entered '{y_n}', Enter 'y' for Yes - Enter 'n' for No: ")` |


   # Deployment

1. Open up [Heroku.](https://dashboard.heroku.com/apps)
2. Click "New" at the top right.
3. Click "Create new app".
4. Choose an "App name" and pick your region.
5. Click "Create app".
6. Click "Settings".
7. Locate config vars and click "Reveal Config Vars".
8. Set the key to "PORT".
9. Set the value to "8000".
10. Click "Add buildpack".
11. Add "python" and "nodejs".
12. Click "Deploy" and connect Github.
13. Search for your "repo-name".
14. Click "Automatic Deploys"

# Cloning
1. Open up the repository [project-3-tic-tac-toe.](https://github.com/CliveC99/project-3-tic-tac-toe)
2. Above the list of files click "Code".
3. Click if you would like to clone as "HTTPS", "SSH", or "GitHub CLI".
4. Once selected press copy.
5. Open Git Bash.
6. Change the directory to where you want the clone to appear.
7. Paste in the link you copied in step 4. (This is the line for my repository): <br>
  `$ git clone https://github.com/CliveC99/project-3-tic-tac-toe`
8. Press enter and the clone will happen.

# Forking
1. Open up the repository [project-3-tic-tac-toe.](https://github.com/CliveC99/project-3-tic-tac-toe)
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
  ![Git Commits](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681686359/p3-tic-tac-toe/git-commits1_esa2s2.jpg)

  # Tools Used
  # **Tools Used**
  - I used [Drawio](https://app.diagrams.net/?src=about) for creating the flowchart.
  - I used [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gclid=Cj0KCQiA_P6dBhD1ARIsAAGI7HBiqtoSkOp8dv2sdvprV-d3z6NkMdyK0guRRH98shquMJ7QiCtVbJQaAnvIEALw_wcB) for the pictures inside the README.
  - I used [Github](https://github.com/) for storing my code.
  - I used [Gitpod](https://gitpod.io/workspaces) for coding.
  - I used [Heroku](https://dashboard.heroku.com/apps) for hosting my game.


  
# Credits

  - I got help with the user input from [Stack Overflow.](https://stackoverflow.com/questions/49496609/user-input-being-incorrectly-appended-to-python-list)
  - I got help with the score counter from [Stack Overflow](https://stackoverflow.com/questions/26514438/python-how-to-keep-score-in-a-tic-tac-toe-game)
  - I got help and inspiration from [Youtube](https://www.youtube.com/)
    - [Tutorial 1](https://www.youtube.com/watch?v=dK6gJw4-NCo&t=276s&ab_channel=CodeCoach)
    - [Tutorial 2](https://www.youtube.com/watch?v=BHh654_7Cmw&t=2977s&ab_channel=CleverProgrammer)
    - [Tutorial 3](https://www.youtube.com/watch?v=kz7kF8CMAso&ab_channel=Code%27sPathshala)
    - [Tutorial 4](https://www.youtube.com/watch?v=M3G1ZgOMFxo&t=159s&ab_channel=ShaunHalverson)
    - [Tutorial 5](https://www.youtube.com/watch?v=8eHpXLDhi6w&ab_channel=JuniLearning)
  - I got help with `os.system('clear')` from [Scaler Topics](https://www.scaler.com/topics/how-to-clear-screen-in-python/)
  - I got help with `time.sleep(3)` from [Digital Ocean](https://www.digitalocean.com/community/tutorials/python-time-sleep)
  - This project would not be possible without the help of my mentor (Rory_Patrick), my friends, and my facilitator (Chris Quinn).
  - I would also like to thank the private "Novemeber 2022-UCD" group on slack for the all the support.



 <p><a href="#table-of-contents">Back to table of contents.</a></p>