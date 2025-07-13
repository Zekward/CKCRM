Author: Zekey Huang

About Project: Simple webpage for CleanKars CRM 

# Quick Start for Running Locally

1. Open this google sheets (https://docs.google.com/spreadsheets/d/14n16WOL1_vzH4QrZ6UM0P0dsrbDR2gqGBf-IjG0NSoI/edit?gid=1054001080#gid=1054001080)
2. Edit the google sheets by creating a new row
    - You will get a popup saying "You’re trying to edit part of this sheet that shouldn’t be changed accidentally. Edit anyway?". Ignore this and edit anyways. 
3. Open this link (https://ckcrm.onrender.com/)
4. Click refresh, a new row should pop up
5. Keep adding rows and click refresh
6. Hover over the green "Group By" button
    - Click on "Stage": this splits the clients into the different stages: new leads, contacted, booked, closed ... 
    - Click on "None": this brings it back into original flat list view. 
7. Fill out new client form at top of page
    - this refreshes page and adds client to bottom


# Techstack

**Frontend**: HTML, CSS, Jinja2
**Backend**: Python, Flask
**Database**: Google Sheets
**Testing**: unittest
**Integrations**: Zapier, Typeform

# Log

## 6/17/25

- Created TypeForm free account
- Created free Zapier account
- Linked Zapier workflow to Google Sheet “MVP CRM Tracker”

Accomplished:
- enter in a typeform -> see it pop up in google sheets 
- set up Github repo for dashboard website

Next steps:
- add other input sources
- add auto emails sent to us when new leads generated 
- trigger an email to lead
- setup web dashboard layout



## 6/18/25

Accomplished: 
- set up Flask server
- when running python py.run, we see base webpage pop up

Next steps:
- add display of sample clients from data.py 
- other input sources



## 6/26/25-6/28/25

All data input streams will be linked to the Google Sheet connected to this Flask app. We can now deploy. 

Accomplished:
- added display of sample clients from data.py loaded from test csv file
- created Google Cloud project and generated a service account key for API authentication
- connected Flask backend to Google Sheets using gspread
- replaced csv test file with live Google Sheets data fetch
- allows new Typeform lead to be displayed on re-run of run.py

Next Steps:
- add support for multiple input sources
- improve frontend layout and styling of dashboard page
- new leads automatically show up when a new Typeform is created
- deploy mvp on aws



## 6/30/25-7/1/25

Accomplished: 
- deployed live MVP dashboard on Render
- converted json files to env variables
- switched to production WSGI server using Gunicorn
- added requirements.txt for dependencies
- Flask app live and publicly accessible on Render

Next Steps:
- front end design
- function to organize rows by stage, location
- other input sources



## 7/6/25 - 7/7/25

Accomplished:
- create grouping function by stage 
- add test suite for data.py functions
- implemented sorting by name and time in both flat and grouped-by-stage views
- group by stage is now fully supported with individual stage tables

Next Steps:
- fix group_by_stage ordering 
- improve visual styling: using color tags or icons for each stage
- add search bar
- enable dragging and dropping into new stages and editing Google Sheets
- make sure each column in the group by stage is lined up properly



## 7/10/25

Accomplished: 
- created add client form allowing for new clients to be appended to sheets
- also viewable in group by stage

Problems for future ref: 
- data structure was not designed first, so new features constantly break or need readjustment to data structure
    - for service focus on designing structure first

Next steps:
- fix column widths in group by staging
- standardize datetime format and phone number format
- make service selectable
- drag & drop feature
- test functions
- refactor data structure to allow for easier feature add-ons



## 7/12/25

Accomplished:
- Refactored codebase and HTML structure to allow for easier scalability
- Fix redirect after adding a client in group stage view
    - previously would redirect to flat view rather than staying in group stage view if already in group stage view
- Get rid of redundant group stage column while in group stage view

Pending features/fixes: 
- fix column widths in group
- standardize datetime and phone number format
- make service selectable with drop down
- drag & drop features
- fix format of sortby buttons on name and time
- fix functionality of sortby (currently only sorts ascending)



## 7/13/25

Accomplished:
- Adjusted group stage view to allow for even column widths. 
- Changed text overflow settings to avoid spilling into other columns

Pending features/fixes:
- standardize datetime and phone number format
- drag & drop 
- fix format of sortby buttons on namne and time
- fix order of group stage
- create topbar with clients list, group stage (actions stream)
- change to each client row displaying only name, number, email, and stage
    - once the client row is clicked on, then redirect to new page with more info
- copy email funcitonality next to each email and number
- followup email auto send button