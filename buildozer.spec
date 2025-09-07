[app]
title = HelloApp
package.name = helloapp
package.domain = org.example

source.dir = .
source.include_exts = py

version = 1.0
orientation = portrait
fullscreen = 0

requirements = python3,kivy

# יעד אנדרואיד
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0

# תמיכה במעבדים מודרניים (הכי חשוב לבעיה שלך)
# בונה גם ל-arm64-v8a וגם ל-armeabi-v7a
android.archs = arm64-v8a, armeabi-v7a

# קבלת רישוי ה-SDK אוטומטית
android.accept_sdk_license = True

# יוציא גרסת release (חתומה)
android.release = 1

[buildozer]
warn_on_root = 0
log_level = 2
