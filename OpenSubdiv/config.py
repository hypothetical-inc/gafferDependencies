{

	"downloads" : [

		"https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v3_4_3.tar.gz"

	],

	"url" : "http://graphics.pixar.com/opensubdiv",

	"license" : "LICENSE.txt",

	"commands" : [

		"cmake"
			" -G {cmakeGenerator}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D NO_DOC=1"
			" -D NO_OMP=1"
			" -D NO_CUDA=1"
			" -D NO_OPENCL=1"
			" -D NO_GLEW=1"
			" -D NO_GLFW=1"
			" -D NO_DX=1"
			" -D NO_TESTS=1"
			" -D NO_TBB=1"
			" -D OPENEXR_LOCATION={buildDir}/lib"
			" ."
		,

		"cmake --build . --config {cmakeBuildType} --target install -- VERBOSE=1 -j {jobs}",

	],

	"manifest" : [

		"include/opensubdiv",
		"lib/libosd*{sharedLibraryExtension}*",

	],

	"platform:windows" : {

		"variables" : {
			"cmakeGenerator" : "\"Visual Studio 15 2017 Win64\"",
		},

		"commands" : [

			"cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D NO_DOC=1"
				" -D NO_OMP=1"
				" -D NO_CUDA=1"
				" -D NO_OPENCL=1"
				" -D NO_GLEW=1"
				" -D NO_GLFW=1"
				" -D NO_DX=1"
				" -D NO_TESTS=1"
				" -D NO_TBB=1"
				" -D OPENEXR_LOCATION={buildDir}/lib"
				" ."
			,

			"cmake --build . --config {cmakeBuildType} --target install",

	],

	},

}
