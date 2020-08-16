<h1 align="center">The Drinking Hub</h1>

<h2 align="center"><a href="https://github.com/joenapper/drinking-hub/blob/master/README.md">Back to full README file</a></h2>

##### Note: FEATURES.MD is in a separate file to the [README.md](https://github.com/joenapper/drinking-hub/blob/master/README.md) to keep the file a reasonable length and to maintain cleanliness.

## Features

### Site Wide 
    - The base of the website is primarily made up of landing page, which explains the purpose of the site, the cocktails page, which shows all the added drink recipes and the 'Add Your Own' page, which allows the user to creat and add there own creations. The use of the Jinja templating language allowed me to implement a consistent layout throughout the site using a 'base.html' file and 'block content'. I was able to build a footer and complex, responsive navbar, with an animated 'burger' icon drop down menu for smaller screen sizes for the 'base.html' page. The use of this allowed me to show the header and footer on every page without having to rewrite any code.    

- ##### The Navigation Bar
    - The navigation bar is fully responsive and is aesthetically pleasing on all platforms and devices. 
    
    - On desktop view (screen width size of 992px and above) the brand name is located at the far left-hand side of the navigation bar followed by the links to the other pages.

    - On tablet view (screen width sizes between 992px to 767px), all the links still fit on a single line and looks good, so no changed are needed.

    - On mobile view & smaller screen sized devices (screen width sizes under 767px) the logo remains over the left-hand side however, the links are replaced by a 'hamburger' icon which stays over to the right. On click of this icon, the 'burger' animates and all the links slide in from the top. The background of this slide in menu is slightly transparent so the user can still see the content, but dark enough so the links stand out and can be seen clearly. 

- ##### The Footer
    - The footer is fairly basic but still necessary. It contains the copyright information for the website as-well-as links for the contact page and privacy policy.

    - The footer is also fully responsive, however, there are no changes as we go down the display sizes as it is not necessary.

### Home Page (Landing Page)
- ##### About section
    - When the site is first opened, the user can see a short paragraph explaining the purpose of the site and also links to the main cocktails page where all the drink recipes are displayed. This information is displayed with a border around it, which catches the attention of the user and makes it more visually inpacting.

    - On tablet and mobile screen sizes, the font-size is changed to look more suited for the intended screen size, as-well-as the width of the box taking up more space on the screen, to display more information without having to scroll down a lot of text, which would cause a bad user experience.

- ##### Liquors section
    - Under the 'About section', all the liquor types are listed as button links, and it becomes very apparent to the user that if they click on one of the links, they will be re-directed to a page which shows them all the recipes containing that specific liquor. For example, clicking 'Vodka', would show all the cocktails containing Vodka.
    
    - On desktop devices, all 8 of these links appear in-line and take up the same width as the above 'About section' which keeps the layout looking professional. If the user hovers over the button, the button changes color and the cursor changes to 'pointer' further adding to their clickability.

    - On tablet, the links appear in 2 rows of 4 with equal margin between each of them and continue to follow a consistent overall width down the entire page.

    - On mobile, i decided to remove the buttons as they only looked good if i were to display each button on its own row. This would have been a problem as the user would have to scroll for a while in order to see all the options. Doing things this way, allowed me to keep 100% of the page visable at all times and avoid any bad user ecperience. 

