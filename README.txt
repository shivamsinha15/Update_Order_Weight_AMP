**IMPORTANT**

To use this executable program to update Amplify orders' weight, follow below steps before running the .exe file:

I.	Save Credentials for Login:

1.	Save Mercury Gate TMS login username to 'username.txt'. Do not leave space at the beginning or the end.
2.	Save Mercury Gate TMS login password to 'password.txt'. Do not leave space at the beginning or the end.

II.	Make Sure the User Has the Access to Folder:

1.	Open 'File Explorer' in laptop, go to 'T:\Amplify204\input'.
2.	Try to write and remove a temporary file in this folder. If any of these actions cannot be completed, please submit a ticket to Service Desk (i.e. DSC IT Service) to request access.

How it works:
1.	EDI team (led by Giri Gopal) saves Amplify 204 messages to folder: 'T:\Amplify204\input'.
2.	The program captures PO#, weight information, finds them in TMS.
3.	If anything is found in TMS, the program will go into the shipment's item list, and update the first item's weight using the information grabbed from 204 file provided by EDI team.
4.	The 204 file will then be removed from the folder: 'T:\Amplify204\input'. This was requested by EDI team to save shared drive space.

Keep in mind:
1.	This should be a temporary process before TMS is fully ready to take order through 204 loader. 
2.	A planner (currently Margo J.) from planning team will inform the owner of this process to update weight. Run this program, and let the planner know as soon as possible that the weight is up to date after it completes. Usually, planning happens twice in a day, early morning and late afternoon.