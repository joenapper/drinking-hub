<h1 align="center">The Drinking Hub</h1>

The Drinking Hub is a drinking database for users to discover recipes for cocktails. Not only will visitors be able to browse recipes for drinks, but also share their own.
  
<h2 align="center"><img src="README-assets/drinkHubBanner.png"></h2>
<h2 align="center"><a href="#">Click HERE For The Live Site</a></h2>

## User Experience (UX)

- ### User stories
    - #### First Time Visitor Goals
        1. As a First Time Visitor, I want to easily find recipes for the drinks I like.
        2. Also, I want to find the ingredients and method for making the cocktail.
        4. Also, I want to easily post my recipe ideas and showcase them to other users.
        3. Also, I want to easily navigate through the site and always have a way of moving to another section.

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
    




