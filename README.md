# wa2html
A Python script to import WhatsApp message exports with image file names, and output an webpage with the images embedded.

How to run
---
The best way to use it currently is running 'python imessage_output.py "WhatsApp Chat with <Contact's name>.txt".
<Contact's name> is parsed out of the input filename, and must match the contacts name in the chat to determine who is the contact sending you messages.

Currently the imessage_output.py script works with this CSS:
https://codepen.io/swards/pen/gxQmbj
Save the CSS file as 'imessage.css' in the same directory.

Known bugs
---
None

To do
---
Add the image file link so you can click and view the full size image. 
Make the output file name based on the input filename
