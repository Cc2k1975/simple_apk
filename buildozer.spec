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

android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0

# תאימות לרוב המכשירים
android.archs = arm64-v8a, armeabi-v7a

# רישוי SDK אוטומטי
android.accept_sdk_license = True

# בניית release
android.release = 1

# <<< מכריחים APK ולא AAB >>>
android.release_artifact = apk
android.bundle = 0

[buildozer]
warn_on_root = 0
log_level = 2
