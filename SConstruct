#!/usr/bin/python

sources = 'source/main.c'

# Base environment 
env = Environment(CCFLAGS = ['-Iinclude'])

(android_all, android_release, android_debug) = SConscript('android.SConscript', ['sources', 'env'])

(ios_all, ios_release, ios_debug) = SConscript('iOS.SConscript', ['sources', 'env'])

# Clean Up 
Clean(ios_all, 'build')
Clean(android_all, 'build')

env.Alias('all', [ios_all, android_all])