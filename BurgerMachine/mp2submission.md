<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Ashwini Valmiki (av659)</td></tr>
<tr><td> <em>Generated: </em> 3/22/2023 10:19:21 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/av659" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226492293-33ba5830-f5bb-4137-bb46-f34b2fe5337a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 ucid and date present in the screenshot , #2 Method calculated the<br>proper value of the inprogress_burger array <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226492729-a32b851f-af76-40d8-980b-3479390a1dbc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 The costs are defined as part of the given data and should<br>aren&#39;t modified<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226492293-33ba5830-f5bb-4137-bb46-f34b2fe5337a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Calculated value is returned from the function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226492796-8af73fc0-88e3-4a57-8824-6a12b121a473.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4  #5 The input() message is properly displayed in the value in<br>currency format. with &quot;$&quot; symbol.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <div>1. The <b>total cost </b>is calculated by using for loop and visiting the</div><div>items<br>that are invoked by the inprogress_burger array :</div><div><ul><li>Inside the for loop ,the expected<br>cost is <b>incremented to n.cost </b>by considering the sum of all the items<br>in the array.</li><li>Then the function is <b>returned</b> to make it print it out<br>to the user .</li><li>While writing the input() message, the <b>"$" </b>symbol is given<br>so as to print the total cost in the currency format</li></ul></div><div>2. <b>Currency formatting<br>:</b></div><div><ul><li>Currency was handled by inserting <b>"{:.2f}" format(expectedcost) </b>in the <b>return</b> function so as<br>to make it print in 2 decimal float value and moreover inserted a<br>dollar symbol inside the input() message.</li><li>This made the total cost to print in<br>currency format in the output.</li></ul></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226494556-7ee004d2-ec5f-4f3e-8f2a-959b53369497.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 Showing how the OutOfStockException is handled with proper user feedback and continued<br>program flow. Showing the stage/category that the choice was out of stock in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226494619-a090b886-b468-425c-a7a3-3710d1649907.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#2 Showing how the NeedsCleaningException is handled where it prompts the user to<br>typed the word &#39;clean&#39; to clean the machine. Printing a message whether or<br>not the machine was cleaned.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226494663-9e8bfb56-5614-4296-83ed-5dbbdc6406e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Showing how the various InvalidChoiceExceptions are handled with proper user feedback and<br>continued program flow. Showing the stage/category that the choice was invalid in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226494712-27138dc6-69d0-404b-bec2-569cccea021a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Showing how the various ExceededRemainingChoicesExceptions are handled with proper user feedback and<br>continued program flow. Showing the stage/category where the choice limit was exceeded. Move<br>the user to the next stage/category<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/226494769-08d3b5c8-37f5-4e3e-9bdb-d909fa1cc575.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 #6 #7 Showing how the InvalidPaymentException is handled with proper user feedback<br>and continued program flow<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ul><li><b><u>OutOfStockException </u>:</b> This exception is raised when the quantity of any item is<br>less than 0. In this project,&nbsp; the quantities of patties and toppings are<br>set seperately in values. Ex : 10. When the self.quantity becomes 0 or<br>less than 0, the out of stock exception is raised. The error is<br>handled by using <b>except </b>statments where in the error is handled by giving<br>using except as per the above code snippet.</li><li><b><u>NeedsCleaningException</u></b> : This exception is raised<br>when the <b>self.remaning_uses is less than 0.</b> In this project, the number of<br>uses is set 15. When the <b>USES_UNTIL_CLEANING </b>becomes&nbsp; 0 or less than 0,<br>the NeedsCleaning exception is raised. The error is handled by using except statment<br>where in the error is handled by giving using except as per the<br>above code snippet . A new <b>input()</b> message is given by asking user<br>to whether clean or quit. if <b>clean is selected,</b> the machine will clean<br>successfully and continues operation using <b>self.reset() </b>function.</li><li><b><u>InvalidChoiceException</u></b>: This exception is raised when the<br>choice selected does not match any of the item. Firstly if <b>there is<br>Invalid choice for bun, or patty or topping selected </b>, the message displays<br>to the user by using except .Same applies for Invalid choice for <b>Patty<br></b>selected&nbsp; as well as Invalid choice for <b>Toppings </b>selected with appropriate message according<br>to the category.</li><li><b><u>ExceededRemainingChoicesException : </u></b>This exception is raised when the maximum patties selected<br>are more than 3. That means self.remaining_patties &lt; 0.Firstly, if there is Exceeded<br>patty limit&nbsp; the message displays to the user by using except. Now the<br>current selection value becomes toppings. Same applies for exceeded limit for toppings. When<br>toppings are exceeded, the exception is handled and printed out to the user<br>and then the current selection will proceed to payment.</li><li><b><u>InvalidPaymentException</u></b> : This exception is<br>raised when the total cost != expected cost. This means that the user<br>has entered wrong payment value, which doesn't match the cost calculated. This exception<br>is handled by using except statement. Further ,current status again prints the total<br>cost and asks the user to enter the same exact value.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227068571-e83bbc1d-65ec-44f4-bf44-34a9e6b331ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 #2Test 1 - bun is  the first selection (can&#39;t add patties/toppings<br>without a bun choice)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227068856-7b005020-eb0a-4d83-adf9-7c4316e383a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#3 Test 2 - can only add patties if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227068959-28f73776-bb27-40ec-ac9d-3d17b8de3503.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#4 Test 3 - can only add toppings if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227069069-615565e2-a141-4bed-8aa0-bb89fd73e877.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5 Test 4 - Can add up to 3 patties of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227069196-003a9d6d-90c3-4b61-800b-34ba3a81bf6e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 5 - Can add up to 3 toppings of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227072047-475de111-4803-4b51-b8aa-eebe6098a54e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7 Test 6 - cost calculated properly based on the choices  (test<br>case have a few permutations of at least 3 valid burgers)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227072260-0ea25861-15a1-47d7-bc31-7ccabda97424.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8 Test 7 - Total Sales (sum of costs) calculated properly (test case<br>have a few permutations of at least 3 valid burgers)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227072424-c285db42-69cf-4788-a69d-ca2058bc3dd8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9 Test 8 - Total burgers properly incremented for each purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227073104-75ce0506-512f-401b-9c4b-7483befae8c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#10 Showing all Tests 1-8 passing and along with test cases output (<br>used &#39;pytest -rA tests/test_burger_machine.py&#39; on the command line)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div><ul><li><u><b>Test case 1</b> </u>: Bun will be the first selection. It is done<br>by asserting <b>machine.currently_selecting.name == STAGE.Bun.name </b>, here <b>assert() function</b> is used to test<br>the if the condition is true. If it turns out to be true<br>, it passes the test.</li><li><b><u>Test case 2</u></b> : Adding patties only when they're<br>in stock. Patties are added when the exception of out of stock is<br><b>false</b>. This is done through <b>assert False </b>under except. And in try block<br>, the quantity is set to 1 , <b>machine.patties[0].quantity = 1.</b> This test<br>has passed since the out of stock exception turned out to be false<br>when quantity is set to 1.</li><li><b><u>Test case 3 </u></b>: Adding toppings only when<br>they're in stock . Toppings are added when the exception of out of<br>stock is false. This is done through <b>assert False </b>under except. And in<br>try block , the quantity is set to 1,&nbsp; <b>machine.toppings[0].quantity = 1.</b> This<br>test has passed since the out of stock exception turned out to be<br>false when quantity is set to 1.</li><li><b><u>Test case 4</u></b>: Can add up to<br>3 Patties.&nbsp; Initially, the Bun is considered, and when <b>for() loop</b> is considered<br>in range<b> machine.MAX_PATTIES -1.</b> Inside this loop, there is patty selected , and<br>then try block is executed to <b>assert machine.remaining_patties==0.</b> This means that max patties<br>test has passed when the exception turns out to be false.</li><li><b><u>Test case 5:</u></b><br>Can add up to 3 toppings.Initially, the Bun is considered, and Patty is<br>"next",&nbsp; &nbsp;when <b>for() loop </b>is considered in range <b>machine.MAX_TOPPINGS -1</b>. Inside this loop,<br>there is toppings selected , and then try block is executed to <b>assert<br>machine.remaning_toppings ==0. T</b>his means that max toppings test has passed when the exception<br>turns out to be false.</li><li><b><u>Test case 6: </u></b>Cost is calculated properly based on<br>the choices . In currency format. Few (3 ) combinations of purchases are<br>considered and for the first burger , <b>assertmachine1.calculated_cost()=='4.00' </b>is given. And the test<br>has passed . Same process for the second burger, assertmachine1.calculated_cost()=='2.75' is given, The<br>test has passed. And then for the third burger , assertmachine1.calculated_cost()=='1.75' is given,<br><b>The test has passed.&nbsp;</b></li><li><b><u>Test case 7: </u></b>Total Sales (sum of costs) is calculated<br>properly (test case should included atleast 3 burger combinations/purchases). Here, first purchase is<br>considered by taking few (3) combinations and burgerCost1 is calculated. Then second purchase<br>is considered and burgerCost2 is calculated. Then third purchase is considered and burgerCost3<br>is calculated. Finally assert the sum of <b>burgerCost1 + burgerCost2 + burgerCost3 which<br>increments the total sales.</b></li><li><b><u>Test case 8 </u></b>: Total burgers is properly incremented for<br>each purchase. Here, first purchase is considered by taking few combinations and burgerCost1<br>is calculated. Then second purchase is considered and burgerCost2 is calculated. As well<br>as burgerCost3 is defined.Finally <b>assert&nbsp; burgerCost1 + burgerCost2 </b>which increments the total burgers<br>to 2 and also burgerCost3 is incremented to 3.</li></ul></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AshwiniValmiki/IS601-004/pull/21">https://github.com/AshwiniValmiki/IS601-004/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <div>I had issues handling<b> exceptions</b> and as well as<b> testcases.</b></div><div><ul><li>I have <b>handled exceptions<br></b>by using except statements along with<b> conditions</b> for every exception.</li><li>&nbsp;I have learned how<br>to <b>use test cases and apply them </b>as required.</li><li>This project was challenging as<br><b>test cases were challenging</b>.</li><li>( learned to use pytest -rA command which displays individually<br>output for each test case)&nbsp;<br></li><li>And using <b>pytest fixtures, </b>which installs pytest and applies<br>for the project ,has really been challenging and advanced by solving test cases<br>.</li><li>Burger Machine is quite <b>interesting</b> though!&nbsp; I'm grateful that I have learned certain<br>things while solving the code.</li></ul></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227078495-3847e939-8c07-4f0a-b45a-4b3812a82d85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful execution of BurgerMachine.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227078640-49e3da11-86b9-4353-98c1-4c31de1f34d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entered &quot;White burger bun&quot; and then gave &quot;Turkey&quot; as Patty <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227078988-b5710081-5179-4b7e-8e06-435f1a5f20b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entered &quot;veggie &quot; as Patty , Then gave &quot;Ketchup&quot; and &quot;pickles&quot; in Topping<br>options and entered &quot;next&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227078988-b5710081-5179-4b7e-8e06-435f1a5f20b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Displayed the cost in currency format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227079322-4e389a87-de45-4c92-ba34-0e97aff009aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully executed for the first burger. Total sales are visible.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227079742-0f56ae67-f5cf-4bfe-8929-bf2243fd7ba3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entered &quot;Wheat burger bun&quot; and then gave &quot;Turkey&quot; as Patty <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227079904-6a5d2e38-28e8-417f-af87-5321a42b7cbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entered &quot;done&quot; and then cost has been displayed in currency format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227079904-6a5d2e38-28e8-417f-af87-5321a42b7cbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully executed . Total sales incremented in the output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227078282-a16ce02c-8d54-4e2f-a107-0377fcdb5804.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the 2 combinations , 1st burger cost has displayed along with Total<br>sales visible. Then 2nd burger cost has displayed along with Total Sales Incremented.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420603/227078282-a16ce02c-8d54-4e2f-a107-0377fcdb5804.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Burger Machine executed successfully.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/av659" target="_blank">Grading</a></td></tr></table>