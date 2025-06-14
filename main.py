import flet as ft
from custom_checkbox import CheckBox


def main(page: ft.Page):
    page.title = "Minhas Tarefas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 600
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)

    def add_newTask(e):
        print(new_task.value)
        task_list.controls.append(CheckBox(text=new_task.value))
        new_task.value = ""
        new_task.focus()
        page.update()
    new_task = ft.TextField(hint_text="Digite uma nova Tarefa.", 
                            expand=True, autofocus=True)
    btn = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_newTask)
    
    task_list = ft.Column()

    card = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    btn,
                ]
            ),
            task_list
        ]
    )
    
    page.add(card)
    

ft.app(target=main)
