# Stock-market-prediction
Prediction of the direction of stock market prices using ensemble learning
The libraries required to run this application are

1. scikit-learn
2. pandas
3. numpy
4. scipy
5. mechanize
6. matplotlib
7. Django version 1.9.*


Please make sure python2.7 is in your system.

Running in windows:
———————————————————
To run in windows operating systems. Please extract “libraries.zip” file. The extracted folder contains required installation packages for the required libraries.

1) Installing scikit-learn: Simply run the installer for scikit-learn (scikit-learn-0.15.2.win32-py2.7.exe)
2) Installing matplotlib: Simply run the installer for matplotlib (matplotlib-1.4.3.win32-py2.7.exe)
  NOTE: matplotlib requires the library “six”, “dateuitl” and “pyparsing” to run.
3) Installing numpy: Open the command line and go to path where the library is contained and run the command “pip install numpy-1.11.0-cp27-none-win32.whl”
4) Installing pandas: Simply run the installer for pandas (pandas-0.15.2.win32-py2.7)
  NOTE: Pandas requires pytz library to run
5) Installing scipy: Simply run the installer for scipy (scipy-0.16.1-win32-superpack-python2.7)
6) Installing mechanize: Open the command line and go the directory “mechanize-0.2.5” which is a subdirectory in the libraries folder. Run the following command to install: python setup.py install
7) Installing django: Open the command line and go to the libraries directory and run
the command “pip install Django-1.9.2-py2.py3-none-any.whl“
8) Installing dateutil: unzip “dateutil-master.zip” and go the extracted folder using the command line and type: python setup.py install
9) Installing pyparsing: Run the installer for pyparsing. (pyparsing-1.5.7.win32-py2.7)
10) Installing pytz: Open the command line and go to the extracted library folder and
run the command “pip install pytz-2016.4-py2.py3-none-any.whl”


Running in Linux:
————————————————
To run in linux, please install the pip installer for python using the following
command line:

sudo apt-get install python-pip

This command will install pip in your system. Pip is a package management system
which is used to install and manage software packages written in python

Install the required python libraries using pip. If “numpy” is to be installed on your
system, run the following command:

sudo pip install numpy

Similarly, other perquisites can be installed in this manner.

Running the application:
————————————————————————
Start the command line prompt or the terminal and go to src/project/ and run the following command to start the server:

python manage.py rumserver <port number>

This command will start the server at the specified port number. Open any
web browser and enter the url “localhost:8000” if 8000 was the specified port number. This will start the application.

The user will have to select the stock and input trading time window. After this is done, the “train” is pressed to 
train the model. After the model has been trained, the user will be redirected to the results page.

