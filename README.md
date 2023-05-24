# StudentAffairSite
Student Affairs Site is a website built using HTML, CSS, JavaScript, Python, SQL, and the Django framework. The website is designed to allow users to manage student information and perform various actions related to student management.

## **Features**

The following features are available on the Student Affairs Site:

Add New Student: Users can add sa new student to the system by providing the student's information, including ID, name, date of birth, GPA, gender, level, status, department, email, and mobile number.

Update Student Information: Users can update an existing student's information, except for the department field, which is disabled for editing.

Delete Student Data: Users can delete an existing student's data through a delete button on the edit student data page. A confirmation dialogue is displayed before deletion occurs.

Search for Active Students: Users can search for "active" students by name on the search for students screen. Students with similar names and active status are rendered as a table.

Assign Student Department: Users can select a specific student after searching to assign a department through the student's department assignment page. The page displays the student's ID, name, and a dropdown list of available departments. This action is only applicable for students with level 3; otherwise, an error is displayed with a clear and understandable error message.

View All Students: Users can view all active/inactive students in a separate page rendered in a table with a related set of attributes only.

Change Student Status: Users can change the status of a student from active to inactive or vice versa from the table viewing all students.

Navigation Bar: The website has a well-designed navigation bar that allows users to navigate through all pages, including the home page.

## Getting Started

To get started with the Student Affairs Site, follow these steps:

Clone the repository to your local machine.

Install Python and Django on your machine if you don't have them already.

Activate the uploaded virtual environment for the project. / Or make yours

Install the required dependencies by running pip install -r requirements.txt.

Run the server using the command python manage.py runserver.

Open the website in your browser at http://localhost:8000/.
