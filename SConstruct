#!/usr/bin/python

env = Environment(CC = 'gcc', CCFLAGS = ['-Iinclude'])

opt = env.Clone()
opt.Append(CCFLAGS = ['-O2'])

dbg = env.Clone()
dbg.Append(CCFLAGS = ['-g', '-DDEBUG'])

sources = 'source/main.c'

opt_obj = opt.Object('build/.obj/spacecorp-opt', sources)
release = opt.Program('build/spacecorp-opt', opt_obj)

dbg_obj = dbg.Object('build/.obj/spacecorp-debug', sources)
debug = dbg.Program('build/spacecorp-debug', dbg_obj)
Default(debug)

# Aliases so that scons can be invoked with a target name instead of a file name
# (i.e. scons reelase = scons /build/spacecorp-opt)
env.Alias('release', release)	# Add alias for named target 'release'
env.Alias('debug', debug) 		# Add alias for named target 'debug'
