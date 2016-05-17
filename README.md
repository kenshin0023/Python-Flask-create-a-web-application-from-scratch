# Python-Flask-create-a-web-application-from-scratch
Python Flask create a web application from scratch

File
app.py
templates
    index.html
    signup.html
static
    signup.css
    
Create dabase
CREATE TABLE `sp_createuser` (
  `id` int(11) NOT NULL,
  `p_name` varchar(255) NOT NULL,
  `p_username` varchar(255) NOT NULL,
  `p_password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

Run
<flask> C:\myproject\app\tutorial>app.py
http://127.0.0.1:5000/
