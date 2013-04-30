#!/usr/bin/python

sources = 'source/main.c'

# Base environment 
env = Environment(CCFLAGS = ['-Iinclude'])

# Android environments
android = env.Clone()
android.Replace(CC = 'gcc')

android_opt = android.Clone()
android_opt.Append(CCFLAGS = ['-O2'])

android_dbg = android.Clone()
android_dbg.Append(CCFLAGS = ['-g', '-DDEBUG'])

android_opt_obj = android_opt.Object('build/.obj/android/spacecorp-opt', sources)
android_release = android_opt.Program('build/android/spacecorp-gcc-opt', android_opt_obj)

android_dbg_obj = android_dbg.Object('build/.obj/android/spacecorp-debug', sources)
android_debug = android_dbg.Program('build/android/spacecorp-gcc-debug', android_dbg_obj)

android_all = [android_debug, android_release]
Clean(android_all, ['build/android', 'build/.obj/android'])

# iOS environments 
ios = env.Clone()
ios.Replace(CC = 'gcc')

ios_opt = ios.Clone()
ios_opt.Append(CCFLAGS = ['-O2'])

ios_dbg = ios.Clone()
ios_dbg.Append(CCFLAGS = ['-g', '-DDEBUG'])

ios_opt_obj = ios_opt.Object('build/.obj/ios/spacecorp-opt', sources)
ios_release = ios_opt.Program('build/ios/spacecorp-gcc-opt', ios_opt_obj)

ios_dbg_obj = ios_dbg.Object('build/.obj/ios/spacecorp-debug', sources)
ios_debug = ios_dbg.Program('build/ios/spacecorp-gcc-debug', ios_opt_obj)

ios_all = [ios_debug, ios_release]
Clean(android_all, ['build/ios', 'build/.obj/ios'])

# Global Targets
debug = [ios_debug, android_debug]
release = [ios_release, android_release]

# Aliases so that scons can be invoked with a target name instead of a file name
# (i.e. scons reelase = scons /build/spacecorp-opt)
env.Alias('android-all', android_all)			
env.Alias('android-release', android_release)	
env.Alias('android-debug', android_debug) 		

env.Alias('ios-all', ios_all)
env.Alias('ios-release', ios_release)
env.Alias('ios-debug', ios_debug)

env.Alias('all', [ios_all, android_all])