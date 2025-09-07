# -*- coding: utf-8 -*-
# MEAT — Kivy demo app with full Hebrew support
# Works on Android via Buildozer

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.resources import resource_find

# נרשום את גופני העברית (שם הקובץ כפי שהעלית עם סוגריים)
# אנחנו משתמשים בתבנית include_patterns ב-buildozer.spec כדי לכלול את הקובץ בתוך ה-APK.
# כאן נטען את הקובץ בזמן ריצה.
FONT_CANDIDATES = [
    "NotoSansHebrew[wdth,wght].ttf",
    # למקרה של שינוי שם עתידי:
    "NotoSansHebrew.ttf",
    "fonts/NotoSansHebrew[wdth,wght].ttf",
    "assets/NotoSansHebrew[wdth,wght].ttf",
]

def _register_hebrew_font():
    # ננסה למצוא את הקובץ בתוך משאבי האפליקציה
    for fname in FONT_CANDIDATES:
        p = resource_find(fname)
        if p:
            LabelBase.register(name="Hebrew", fn_regular=p)
            return True
    # אם לא מצאנו—עדיין נרוץ עם ברירת המחדל של קיווי
    return False

class MeatRoot(BoxLayout):
    pass

class MeatApp(App):
    title = "MEAT"

    def build(self):
        _register_hebrew_font()
        root = BoxLayout(orientation='vertical', padding=24, spacing=16)

        hello = Label(
            text="ברוך הבא ל־MEAT\nהאפליקציה רצה על Kivy באנדרואיד",
            halign="center",
            valign="middle",
            font_name="Hebrew",
            font_size="22sp",
        )
        hello.bind(size=lambda *_: setattr(hello, 'text_size', hello.size))

        btn = Button(
            text="בדיקת עברית - לחץ אותי",
            font_name="Hebrew",
            size_hint=(1, None),
            height="48dp",
        )

        def on_press(_):
            hello.text = "הכול עובד! 🎉\nנבנה ב-GitHub Actions לקובץ APK"
        btn.bind(on_press=on_press)

        root.add_widget(hello)
        root.add_widget(btn)
        return root


if __name__ == "__main__":
    MeatApp().run()
