# Movie&Music

## Web project.

It is an application that allows you to create a movie and song database added by users

## In short

- the main movie and music section is open to the public and has a list of all videos/songs that have been added by users
- after logging in, everyone has access to all app content
- users can add comments to each entry and issue a scale rating from 1 to 5
- anyone can register via the registration form
- only admin can delete users by Django admin site or after adding special rights to users
- app has a basic Django Rest Framework with users, movies and songs

## Where to start?
The application has a home page with a movie section, a music section, a login and registration section, an editing section, a full description of each entry with the ability to rate it.

1. Home page
     ![movies](https://user-images.githubusercontent.com/121942715/221520338-ac6c74b1-8e8f-47b4-88a0-6f6ea1d69ee2.png)
2. Login and registration section
     ![login](https://user-images.githubusercontent.com/121942715/221520929-0fb9af98-0f90-4939-a905-7d88e0b8d56b.png)
     ![register](https://user-images.githubusercontent.com/121942715/221521001-388a82d3-89a5-4767-8921-d5046006c5d4.png)
3. When the user want to add movie by pressing "Add" button
     ![newmovie](https://user-images.githubusercontent.com/121942715/221521540-98d62297-dd1c-43b1-bcaf-7d47bd315706.png)
4. After adding, we are redirected to the main page where we have the option to delete, edit and see the full description
     ![fullmovie](https://user-images.githubusercontent.com/121942715/221522458-1477eac7-2188-4906-a499-f2f7be126ef1.png)
     ![delete](https://user-images.githubusercontent.com/121942715/221522511-d0ada1e9-ef0d-4664-86fa-6becab283304.png)
     ![editmovie](https://user-images.githubusercontent.com/121942715/221522884-57ef4d1d-deaa-4a7c-9fa7-4ac41f54e380.png)
     ![descmovie](https://user-images.githubusercontent.com/121942715/221522958-f57d1b1c-aa4d-40d4-af3c-d6d42e088ac7.png)
5. In the full description section you can leave your comment after pressing "Add your comment here" and after successful addition, you will receive a confirmation message
     ![reviewmovie](https://user-images.githubusercontent.com/121942715/221523643-5c7f5706-9e09-4ca1-9c19-8cb24075e1f6.png)
     ![desc2movie](https://user-images.githubusercontent.com/121942715/221523660-59c867cb-3a7c-411c-a28b-404b195c9869.png)
    - we can add starts from 1 to 5, default is 0
6. After pressing "Music section" we go to the main Music section page
    ![endmusic](https://user-images.githubusercontent.com/121942715/221524699-3e9d8394-f6fb-4904-afff-b98f0abfc1c1.png)
7. Here, in the edit section, we can add an additional song with a maximum weight of 10mb
     ![editmusic](https://user-images.githubusercontent.com/121942715/221525304-821da88a-c1a6-4c6e-8083-cecb9b312bbb.png)
8. In addition, you can set the genre
     ![relation](https://user-images.githubusercontent.com/121942715/221525559-0ab9ef8a-379d-42e1-97c1-bb251249a877.png)
     Generally there are 3 relations in the database:
     - genre - one to one
     - comments - one to many
     - artists, albums - many to many
9. In the full section it is similar to the movies section with the difference that we additionally have the option of listening to the music that the user has added
     ![fullmusic](https://user-images.githubusercontent.com/121942715/221526397-36a7c8a7-8435-445d-8bcd-800c0d8b29af.png)
     - music can only be added in mp3/wav format
10. This leaves the api section that uses the Django Rest Framework
    ![apistart](https://user-images.githubusercontent.com/121942715/221527258-fa34d3b7-0261-4365-8073-3d8e6bb08b6c.png)
    ![apiend](https://user-images.githubusercontent.com/121942715/221527269-991fcc54-047d-45aa-9d3f-2684aec1f3b4.png)


## What sources did I use?

**Python:**

- django
- Pillow
- django-bootstrap-form
- pydub
- ffmpeg-python
- djangorestframework


**Programs:**

- GIT
- VSC

**Pages that were helpful:**

- https://getbootstrap.com/
- https://fontawesome.com/
