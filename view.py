import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        # ROW1
        self.ddLanguage = ft.Dropdown(
            value = "Choose language",
            label="Language",
            width=200,
            options=[ft.dropdown.Option("italian"), ft.dropdown.Option("english"), ft.dropdown.Option("spanish")],
            on_change=self.__controller.handleLanguageSelection
        )


        # ROW2 (a sinistra il menu a tendina, al centro spazio per testo e a destra bottone)
        # Sinistra
        self.ddModality = ft.Dropdown(
            value = "Choose modality",
            label = "Search Modality",
            width=300,
            options = [ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic")],
            on_change = self.__controller.handleModalitySelection
        )
        # Centro
        self.txtIn = ft.TextField(
            label = "Text",
            width=200,
        )
        # Destra
        self.btnCorrection = ft.ElevatedButton(
            text = "Start Spell Check",
            on_click= self.__controller.handleSpellCheck
        )
        row2 = ft.Row(controls=[self.ddModality, self.txtIn, self.btnCorrection], alignment=ft.MainAxisAlignment.CENTER)


        # ROW3
        self.txtOut = ft.ListView(spacing=1, expand=1, padding=15, auto_scroll=True)  # padding controlla la distanza da ciò che c'è sopra


        # Metto tutto insieme nella pagina
        self.page.add(self.ddLanguage, row2, self.txtOut)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
