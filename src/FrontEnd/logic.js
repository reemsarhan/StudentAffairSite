


const sname = document.getElementById('name');
const svalue = document.getElementById('value');
const semail =document.getElementById('stdemail');
const sdepartment = document.querySelector('#stddepartment');
const slevel=document.getElementById('stdlevel');
const sGpa = document.getElementById('stdgpa');
const sDate = document.getElementById('stddate');
const statusRadioButtons = document.querySelectorAll('input[name="status"]');
        let sstatus;

        statusRadioButtons.forEach((radioButton) => {
            radioButton.addEventListener("change", () => {
                sstatus = radioButton.value;
            });
        });


        const genderRadioButtons = document.querySelectorAll('input[name="gender"]');
        let sgender;

        statusRadioButtons.forEach((radioButton) => {
            radioButton.addEventListener("change", () => {
                sgender = radioButton.value;
            });
        });



function Save(){
    const student = {
    name: sname.value,
    id: svalue.value,
    Bdate:sDate.value,
     email: semail.value,
   department: sdepartment.value,
    status: sstatus.value,
    gender:sgender.value,
    Gpa:sGpa.value,
    level:slevel.value
  }; 
  localStorage.setItem(svalue.value, JSON.stringify(student));
}

// function getStudent() {
//   const searchInput = document.querySelector('#searchid').value;
//   const xhr = new XMLHttpRequest();
//   xhr.open('GET', `https://example.com/student-info?name=${searchInput}`);
//   xhr.onload = function () {
//     if (xhr.status === 200) {
//       const studentData = JSON.parse(xhr.responseText);
//       const studentTable = createStudentTable(studentData);
//       const studentInfoPage = window.open('studentInfo.html', '_blank');
//       studentInfoPage.document.write(studentTable.outerHTML);
//     }
//   };
//   xhr.send();
// }

// function createStudentTable(studentData) {
//   const table = document.createElement('table');
//   const headerRow = table.insertRow(0);
//   Object.keys(studentData[0]).forEach(key => {
//     const headerCell = headerRow.insertCell();
//     headerCell.textContent = key;
//   });
//   studentData.forEach(student => {
//     const row = table.insertRow();
//     Object.values(student).forEach(value => {
//       const cell = row.insertCell();
//       cell.textContent = value;
//     });
//   });
//   return table;
// }


  // function getstudent() {  
 
  //   var id = document.getElementById("searchid").value;
  //   var student = JSON.parse(localStorage.getItem(id));
  //   if (student) {
  //     var tableRow = document.createElement("tr");
  //     var nameCell = document.createElement("td");
  //     var idCell = document.createElement("td");
  //     var dobCell = document.createElement("td");
  //     var gpaCell = document.createElement("td");
  //     nameCell.innerHTML = student.name;
  //     idCell.innerHTML = student.id;
  //     dobCell.innerHTML = student.Bdate;
  //     gpaCell.innerHTML = student.Gpa;
  //     tableRow.appendChild(nameCell);
  //     tableRow.appendChild(idCell);
  //     tableRow.appendChild(dobCell);
  //     tableRow.appendChild(gpaCell);
  //     var searchResultsDiv = document.getElementById("search-results");
  //     searchResultsDiv.appendChild(tableRow);
  //   }
  //   // window.location.href='studentInfo.html';
  //   document.getElementById("search-results").style.display = "block";
  // }



  // function getstudent() {  
  //   var id = document.getElementById("searchid").value;
  //   var student = JSON.parse(localStorage.getItem(id));
  //   if (student) {
  //     var tableRow = document.createElement("tr");
  //     var nameCell = document.createElement("td");
  //     var idCell = document.createElement("td");
  //     var dobCell = document.createElement("td");
  //     var gpaCell = document.createElement("td");
  //     nameCell.innerHTML = student.name;
  //     idCell.innerHTML = student.id;
  //     dobCell.innerHTML = student.Bdate;
  //     gpaCell.innerHTML = student.Gpa;
  //     tableRow.appendChild(nameCell);
  //     tableRow.appendChild(idCell);
  //     tableRow.appendChild(dobCell);
  //     tableRow.appendChild(gpaCell);
  //     // Store table row data in localStorage
  //     localStorage.setItem("tableRow", tableRow.outerHTML);
  //     // Navigate to the studentInfo.html page
  //     window.location.href = "studentInfo.html";
  //   }
  // }
  
  

  

function getstudent() {  
    var id = document.getElementById("searchid").value;
    var student = JSON.parse(localStorage.getItem(id));
    if (student) {
        var tableRow = document.createElement("tr");
        var nameCell = document.createElement("td");
        var idCell = document.createElement("td");
        var dobCell = document.createElement("td");
        var gpaCell = document.createElement("td");
        nameCell.innerHTML = student.name;
        idCell.innerHTML = student.id;
        dobCell.innerHTML = student.Bdate;
        gpaCell.innerHTML = student.Gpa;
        tableRow.appendChild(nameCell);
        tableRow.appendChild(idCell);
        tableRow.appendChild(dobCell);
        tableRow.appendChild(gpaCell);
        var searchResultsDiv = document.getElementById("search-results");
        searchResultsDiv.appendChild(tableRow);
        sessionStorage.setItem('student', JSON.stringify(student)); // Store student object in session storage
    }
    
}