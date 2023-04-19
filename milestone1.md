<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Ashwini Valmiki (av659)</td></tr>
<tr><td> <em>Generated: </em> 4/19/2023 4:58:25 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/av659" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233129583-b4fc4fef-8bf5-4ca7-8012-60c89c603c2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233131710-0eac521f-f836-4cc6-86e5-61696a9ace29.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233130133-1a7401d5-1290-4f4a-99d1-da02f113826f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233132868-9f60d840-1184-4a08-b672-ddf754ec3d33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233132868-9f60d840-1184-4a08-b672-ddf754ec3d33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233133855-d14b53ab-c19d-4b05-8c28-b84e2d5e1c14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233134313-25e720c3-95ef-4c2b-8c07-246f1e54080a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last row has been added in the databse<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(34, 34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small;">Here the form<br>was handled by usage of WTForms.&nbsp;</span><div><span style="color: rgb(34, 34, 34); font-family: Arial, Helvetica,<br>sans-serif; font-size: small;">1. These forms handles&nbsp;</span><span style="color: rgb(34, 34, 34); font-family: Arial, Helvetica,<br>sans-serif; font-size: small;">the rendering and validation in Python.</span><div dir="auto" style="color: rgb(34, 34, 34);<br>font-family: Arial, Helvetica, sans-serif; font-size: small; box-sizing: border-box;">2. The registration class and login<br>class, these two are included in the forms.py which will be used. This<br>registration form will be using the user&#39;s email and password along with confirming<br>the password, thus creating a new user. The login class will be using<br>the existing user&#39;s emailand password to perform a successful login.</div><div dir="auto" style="color: rgb(34,<br>34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small; box-sizing: border-box;">3. The password is<br>such a way that when user tries to attempt a login, the passwords<br>will be matched to the stored data in the database, and when it<br>matches correctly then<br style="box-sizing: border-box;">the user will be able to succeed logging in.</div>&lt;div<br>dir=&quot;auto&quot; style=&quot;color: rgb(34, 34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small; box-sizing: border-box;&quot;&gt;4.<br>DB is utilised by storing the data. All the required data , i.e<br>email and password ,<br style="box-sizing: border-box;">once registered will be in the database. Login<br>will be linked to the<br style="box-sizing: border-box;">database having password values /hashed values .</div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233135497-af6101e9-ab88-4f11-bcf2-c75ecc24ccee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233136833-d32e197a-bc0c-4b14-8404-aa26444a01b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid User <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233137351-46415425-8c75-4772-bcd9-4f8f5e82f284.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login successful , landing page has appeared <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(34, 34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small;">Here the form<br>was handled by usage of WTForms.&nbsp;</span><div><span style="color: rgb(34, 34, 34); font-family: Arial, Helvetica,<br>sans-serif; font-size: small;">1. These forms handles&nbsp;</span><span style="color: rgb(34, 34, 34); font-family: Arial, Helvetica,<br>sans-serif; font-size: small;">the rendering and validation in Python.</span><div dir="auto" style="box-sizing: border-box; color: rgb(34,<br>34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small;">2. The registration class and login<br>class, these two are included in the forms.py which will be used. This<br>registration form will be using the user&#39;s email and password along with confirming<br>the password, thus creating a new user. The login class will be using<br>the existing user&#39;s emailand password to perform a successful login.</div><div dir="auto" style="box-sizing: border-box;<br>color: rgb(34, 34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small;">3. The password is<br>such a way that when user tries to attempt a login, the passwords<br>will be matched to the stored data in the database, and when it<br>matches correctly then<br style="box-sizing: border-box;">the user will be able to succeed logging in.</div>&lt;div<br>dir=&quot;auto&quot; style=&quot;box-sizing: border-box; color: rgb(34, 34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small;&quot;&gt;4.<br>DB is utilised by storing the data. All the required data , i.e<br>email and password ,<br style="box-sizing: border-box;">once registered will be in the database. Login<br>will be linked to the<br style="box-sizing: border-box;">database having password values /hashed values .</div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233138917-0af728d8-bbf7-459d-b1be-eb7d3e5337d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing &quot;Sucessfully logged out &quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233139470-6a3f205b-2288-46d0-97d3-0f77e8d060a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Not logged in <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;"><span lang="EN-GB">The session login<br>handles presenting the login form and receiving/validating the data&nbsp;</span><span style="font-size: 10pt;">to login a<br>user via login_user() from flask_login.&nbsp;</span><span style="font-size: 10pt;">size="2"&gt;Both register and login will create a</span></p><p<br>class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;"><span lang="EN-GB">form object of their<br>respective form.<o:p></o:p></span></p><p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;"><span lang="EN-GB">They’ll use&nbsp;</span><span<br>style="font-size: 10pt;">validate_on_submit() which runs the validator rules of the form when the form<br>submission&nbsp;</span><span style="font-size: 10pt;">is received by the server (again these are client-side and server-side<br>so you&nbsp;</span><span style="font-size: 10pt;">shouldn’t need to do extra validations).</span></p><p class="MsoNormal" style="margin: 3pt 0in;<br>font-size: 10pt; font-family: Verdana, sans-serif;"><span style="font-size: 10pt;">We’ll fetch&nbsp;</span><span style="font-size: 10pt;">the data of the<br>form via form.field.data.&nbsp;</span><span style="font-size: 10pt;">Next,</span></p><p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana,<br>sans-serif;"><span lang="EN-GB">we’ll need to hash the password.<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233139470-6a3f205b-2288-46d0-97d3-0f77e8d060a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Not logged in <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233146464-60dccb51-0482-475a-a1e5-696bdcd44534.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233147676-bd43982d-24aa-4a2e-802a-7c7fe9a350dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>One valid record as Admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233175411-0c7ab989-e437-42f0-b124-4adbc04d70e1.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles Table <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233176051-e734ea68-5bc4-4604-b79d-107edb69d687.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>Id 1 and Id 2 as admins<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>A sample login-protected route. Upon invalid access, it&#39;ll route the user to a<br>built-in access denied page that we&#39;ll override.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>A sample role-proted route. Upon invalid access, it&#39;ll route the user to a<br>built-in access denied page that we&#39;ll override.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233179332-ac45f2e2-b47f-4972-bc2a-8ce7bbddc034.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation is styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233179641-a9baf2cd-4452-41d5-b673-e10c84391c84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login form styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233179332-ac45f2e2-b47f-4972-bc2a-8ce7bbddc034.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Register form styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233180388-88984746-a72a-4f56-9b80-2ae2f8427f54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile form styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233180388-88984746-a72a-4f56-9b80-2ae2f8427f54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles form Styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233181254-8b718bc1-9af0-4449-95da-ec9b039cbcdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output showing in rows<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;"><span lang="EN-GB"><br></span></p><p class="MsoNormal" style="margin:<br>3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;"><span lang="EN-GB">Using Bootstrap navigation,&nbsp;</span><span style="font-size: 10pt;">Navigation is<br>styled by giving "Secondary" and "dark" style color in the nav.html. This made</span></p><p<br>class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;">the site's navigation bar turn<br>black and grey .</p><p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;">In<br>layout.html the edit for footer was done.&nbsp;<br>Since the BG colors were black in<br>color, the text was supposed to be in light.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233135497-af6101e9-ab88-4f11-bcf2-c75ecc24ccee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233187641-f4700640-f60f-475a-b350-45594994a4e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page not found <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233187156-4993a1cb-fab4-44c0-8e42-9b97b5bbaeea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;"><o:p>&nbsp;</o:p></p><p class="MsoNormal" style="margin: 3pt<br>0in; font-size: 10pt; font-family: Verdana, sans-serif;">e're going to use flash messages in order<br>to let know user what<br>exactly is the issue. Letting /prompting such kind can<br>develop a complete clarity<br>to the user.&nbsp;<br>Hence user will not get confused when something<br>wrong happens (wrongly<br>given credentials)&nbsp; since user-friendly messages have been established.<span lang="EN-GB"><o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233188591-57270d72-3d9a-4e1e-bde7-22103fe0b18f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username prefilled properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;"><o:p>&nbsp;</o:p></p><p class="MsoNormal" style="margin: 3pt<br>0in; font-size: 10pt; font-family: Verdana, sans-serif;">From the current_user_flask_login we get the user_id. profileform<br>will get the fresh session data of "user" from profile route in auth.py.<span<br>lang="EN-GB"><o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233190087-bd653746-3aaa-445c-976d-e8b7cb9a9906.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username validation message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233190525-4e8fbf0f-d2d0-49b1-a1f1-2d2847aec6a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233191040-ee992ab7-7a16-43cb-ad4a-bbbdbe9b9060.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233191371-574a41e5-030e-42ac-b2cb-996d365ea94c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233195097-61841c3d-c8a5-485d-bccc-bd6d083aa8f1.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing password <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/233195097-61841c3d-c8a5-485d-bccc-bd6d083aa8f1.jpg"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing Password - hash value changed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/37">https://github.com/AshwiniValmiki/IS601-004/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <ul dir="auto" style="font-size: small; box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; font-family:<br>-apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe<br>UI Emoji&quot;; color: rgb(240, 246, 252);"><li class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family:<br>Verdana, sans-serif;"><span style="color: rgb(0, 0, 0); font-size: 10pt;">On submit will check</span><br></li><p class="MsoNormal" style="margin:<br>3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif; color: rgb(0, 0, 0);">email/username<span style="font-size: 10pt;">Username<br>is checked via regex</span></p><p class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;<br>color: rgb(0, 0, 0);">If current_password, password, and confirm are set it’ll validate<br>current password<br>similar to how login does, and update the password hash with<br>the new password<br>if all succeeds<o:p></o:p></p><ul type="disc" style="margin-bottom: 0in; color: rgb(0, 0, 0); font-size: medium; margin-top:<br>0in;"><ul type="circle" style="margin-bottom: 0in; margin-top: 0in;"><li class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family:<br>Verdana, sans-serif;">Will blindly<br>attempt to update email/username even if there was no change (cheaper<br>than checking<br>first)<o:p></o:p></li><li class="MsoNormal" style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;">Lastly, selects fresh<br>data, applies it to<br>the ProfileForm and refreshes the session data of “user.</li><li class="MsoNormal"<br>style="margin: 3pt 0in; font-size: 10pt; font-family: Verdana, sans-serif;">It’ll then pass the user data<br>to the profile.html template which will be similar to register except with the<br>extra fields<br></li></ul></ul></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: &quot;Times New Roman&quot;, serif;"><span lang="EN-GB">&nbsp;</span></p><p class="MsoNormal"<br>style="margin: 0in; font-size: 12pt; font-family: &quot;Times New Roman&quot;, serif;"><span lang="EN-GB">&nbsp;</span></p><p class="MsoNormal" style="margin: 0in;<br>font-size: 12pt; font-family: &quot;Times New Roman&quot;, serif;">I have learned how to implement Flask-Auth,<br>Flask-Roles and as well as Flask-Profile.<o:p></o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: &quot;Times<br>New Roman&quot;, serif;">While<br>implementing I had an issue with the flask - profile updation.<br>And as<br>well as validation messages.<o:p></o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: &quot;Times New<br>Roman&quot;, serif;">Deploying each branch has made me learn changes in the<br>flask application. Also<br>how the records are registered and updated has made me<br>enthusiastic towards implementing application..<br>Hence<br>I have implemented them.<o:p></o:p></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-av659-prod.herokuapp.com/login">https://is601-av659-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/av659" target="_blank">Grading</a></td></tr></table>