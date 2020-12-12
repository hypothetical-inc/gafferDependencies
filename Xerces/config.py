{

	"downloads" : [

		"http://apache.mirror.anlx.net//xerces/c/3/sources/xerces-c-3.2.3.tar.gz"

	],

	"url" : "https://xerces.apache.org",

	"license" : "LICENSE",

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
		 	" cmake"
		 	" -G {cmakeGenerator}"
		 	" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
		 	" -D CMAKE_INSTALL_PREFIX={buildDir}"
		 	" ..",
		"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}"
	],

	"manifest" : [

		"lib/{libraryPrefix}xerces-c*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}xerces-c*.lib",

	],
	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild &&"
			 	" cmake"
			 	" -G {cmakeGenerator}"
			 	" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
			 	" -D CMAKE_INSTALL_PREFIX={buildDir}"
			 	" -D BUILD_SHARED_LIBS=OFF"
			 	" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",

		]

	}

}
