This is a simple python project on generating food-related tweets

APIs and Frameworks used: <br />
Flask <br />
Tweepy<br />
python-dotenv <br />
AWS Cloud9 <br />
TwitterAPI <br /> <br />


Follow this methodology in order to view the webpage with the tweets:
0. First clone the repository using the git clone command: git clone https://github.com/NJIT-CS490/Proj1-Tweeting.git
1. Once the repository is cloned, you can access the deliv1.py file. Run the python file using the python command: "python deliv1.py". 
2. If you are using AWS cloud9, preview the webpage by using the preview dropdown and selecting "Preview Running Application".

Deployed on Heroku:
The application can be accessed through the URL: https://calm-scrubland-93940.herokuapp.com/

Problems Encountered:
- Wasn't sure exactly what food tweets to captured. I felt it was not very specific in the guidelines as to whether the tweets had to be picked by the user and how specific the foods had to be. I resolved this by going to the TA office hours.
- Another issue I came across was that when I updated my CSS file, the same edits weren't being updated onto my page. I resolved this by running the styling in the HTML file itself.
- I was unsure of how many tweets should be displayed onto the page. It was clarified on the slack channel that the number doesn't matter.
- I was trying to figure out why one tweet rather than 7 was displaying for the my tweetList, but realized later that I forgot to initialize the array before the for loop :D
- I initially had a very ambitious idea for the project which involved the user entering a specific ingredient and a carousel appearing with recipes. However, due to the lack of time I wasn't able to go through with this idea. I would've been able to implement animation and user interface.
- Another issue I came across a lot during working on this project was key errors. I didn't realize until afterwards that spoonacular keys would expire after a certain amount of time. I resolved this by hardcoding the keys and creating a new account on spoonacular if need be.
- Lastly, I was having issues deploying on Heroku. I realized that I had needed to create a requirements text file and Procfile in order for my app to be deployed. In the future, I will keep that these files are important and must be there in order to deploy.