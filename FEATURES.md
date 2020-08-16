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

### All Cocktails
- ##### Search bar
    - The search bar is located at the top of the page and also remains there when searching to other pages. The placeholder text "Search for drinks containing your favourite liquor" makes it easy for users to understand that if theyre looking for drinks containing, for example, Whiskey, they type in whiskey and it will search for all drinks containing whiskey. This search engine is smart and doesnt need the user to be case sensitive or even spell the word correctly. The most relevant data linked to the search will be displayed. The actual search button is standoff-ish on its own and clearly indicates its purpose (search for the queried liquor). Alternatively, the user can also just press the enter key, which is more commonly used on desktop devices, which will give them the same result.  

    - The search bar will always appear at the top on all varied screen size devices, but adjusted its width according to keep everything looking professional and in-line.

- ##### Pagination
    - Using pagination, i was able to reduce how far the user needed to scroll to get to the bottom of the page. Instead of showing every single cocktail recipe on the page, the content is split using pagination. So the user can see the total amount of recipes followed by the number of pages. For example, 'Showing 1 - 9 of 26 Results' - so the user can see 9 of the total 26 results. The total number of pages is then listed, which in this case would be 3 pages, each of which would show a new 9 recipes. As-well-as the number of pages, at the left and right of the number of pages, are a 'Prev' and a 'Next' button. This allows the user to easily navigate through the results. 

    - On desktop, the results for each page are displayed in rows of 3 and also line up with the other elements in the body. Each recipe is displayed in a card format - the user can see an image of the cocktail, followed by the name of the cocktail, what liquors it contains and a link to show more information about the cocktail.

    - On tablet, the recipe cards still look good using the same layout because the content of the page uses less margin on the left and right meaning the cards dont get squashed together.

    - On mobile, the results appear 1 at a time which does take up more real estate on the page, however the images for each drink would be too blurred if i had tried to add more than 1 to each row. This way the image quality remains the same and user can easily see what the specific cocktail has to offer.

- ##### Specific cocktail page (i.e: Sex On The Beach)
    - Clicking 'View Cocktail' on any of the recipes will take the user to that specific drinks page which will show the cocktails ingredients, how to make it and also manage buttons which allow the user to edit that drink, if theirs a missing ingredient, or delete that drink, if its possibly a duplicate or just completely doesnt work.

    - Each ingredient is displayed on its own line next to contasting greater than sign which makes the list easy to read and understand on all screen sizes. On desktop and tablet, the ingredients appear next to the image of the cocktail to reduce any un-necessary scrolling.

    - The 'How to make' information is displayed as a paragraph and takes advantage of the CSS line-height property to make it easier to read on all screen sizes. 

    - For mobile users, all the information is displayed on its own row. Again to maintain the quality of the image, but also keep the content easy to read and visually impacting.

    - ##### Manage buttons
        - Edit: Clicking the edit button will redirect to a page very similar to the 'Add Your Own'. The same form to add your own cocktail will be displayed, however all the information will already be filled in corresponding to the specific cocktail the user has chosen to edit. From here the user can easily pin point the mistake that needs to be edited and then simply click the 'Update Cocktail' button. This will then redirect the user to the page where they can see there changes have been made successfully.
        - Delete: Clicking the delete button will prompt a pop up to appear asking the user if theyre sure they want to delete the cocktail. This adds a layer of security and validation incase the user clicks the wrong button and would accidently delete there recipe.

### Add Cocktail
- ##### Add cocktail form
    - On the 'Add your own cocktail' page, i have made it very clear to guide users, step by step, through adding there own cocktail recipe. Each input field has its own 'title' which informs the user what information goes where. Not only that, but each text-box has placeholder text, further helping the user. 

    - The form is very easy to read and keeps the same principles on all screen sizes. Each text box takes up 100% of the allowed space (within the body margin) and makes for good readability.

    - The actual 'Add Cocktail' button is clearly located at the end of form and uses the strong blue color to stand out amongst the other content. I also positioned the buttom at the right hand side, staggering it from the title, as it is said to improve readability and make the design look better. After all the information is filled out, the user needs to click this button, which will then redirect them to the full list of cocktails where they can see there newly added recipe at the top, showing the user there recipe has been added successfully.

<h3 align="center"><a href="https://github.com/joenapper/drinking-hub/blob/master/README.md">Return to README.md</a></h3>