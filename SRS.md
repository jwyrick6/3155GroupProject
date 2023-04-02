# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Daren Daya](ddaya@uncc.edu)
* [Jordan Wyrick](jwyrick6@uncc.edu)
* [Dustin Putnam](dputnam6@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.0 | 03/29/23 | GroupMembers | [Daren Daya](mailto:ddaya@uncc.edu) | [Daren Daya](mailto:ddaya@uncc.edu) |
| 1.0 | 03/29/23 | Added my information | [Dustin Putnam](dputnam6@uncc.edu) | [Dustin Putnam](dputnam6@uncc.edu)|


## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction
For our project, we are wanting to create a website that will able to receieve inputs from the user and gather information to create clubs. Our website will also have the ability to search certain characteristics to find the right club for the user. The stakeholders of the system are users looking to connect with others and do the things they enjoy with others.

## Requirements

Jordan Wyrick:
1) ID:REQ-1, Description: create a user repository, Type: Functional, Priority: 1, Rationale: important because it collects users info, Testing: tested with terminal and see if data is saved.
2) ID:REQ-2, Description: create a club repository, Type: Functional, Priority: 2, Rationale: importance because it collects the clubs info, Testing: tested with terminal and see if data is saved.
3) ID:REQ-3, Description: create a app file, Type: Functional, Priority: 3, Rationale: important because it will connect the code and will be the skeleton of all code, Testing: should connect all info from user, website, signup info etc.

Daren Daya:

1) ID:REQ-4, Description: create a catalog repository, Type: Functional, Priority: 1, Rationale: important because it will have a catalog of clubs to join, Testing: should show all options on the website and able to join or request to join.

2) ID:REQ-5, Description: create a interest repository, Type: Functional, Priority: 2, Rationale: important because it will group people with similar views and beliefs for a club, Testing: should detemrine a match based off similar interests.

3) ID:REQ-6, Description: create a hybrid/onsite repository, Type: Functional, Priority: 2, Rationale: important because it will show what clubs are in person or online, Testing: Will show what setting this club would meet in and determine what the user wants and show results based off user input.

Dustin Putnam:
1) ID:REQ-7, Description: create a tag system, Type: Functional, Priority: 1, Rationale: important because it will be the mechanism for how people can find clubs and how the clubs themselves are grouped, Testing: test whether tags can be created, edited, deleted, and that they persist.

2) ID:REQ-8, Description: create a chat system, Type: Functional, Priority: 3, Rationale: important because it allows people to chat with others in clubs, Testing: test whether text is saved, edited, deleted, and that they persist.

3) ID:REQ-9, Description: create a calendar system, Type: Functional, Priority: 2, Rationale: important because it allows the club to post reminders for events, Testing: test whether the reminders can be saved, edited, deleted, and if they persist.


## Constraints
Jordan Wyrick
1) Other classes
2) Work

Daren Daya:
1)The project will be mainly written in python, but a constraint with that is the design of the page will be in a different language such as CSS or may even have to use HTML, so we are limitied with design features due to python as the main language.
2) The timeline will be a constraint as it will be due near the time finals start, so getting this done and not waiting until the last minute will be crucial. Finals is very stressful and not having this done before that would add on to stress.

Dustin Putnam:
1) The main constraint for me is that I have little experience with web development, so it will be a challenge.
2) I have a decent sized workload, so I won't have as much time as I would like to work on it.


## Use Cases

Jordan Wyrick:
1) ID: UC-1, Description: user will be able to input club name, club description, club events and club loactions, Actors: Users, Precondtions: the user must have a real club with the info above, Postconditions: club will either be created or searched for clubs that are similiar. 

2) ID: UC-2, Description: User will sign-up and create a account, Actors: Users, Preconditions: user will be given the option  to signup entering a email and a password, Postconditions: user will have a account with the given email.

Daren Daya: 

3) ID: UC-3, Decription: User will be able to see what clubs are offered online and in person. Actors: Users, Preconditions: the user must input what the desired club meeting setting they are looking for, PostConditions: clubs will show based off of the desired user selected club meeting setting.

4) ID: UC-4, Description: User will select what category club they want to join. Actors: Users, Preconditions: the user must input what kind of category club the user wants to join, PostConditions: the page will display results of clubs selected based off category the user selected.

Dustin Putnam:

5) ID: UC-5, Description: User will be able to chat with others in a club, Actors: Users, Preconditions: The user must have an account and sign up for a club, Postconditions: The users chatting will receive the messages.

6) ID: UC-6, Description: User will be able see reminders about events for their club, Actors: Users, Preconditions: The user must have an account and be signed up for a club, Postconditions: The user will be able to see the reminders and when they will happen.


## User Stories

Jordan Wyrick:
1) ID: US-1, Type of User: Student, Description: I want to attend a basketball club event but I dont know when and where so I searched up basketball clubs and it told me the information that I needed.

2) ID: US-2, Type of User: Student, Description: I want to create a club so I can make new friends so I create a video geama club for other people that like video games.

Daren Daya:
1) ID: US-3, Type of User: Student, Description: I want to see what clubs are online and which ones are in person, I prefer to join a in person basketball club to make new friends and play basketball with them.

2) ID: US-4, Type of User: Student, Description: I want to see what kind of clubs are online for gaming specifically Call of duty, NBA 2K23, and FIfa 23. I am also open to any in person clubs.

Dustin Putnam:
1) ID: US-5, Type of User: Student, Description: I want to be able to communicate with other students outside of meeting times to keep in touch with the people I meet.

2) ID: US-6, Type of User: Student, Description: I want to be able to easily remember when events are happening for my clubs so that I am less likely to miss them.


## Glossary

Jordan Wyrick:
1) Term: Repository, Definition: computer storage for maintaining data or software packages

Daren Daya:
1) Term: CSS, Defintion: Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML

Dustin Putnam:
1)Term: Query, Description: a request for data from a database
