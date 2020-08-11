<h1 align="center">The Drinking Hub</h1>

The Drinking Hub is a drinking database for users to discover recipes for cocktails. Not only will visitors be able to browse recipes for drinks, but also share their own.
  
<h2 align="center"><img src="README-assets/drinkHubBanner.png"></h2>
<h2 align="center"><a href="#">Click HERE For The Live Site</a></h2>

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
            as opposed to black, white is a reflective colour which in recent studies has been shown to create better user experience. This is due to sub-conscious
            response where, as a user, we are less likely to click on white space and accidently end up on a different page. 
            - [#2474D2](https://www.colorhexa.com/2474d2) (Strong Blue): The strong blue color was used for all the titles, subtitles and most buttons.
            These contrasts really well against off-white background and stand out to the user, therefor increasing user interactions and making links and other interactive
            features harder to miss.
        To conclude, the color scheme is implemented to create a professional, elegant looking site with great visual representations - contrasting typography
        and striking imagery.

    - #### Layout
        - Throughout the site I maintained a consistent layout through connecting pages and took advantage of multiple CSS classes to enforce the same design principle
        on other pages and reduce the amount of code needed. Doing this also made the source code cleaner, easier to read and will allow for easy maintainance (if and
        when is necessary). To create my layout I used CCS grid and flexbox properties.
            - [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout): Grid layout was used mainly on the landing page to equally position
            all the images which are labelled and link to a specific drink/recipe. The use of this made easy work of perfectly lining up all the images whilst also
            maintaining some responsiveness. I could them simply target the grid layout for smaller screen sizes adjust the sizes to suit.
            - [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox): Flexbox was used primarily for stagering
            sections where there is a lot of text. Breaking up sections by stagering images and text actually improves user readability and creates a better
            overall look.
        The use of these features allowed for great responsive design. Using the google developer tools I could keep checking how response each section was and keep working
        on each area untill I was happy. I had also pre-planned a lot of the interactive features so that I knew how they would function on all screen sizes. For example, the
        navigation bar which collapses into a 'hamburger' menu on mobile and animates smoothly on open and close.

    - #### Typography
        - I used [Google Fonts](https://fonts.google.com/) to import the [Saira](https://fonts.google.com/specimen/Saira?query=saira) font which was set as the base
        font-family for the website. I decided to stick with the one font as I really liked the impact it had on the site. Saira, is a highly professional looking
        font and looks great in any size, color, case and symbol. The font is available in 9 different weights from 'Thin' (100 weight) to 'Black' (900 weight).
        I took advantage of the font-weight property to help distinguish paragraphs from more important headers and titles. The font was imported from Google Fonts to
        the 'style.css' directory, where I could then easily implement it into my work. Although google is an extremely reliable external source, I added a fallback
        of sans-serif just in case, for whatever reason, the font doesnt get imported correctly.

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
        - Jinja is the default templating language for flask and is used to display data from the python application in the frontend html pages

- ### Tools Used
    1. [Figma:](https://www.figma.com/)
        - Figma was used to create the wireframes during the design process.
    2. [MongoDB Atlas:](https://www.mongodb.com/)
        - MongoDB Atlas is the database used.
    3. [MongoDB Compass:](https://www.mongodb.com/)
        - MongoDB Compass is an app that allowed me to access the database directly and perform CRUD operations separate to the project.
    4. [Git:](https://git-scm.com/)
        - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
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

    - #### JavaScript
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
        - As a user, adding my own cocktail is the easiest part of the site. In the navbar theirs a 'Add your own' link which takes you to a form. Here you can add your own cocktail with ingredients, how to make and even your own image. After your recipe is submitted, the user is redirected to the main page were they can see their newly added cocktail at the top of the page. Giving confirmation to the user that their drink has actually been published.
    4. I want to easily navigate through the site and always have a way of moving to another section.
        - The main landing page, add cocktail page and pages which show more information about each cockail, are pages that arent too long, therfor dont allow the user to get trapped as the navbar is always in vision. The navbar allows the user to easily navigate to a desired part of the website and even in smaller screen sizes, transforms into a dropdown menu meaning its always accessable. On main content pages were the list of cocktails is displayed, i used pagination to only show a certain amount of recipes per page, thus cutting down the amount of scrolling for the user. Not only that but i added a 'Back to Top' button at the bottom of the document just to make the site even easier to navigate and avoid any negative experiences.

- #### Returning Visitor Goals
    As a Returning Visitor...
    1. I want to see new recipes that I can try.
        - The list of cocktails has been sorted so that the newest added recipes appear at the top, meaning the user will always see the most recently added first.
    2. I want to easily edit or remove my own recipes depending on popularity.
        - As a user, if i feel like my recipe no longer works or i have found a way to improve it, i can easily edit or delete my recipe using the manage buttons that appear on the main page of each cocktail. If the user wants to delete the recipe, they can click the delete button which will show a disclaimer asking if they are sure. If no is selected, the popup will close, If yes is selected, the drink will be deleted and the user will be returned to the main page. If the edit button is selected, the user will be redirected to a similar form to the 'Add to your' except all the information will already to filled out. Here the user can confirm any changed or simply cancel. 

- #### Frequent User Goals
    As a Frequent User...
    1. I want to easily contact the admins of the site if I see any issues or bugs.
        - If any issues or bugs are found in the site, the user can fill out the contact form (link in the footer) which will send there message to the admin of the site. Alternatively, two other emails are provided in case, for whatever reason, the form goes down. Not only that, but the email addresses are acually clickable and will automatically bring up an email form to make sending an email faster and easier.
    2. I want to see continual growth of the database and more recipes.
        - As stated before, the website automatically shows the newest added cocktails so new drinks can always be easily seen. At the top of the cocktails page, theirs also a counter which shows how many drinks in total. For example "Showing 1-9 of 27 Results". This will update everytime a drink is added, showing the user how many drinks in total their is.
