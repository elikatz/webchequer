/*
 * ************************************************
 * This is the javascript for the GPA calculator.
 * ************************************************
 */
 
  var semesterGPA = 0;
  var semesterCredits = 0;

  /*
   * Gets the number of Rows in the table
   */
  function getRowNum(){
    return (document.getElementById('gpa_table').getElementsByTagName('tr').length);
  }
  
  /*
   * Adds a row to the table
   */
  function addRow(){
    clearErrorMsg();
    var numRows = getRowNum();
    var newRow = document.getElementById('gpa_table').insertRow(numRows);
    var classRow = newRow.insertCell(0);
    var gradeRow = newRow.insertCell(1);
    var creditRow = newRow.insertCell(2);
    classRow.innerHTML = "Class " + numRows;
    gradeRow.innerHTML = "<input type=\"text\" name=\"grade" + numRows + "\" onchange=\"javascript:findGPA()\">";
    creditRow.innerHTML = "<input type=\"text\" name=\"credit" + numRows + "\" onchange=\"javascript:findGPA()\">";
  }
  
  /*
   *Will delete a Row in the table  
   */
  function deleteRow(){
    var numRows = getRowNum();
    if (numRows > 2){
      var newRow = document.getElementById('gpa_table').deleteRow(numRows-1);
      clearErrorMsg();      
    }
    else{
      document.getElementById('error_msg').innerHTML = "Can't delete only row";
    }
  }
  
  /*
   * There is an error message under Add Row. This will clear that message.
   */
  function clearErrorMsg(){
    document.getElementById('error_msg').innerHTML = " ";
  }
  
  function findNewGPA(){
    var gpaBox = document.getElementById('current_gpa').getElementsByTagName('input');
    var currentGPA = parseFloat(gpaBox[0].value);
    var currentCredits = parseFloat(gpaBox[1].value);
    findGPA();
    var newTotalGPA = (semesterGPA*semesterCredits + currentGPA*currentCredits)/(semesterCredits + currentCredits);
    document.getElementById('term_gpa').innerHTML = "Your new GPA will be " + newTotalGPA;
  }
  
  /**
   * This will find the GPA based on the values in the table and then insert the answer into the html
   * on the page
   */
  function findGPA(){
    var numRows = getRowNum();
    var x = document.getElementById('gpa_table').getElementsByTagName('input');
    //Reading in the values
    var grades = new Array(numRows);
    var credits = new Array(numRows);
    var j = 0;
    for (var i = 0; i < x.length; i+=2){
      grades[j] = x[i].value;
      j++;
    }
    var k = 0;
    for (var i = 1; i < x.length; i+=2){
      credits[k] = x[i].value;
      k++;
    }
    
    //Calculating the GPA
    var goodCalc = true;
    var sumCredits = 0;
    var sumTotal = 0;
    for (var i in grades){
      var g = getGradeValue(grades[i]);
      var c = getCreditValue(credits[i]);
      if (g == -1 || c == -1){
        goodCalc = false;
        break;
      }
      sumTotal += g*c;
      sumCredits += c;
    }
    semesterGPA = sumTotal/sumCredits;
    semesterCredits = sumCredits;
    var outputString = "Your Term GPA is " + semesterGPA;
    if (goodCalc == false){
      outputString = "Bad Values. Please try again";
    }
    document.getElementById('term_gpa').innerHTML = outputString;
  }
  
  /*
   * Checks whether a value passed is a valid grade and returns the index in the grade array if true
   * or -1 if false. The grade array is decreasing.
   */
  function getGradeValue(g){
    var gradeValues = new Array("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F");
    var gradePointValues = new Array(4.33, 4.0, 3.66, 3.33, 3.0, 2.66, 2.33, 2.0, 1.66, 1.0, 0);
    var value = -1;
    for (var i in gradeValues){
      if (gradeValues[i] == g){
        value = gradePointValues[i];
      }
    }
    return value;
  }
   
  /*
   * Checks whether a value passed is a number and is in (0,10). Returns -1 if either is false.
   */ 
  function getCreditValue(c){
    var credit = parseFloat(c);
    var returnValue = -1;
    if (credit > 0 && credit < 10){
      returnValue = credit;
    }
    return returnValue;
  }