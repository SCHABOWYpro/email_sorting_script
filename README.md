<h1>Email sorting sricpt</h1>
<h3> Author: Jarosław Żurek </h3>
<h2>General Info</h2>
<p>This script allows user to perform simple operations on text and csv files, which include list of unsorted emails.</p> 
<h2>Technologies</h2>
<p>Project is created with:</p>
<ul>
  <li>Python 3.10.5</li>
  <li>Pycharm 2022.1.3</li>
</ul>
<h2>Setup</h2>
<p> You can install this scirpt using pip install: </p>

```

pip install git+https://github.com/SCHABOWYpro/email_sorting_script.git

```



<p> Or, you can clone the source:</p>

```
$ git clone https://github.com/SCHABOWYpro/email_sorting_script.git

```
<h2>How to use the script</h2>
<ol>
  <li>You can open this code with any Integrated Development Environment.</li>
  <li>If you don't have any IDE on your computer, open command line, by clicking WIN+R and typing "CMD" on Windows system.</li>
  <li>Navigate to directory where you have downloaded this scripit using "..cd/" in command line.</li>
  <li>Inside directory "email_sorting_script-master", run program "main.py".</li>
  <li>After running the script, instruction will be displayed inside the console.</li>
  <li>To quit program simply type: stop</li>
  <li>If you want to display list of incorrect emails, type:</li>
    <ul>
      <li>"--incorrect-emails" or "-ic"</li>
  </ul>
  <li>For list of grouped email by domain, type:</li>
    <ul>
      <li>"--group-by-domain" or "-gbd"</li>
  </ul>
  <li>If you want to search email by given word, type:</li>
    <ul>
      <li>"--search" or "-s"</li>
      <li>Program will ask user for word: "What word do you search for?".</li>
      <li>Type word you are searching for.</li>
  </ul>
  <li>If you want to display emails that are not in logs file, type:</li>
    <ul>
      <li>"--find-emails-not-in-logs" or "-feil"</li>
      <li>Program will ask user for logfile URL: "Add logfile URL".</li>
      <li>Paste URL with RAW logfile.</li>
  </ul>
  <li>To quit program simply type: "stop"</li>
</ol>
