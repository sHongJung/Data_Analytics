var $tbody = document.querySelector("tbody");

$tbody.innerHTML = "";

for (var i =0; i<100; i++){
var $row = $tbody.insertRow(i);
 var $cell = $row.insertCell(0)
    $cell.innerText = addressData[i].id
 var $cell = $row.insertCell(1)
    $cell.innerText = addressData[i].country
 var $cell = $row.insertCell(2)
    $cell.innerText = addressData[i].state
 var $cell = $row.insertCell(3)
     $cell.innerText = addressData[i].city
 var $cell = $row.insertCell(4)
    $cell.innerText = addressData[i].street_name
 var $cell = $row.insertCell(5)
    $cell.innerText = addressData[i].street_number
}
