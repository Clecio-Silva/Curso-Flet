import flet as ft
from custom_checkbox import CheckBox


def main(page: ft.Page):
    page.title = "Minhas Tarefas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 450
    page.window.height = 600
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    WIDTH : int = page.width
    HEIGHT : int = page.window.height

    def add_newTask(e):
        #print(new_task.value)
        if new_task.value == "":
            new_task.focus()
            return
        task_list.controls.append(CheckBox(text=new_task.value))
        new_task.value = ""
        new_task.focus()
        page.update()
    new_task = ft.TextField(hint_text="Digite uma nova Tarefa.", 
                            expand=True, autofocus=True, on_submit=add_newTask)
    btn = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_newTask)
    
    task_list = ft.Column(height=HEIGHT, scroll=ft.ScrollMode.ADAPTIVE)

    card = ft.Column(
        width=450,
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
