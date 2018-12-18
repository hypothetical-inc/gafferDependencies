{

	"downloads" : [

		"https://download.sourceforge.net/project/libjpeg-turbo/1.5.2/libjpeg-turbo-1.5.2.tar.gz",

	],

	"url" : "https://libjpeg-turbo.org",
	"license" : "LICENSE.md",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"include/jconfig.h",
		"include/jerror.h",
		"include/jmorecfg.h",
		"include/jpeglib.h",

		"lib/libjpeg*{sharedLibraryExtension}*",	# lib prefix is accurate for all platforms
		"lib/jpeg62{sharedLibraryExtension}",	# Windows only
		"lib/turbojpeg{sharedLibraryExtension}",	# Windows only
	],
	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild && "
				" cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D WITH_SIMD=OFF"
				" ..",

			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",

		],

	},

}
