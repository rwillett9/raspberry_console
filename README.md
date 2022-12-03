# raspberry_console
Solo side project where I will create a console-like display to use with the Raspberry Pi 4 Model B and the 7" touch screen display made for the Raspberry Pi

# SETUP
1. Create a virtual environment using the following command:  
&emsp;Mac:  
&emsp;&emsp;```python3 -m venv venv```  
&emsp;Windows:  
&emsp;&emsp;```python -m venv venv```

2. Navigate to the ```venv/bin/activate``` script and make the following additions:  
&emsp;At the beginning of the ```deactivate``` function, add this line of code:  
&emsp;&emsp;```unset wanikani_token```  
&emsp;Just after the ```deactivate``` function, add a line of code that looks like this except replace YOUR-TOKEN-KEY with your token key from WaniKani:  
&emsp;&emsp;```wanikani_token="YOUR-TOKEN-KEY"```
