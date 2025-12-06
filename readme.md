#-----Important-----#

Please read this document carefully

I have submitted 2 versions of the app: The first one I submitted is the one that is running on AWS server, with Postgresql; the second one (this version) works with local sqlite database.

When I submitted the paper initially, I though the one that is uploaded to AWS works on all machines locally as well. However, it turns out it does not. The reason is that the database can be accessed by only certain IP addresses. Currently, I set it in a way that only the web application can access the database. 

There was an option to select my IP address but it would only work on my pc. I could also set the IP as something like 0.0.0.0/0 with IPv4 but the problem is in this case the database would be vulnerable to external attacks. Additionally, the uni PCs do not allow accessing this IP address. Therefore, I decided to leave the local sqlite for local testing. The one that I submitted initially, with filename app-5aa6-251205_232815232176.zip also contains sqlite database file but it uses postgres by default. I used sqlite just for testing and decided to leave it just for your reference

As it was the first time I am using AWS, I did not know about these nuances so I am uploading this CW late.

------------IMPORTANT------------
------------AI USAGE-------------

I used AI some parts of the CW and here I want to mention where I used AI:

I constantly had problems with running my AP on AWS, so I had to use AI to get some understanding about using AWS. I have attached my conversation with AI in the previous submission, in text files named INSTANCE_COMMANDS.txt and FINAL_FIX.txt. Also, the code deploy.sh was also partially AI generated.

In all other parts, except connecting to AWS, I did not use AI. All of the work was solely my own. 

USER CREDENTIALS:

--Owner--

username: owner

password: StrongPass123

--Cashier--

username: cashier

password: 1234

--Sales Associate--

username: associate

password: 1234

The username and passwords are the same for both sqlite and postgres. 

Both of the applications running on AWS and locally are the same except databases so the sales history, inventory is not consisted. You can check the functionality of the AWS app by registering some products to the inventory (only owner account can do it).