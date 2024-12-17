import flet
from flet import (
    Page,
    colors
)
 
if __name__ == "__main__":
 
    def main(page: Page):
 
        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = TrelloApp(page)
        page.add(app)
        page.update()
 
    flet.app(main, view=flet.WEB_BROWSER)