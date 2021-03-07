{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openexr/archive/v2.4.1.tar.gz"

	],

	"url" : "http://www.openexr.com",

	"license" : "LICENSE.md",

	"dependencies" : [ "Python", "Boost" ],

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			# OpenEXR's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D Boost_NO_SYSTEM_PATHS=TRUE"
			" -D Boost_NO_BOOST_CMAKE=TRUE"
			" -D BOOST_ROOT={buildDir}"
			" -D Python_ROOT_DIR={buildDir}"
			" -D Python2_ROOT_DIR={buildDir}"
			" -D Python3_ROOT_DIR={buildDir}"
			" -D Python3_FIND_STRATEGY=LOCATION"
			" ."
		,

		"make VERBOSE=1 -j {jobs}",
		"make install",

		"mkdir -p {buildDir}/python",
		"mv {pythonLibDir}/python{pythonVersion}/site-packages/iex.so {buildDir}/python",
		"mv {pythonLibDir}/python{pythonVersion}/site-packages/imath.so {buildDir}/python",

	],

	"manifest" : [

		"bin/exrheader",
		"include/OpenEXR",
		"lib/{libraryPrefix}IlmImf*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}Iex*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}Half*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}IlmThread*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}Imath*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}PyIex*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}PyImath*{sharedLibraryExtension}*",

		"lib/{libraryPrefix}IlmImf*.lib",
		"lib/{libraryPrefix}Iex*.lib",
		"lib/{libraryPrefix}Half*.lib",
		"lib/{libraryPrefix}IlmThread*.lib",
		"lib/{libraryPrefix}Imath*.lib",
		"lib/{libraryPrefix}PyIex*.lib",
		"lib/{libraryPrefix}PyImath*.lib",

		"python/iex{pythonModuleExtension}",
		"python/imath{pythonModuleExtension}",

	],

	"platform:windows" : {

		"variables" : {
			"cmakeGenerator" : "\"Visual Studio 15 2017 Win64\"",
		},

		"downloads" : [

			"https://github.com/openexr/openexr/archive/v2.4.1.zip"

		],

		"dependencies" : [ "Python", "Boost", "Zlib" ],


		"commands" : [
			"mkdir gafferBuild",
			"cd gafferBuild && cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -G {cmakeGenerator}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D OPENEXR_PACKAGE_PREFIX={buildDir}"
				" -D OPENEXR_LIB_SUFFIX="
				" -D ILMBASE_LIB_SUFFIX="
				" -D PYILMBASE_LIB_SUFFIX="
				" -D OPENEXR_BUILD_TESTS=OFF"
				" -D ZLIB_ROOT={buildDir}"
				" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			"if not exist {buildDir}\\python mkdir {buildDir}\\python",
			"copy {buildDir}\\lib\\site-packages\\iex.pyd {buildDir}\\python\\iex.pyd",
			"copy {buildDir}\\lib\\site-packages\\imath.pyd {buildDir}\\python\\imath.pyd",
			"copy {buildDir}\\bin\\{libraryPrefix}IlmImf*{sharedLibraryExtension}* {buildDir}\\lib\\",
			"copy {buildDir}\\bin\\{libraryPrefix}Iex*{sharedLibraryExtension}* {buildDir}\\lib\\",
			"copy {buildDir}\\bin\\{libraryPrefix}Half*{sharedLibraryExtension}* {buildDir}\\lib\\",
			"copy {buildDir}\\bin\\{libraryPrefix}IlmThread*{sharedLibraryExtension}* {buildDir}\\lib\\",
			"copy {buildDir}\\bin\\{libraryPrefix}Imath*{sharedLibraryExtension}* {buildDir}\\lib\\",
			"copy {buildDir}\\bin\\{libraryPrefix}PyIex*{sharedLibraryExtension}* {buildDir}\\lib\\",
			"copy {buildDir}\\bin\\{libraryPrefix}PyImath*{sharedLibraryExtension}* {buildDir}\\lib\\",
		]
	},

}
