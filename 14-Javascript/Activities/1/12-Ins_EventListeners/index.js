var todos = [
  {
    complete: false,
    text: "Learn JavaScript"
  },
  {
    complete: false,
    text: "Learn JavaScript Charting"
  },
  {
    complete: false,
    text: "Make Awesome Front-End Projects"
  }
];

// Getting a reference to the button on the page with the id property set to `remove-todo`
var removeTodoBtn = document.querySelector("#remove-todo");

// Getting a reference to the input element on the page with the id property set to 'input-field'
var inputField = document.querySelector("#input-field");

// This function is triggered when the removeTodoBtn is clicked
removeTodoBtn.addEventListener("click", function() {
  // pop is an Array method which removes the last element
  todos.pop();
  renderTodos();
});

// This function is triggered whenever the mouse enters the input field
inputField.addEventListener("pointerenter", function() {

  // Log the message "Mouse entered!" when user moves mouse away from input field
  console.log("Mouse entered!");
});

// This function is triggered whenever the mouse leaves the input field
inputField.addEventListener("pointerleave", function() {

  // Log the message "Mouse left!" when user moves mouse away from input field
  console.log("Mouse left!");
});

function renderTodos() {
  // document.querySelector can be used to store a reference to a DOM element
  var todoList = document.querySelector("#todo-list");
  var todoHTML = "";
  for (var i = 0; i < todos.length; i++) {
    todoHTML += "<li>" + todos[i].text + "</li>";
  }

  todoList.innerHTML = todoHTML;
}

renderTodos();
