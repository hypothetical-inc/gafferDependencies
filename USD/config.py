{

	"downloads" : [

		"https://github.com/PixarAnimationStudios/USD/archive/v20.02.tar.gz"

	],

	"url" : "https://graphics.pixar.com/usd",

	"license" : "LICENSE.txt",

	"dependencies" : [ "Boost", "Python", "OpenImageIO", "TBB", "Alembic" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D Boost_NO_SYSTEM_PATHS=TRUE"
			" -D Boost_NO_BOOST_CMAKE=TRUE"
			" -D PXR_BUILD_IMAGING=FALSE"
			" -D PXR_BUILD_TESTS=FALSE"
			" -D PXR_BUILD_ALEMBIC_PLUGIN=TRUE"
			" -D PXR_ENABLE_HDF5_SUPPORT=FALSE"
			" -D ALEMBIC_DIR={buildDir}/lib"
			" -D OPENEXR_LOCATION={buildDir}/lib"
			# Disable Python support until USD supports Python 3.
			" -D PXR_ENABLE_PYTHON_SUPPORT=FALSE"
			# Needed to prevent CMake picking up system python libraries on Mac.
			" -D CMAKE_FRAMEWORK_PATH={pythonLibDir}"
			" ."
		,

		"make VERBOSE=1 -j {jobs}",
		"make install",

	],

	"manifest" : [

		"bin/usd*{executableExtension}",
		"bin/sdfdump{executableExtension}",

		"include/pxr",

		# lib prefix is accurate for all platforms
		"lib/{libraryPrefix}trace{sharedLibraryExtension}",
		"lib/{libraryPrefix}arch{sharedLibraryExtension}",
		"lib/{libraryPrefix}tf{sharedLibraryExtension}",
		"lib/{libraryPrefix}js{sharedLibraryExtension}",
		"lib/{libraryPrefix}work{sharedLibraryExtension}",
		"lib/{libraryPrefix}plug{sharedLibraryExtension}",
		"lib/{libraryPrefix}kind{sharedLibraryExtension}",
		"lib/{libraryPrefix}gf{sharedLibraryExtension}",
		"lib/{libraryPrefix}vt{sharedLibraryExtension}",
		"lib/{libraryPrefix}ar{sharedLibraryExtension}",
		"lib/{libraryPrefix}sdf{sharedLibraryExtension}",
		"lib/{libraryPrefix}pcp{sharedLibraryExtension}",
		"lib/{libraryPrefix}usd*{sharedLibraryExtension}",

		"lib/{libraryPrefix}trace.lib",
		"lib/{libraryPrefix}arch.lib",
		"lib/{libraryPrefix}tf.lib",
		"lib/{libraryPrefix}js.lib",
		"lib/{libraryPrefix}work.lib",
		"lib/{libraryPrefix}plug.lib",
		"lib/{libraryPrefix}kind.lib",
		"lib/{libraryPrefix}gf.lib",
		"lib/{libraryPrefix}vt.lib",
		"lib/{libraryPrefix}ar.lib",
		"lib/{libraryPrefix}sdf.lib",
		"lib/{libraryPrefix}pcp.lib",
		"lib/{libraryPrefix}usd*.lib",

		"lib/usd",

		"python/pxr",

		"share/usd",

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
				" -D Boost_NO_BOOST_CMAKE=TRUE"
				" -D PXR_BUILD_IMAGING=FALSE"
				" -D PXR_BUILD_TESTS=FALSE"
				" -D Boost_NO_SYSTEM_PATHS=TRUE"
				" -D PXR_BUILD_ALEMBIC_PLUGIN=TRUE"
				" -D PXR_ENABLE_HDF5_SUPPORT=FALSE"
				" -D ALEMBIC_DIR={buildDir}\\lib"
				" -D OPENEXR_LOCATION={buildDir}\\lib"
				" ..",

			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",

			"xcopy /s /e /h /y /i {buildDir}\\lib\\python\\pxr {buildDir}\\python\\pxr",

		],

	},

}
