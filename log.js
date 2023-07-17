function convert() {
    var unit1 = document.getElementById("unit1").value;
    var value = document.getElementById("value").value;
    var unit2 = "volts";
  
    var converted_value = convert(unit1, unit2, value);
  
    alert("The converted value is " + converted_value);
  }