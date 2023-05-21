
function storeStudentData() {
    // Get the values of the input fields
    var name = document.getElementById('stdname').value;
    var id = document.getElementById('stdid').value;
    var date = document.getElementById('stddate').value;
    var gpa = document.getElementById('stdgpa').value;
    var gender = document.querySelector('input[name="gender"]:checked').value;
    var level = document.getElementById('stdlevel').value;
    var status = document.querySelector('input[name="status"]:checked').value;
    var department = document.getElementById('stddepartment').value;
    var email = document.getElementById('stdemail').value;
    
    // Create an object to store the data
    var studentData = {
      name: name,
      id: id,
      date: date,
      gpa: gpa,
      gender: gender,
      level: level,
      status: status,
      department: department,
      email: email
    };
 
  
    // Store the data in the local storage
    localStorage.setItem('studentData', JSON.stringify(studentData));
  }
  
  function mySave() {
    var myContent = document.getElementById("myTextarea").value;
    localStorage.setItem("myContent", myContent);
  }
  function myLoad() {
    var myContent = localStorage.getItem("myContent");
    document.getElementById("myTextarea").value = myContent;
  }