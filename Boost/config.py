{

	"downloads" : [

		"https://dl.bintray.com/boostorg/release/1.68.0/source/boost_1_68_0.tar.gz"

	],

	"license" : "LICENSE_1_0.txt",

	"url" : "http://www.boost.org",

	"dependencies" : [ "Python" ],

	"variables" : {

		"boostVersionSuffix" : "",

	},

	"environment" : {

		# Without this, boost build will still pick up the system python framework,
		# even though we tell it quite explicitly to use the one in {buildDir}.
		"DYLD_FALLBACK_FRAMEWORK_PATH" : "{buildDir}/lib",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"MACOSX_DEPLOYMENT_TARGET" : "10.9",
		# Give a helping hand to find the python headers, since the bootstrap
		# below doesn't always seem to get it right.
		"CPLUS_INCLUDE_PATH" : "{pythonIncludeDir}",

	},

	"commands" : [

		"./bootstrap.sh --prefix={buildDir} --with-python={buildDir}/bin/python --with-python-root={buildDir} --without-libraries=log --without-icu",
		"./bjam -d+2 -j {jobs} --disable-icu cxxflags='-std=c++{c++Standard}' variant=release link=shared threading=multi install",

	],

	"manifest" : [

		"include/boost{boostVersionSuffix}",
		"lib/{libraryPrefix}boost_*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}boost_*.lib",
		"lib/{libraryPrefix}boost_test_exec_monitor{staticLibraryExtension}",

	],

	"platform:windows" : {

		"dependencies" : [ "Python", "Zlib" ],
	
		"variables" : {

			"boostVersionSuffix" : "-1_68",

		},

		"environment" : {

			# Boost needs help finding Python
			"PATH" : "%PATH%;{buildDir}\\bin",
			"PYTHONPATH" : "{buildDir};{buildDir}\\bin;{buildDir}\\lib64;{buildDir}\\lib"

		},

		"commands" : [

			"bootstrap.bat --prefix={buildDir} --with-python=\"{buildDir}\" --with-python-root=\"{buildDir}\" --without-libraries=log",
			"b2 -d+2 --prefix={buildDir} --toolset=msvc architecture=x86 address-model=64 --build-type=complete variant=release link=shared threading=multi cxxflags=\"/std:c++{c++Standard}\" -s ZLIB_SOURCE=%ROOT_DIR%\\Zlib\\working\\zlib-1.2.11 -s ZLIB_INCLUDE={buildDir}\\include -s ZLIB_LIBPATH={buildDir}\\lib -s ZLIB_BINARY=zlib install"

		],

	},
}
