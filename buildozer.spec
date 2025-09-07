[app]
title = SimpleApp
package.name = simpleapp
package.domain = com.example

source.dir = .
source.include_exts = py

version = 0.1
orientation = portrait
fullscreen = 0

# ספריות Python
requirements = python3,kivy

# אנדרואיד – גרסאות יציבות
android.api = 34
android.minapi = 21
# נכפה גרסת Build-Tools יציבה (מונע משיכה של 36.1-rc1)
android.build_tools_version = 34.0.0
android.arch = armeabi-v7a
android.debug = 1

# לא לעצור על אזהרת root
[buildozer]
log_level = 2
warn_on_root = 0
# קבלה אוטומטית של רשיונות ה-SDK
android.accept_sdk_license = True
