import functions
import PySimpleGUI as sg

label = sg.Text("Type your todo ")
input_box = sg.InputText(tooltip="Enter your todo here")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()