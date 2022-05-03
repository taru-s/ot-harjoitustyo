# Requirement specification

## Fabric stash manager

An application for managing fabrics and sewing projects
Multiple users can use the application on the same machine by providing unique usernames.

## Basic functionalities:

### before logging in, a user can:
- create a new user name
  - has to be unique  
- log in by providing an existing username
  - if the username provided does not exist, user is prompted to try again or create a bew one
     

### while logged in, a user can:
- view the registered fabrics as a list (done, gui)
  - view the information of a registered fabric (done, gui)
- register new fabrics to the stash (done)
- edit the information of registered fabrics (done, gui)
- delete registered fabrics
  - all (done, text ui)
  - one (done, gui)
- log out and return to the login screen


### additional functionality:

- search and filter fabrics based on certain properties 
  - name (done, text ui, gui)

- register sewing projects in addition to fabrics
- assign fabrics to projects
- view ongoing and finished projects
- edit project details 
- track the completion of project: 
  - add stages to the project
  - mark them as done


## User Interface sketch

![UI sketch of the fabric stash manager application's basic functionality](https://github.com/taru-s/ot-harjoitustyo/blob/master/fabric-stash/dokumentaatio/kuvat/user-interface-sketch.png)

