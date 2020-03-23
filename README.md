# Fridge
SFIA Project 1
# Fridge App
## Contents:
1. Brief
2. Planning and Proposal
3. Risk Assessment
4. Entity Relationship Diagrams
5. Testing
6. CICD
7. Deployment
8. Technologies Used
9. What I would change
10. What worked well

### Brief

The brief was to create and a CRUD functional application which was linked to a database that has a minimum of 2 tables, sharing a relationship. The tables were not allowed to be called Users or Posts

### Planning and Proposal

I developed my app called ‘Fridge’. In this app I had 2 tables: Food and Recipes, because they had a many to many relationship, I had to create a third table; ingredients.

The home page would allow you to see what items in the fridge, with options to add, update or delete these files provided on the app

I planned using my Trello board (link here https://trello.com/b/clVv6OSR/in-my-fridge). I used the agile method to cover the MVP first, and then added more functionalities and options in later sprints.

### Risk Assessment

I created a risk assessment to map out risks, and create solutions. I took these solutions and integrated it with my project.
[riskassessmentlink]

### Entity Relationship Diagrams
![FirstFridgeSprint](/Documentation/FirstFridgeSprint.png)

My first fridge sprint was to cover the MVP. 2 very simple tables, with a table that connects them both

![SecondFridgeSprint](/Documentation/SecondFridgeSprint.png)
My Second Sprint gave the items more details 

### Deployment
To deploy my working app, I created a freestyle project on Jenkins. When this test was run it executed a shell which ran commands (including secret keys etc.) that deployed my app using Gunicorn.

### Testing 

I utilised pytest and started to develop integrated testing with selenium to test my website. This was an aspect I would need to add more to.

### CICD Pipeline
![FirstFridgeSprint](/Documentation/FirstFridgeSprint.png)

###Technologies Used
Kanban Board: Trello
Database: GCP SQL Server
Programming language: Python
Unit Testing with Python (Pytest)
Integration Testing with Python (Selenium)
Front-end: Flask (HTML)
Version Control: Git
CI Server: Jenkins
Cloud server: GCP Compute Engine

### What worked well
During this project, I think I adapted well to working from home, and re-learning the materials with help from trainers. I enjoyed debugging my code when there were errors and learning through making mistakes.


### What I would change
With more time I would firstly include more testing. I would also like to add functionality noted on my Trello board and create a web hook so my app would update and test along with any changes made on the repository.


