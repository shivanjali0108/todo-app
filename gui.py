import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(
    values=functions.get_todos(),
    key="todos",
    enable_events=True,
    size=(45, 10)
)

edit_button = sg.Button("Edit")

window = sg.Window(
    "My To-Do App",
    layout=[
        [label],
        [input_box, add_button],
        [list_box, edit_button],
    ],
    font=("Helvetica", 20)
)

while True:
    event, values = window.read()

    match event:

        case "Add":
            todos = functions.get_todos()

            new_todo = values["todo"].strip()

            if new_todo:
                todos.append(new_todo + "\n")
                functions.write_todos(todos)

                window["todos"].update(values=todos)
                window["todo"].update(value="")

        case "todos":
            window["todo"].update(value=values["todos"][0].strip())

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].strip()

                todos = functions.get_todos()

                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"

                functions.write_todos(todos)

                window["todos"].update(values=todos)

            except IndexError:
                sg.popup("Please select a to-do item first.")

        case sg.WIN_CLOSED:
            break

window.close()
