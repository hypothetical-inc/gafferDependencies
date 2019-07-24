{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openvdb/archive/v7.0.0.tar.gz"

	],

	"url" : "http://www.openvdb.org",

	"license" : "LICENSE",

	"dependencies" : [ "Blosc", "TBB", "OpenEXR", "Python" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"mkdir build",
		"cd build && cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			# OpenVDB's CMake setup uses GNUInstallDirs, which unhelpfully
			# puts the libraries in `lib64`. Coax them back.
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D OPENVDB_BUILD_PYTHON_MODULE=ON"
			" -D PYOPENVDB_INSTALL_DIRECTORY={buildDir}/python"
			" .."
		,

		"cd build && make VERBOSE=1 -j {jobs} && make install",

	],

	"manifest" : [

		"include/openvdb",
		"include/pyopenvdb.h",
		"lib/{libraryPrefix}openvdb*{sharedLibraryExtension}*",
		"python/pyopenvdb*",

	],

	"platform:windows" : {

		"variables" : {
		
			"cmakeGenerator" : "\"Visual Studio 15 2017 Win64\"",
		},

		"commands" : [
			# OpenVDB requests Python 2.7 specifically but Boost doesn't add version numbers until v1.67
			"mkdir gafferBuild",
			"cd gafferBuild && "
				" cmake"
				" -Wno-dev"
				" -G {cmakeGenerator}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D OPENVDB_BUILD_UNITTESTS=OFF"
				" -D OPENVDB_BUILD_DOCS=OFF"
				" -D OPENVDB_BUILD_PYTHON_MODULE=ON"
				" -D USE_GLFW3=OFF"
				" -D TBB_LOCATION={buildDir}"
				" -D BOOST_ROOT={buildDir}"
				" -D GLEW_LOCATION={buildDir}"
				" -D ILMBASE_LOCATION={buildDir}"
				" -D OPENEXR_LOCATION={buildDir}"
				" -D BLOSC_LOCATION={buildDir}"
				" -D OPENVDB_ENABLE_3_ABI_COMPATIBLE=OFF"
				" ..",

			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			# v7.0.0 names the Python library incorrectly
			# v7.1 fixes this, when updating this line should change the extension to .pyd
			# for both source and destination
			"copy {buildDir}\\lib\\python2.7\\pyopenvdb.dll {buildDir}\\python\\pyopenvdb.pyd"

		],

	},

}
