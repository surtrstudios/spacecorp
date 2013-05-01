#!/usr/bin/python
Import(['sources', 'env'])

# iOS environments 
ios = env.Clone()
ios.Replace(CC = 'gcc')

ios_opt = ios.Clone()
ios_opt.Append(CCFLAGS = ['-O2'])

ios_dbg = ios.Clone()
ios_dbg.Append(CCFLAGS = ['-g', '-DDEBUG'])

ios_opt_obj = ios_opt.Object('build/.obj/ios/spacecorp-opt', sources)
ios_release = ios_opt.Program('build/ios-gcc-opt/spacecorp', ios_opt_obj)

ios_dbg_obj = ios_dbg.Object('build/.obj/ios/spacecorp-debug', sources)
ios_debug = ios_dbg.Program('build/ios-gcc-debug/spacecorp', ios_opt_obj)

ios_all = [ios_debug, ios_release]
Clean(ios_all, ['build/ios', 'build/.obj/ios'])

env.Alias('ios-all', ios_all)
env.Alias('ios-release', ios_release)
env.Alias('ios-debug', ios_debug)

Return('ios_all', 'ios_release', 'ios_debug')