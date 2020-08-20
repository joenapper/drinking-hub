<h1 align="center">The Drinking Hub</h1>

The Drinking Hub is a drinking database for users to discover recipes for cocktails. Not only will visitors be able to browse recipes for drinks, but also share their own.
  
<h2 align="center"><img src="README-assets/drinkHubBanner.png"></h2>
<h2 align="center"><a href="https://drinking-hub.herokuapp.com/">Click HERE For The Live Site</a></h2>

## Table Of Contents
[UX](#user-experience-(ux)) || [User Stories](#user-stories) | [Design](#design) | [Layout](#layout) | [Typography](#typography)

## User Experience (UX)

- ### User stories
    - #### First Time Visitor Goals
        1. As a First Time Visitor, I want to easily find recipes for the drinks I like.
        2. Also, I want to find the ingredients and method for making the cocktail.
        3. Also, I want to easily post my recipe ideas and showcase them to other users.
        4. Also, I want to easily navigate through the site and always have a way of moving to another section.

    - #### Returning Visitor Goals
        1. As a Returning Visitor, I want to see new recipes that I can try.
        2. Also, I want to easily edit or remove my own recipes depending on popularity.

    - #### Frequent User Goals
        1. As a Frequent User, I want to easily contact the admins of the site if I see any issues or bugs.
        2. Also, I want to see continual growth of the database and more recipes.

- ### Design
    - #### Colour Scheme
        - The 2 primary colours I chose for my project was an off white (hex colour #F4F4F4) and a strong blue (hex colour #2474D2). I picked these two colours
        as they compliment each other and radiate cleanliness and simplicity. The psychological effects that the colour scheme has on the user is instant and can
        dictate whether the user will continue to browse the site or leave, thus making it a vital asset.
            - [#F4F4F4](https://www.colorhexa.com/f4f4f4) (off-White): The off-white was used for the background color of the website. This is because,
            as opposed to black, white is a reflective colour which in recent studies has been shown to create a better user experience. This is due to a sub-conscious
            response where, as a user, we are less likely to click on white space and accidentally end up on a different page. 
            - [#2474D2](https://www.colorhexa.com/2474d2) (Strong Blue): The strong blue color was used for all the titles, subtitles, and most buttons.
            These contrast really well against off-white background and stand out to the user, therefor increasing user interactions and making links and other interactive
            features harder to miss.
        To conclude, the color scheme is implemented to create a professional, elegant looking site with great visual representations - contrasting typography
        and striking imagery.

    - #### Layout
        - Throughout the site, I maintained a consistent layout through connecting pages and took advantage of multiple CSS classes to enforce the same design principle
        on other pages and reduce the amount of code needed. Doing this also made the source code cleaner, easier to read, and will allow for easy maintenance (if and
        when is necessary). To create my layout I used CCS grid and flexbox properties.
            - [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout): Grid layout was used mainly on the landing page to equally position
            all the images which are  labeled and link to a specific drink/recipe. The use of this made easy work of perfectly lining up all the images whilst also
            maintaining some responsiveness. I could then simply target the grid layout for smaller screen sizes and adjust them suit.
            - [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox): Flexbox was used primarily for staggering
            sections where there is a lot of text. Breaking up sections by staggering images and text actually improves user readability and creates a better
            overall look.
        The use of these features allowed for a great responsive design. Using the google developer tools I could keep checking how response each section was and keep working
        on each area until I was happy. I had also pre-planned a lot of the interactive features so that I knew how they would function on all screen sizes. For example, the
        navigation bar which collapses into a 'hamburger' menu on mobile and animates smoothly on open and close.

    - #### Typography
        - I used [Google Fonts](https://fonts.google.com/) to import the [Saira](https://fonts.google.com/specimen/Saira?query=saira) font which was set as the base
        font-family for the website. I decided to stick with the one font as I really liked the impact it had on the site. Saira is a highly professional looking
        font and looks great in any size, color, case, and symbol. The font is available in 9 different weights from 'Thin' (100 weight) to 'Black' (900 weight).
        I took advantage of the font-weight property to help distinguish paragraphs from more important headers and titles. The font was imported from Google Fonts to
        the 'style.css' directory, where I could then easily implement it into my work. Although Google is an extremely reliable external source, I added a fallback
        of sans-serif just in case, for whatever reason, the font doesn't get imported correctly.

## Features

**Note:** All Features Information can be located in the separate [FEATURES.md](https://github.com/joenapper/drinking-hub/blob/master/FEATURES.md) due to the length of content.

## Technologies Used

- ### Languages Used
    - [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- ### Libraries Used
    1. [Google Fonts:](https://fonts.google.com/)
        - Google fonts was used to import the 'Saira' font into the 'style.css' file which is used on all pages throughout the project.
    2. [Flask:](https://palletsprojects.com/p/flask/)
        - Flask is the micro web framework that runs the application.
    3. [PyMongo:](https://pymongo.readthedocs.io/en/stable/)
        - PyMongo was used to enable the python application to access the Mongo database.
    4. [Jinja:](https://jinja.palletsprojects.com/en/2.11.x/)
        - Jinja is the default templating language for Flask and is used to display data from the python application in the frontend HTML pages.

- ### Tools Used
    1. [Figma:](https://www.figma.com/)
        - Figma was used to create the wireframes during the design process.
    2. [MongoDB Atlas:](https://www.mongodb.com/)
        - MongoDB Atlas is the database used.
    3. [MongoDB Compass:](https://www.mongodb.com/)
        - MongoDB Compass is an app that allowed me to access the database directly and perform CRUD operations separate from the project.
    4. [Git:](https://git-scm.com/)
        - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
    5. [Gitpod:](https://www.gitpod.io/)
        - Gitpod was the IDE used throughout the entirety of the project. 
    6. [GitHub:](https://github.com/)
        - GitHub is used to store the project's code after being pushed from Git.
    7. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
        - Photoshop was used to create 'README-assets' images. 
    8. [Web Formatter:](https://webformatter.com/)
        - Web Formatter was used to beautify code to keep everything neat and improve readability. 
        - This can also be done by utilizing Beautify Cmd (Shift + Alt + F) in GitPod.
    9. [Grammarly:](https://app.grammarly.com/)
        - Grammarly was used at the end to correct any spelling/grammar mistakes. 
    10. [Jasmine:](https://jasmine.github.io/)
        - Jasmine was used to test the JavaScript before Implementing It into the website.
    11. [EmailJS:](https://www.emailjs.com/)
        - The EmailJS API was used to allow users to contact site admin on bug fixes or any general enquiries. 

- ### Hosting
    1. [Heroku:](https://www.heroku.com/)
        - Heroku was used to deploy the final version of the site.

## Testing

- ### Code Validation
    - #### HTML
        - [W3C HTML Validator](https://validator.w3.org/)
            - All HTML was passed through the HTML validator. Outside of errors thrown due to using the Jinja templating language, which are unavoidable given the nature of the project, everything came back fine.

    - #### CSS
        - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
            - The W3C CSS Validator was used to validate the CSS page to ensure there were no syntax errors in the document.

    - #### JavaScript
        - [JSHint](https://jshint.com/)
            - The JavaScript files were run through JSHINT and apart from a few missed semicolons (which were rectified), no errors displayed.

    - #### Python
        - [Python](http://pep8online.com/)
            - The Python script was checked using pep8online and is fully PEP8 compliant with zero errors or warnings.

- ### Testing User Stories from User Experience (UX) Section

- #### First Time Visitor Goals
    As a First Time Visitor...
    1. I want to easily find recipes for the drinks I like.
        - On the home page theirs a search bar that allows the user to search for drinks that contain a specific liquor. For example... if the user searches 'Vodka'.
    2. I want to find the ingredients and method for making the cocktail.
        - Each cocktail from the home page has a 'View Cocktail' button. If the user likes the look or sound of a drink, they can click this button and it will open a page displaying more information about that specific cocktail, including the ingredients and how to make the drink.
    3. I want to easily post my recipe ideas and showcase them to other users.
        - As a user, adding my own cocktail is the easiest part of the site. In the navbar theirs a 'Add your own' link which takes you to a form. Here you can add your own cocktail with ingredients, how to make, and even your own image. After your recipe is submitted, the user is redirected to the main page where they can see their newly added cocktail at the top of the page. Giving confirmation to the user that their drink has actually been published.
    4. I want to easily navigate through the site and always have a way of moving to another section.
        - The main landing page, add cocktail page, and pages that show more information about each cocktail, are pages that aren't too long, therefore don't allow the user to get trapped as the navbar is always in vision. The navbar allows the user to easily navigate to a desired part of the website and even in smaller screen sizes, transforms into a dropdown menu meaning its always accessible. On main content pages where the list of cocktails is displayed, I used pagination to only show a certain amount of recipes per page, thus cutting down the amount of scrolling for the user. Not only that but I added a 'Back to Top' button at the bottom of the document just to make the site even easier to navigate and avoid any negative experiences.

- #### Returning Visitor Goals
    As a Returning Visitor...
    1. I want to see new recipes that I can try.
        - The list of cocktails has been sorted so that the newest added recipes appear at the top, meaning the user will always see the most recently added first.
    2. I want to easily edit or remove my own recipes depending on popularity.
        - As a user, if I feel like my recipe no longer works or I have found a way to improve it, I can easily edit or delete my recipe using the manage buttons that appear on the main page of each cocktail. If the user wants to delete the recipe, they can click the delete button which will show a disclaimer asking if they are sure. If no is selected, the popup will close, If yes is selected, the drink will be deleted and the user will be returned to the main page. If the edit button is selected, the user will be redirected to a similar form to the 'Add to your' except all the information will already be filled out. Here the user can confirm any changed or simply cancel. 

- #### Frequent User Goals
    As a Frequent User...
    1. I want to easily contact the admins of the site if I see any issues or bugs.
        - If any issues or bugs are found in the site, the user can fill out the contact form (link in the footer) which will send there message to the admin of the site. Alternatively, two other emails are provided in case, for whatever reason, the form goes down. Not only that, but the email addresses are actually clickable and will automatically bring up an email form to make sending an email faster and easier.
    2. I want to see continual growth of the database and more recipes.
        - As stated before, the website automatically shows the newest added cocktails so new drinks can always be easily seen. At the top of the cocktails page, theirs also a counter which shows how many drinks in total. For example "Showing 1-9 of 27 Results". This will update every time a drink is added, showing the user how many drinks in total there is.

- ### CRUD Testing
    1. Create
        - I tested the create functionality of the website by using the 'Add My Own' form. I tried to replicate recipes that I already had in the database, which were added in MongoDB, and then check to see all the information was displayed in the same way. 
    2. Read
        - The read functionality was testing using for loops to display all the cocktails in the database and then from there, all the ingredients and information for each cocktail. This was made more aesthetically pleasing using CSS and displayed in a more professional manner. On the main page, I only displayed the cocktail name, image, and liquors that were in the cocktail so I could display more on the page. If the user wanted to read more about a cocktail, they can click the 'View Cocktail' button, and all the information will be displayed. 
    3. Update
        - The update functionality was tested by adding an 'Edit' button to each cocktail page. I would deliberately add a new cocktail with a spelling mistake and then use the edit button to correct the mistake. I would then go back to the cocktail page and make sure the changes were successful.
    4. Delete
        - The delete functionality was tested by adding clones of a recipe to the database and then using the delete button to make sure the recipes were deleting. I used duplicate cocktails to make sure I wasn't deleting any valuable information from the database. There is also a validation step to the delete process where the user has to click that they are sure they want to delete. I did this just to make sure the user didn't click the button by accident and end up deleting something that they didn't want to.

- ### Bug issues
    - From the start of the project, I was having a lot of trouble using arrays from within MongoDB. I could easily iterate through the data and have it display how I wanted but the problem came when I was trying to add recipes from the form within the website. I'll use the ingredients for example, 50ml of Vodka. So when trying to add this ingredient to the ingredients array... instead of it going into the database as '50ml of Vodka', each letter would display in its own line (i.e. '5' '0' 'm' 'l'..). Because of this bug, I instead listed all the ingredients inside a 'string' and used the .split() method to show each ingredient on its own line. 

- ### Further Testing
    - The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, and Safari browsers. 
    - The website was viewed on a variety of devices such as Desktop, Laptop, Samsung Galaxy S10, iPhone 6s & iPhone X.
    - A large amount of testing was done to ensure that everything rendered and linked correctly on all browsers and a wide variety of devices.
    - All JavaScript code was tested in a separate workspace using Jasmine before importing it into the project. 
    - Friends and Family members were asked to review the site and report feedback on any bugs and/or user experience issues/negative experiences.

## Deployment

- ### Heroku
    - The site was deployed to [Heroku](https://www.heroku.com/) using the following steps...

- #### GitPod
    1. I turned off Flask debugging by setting 'debug=False'.
    2. I created a requirements file with the command 'pip3 freeze --local > requirements.txt'.
    3. I created the Procfile, using the command 'echo web: python app.py > Procfile'. What tells Heroku to run app.py on start-up.
        - Alternatively, this can be achieved by creating the 'Procfile' manually and typing in 'web: python app.py'.
    4. I then logged into Heroku using the command line (heroku login).
    5. I then pushed the repository to Heroku using the command 'git push heroku master'.
    6. Finally, I ran the app using the command 'heroku ps:scale web=1' which tells Heroku to get the site running.

- #### Heroku
    1. From the Heroku dashboard I created a new app, using the name 'drinking-hub' and set the region to Europe.
    2. In the settings tab I clicked reveal config vars and entered the required environment variables, which in this case were:
        - IP: '0.0.0.0'
        - PORT: '5000'
        - Mongo_URI: 'mongodb+srv://root:<password_removed>@myfirstcluster-fai9p.mongodb.net/drink_hub?retryWrites=true&w=majority'
    3. Finally, click the 'open app' button located at the top right of the screen to open the live website.

By completing the above steps I was able to take my code from GitPod and successfully deploy the project to Heroku.

- ### Local Deployment

The following instructions are based on the user running GitPod on Windows 10. If your IDE / OS is different, your commands may differ slightly, but the process remains the same.

As a minimum, you will need Python 3 installed on your machine. You will also need PIP which comes preinstalled with Python versions 3.4 and later. Having a Github account is also necessary.

To deploy locally on your own machine, follow these steps:
- Open the add on / extensions tab in your browser and search for GitPod. The very first result should be the correct extension - click on the result, confirm and 'Add' to your browser.
- Head over to 'https://github.com/joenapper/drinking-hub' and click the green 'GitPod' button (added from the add on / extension). This should open the code in GitPod.
- Install any required modules using the 'pip3 install -r requirements.txt' command in the terminal.
- Within the file app.py change the line app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME") to app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME", '<your_database_name>) where <your_database_name> is the name of the database.
- Also change app.config["MONGO_URI"] = os.getenv('MONGO_URI') to app.config["MONGO_URI"] = os.getenv("MONGO_URI", <your mongo_uri string>) where <your mongo_uri string> is the string that points to your own MongoDB.
- Your database should be named "drink_hub" with collections set up as outlined in the database design section of this document.
- From the terminal, you can then run the app with the command "python3 app.py" and view it in a browser at "http://0.0.0.0:8080/".

## Credits

- ### Content
    - All HTML, CSS, JavaScript and Python code is my own.
    - The recipes for the drinks were sourced from [BBC Good Food](https://www.bbcgoodfood.com/).
    - All other words and text are my own.

- ### Media
    - The images for the drinks have been sourced from their respective recipes at [BBC Good Food](https://www.bbcgoodfood.com/).
    - The cocktail logo was sourced from [Google Images](https://www.google.com/imghp?hl=en)

- ### Acknowledgements
    - My Mentor Mark Railton for continuous helpful feedback and ideas to improve both myself as a developer and my project.