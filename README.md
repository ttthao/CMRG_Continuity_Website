# Cardiac Mechanics Continuity Development Site #
by Jonathan Chiu and Tommy Truong

## CMRG Gmail account:
Used for google analytics.

user: cmrgweb@gmail.com
pass: cmrg lover

## Last Changes: 

#### Thursday, 6/30/2016
Extended the Tutorial table in the Tutorial app to include a header field to be outputted in the jumbotron. Enlarged the faq's question field to char(350) because one of the questions was longer than the original value, 250. Added icons to the footer, made stpes inline editable within the tutorial creation page. Additional styling.

#### Wednesday, 6/29/2016
Finished the Theory App. The functionality of the site is now complete. We will consider adding an extra field within the tutorial's steps table to include a youtube video, so that we can embed it alongside the placeholder. Begun styling the site, picked out a preliminary color palatte, listed below.

#### Tuesday, 6/28/2016
Animations, mobile friendliness, started on Theory app.

#### Monday, 6/27/2016
Finished the structure of the tutorials apphook, including the template and models. New tutorials, tutorial categories, and
individual steps can be created in django's admin panel and dynamically rendered at /tutorial where the apphook is.
Each step has a placeholder field that allows frontend editing.
Default images are now implemented for tutorial categories.

#### Thursday, 6/23/2016
Finished the FAQ app/plugin, including the admin panel and the template.
Structured the sidebar navigation in the Getting Started page.

#### Wednesday, 6/22/2016
Fixed a bug in cms_extensions app where the site would crash if the icon field were left blank.
Finished designs for the rest of the website.

#### Tuesday, 6/21/2016
Finished the Tutorial Category page. We can now view each category and the page will display the individual tutorials in a list-group.
Finished the structure of the tutorial section. Each individual tutorial has a navigation sidebar detailing each step of the tutorial.
Changed styling so that the menu is closed on both desktop and mobile by default.

#### Monday, 6/20/2016
Extended the Page model to include icon and description fields for the Tutorial Home page.

## Todo list
* make a featured app that displays how people put continuity to use. This has to be a plugin (for the carousel in the home page) and also an apphook for the featured page.
* colab with someone from the lab to utilize the youtube addon for the tutorial to make one whole tutorial.

## Things you do not put in the repo:
* static folder (the main one, but do put your app's static folder in the repo)
* pyc files
* swp files

## Any Configuration Changes should be made on the lys server directly
Whenever we pull from the remote onto the lys server, we must do the following:
* chmod 777 project.db
* chmod 777 folder/containing/project.db
* change settings.py to include the absolute path of project.db
* run collectstatic if necessary

## Directory Tree
* Home
* Getting Started
* Tutorial Home
* Theory
* FAQ
* Forum (Piazza for bugs)

## Color Palatte
* black #273030
* white #f7f7f7
* light blue #459db7
* dark blue #0c314b