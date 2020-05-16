{

	"downloads" : [

		"https://github.com/01org/tbb/archive/2018_U5.tar.gz"

	],

	"url" : "http://threadingbuildingblocks.org/",

	"license" : "LICENSE",

	"commands" : [

		"make -j {jobs} stdver=c++{c++Standard}",
		"cp -r include/tbb {buildDir}/include",
		"{installLibsCommand}",

	],

	"manifest" : [

		"include/tbb",
		"lib/{libraryPrefix}tbb*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}tbb*.lib",

	],

	"platform:linux" : {

		"environment" : {

			"tbb_os" : "linux",

		},

		"variables" : {

			"installLibsCommand" : "cp build/*_release/*.so* {buildDir}/lib",

		},

	},

	"platform:osx" : {

		"environment" : {

			"tbb_os" : "macos",

		},

		"variables" : {

			"installLibsCommand" : "cp build/macos_*_release/*.dylib {buildDir}/lib",

		},

	},

	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild && "
				" cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_CXX_STANDARD={c++Standard}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D TBB_BUILD_TESTS=OFF"
				" ..",

			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",
			"copy {buildDir}\\bin\\{libraryPrefix}tbb*{sharedLibraryExtension}* {buildDir}\\lib\\",

		],

	},

}
