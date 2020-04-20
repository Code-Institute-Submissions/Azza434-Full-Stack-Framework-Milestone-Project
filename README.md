[![Build Status](https://travis-ci.com/Azza434/Full-Stack-Framework-Milestone-Project.svg?branch=master)](https://travis-ci.com/Azza434/Full-Stack-Framework-Milestone-Project)
# **ARK Websites**

Ark is a Full Stack Django Website for selling websites, it comes packed with a Profile page for you to check out your account
a Contact Us page where you can complete a form with any questions you might have, and even an about page where you can read
all about who we are.

More importantly it has Websites for sale,A Cart and a Checkout application!
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a customer, I want to be able to add a product to my shopping cart, so that I can procced to purchaes the product.
- As a customer, I want to be able to change the ammount of items in my shopping cart, in case I add to many.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.
![Wireframe 1](https://github.com/Azza434/Full-Stack-Framework-Milestone-Project/blob/master/wireframes/Wireframe%201.png)
![Wireframe 2](https://github.com/Azza434/Full-Stack-Framework-Milestone-Project/blob/master/wireframes/Wireframe%202.png)
## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - Contact Us App | The Contact Us App allows the customer to contact the owner of the website via them filling out an email form.
- Feature 2 - Profile App | The Profile App allows the customer to view their account details,I.E. Full Name and Email.

### Features Left to Implement
- Adding and Changing Items for sale via the items page
- Add more content for the end user to see on their Profile page

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [Python](https://www.python.org/)
    - This project is coded in **Python**
- [Django](https://www.djangoproject.com/)
    - The framework used in this project is **Django**
- [Bootswatch](https://bootswatch.com/)
    - The theme for this project is from **Bootswatch**
- [Bootstrap](https://getbootstrap.com/docs/3.3/)
    - Additional styling used ub this project is from **Bootstrap**
- [Stripe](https://stripe.com/gb)
    - **Stripe** is used to handle payments used in this project
- [AWS](https://aws.amazon.com/)
    - This project uses **AWS** for storage and it's database
- [Heroku](https://dashboard.heroku.com/apps)
    - This project is deployed on **Heroku** [Here](https://ark-websites.herokuapp.com/)


## Testing
Website tested across multiple devices.
- Chrome,Mozila, and Firefox
- iPhone 5 to iPhone X
- iPad and iPad Pro
- Pixel 2 and Pixel 2 XL
- Samsung Galaxy S5

![iPhone](https://github.com/Azza434/Full-Stack-Framework-Milestone-Project/blob/master/wireframes/Iphone%205.png)
![iPod](https://github.com/Azza434/Full-Stack-Framework-Milestone-Project/blob/master/wireframes/iPad.png)

## Deployment
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Heroku Config Vars
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET

In addition, if it is not obvious, you should also describe how to run your code locally.
- Open this project in Gitpod
    - Type in the Terminal **python3 manage.py runserver**
    - You will be promted with a window saying *A service is available on port 8000* Click **Open Browser**
    - You can then register and login

## Credits

### Content
- The text used is Lorem Ipsum

### Media
- The photos used in this site were obtained from my old projects

### Acknowledgements
- I received inspiration for this project from all my projects leading up to this one