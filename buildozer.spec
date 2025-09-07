[app]
title = HelloApp
package.name = helloapp
package.domain = org.example

# קבצי מקור
source.dir = .
source.include_exts = py

version = 1.0
orientation = portrait
fullscreen = 0

# תלות מינימלית
requirements = python3,kivy

# גרסאות אנדרואיד
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0

# תמיכה בארכיטקטורות נפוצות
android.archs = arm64-v8a, armeabi-v7a

# קבלת רישיונות ה-SDK אוטומטית
android.accept_sdk_license = True

# בניית ריליס
android.release = 1

# <<< מכריחים יצירת APK ולא AAB >>>
android.release_artifact = apk
android.bundle = 0

[buildozer]
warn_on_root = 0
log_level = 2

