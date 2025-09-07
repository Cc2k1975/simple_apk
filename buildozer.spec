[app]
title = MEAT
package.name = MEAT
package.domain = com.cc2k
source.dir = .
source.include_exts = py,kv,ttf,png,jpg,jpeg,webp,svg
# נכליל את קובץ הפונט עם סוגריים ע"י תבנית כללית:
include_patterns = NotoSansHebrew*, *.kv

version = 1.0.0
# קוד גרסה לאנדרואיד (מספר שלם)
android.numeric_version = 1

# דרישות פייתון
requirements = python3,kivy

# אייקון / ספלש (אופציונלי; אפשר לעדכן מאוחר יותר)
# icon.filename = icons/icon.png
# presplash.filename = icons/presplash.png

orientation = portrait
fullscreen = 0
log_level = 1

# מתיר הרשאות בסיסיות בלבד (אפשר להרחיב בהמשך)
android.permissions =

# תמיכה ב-utf8
android.allow_backup = 0

# הגדרות אנדרואיד
android.api = 34
android.minapi = 24
# ארכיטקטורות היעד
android.archs = arm64-v8a, armeabi-v7a

# שימוש ב-Gradle (ברירת מחדל)
android.gradle_dependencies =

# תוקן ל-gradle דיפולטי של buildozer
p4a.local_recipes =

# קידוד ברירת מחדל
osx.kivy_version = 2.3.0

[buildozer]
log_level = 1
warn_on_root = 0
