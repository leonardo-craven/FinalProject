# Installation Instructions:

Install nodejs https://nodejs.org/en/  

Next, install this package:  
https://www.npmjs.com/package/serve  
by running `npm i serve` in the project directory  

Then, run the program by running `npx serve` in the project directory  
It will launch with port 3000 if available  
http://localhost:3000/gallery/twitter.html  

# How to Use:  

Use the time slider to control the range of time for both visualizations  
Use the textbox to input a hashtag to track over the selected date range (note: most hashtags do not have enough data to visualize, use \#coronavirus for a good test case)  
The hashtag visualization only updates when *clicking* the Submit button and after changing the date range (it may take a minute to appear if the date range is more than a couple of days)  
