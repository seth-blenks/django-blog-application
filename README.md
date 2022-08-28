# Django Blog Application ( A Blog)

ABlog is a blogging Web Application built with Django Backend Framework, it include some basic features of a blog site, which include: 
- Post upload
- Post Update
- Post Delete
- Post Display
- Categorical Post Grouping
- Administrators Panel




###  The Landing Page
![Landing Page](/blog/media/s6.png)

### The Details Page
![Details Page](/blog/media/s8.png)

### The Administrator Post Upload Page
![Admins post Upload page](/blog/media/s2.png)
![Admins post upload page](/blog/media/s3.png)

### The General admin post view page
![Admins post view page](/blog/media/s4.png)

## CRUD Operations Using Django Admin

The Django Admin panel, provides an elegant interface for working with the applications models. By replacing the textarea field with Tinymce Editor, the blog post functionality is remarkably transformed into a brilliant editor for all blogging purposes.

## Signal Based Thumbnail Generation

During post upload, thumbnail is implicitly created using the signal functionality of Django. Thumbnails, being placeholder images, are used as previews in a blog website. They are small in size with a very low resolution, and are usually replaced by the original image after the original image has been fully loaded. In this application, this principle is applied using Yall.js.

## Tech Stack

The following tech stack were used to build this application:

- Postgresql
- python ( Django )
- Javascript
- HTML
- CSS
