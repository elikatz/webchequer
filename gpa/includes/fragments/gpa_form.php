<div id="content">
  <div id="instructions">
  
  </div>
    <div id="gpa_form">
    <table border="0" id="gpa_table">
      <tr>
        <th>Class</th>
        <th>Grade</th>
        <th>Credits</th>
      </tr>
      <tr>
        <td>Class 1</td>
        <td><input type="text" name="grade1" onchange="javascript:findGPA()"></td>
        <td><input type="text" name="credit1" onchange="javascript:findGPA()"></td>
      </tr>
    </table>
      <div id="actions">
      <a href="javascript:addRow()">Add Row</a>
      <a href="javascript:deleteRow()">Delete Row</a>
      <div id="error_msg"></div>
      </div>
    </div>
    
    <div id="current_gpa">
      <p>Current GPA: <input type="text" name="currentGPA"/></p>
      <p>Credits Earned Thus Far: <input type="text" name="currentCredits"/></p>
      <a href="javascript:findNewGPA()">Find Overall GPA</a>
    </div>
    
    <div id="term_gpa"></div>
    
  </div>