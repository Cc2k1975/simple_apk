[app]
title = HelloApp
package.name = helloapp
package.domain = org.example

source.dir = .
source.include_exts = py

version = 0.1
orientation = portrait
fullscreen = 0

requirements = python3,kivy

# גרסאות יציבות
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0
android.arch = armeabi-v7a
android.accept_sdk_license = True

[buildozer]
warn_on_root = 0
log_level = 2
