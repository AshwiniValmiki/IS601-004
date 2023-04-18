<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Ashwini Valmiki (av659)</td></tr>
<tr><td> <em>Generated: </em> 4/13/2023 8:12:54 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/av659" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231017981-b1490b1a-8996-48ea-8d17-d24c29fa85bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 DIAR-mt85 updated to DIAR-av659 of the student (in nav.html)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231549975-a982267e-1395-49b6-9b75-e85186ef330d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 URL is visible and is from heroku dev #3 Index page&#39;s &quot;Brought<br>to you by...&quot; message updated to include my firstname, ucid, and IS601 section<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231018072-6b38c300-41dd-4dbc-bd5c-6f6eecf41e4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Relevant url_for reference added for company search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231018072-6b38c300-41dd-4dbc-bd5c-6f6eecf41e4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Relevant url_for reference should be added for company add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231018334-624148a2-b3f2-46ce-a709-f100e0b65d85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 Relevant url_for reference should be added for employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231018334-624148a2-b3f2-46ce-a709-f100e0b65d85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 Relevant url_for reference should be added for employee add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231018774-a95964c5-2d40-4fd4-b658-2ac298239260.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Relevant url_for reference should be added for admin import<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231019786-00f5a142-1502-4bc0-9c06-a7934d7c1248.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 IS601_MP3_Companies table should be visible (it may be empty or populated)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231019265-538a6a0a-f3b3-4f6e-966e-9515a7e98ee8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 IS601_MP3_Employees table should be visible (it may be empty or populated)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231020122-fbced867-46d5-4e8c-869d-d06362b3795a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 UCID / DB name is visible<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231023845-99e28b4f-1f89-43b1-8520-523d116e5fd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Code checked if the file is a .csv file otherwise reject with<br>a flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231024157-79f7d0a6-95ff-44c7-8254-44d3162bcb31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2	CSV file read from the provided stream as a dict, #3 Extracted employee<br>data appended as a dict to the employee list, #4 Extracted company data<br>appended as a dict to the company list.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231024424-3389c896-48e1-4673-b0b9-505eeb688486.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5After each query flash message about number of companies inserted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231024607-0f1022dc-18a6-4ca8-ac68-70c07c3e33dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 flash message that no companies were loaded if empty data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231025077-3851434e-f51c-4a1d-a6ab-ee5ec3cd2e4c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 After each query flash message about number of employees inserted, #6 Flash<br>message about no companies were loaded if empty data.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231551569-15485864-32f5-478c-b814-f3aa933585f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Showing proper success message #2 Showing proper count messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231559165-01caaf0e-f2b5-4c23-8bdb-95eab584833c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Show the error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231559653-af35ea27-4293-4cb1-b45e-8b0fa701e3d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Show the error message when the form was submitted without a file<br>attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231560336-5f1a507e-ed69-4a3a-86c4-d2c5336d4680.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Screenshot showing some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231560336-5f1a507e-ed69-4a3a-86c4-d2c5336d4680.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Screenshot showing some company data was uploaded #3, #4 Ucid/db name is<br>visible.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231562042-727d7963-b380-4158-9c10-233eac157c11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1, Code should retrieve first_name, last_name, company (id), #2 email, first_name is required<br>(flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231562042-727d7963-b380-4158-9c10-233eac157c11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 last_name is required (flash proper error message if missing),  #4 Company<br>doesn&#39;t require a flash and may be empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231562042-727d7963-b380-4158-9c10-233eac157c11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Email is required (flash proper error message if missing), #6 Email format<br>should be verified (no specific rule, just as long as there&#39;s some attempt<br>that&#39;ll mostly work)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231564616-98d2ed29-869a-4cbe-9d95-2f39c31994c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 Proper INSERT query should be visible along with the data being passed<br>in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231564616-98d2ed29-869a-4cbe-9d95-2f39c31994c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Except block should have a user-friendly message flashed and a print() of<br>the exception #9 #10<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231620392-e6caf927-f342-45df-a762-230ea42397fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231620654-8460f0d7-1494-4285-908a-37e361e7972c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231620887-43e8a312-cb90-4428-a3b1-1dcc0cd9f79e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Show first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231621216-7b111d0d-b441-407c-aceb-ec117ca7102f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Show last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231621452-30870530-59ef-4cd8-af2a-fa925b0e4bca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Show email error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231621452-30870530-59ef-4cd8-af2a-fa925b0e4bca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 URL is visible and is from heroku dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231623572-6417dc98-20b9-489a-ac89-4149af192c52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 included the valid employee data shown previously, #2 Highlighted to which employee<br>to check<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231623572-6417dc98-20b9-489a-ac89-4149af192c52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Ucid/db name should be visible in the screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231624188-45f1eb58-c91d-490d-bc94-7e4668eb92a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 SELECT query should be filled in properly to pull employ id, first_name,<br>last_name, email, company_id, company_name via a LEFT<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231624188-45f1eb58-c91d-490d-bc94-7e4668eb92a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Check request args for fn, ln, email, company, column, order, limit (exact<br>naming is required)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231624446-cde6d949-9294-4af8-af95-3235154e25ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Append like filter for first_name if provided; should have proper wildcards<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231624446-cde6d949-9294-4af8-af95-3235154e25ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Append like filter for last_name if provided; should have proper wildcards<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231624446-cde6d949-9294-4af8-af95-3235154e25ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Append like filter for email if provided; should have proper wildcards<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231624446-cde6d949-9294-4af8-af95-3235154e25ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 Append equality filter for company_id if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231625649-e1af8df3-a9e1-4d09-bafc-5b7a51a17c93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 Append sorting if column and order are provided and within the allowed<br>columns and order options (asc, desc) allowed_columns = [&quot;first_name&quot;, &quot;last_name&quot;, &quot;email&quot;, &quot;company_name&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231625649-e1af8df3-a9e1-4d09-bafc-5b7a51a17c93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Append limit (default 10) or limit greater than or equal to 1<br>and less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231625649-e1af8df3-a9e1-4d09-bafc-5b7a51a17c93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9 Provide a proper error message if limit isn&#39;t a number or if<br>it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231626119-44777518-8015-4b22-b277-ad92d65c902a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#10 Except block should have a user friendly message flashed and a print()<br>of the exception, #11, #12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231627928-6a9d8e37-b78f-4dd0-894f-af5589f30ad0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231628415-98f6fc03-c14c-499e-9488-52962e3c8d18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 results with last_name filter applied;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231628530-4266e1c0-5c2d-4f06-b818-f4bbaf8ea016.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231629157-b5f3d154-0683-47e2-8980-b59cdc8024fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 results with company filter applied;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231628999-72cbb85b-3e28-46d1-b524-86eed49516dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Show one asc filter applied - First_name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231629413-e646c0c4-b0e3-47be-b3d7-f884c63704b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 Show one desc filter applied -<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231629863-7b18be30-38b0-4ed4-8950-aba326a3a732.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Code should retrieve id (from request args) first_name, last_name, company (id), email<br>from form. Missing id should be handled with a flash message and redirected<br>back to employee search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231629863-7b18be30-38b0-4ed4-8950-aba326a3a732.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 First_name is required (flash proper error message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231629863-7b18be30-38b0-4ed4-8950-aba326a3a732.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Last_name is required (flash proper error message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231629863-7b18be30-38b0-4ed4-8950-aba326a3a732.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Company doesn&#39;t require a flash and may be empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231629863-7b18be30-38b0-4ed4-8950-aba326a3a732.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Email is required (flash proper error message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231631052-32023421-cc1e-4e31-b762-fa330b572cb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 	Proper UPDATE query should be visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231631052-32023421-cc1e-4e31-b762-fa330b572cb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 Except blocks (two) should have a user friendly message flashed and a<br>print() of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231631052-32023421-cc1e-4e31-b762-fa330b572cb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Proper SELECT query should be visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231631052-32023421-cc1e-4e31-b762-fa330b572cb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9 Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231632057-408a73ec-3dbb-4ca0-91e1-ea86356fb1a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Showing data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231632609-f36d18eb-37e6-42a6-b8e7-62c662ba414a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Showing data after an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231632883-7c9f074a-81d4-41d1-986b-a146ab2144bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Page should show employee data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231633561-d332ad9a-918b-47e6-a53d-a965b03885b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 #2 Rebbeca&#39;s last name has changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231633561-d332ad9a-918b-47e6-a53d-a965b03885b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Ucid/db name should be visible in the screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Code should retrieve form data for name, address, city, state, country, zip,<br>website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 name is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 address is required (flash proper error message proper message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 city is required <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 state is required <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 state should be validated against pycountry package.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 country is required.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Country should be validated against pycountry package<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9 website is not required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231637926-35a38d6e-28ee-446c-b6d0-7d0ace048880.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#10 zipcode is required (flash proper error message if missing)  .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231639274-1141f0b9-6ed6-4dcc-af79-5f1091fb5b9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#11 Proper INSERT query should be visible along with the data being inserted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231639274-1141f0b9-6ed6-4dcc-af79-5f1091fb5b9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#12 Except block should have a user-friendly message flashed and a print() of<br>the exception #13, #14<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231640973-04552485-45d8-4179-b070-1fe96f447335.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1	Show filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231642595-e6e9aa4f-97ec-4185-9998-18f3c57831a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231642872-ee27bf93-72fa-4a7f-8e33-b67774967c88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Show name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231643138-517f1201-02c9-4509-93b7-2e349776bb9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Show address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231643138-517f1201-02c9-4509-93b7-2e349776bb9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 	Show city error message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231643802-0b801fda-0237-4d72-8090-541511618e01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 Show state error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231643802-0b801fda-0237-4d72-8090-541511618e01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 Show country error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231642872-ee27bf93-72fa-4a7f-8e33-b67774967c88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Show Zip error messsage, #9 , #10<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231645103-0e94d548-89d8-4a73-a7a1-40076ab79c02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Should include the valid company data shown previously,#2<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231647163-d32fbee6-a2be-4ff1-bedc-a23fae7b0763.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 SELECT query should fetch id, name, address, city, country, state, zip, website,<br>employee count (as employee) for the company (likely a sub-query is needed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231647163-d32fbee6-a2be-4ff1-bedc-a23fae7b0763.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Check request args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231651511-2f2f9895-b823-45b8-aa33-50073c7b6949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Append a LIKE filter for name if provided; should have proper wildcards<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231651511-2f2f9895-b823-45b8-aa33-50073c7b6949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Append an equality filter for country if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231651511-2f2f9895-b823-45b8-aa33-50073c7b6949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Append an equality filter for state if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231651511-2f2f9895-b823-45b8-aa33-50073c7b6949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 Append sorting if column and order are provided and within the allows<br>columsn and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231651511-2f2f9895-b823-45b8-aa33-50073c7b6949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 Append limit (default 10) or limit greater than or equal to 1<br>and less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231651511-2f2f9895-b823-45b8-aa33-50073c7b6949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Provide a proper error message if limit isn&#39;t a number or if<br>it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231652308-ddfb2023-f07c-458f-8cb7-a4328e932a63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9 Except block should have a user friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231653598-2da69647-284f-4fae-a0ae-5e904687323d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Results with name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231653963-ec127b88-c06b-423e-b649-0678c7b0ec36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2  Results with country filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231654315-502bb1c1-7a90-4742-8a7c-b6ffea7bbdf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Show results with state filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231654498-5027f618-ad4f-4ecc-a92f-195112078eb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Show one asc filter applied- Name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231738054-9ab8a948-f34c-4952-ab90-3e762e02ab11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Show one desc filter applied- City<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231738416-736e0e65-8adc-4ec7-b8f5-1a228d661f67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Code should retrieve id (from request args) name, address, city, state, country,<br>zip, website from form. If id isn&#39;t present flash related error message and<br>redirect to company search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231739039-1e0116c7-495b-4928-b059-b34c58b37df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Name is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231739039-1e0116c7-495b-4928-b059-b34c58b37df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Address is required <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231739039-1e0116c7-495b-4928-b059-b34c58b37df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 City is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231739039-1e0116c7-495b-4928-b059-b34c58b37df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 State is required.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231739039-1e0116c7-495b-4928-b059-b34c58b37df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6 State should be validated against pycountry package <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231739039-1e0116c7-495b-4928-b059-b34c58b37df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 country is required <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231739039-1e0116c7-495b-4928-b059-b34c58b37df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 country should be validated against pycountry package <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231740502-86b5dc63-320f-4fe3-87d9-44586b7333c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9 Proper UPDATE query should be visible with the passed in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231740502-86b5dc63-320f-4fe3-87d9-44586b7333c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#10 Except blocks (two) should have a user friendly message flashed and a<br>print() of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231741157-2e46d01e-080a-44b1-b9fc-deaad51221d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#11 Proper SELECT query should be visible with the passed in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231741157-2e46d01e-080a-44b1-b9fc-deaad51221d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#12 Company data should be passed to the render_template(), #13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231741688-3f96d307-e703-45d2-9409-4141ab48075a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Showing data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231742139-02f2a2b4-00ab-4874-9f60-9f95dc6a8f46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Showing data after an edit - address changes <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231742317-f0ef4de8-de97-4635-8742-908565b8bea9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Page should show company data in both scenarios, #4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231742898-77cd2ec4-7ce5-4d9c-91bd-74c20d0c1a32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Address has changed<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231743192-7bd2964d-34b8-4514-9175-ba1a38ca7d2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Delete employee by id, if missing should flash the related message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231743192-7bd2964d-34b8-4514-9175-ba1a38ca7d2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Redirecting to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231743192-7bd2964d-34b8-4514-9175-ba1a38ca7d2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 All request args (minus id) are passed to the redirect route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231743192-7bd2964d-34b8-4514-9175-ba1a38ca7d2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Success message should be flashed if the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231744586-7ec6863d-c984-4a8c-a1b6-94db563defce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Before deleting employee with name Rebecca <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231744387-19b6ae7e-ea5c-4175-b8c6-44c8e8741d00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 After deleting an employee with name Rebecca <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231745878-8bd65f6c-102d-4d1c-8dcc-181f9ca15ce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Delete company by id, if missing should flash the related message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231745878-8bd65f6c-102d-4d1c-8dcc-181f9ca15ce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Redirect to company search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231745878-8bd65f6c-102d-4d1c-8dcc-181f9ca15ce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 All request args (minus id) are passed to the redirect route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231745878-8bd65f6c-102d-4d1c-8dcc-181f9ca15ce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Success message should be flashed if the process worked, #5 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231747881-a2ee147c-bfd0-4acb-b1e9-42e0cfd1c1b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Before deleting company 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231748064-6747cf3a-38af-45eb-9de2-6aa5d5522b1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 After deleting company 1 , #3 Sucess message flashed when the process<br>has worked<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231748786-80a1ce44-d5a4-4cb7-a497-9973a4e01522.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_add_company passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231749107-82cdd9a4-5823-43db-8845-a97d2a69bfd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> test_add_employee passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231749461-03968cc4-cc5d-4fff-9d50-bc6b1bdddecc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_edit_company passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231749648-b1616200-1e21-48c1-ba1f-9da635da76ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_edit_employee passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231750052-75c684fa-c0a2-4a8b-bd81-efce46084071.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_search_company passed <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231750318-99320a8e-797b-41d0-b74f-59ae56cc0c19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_search_employee passed <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231750599-215e65f7-24fc-4c47-921b-8f6a71549bb0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_upload_csv passed <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/231751036-161181de-1bca-456d-8d92-d091fe24119b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases passed <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><o:p>&nbsp;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size:<br>12pt; font-family: Calibri, sans-serif;">-&gt; I have learned a lot of significant concepts while<br>doing the project.<br>-&gt;<br>Initially, pip installing the packages made me run the local server<br>application.<br>-&gt; Changing<br>working directory to current project directory in yml file, and then including<br>the<br>current branch name.&nbsp;<br>-&gt; Then I had a problem running test cases, hence I<br>have<br>enabled eco dynos, in the resources tab in Heroku app as well<br>as API<br>key ni github secrets.<br>-&gt; Configured vars in the form of Key<br>value pairs and<br>verifying the same in .env file, Test cases passed as<br>well as app deployed<br>in Heroku<o:p></o:p></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/av659" target="_blank">Grading</a></td></tr></table>