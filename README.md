
https://pypi.org/project/fileGL/
# fileGL
Tired of organizing your files? Yes, You got a Perfect Solution! fileGL is a python package for organizing files into folders.


## Files can be organized based on

    -File creation date
    -File format
    -File Name


# Before starting Please install the PyPi package!!

## To Install:

    pip install fileGL

## After installing, to use the package

    from fileGL import fileGL

### Which folder do you want to sort ?

-If you want to sort the files current folder(current command line working directory) 
then you can skip this step and go to Organising ways

-If you want to sort a files in other directories,
then copy the address(path) .Then call the function
working_path() which takes two optional parameters

    fileGL.working_path(src=True,dest=False)

        -src :source directory 
        -dest:destination directory

        if you want to sort your files in the same directory then call:
                working_path(True)
                when prompted enter the path you have previously copied
        if you want to sort your files in the different directories then call:
                working_path(True,True)
                Now,it will ask two paths,one for source and one for destination
                when prompted enter the both the path you have previously copied.

### Organising Ways

For all the ways of Organising,the function will take a parameter,
    history:For generating a text file containing organising information suchas
            date,time,type of organising ,os_platform, files organised etc,.

### Date-Based Organising

    If you want to organize your files based on date ,
    then call,
        fileGL.datewise(True)

### File-Format based Organising

    If you want to organize your files based on file-format ,
        then call,
            fileGL.typewise(True)

### File-Name based Organising

    If you want to organize your files based on name ,
        then call,
            fileGL.namewise(True)
        In this type,user will be prompted to enter list of file name to organise
        this type of organising will organise by matching list of file names
        entered by user with the file names
        
### What to expect in Future from this package?

    This package is now in development phase.In the mere future various other types will also be added in this package. 
    To list few, dedicated organiser for organising programming files, organising music files etc.,
