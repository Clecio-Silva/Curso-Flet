import flet as ft


# class para criar as tarefas
class Task(ft.Column):
    pass

# class para criar o aplicativo.
class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(
            hint_text="Digite uma tarefa:",
            expand=True,
            on_submit=self.add_task,
            on_focus=True,
        )

        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="Ativas"),
                ft.Tab(text="Concluidas"),
            ])

        self.items_left = ft.Text("0 tarefas adicionadas.")

        self.controls = [
                # Titulo da aplicação
                ft.Row([
                        ft.Text(
                            value="Tarefas",
                            size=30,
                            weight="bold",
                            )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                # Campo de adicionar tarefas
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.IconButton(icon=ft.Icons.ADD, on_click=self.add_task),

                    ]
                ),
                ft.Column(
                    controls=[
                        self.filter,
                        self.tasks,
                        ft.Row(
                            controls=[
                                self.items_left,
                                ft.OutlinedButton("Apagar Tarefas Concluidas".upper(), on_click=self.clear_completed_tasks)
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ]
                ),
            ]

    def clear_completed_tasks(self, e):
        pass

    def tabs_changed(self, e):
        pass
    
    def add_task(self, e):
        pass


def main(page: ft.Page):
    page.title = "Minhas Tarefas"
    page.window.width = 600
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.all(20)
    page.theme_mode = ft.ThemeMode.LIGHT

    app = TodoApp()

    page.add(app)
    page.update()


ft.app(target=main)