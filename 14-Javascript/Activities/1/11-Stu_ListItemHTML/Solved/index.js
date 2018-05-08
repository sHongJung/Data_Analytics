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


function renderTodos() {
  // document.querySelector stores a reference to a DOM element
  var todoList = document.querySelector("#todo-list");

  // Loop through array and store in HTML
  for (var i = 0; i < todos.length; i++) {
    // Empty String to hold HTML
    var todoListItem = document.createElement("li");

    // Retrieve todo object from todos list
    var todo = todos[i];

    // Update todoListItem's innerHTML w/ the text of the todo object
    todoListItem.innerHTML = todo.text;

    // Add todo to the list
    todoList.appendChild(todoListItem);
  }
}

// Calling render todos to run the function when the page loads
renderTodos();
