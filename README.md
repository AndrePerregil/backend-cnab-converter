# backend-cnab-converter
Simple app, back-end tech interview. The goal was to manage the upload of a CNAB file, to decode it, write it's info in a DB and present it's information for the uploader.</br>

## Intro
I was given an example of what the file should be like (it's structure), you can find it in the repo under the name CNAB.example.txt, the context of the file was to encode financial transactions.</br>
It was also requested the the app was designed using python 3.0, i opted to use Django (as even if i didn't know how, i knew with Django i would be able to present the decoded data visually).</br>
It was a really useful exercise, as up to this point i never dealt with file uploading, nor did i work with Django for the front-end (only API).</br>
I definetly want to look more into Django as a front/full-stack framework, really interesting toolset. 

## How it works
It's fairly simple, go to 'http://127.0.0.1:8000/tech_interview/upload/', you'll find a single field form with an upload field.</br>
In this very repo you can find a CNAB file (CNAB.example.txt) select that as your upload (i'm not sure if all CNAB files are strutured in the same way).</br>
After you submission, all the data in the file is decoded and presented back to you, alongside a balance summary at the end for both users and their individual businesses.</br>
</br>
I also took the liberty of doing a single view that does the same, but works more as a standard API. Feel free to check it out on a tool like insomnia. You'll find it at 'http://127.0.0.1:8000/tech_interview/data/'</br>
Just send a 'POST' request with a body of a multipartForm with a filed named file (and the CNAB.example.txt file, of course).</br>
it's logic is identical to the page above, it just doesn't have the rendering to a webpage with the data.

## How to run the project
