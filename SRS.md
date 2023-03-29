# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Daren Daya](mmailto:ddaya@uncc.edu)
* [Jordan Wyrick](jwyrick6@uncc.edu)
* [Name](mmailto:email@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.0 | 03/29/23 | GroupMembers | [Daren Daya](mailto:ddaya@uncc.edu) | [Daren Daya](mailto:ddaya@uncc.edu) |


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

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

Jordan Wyrick:
1) ID:REQ-1, Description: create a user repository, Type: Functional, Priority: 1, Rationale: important because it collects users info, Testing: tested with terminal and see if data is saved.
2) ID:REQ-2, Description: create a club repository, Type: Functional, Priority: 2, Rationale: importance because it collects the clubs info, Testing: tested with terminal and see if data is saved.
3) ID:REQ-3, Description: create a app file, Type: Functional, Priority: 1, Rationale: important because it will connect the code and will be the skeleton of all code, Testing: should connect all info from user, website, signup info etc.

Daren Daya:
1) ID:REQ-4, Description: create a catalog repository, Type: Functional, Priority: 1, Rationale: important because it will have a catalog of clubs to join, Testing: should show all options on the website and able to join or request to join.

 2)ID:REQ-5, Description: create a interest repository, Type: Functional, Priority: 2, Rationale: important because it will group people with similar views and beliefs for a club, Testing: should detemrine a match based off similar interests.

 3)ID:REQ-6, Description: create a hybrid/onsite repository, Type: Functional, Priority: 2, Rationale: important because it will show what clubs are in person or online, Testing: Will show what setting this club would meet in and determine what the user wants and show results based off user input.

1)

2)

3)

* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement. Do not replace the word `Description` with the actual description. Put the description in the space where these instructions are written. Maintain that practice for all future sections.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.

## Constraints
Jordan Wyrick
1) Other classes
2) Work

Daren Daya:
1)The project will be mainly written in python, but a constraint with that is the design of the page will be in a different language such as CSS or may even have to use HTML, so we are limitied with design features due to python as the main language.
2) The timeline will be a constraint as it will be due near the time finals start, so getting this done and not waiting until the last minute will be crucial. Finals is very stressful and not having this done before that would add on to stress.

Dustin Putnam:
1)
2)
In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:
Jordan Wyrick
1)ID: UC-1, Description: user will be able to input club name, club description, club events and club loactions, Actors: Users, Precondtions: the user must have a real club with the info above, Postconditions: club will either be created or searched for clubs that are similiar. 
2)ID: UC-2, Description: User will sign-up and creaate a account, Actors: Users, Preconditions: user will be given the option  to signup entering a email and a password, Postconditions: user will have a account with the given email.

Daren Daya: 
3. ID: UC-3 Decription: User will be able to see what clubs are offered online and in person. Actors: Users, Preconditions: the user must input what the desired club meeting setting they are looking for, PostConditions: clubs will show based off of the desired user selected club meeting setting.
4. ID: UC-4 Description: User will select what category club they want to join. Actors: Users, Preconditions: the user must input what kind of category club the user wants to join, PostConditions: the page will display results of clubs selected based off category the user selected.



Dustin Putnam:
* **ID:** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:


Jordan Wyrick:
1) ID: US-1, Type of User: Student, Description: I want to attend a basketball club event but I dont know when and where so I searched up basketball clubs and it told me the information that I needed.
2)ID: US-2, Type of User: Student, Description: I want to create a club so I can make new friends so I create a video geama club for other people that like video games.

Daren Daya:
1) ID: US-3, Type of User: Student, Description: I want to see what clubs are online and which ones are in person, I prefer to join a in person basketball club to make new friends and play basketball with them.
2) ID: US-4, Type of User: Student, Description: I want to see what kind of clubs are online for gaming specifically Call of duty, NBA 2K23, and FIfa 23. I am also open to any in person clubs.


Dustin Putnam:
1)
2)




* **ID:** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:
Jordan Wyrick:
1) Term: Repository, Definition: computer storage for maintaining data or software packages

Daren Daya:
1)Term: CSS, Defintion: Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTM


Dustin Putnam:
1)
* **Term:** The term that is being defined. This should be a single word or phrase that is being defined.
  * **Definition:** A definition of the term. This should be a short description of the term that is being defined. This should be a single sentence that describes the term.
