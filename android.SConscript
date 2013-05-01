#!/usr/bin/python
Import(['sources', 'env'])

# Android environments
android = env.Clone()
android.Replace(CC = 'gcc')

android_opt = android.Clone()
android_opt.Append(CCFLAGS = ['-O2'])

android_dbg = android.Clone()
android_dbg.Append(CCFLAGS = ['-g', '-DDEBUG'])

android_opt_obj = android_opt.Object('build/.obj/android/spacecorp-opt', sources)
android_release = android_opt.Program('build/android-gcc-opt/spacecorp', android_opt_obj)

android_dbg_obj = android_dbg.Object('build/.obj/android/spacecorp-debug', sources)
android_debug = android_dbg.Program('build/android-gcc-debug/spacecorp', android_dbg_obj)

android_all = [android_debug, android_release]
Clean(android_all, ['build/android', 'build/.obj/android'])

env.Alias('android-all', android_all)        			
env.Alias('android-release', android_release)	
env.Alias('android-debug', android_debug)    		

Return('android_all', 'android_release', 'android_debug')