{

	"downloads" : [

		"https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz"

	],

	"url" : "https://sourceware.org/libffi/",
	"license" : "LICENSE",

	"commands" : [

		"./configure --prefix={buildDir} --libdir={buildDir}/lib --disable-multi-os-directory --without-gcc-arch",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"lib/{libraryPrefix}ffi*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}ffi*{staticLibraryExtension}*",

	],

	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild && "
				" cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" ..",

			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",
			"mkdir lib",
			"copy gafferBuild\\ffi.dll lib\\ffi.dll",
			"copy gafferBuild\\ffi.lib lib\\ffi.lib",

		],

	},

}
