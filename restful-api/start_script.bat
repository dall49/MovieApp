@ECHO OFF


	set root=c:\xampp\
	start %root%mysql\bin\mysqld.exe --defaults-file=%root%mysql\bin\my.ini 



pipenv install

pipenv run python app.py
