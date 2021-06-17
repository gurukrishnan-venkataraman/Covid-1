# CoWIN vaccination slot availability using Python

Script to check the available slots for Covid-19 Vaccination Centers from CoWIN API in India. This CANNOT book slots automatically. The Indian Government had blocked the API for crawlers, but we are good to go.
This is modified from the Github https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/

[Click to view the Website](https://bit.ly/3eQkvgl)

<!---
[Click to view the Website](https://bit.ly/3ob9l94)
-->

# Installing Python
Python is a programming language that is powerful but easy to learn. It is free, platform-independent, and popular among scientists.

## Recommended Method: Anaconda
The Anaconda Python distribution is an easily-installable bundle of Python and many of the libraries used throughout this class. Unless you have a good reason not to, we recommend that you use Anaconda.

### Mac/Linux users
1. Download the [appropriate version](https://www.anaconda.com/products/individual) of Anaconda
2. Follow the instructions on that page to run the installer
3. Test it out: open a terminal window, and type ``python``, you should see something like
```
Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
```
If `Anaconda` doesn't appear on the first line, you are using a different version of Python. See the troubleshooting section below.

1. Test out the IPython notebook: open a Terminal window, and type `ipython notebook`. A new browser window should pop up. 
2. Click `New Notebook` to create a new notebook file
3. Update IPython to the newest version by typing `conda update ipython` at the command line

### Windows Users
1. Download the [appropriate version](https://www.anaconda.com/products/individual) of Anaconda
2. Follow the instructions on that page to run the installer.
3. Go to Start and Run Jupyter Notebook.
4. Click `New Notebook`, which should open a new page.

# Usage
- Clone the repository. using `! Git Clone https://github.com/gurukrishnan-venkataraman/Covid-1`
- The tool only works with Indian IP addresses so disconnect your VPN if needed.
- Enter the command - `cd cowin-vaccination-slot-availability/`
- Install all the dependencies - `! pip3 install -r requirements.txt
- Open explorer and go to your directory eg.  C:\Users\lenovo\Desktop\Jupyter Notebooks\2021\Cowin\Covid-1
- Open App3.py file in notepad++ or any editor
- Change the below configurations to suit your needs  and save the file

	#*************Configuration***************************
	numdays=14 # No. of days to monitor from today
	dist_inp='Chennai' # refer district_mapping.csv for exact district name
	age_limit=18 #put age_limit = 18 or age_limit = 45 or age_limit='' (for both)
	vaccine_type = '' #('COVAXIN'/'COVISHIELD'/'')
	Dose = 2 #(0-both,1=1st only, 2-2nd only)
	ringtone='tune.mp3'
	#*****************************************************

- Run Anaconda Promt (Run as Administrator) From Start Menu.
- Go to your Directory Eg `cd C:\Users\lenovo\Desktop\Jupyter Notebooks\2021\Cowin\Covid-1`
- Run `streamlit run app2.py`. This version will alert you for open slots by a ringtone. If you need the Original version, Run `streamlit run app.py`

-   You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.7:8501

# Demo
![](https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/blob/main/demo/demo_1.gif)
# Articles
&nbsp;
[Link to the article 1](https://analyticsindiamag.com/data-scientist-creates-python-script-to-track-available-slots-for-covid-vaccinations/)    
&nbsp;
[Link to the article 2](https://yourstory.com/2021/05/paytm-launches-covid-19-vaccine-finder-tracks-slot-availability/amp)

## To view the video

<table>
   <tr>
      <td><a href="http://www.youtube.com/watch?v=tZ2xA19ZALA" target="_blank"><img height="50" src = "https://img.shields.io/youtube/views/tZ2xA19ZALA?color=blue&label=Watch%20on%20YouTube&logo=youtube&logoColor=red&style=for-the-badge"></a></td>
   </tr>
</table>

or click on the image below

[![Python Script to Track Available Slots For Covid-19 Vaccinations in India](http://img.youtube.com/vi/tZ2xA19ZALA/0.jpg)](http://www.youtube.com/watch?v=tZ2xA19ZALA)
