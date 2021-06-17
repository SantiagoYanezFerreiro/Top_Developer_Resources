# Top Developer Resources. Milestone Project 3

![Site Logo](https://santiagoyanezferreiro.github.io/Top_Developer_Resources/static/images/logo.PNG)

[Live Website Link](http://flask-top-developer-resources.herokuapp.com/home)

[GitHub Repository Link](https://github.com/SantiagoYanezFerreiro/Top_Developer_Resources)

![Top Developer Resources Responsive Design](static/images/ResponsiveDesign.PNG)

Top Developer Resources is a community website where people can share the top resources they used in their Software Development Learning journey so that other people can profit from them and reach their Development goals faster (getting a job, learning a new language, etc).

It is a website where the community can share useful materials they used to develop their skills. All users can search through dataset provided by community members. 
Registered users can create, edit or delete their own dataset. Upon registering, users can add assets to the website.  

Only the admin has permission to delete assets. The goal of this is preventing malicious users from undoing the hard work of other users. 

User have a profile page where info about their account is displayed.  
My biggest hope is that Top Developer Resources will give valuable information to every person interested in developing their Coding Skills. This is an educational project only.

## User Stories

General User Goals

- Users expect the site to have a clear purpose so that they can understand what it is intended for upon entering.

- Users want to easily navigate the site and find the desired content quickly and easily.

- Users expect the site to be responsive across all devices.

- Users want to have the option to contact the site owner to have their questions/requests answered.

Sign in/Signup Module.

- Register easily and being able to login immediately after registration.

- View/Edit personal details on their profile after having logged in. 

User Action Module

- Discover New High Quality Learning Resources 

- Being able to do searches based on user criteria to find suited resources.

- User’s ability to review learning resources from the site with info about each of them

Crud Operation Module

- Users should be able to add new resources to the to the site.

- Users should be able to edit their added learning resources in the site. 

- Users should be able to Delete them. 

- Users should be getting a confirmation message on every action (Triggering email on action performed).

## Design

### Colour Scheme

The main colors user on the site are grey (#e1e2e2), used for the background, , orange, mainly used for the text, (#fb8122) and black which was used for the nav bar.

### Typography

Arial is the main font used and sans-seriff as fallback. I opted for them because they looks stylish and are easy to read.

### Imagery

The images used are mainly from Unsplash and Pexels.

## Wireframes

I have included all Wireframes in another separate file: 
![Wireframes File](ReadmeFiles/wireframes.md)

## Modifications from the Original Wireframes

- Moved informative content from the index page to a specially created Abous Us page.
- Moved the search box and put it below the image on the home page to make it stand out more.

## Website Structure

### Home

Contains mainly a Search Bar within an Image Background that users can employ to search for learning resources. I used a Mongo DB Search Index to allow users based on the description and name of the learning resources. 

### Resources

Library of Learning Resources. Every learning resource is displayed on a card, being the picture on the left and the info about its type, description, link and created_by on the right

### Log In

To allow users to log in. Users need to submit their email and password to do it. After succesfully having logged in, users get redirected to the profile page. A Register button for non-users can be found on this page.

### Register

Page where is possible to create an account by inputing First and Last Name, Email and a Password. A Login link is  also displayed for visitors that already have an account.

### Ad Resource

Page used to add Learning Resources. All fields (Name, Type, Description and Image) must be filled to complete the process. 
The form is validated and when submited succesfully the user gets redirected to their profile page. 
There is also a reset button to clear all inputted info.

### Profile

Users must have logged in to be able to access their profile page.
On the top of the page there is a Welcome message including the name of the user.
Then there is an image and a section with the user's details (First and Last name and Email Address).
Below that, there is the section Your Resources with 3 Buttons to Add New Resources, Show all of Them and Hide Them.

### Log Out

Log Out option to close the session and go back to the home page.

### About Us

Section with general info about the site: Its purpose, how to use it and general information about the site.

### Common Elements

Refering to the Elements inherited from the base.html Template.

They are the Flash Messages, the navigation menu with Links to the other pages and the footer with Social Media Links.

## Existing Features

• ****Search Box – Used by users to search for resources based on their preferences. 

• ****Resources – Main Elements of the site. Information about the name, type, description and a picture of every one of them is available on the site. They can also be edited and deleted.

• ****Sign Up –  After signing up users can access their profile and upload resources.

• ****Log In –  Used by users to access their accounts

• ****Ad Resources Page – Used by users to access learning resources that will be displayed on the site 

• ****Profile Page - Page that contains info about every user - Their name, email and added learning resources. 

• ****Contact Page - Users can contact through the form with the company regarding requests/doubts. 

## Database Design

MongoDB Object format examples:

Collection: resources
{

    _id:605baeaf012daf172f09a4e4

    resource_category: "Online Education"

    name:"React - The Complete Guide (incl Hooks, React Router, Redux) "

    description: "Learn React or dive deeper into it. Learn the theory, solve assignment..."

    created_by: "SantiagoYanezDub"

    link: "https://www.udemy.com/course/react-the-complete-guide-incl-redux/"

    image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bi..."
}

Collection: resource_type
{

    _id :608abaab4471e2698e7cc453

    resource_category: "Presential Education"
}

Collection: users
{
    
    _id :60a403e6995a56291422199c

    first_name: "santiago"

    last_name: "hernandez"

    email: "santiagohernandez@gmail.com"

    password :"asdasdasd21345!XDA"
}

Security

Database connection details are in an env.py file for development. For security reasons this is not uploaded to GitHub so that database and connection details are not visible to users. 

## Features to Implement in the future

Transform the urls from the resources into affiliate links so that they will be profitable for the company.
Courses Recommendations based on the user profile.
Blog & Relevant News Section about Software Development.
Include an option to review the different resources and filter them based on the reviews.

## Technologies Used
• HTML, CSS & JavaScript Programming Languages

• Python was used for the back-end logic and the means to run/view the Website.
Python Modules used:

click==7.1.2

DateTime==4.3

dnspython==2.1.0

Flask==1.1.2

flask-paginate==0.8.1

Flask-PyMongo==2.3.0

itsdangerous==1.1.0

pymongo==3.11.3

pytz==2021.1

Werkzeug==1.0.1

zope.interface==5.4.0

• GitPod – Used as the Development IDE.

• Bootstrap4 layout to make the form responsive, used a CDN to include it in the project.

• FontAwesome: Great Icons Resource.

• Auto-Prefixer: Extension that adds all necessary extensions to the webite so that it works properly on all major browsers.

• Unsplash: Website that offers high quality free images.

• Realfavicongenerator: Used to create the Favicon.

• FreeLogoDesign: Tool used to design the logo.

• Balsamiq WireFrames: Outstanding Wireframe Software.

• EmailJS: To make the form work and receive visitors requests.

## Testing
The code was validated with the W3C Markup, W3C CSS and JSHint Validator Services to look for syntax errors.
The website passed all tests succesfully with no errors. An excel file with info about the tests performed was included in the repository.

### User Story Testing 

Done using the Test Cases present in the Excel Sheet (Refered as TC-Number)

#### General User Goals

- Users expect the site to have a clear purpose so that they can understand what it is intended for upon entering.
It is clear from the site that is a go-to website for people that want to find resources to improve their coding skills

- Users want to easily navigate the site and find the desired content quickly and easily. Can be done by accessing the resources page and using the search function.

- Users expect the site to be responsive across all devices. TC001, TC002, TC003.

- Users want to have the option to contact the site owner to have their questions/requests answered. TC011, TC012.

#### Sign in/Signup Module.

- Register easily and being able to login immediately after registration. TC009.

- View/Edit personal details on their profile after having logged in. TC014, TC015, TC016, TC017,TC018 & TC019. 


#### User Action Module

- Discover New High Quality Learning Resources. TC006, TC007 & TC008. 

- Being able to do searches based on user criteria to find suited resources. TC006.


#### Crud Operation Module

- Users should be able to add new resources to the to the site. TC015.


- Users should be able to edit their added learning resources in the site. TC018.


- Users should be able to Delete them. TC019.


- Users should be getting a confirmation message on every action (Triggering email on action performed).TC013.


### Test Results
![Test Results](static/images/TestResultsMS3.PNG)

Complete Test Info can be found here 
![Test Results File](ReadmeFiles/Test_Results_MS3.xlsx)

It is an .xlsx file and will a compatible program like excel or google docs to open the file.

## Links and images
All links function and all images are in the Gitpod repository.

## Bugs & Problems found during Testing

• Had problems implementing the search function logic and had to fix several syntax mistakes to make it work. 

• Had problems with the image sizes, needed to give it a though to decide how to make the resources card look as good as possible.

### Further Testing

## Deployment
The website was developed to Heroku, while using Gitpod a a development environment and commiting all changes to GitHub., committed to git and pushed to GitHub. It was then deployed with Github pages from its GitHub following these steps:

Then connected my GitHub account to Heroku and set up Automatic deployment in Heroku under Deploy section in my coinscatalog app.

To run this project follow below steps:

MongoDb:
    Setup MongoDB account and atlas.
    Create a cluster.
    Create new Database learning_resources and add 3 collections: resources, resource_type, users.

Github:
    Create an account and Log in to GitHub, go to the Top_Developer_Resources and download it.
    Click on Code and then on Download the ZIP file
    Upload it to your GiHub Account
    Another Alternative Option would be to Clone or Fork this repository into your github account
    Run the repository from your GitHub repository clicking on the Gitpod button.

Gitpod:
    Create env.py file

    Add env.py file to gitignore

    Add details to env.py file:

      import os
      
      os.environ.setdefault("IP", "0.0.0.0")
      os.environ.setdefault("PORT", "5000")
      os.environ.setdefault("SECRET_KEY", "YOURSECRETKEY")
      os.environ.setdefault("MONGO_URI", "mongodb+srv://root:YOURPASSWORD@YOUR-CLUSTER-NAME.mongodb.net/YOUR-DATABASE-NAME?retryWrites=true&w=majority")
      os.environ.setdefault("MONGO_DBNAME", "YOUR-DATABASE-NAME")

    In terminal create a requirements.txt file by typing pip3 freeze --local > requirements.txt

    In terminal create a Procfile by typing python app.py > Procfile

    In terminal add files, commit and push changes to Github

Deploy a project to Heroku:

    Create a Heroku account and Log in on it
    From dashboard click new > create new app and add the desired name.
    When connected, click on settings > Config Vars and add key and value pairs. Variables shoud be the same as in the env.py file
    From Deploy open Automatic deployment and Connect to GitHub section, then click on github username and repository name
    Heroku will receive all info from your Github repository. Wait for the succesfully completed message.
    Click Open App from top right corner to view the app in a new window.

## Cloning

• Type ‘cd’ in the terminal followed by the desired directory name where 
it will get cloned.

• Click on ‘Code’ (the green drop-down button on the top of the page).

• Copy the last link and type and type ‘git clone’ followed by the copied name.

## Content
• Social Media Icons are from Font Awesome.

• Bootstrap Navbar Documentation helped me to create the navigation menu.

## Media
• Pictures are from Unsplash.com and Google Images.

• The RealFavIconGenerator Page was created using the resource.

## Code

## Acknowledgements
• I would like to thank my mentor Narender Singh, who was of great help in this project and was always really willing to help me and giving me useful feedback to get the most out of my project.

• I checked projects from other students to get an idea of the scope of the project and as inspiration for my project.

## Disclaimer
Fictional Companny Website created as my Milestone Project 3 of the Code Institute Full Stack Program.
