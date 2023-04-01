# Aibo
#### Video Demo:  <https://youtu.be/ukj3PpZ8Iv4>
#### Description:

My girlfriend and I will be moving to Canada soon so I thought of creating a web application that could be beneficial in our new adventure. We always wanted to have an intuitive app where we can easily input, edit, save and delete all our daily expenses without the need of having to go through so many hoops just to record and view past transactions. It should also be an app that we can easily use on-the-go every time we need it.

I chose to name the application "Aibo" which stands for "partner" in japanese. Our dream has always been to live in Japan and everything that we're doing is towards reaching that goal. This app will serve as one of our partners in this journey whose main role is to help us keep our finances in check along the way.

That's the inspiration for my project - to create something useful, convenient, and easy to use for our next step in life!

The design is very minimalistic and makes use of several icons and buttons to navigate around the application. I wanted it to look sleek, clean and less intimidating so that my partner and I will enjoy using it on a daily basis. Looking at a page or application that's too wordy and cluttered on a daily basis might make the user feel that it's too much of a hassle to use and stressful to look at. I also took the width of an Iphone into consideration because it's the device that we plan on using the web app on everyday.

The application retrieves its data from the project.db database which contains the following tables:
'1. users table - The users table contains the id, unique username and password hash of the registered user
'2. transaction_type table - This table contains the different categories the user can file his/her purchases under
'3. session table - The sessions table contains all the purchases of the user for the current shopping session. The table initally records all the necessary information about the purchase. This table is cleared once the user chooses to save all the contents to their account/total expenses.
'4. savedData table - The savedData table houses all the saved purchases of all users. The information from the session table is transfered here once the user chooses to save the current shopping session.
'5. budget table - This contains the budget set by the users for a specified month as well as the expense retrieved from the users total expenses in the savedData table.

Aibo has three main pages - the user's current shopping session (index.html), the summary of the user's expenses (summary.html) and the user's budget analysis (budget.html).

index.html:
The index of the page contains required input fields for the item that was or will be purchased. Once an item has been placed, it will be stored in the session table found in project.db.

The session database will house all items that have been purchased by the user for the current shopping session. It will store the user's id and the transaction number of the purchase, as well as the item's category, purchase date, description, price, quantity and total cost.

If, at any point, the user wishes to clear all the contents of the current shopping session, he/she can click the refresh/reset icon. This will delete all rows in the session table without saving it anywhere. After clicking, a prompt will appear to reconfirm the user's actions. If the user clicks yes, the deletion of table rows will be executed.

If the user wishes to delete only one row, he/she can click on the delete button and choose the transaction number of the item that he/she wishes to delete from the current shopping session.

Once the user is satisfied with his/her purchases for the session, he/she can save the contents of the cart by clicking on the save icon. The application copies the contents of the session table, inserts them to the savedData table before, finally, clearing all the rows in the session table.

summary.html:
The summmary page contains all the contents of the saved purchases of the user which is stored in the savedData table of project.db. Here the user can view the his/her total expenses for each category.

The user can edit or delete past purchases by clicking on the Edit/Delete button. This will manipulate the rows of the savedData table. To avoid errors, editing a row would require the user to input an item name, quantity and price of the selected transaction number. Similar to the delete function found on the index page, the delete function on the summary page will only require the transaction number to avoid deletion of similar items.

The contents of the table can also be filtered by date through the "Select Date" button. This will change the tables displayed to only show the contents from the selected date.

Lastly, the "Save" button will give the user the option to print the displayed table. A new page will be opened up and the contents of the currently selected date and category will be written on a table there. The user will then be prompted to Print/Save the page. If the user decides to cancel the action, the page will automatically close.

To keep the page sleek and clean, I chose to display the categories in regular underlined text. I included a hover animation, which looks like a post-it tab, to indicate which category is being selected to avoid confusion on the user's end. These buttons will filter the contents of the displayed table based on the chosen category. Even if a different category has been chosen, the date selected will not change. The buttons have been arranged in a way that will fit inside an Iphone's display width. I limited the button's width to 100px to avoid too much resizing whenever the screen size changes and keep it uniform.

budget.html:
The budget page shows an analysis of the budget for the specified date and the amount already used up by the user's expenses, broken down by category.

The user can filter the items displayed on the table by clicking on the "Date" button. Selecting a date will change the displayed budget to the assigned budget for the specified month or, if no budget has been assigned, zero.

If the user wishes to set a budget for a particular month, he/she can click on the "Budget" button and fill in the necessary details. This will insert a new row on the budget table found in project.db which will contain the user's id, expenses for the specified date, the set budget for the specified date, and the savings for the month calculated by subtracting the user's expenses from the set budget.

Clicking the "Summary" button will show a table that contains all the rows found in the budget table in project.db.

The "Date" and "Budget" actions will generate new rows if the selected date or date visited has no prior record. These new rows will also appear in the "Summary" table of the page.

Lastly, aside from the main pages, Aibo also has a login and registration feature. New users can create their own accounts through the registration page (register.html). The username should be 5-20 characters long and allows alphanumeric characters to be used including "." and "_". Passwords should be at least 8 characters long and allows alphanumeric characters and symbols to be used. Once the user has chosen a password, it should be retyped on the confirmation field before submitting. The information stored as the password is the password hash generated by werkzeug.security. All of the registered user's information are saved in the user's table in project.db
