{

	"downloads" : [

		"https://www.openssl.org/source/old/1.0.2/openssl-1.0.2h.tar.gz",

	],

	"url" : "https://www.openssl.org",

	"license" : "LICENSE",

	"commands" : [

		"./config --prefix={buildDir} -fPIC",
		"make -j {jobs}",
		"make install",

	],

	"platform:osx" : {

		"environment" : {

			"KERNEL_BITS" : "64",

		},

	},

	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild && "
				" cmake"
				" -G {cmakeGenerator}"
				" -D BUILD_OBJECT_LIBRARY_ONLY=ON"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" ..",

			"if not exist \"{buildDir}\\lib\" mkdir {buildDir}\\lib",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} -- -j {jobs}",
			"cd gafferBuild && copy crypto\\crypto.lib {buildDir}\\lib",
			"cd gafferBuild && copy ssl\\ssl.lib {buildDir}\\lib",
			"cd gafferBuild && xcopy /e /q /y /i include {buildDir}\\include",

		],

	},

}
