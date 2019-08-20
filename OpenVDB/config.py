{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openvdb/archive/v6.0.0.tar.gz"

	],

	"license" : "LICENSE",

	"variables" : {

		"pythonVersion" : "2.7",

	},

	"commands" : [

		"cd openvdb && make install"
			" -j {jobs} "
			" DESTDIR={buildDir}"
			" BOOST_INCL_DIR={buildDir}/include"
			" BOOST_LIB_DIR={buildDir}/lib"
			" BOOST_PYTHON_LIB_DIR={buildDir}/lib"
			" BOOST_PYTHON_LIB=-lboost_python"
			" EXR_INCL_DIR={buildDir}/include"
			" EXR_LIB_DIR={buildDir}/lib"
			" TBB_INCL_DIR={buildDir}/include"
			" TBB_LIB_DIR={buildDir}/lib"
			" PYTHON_VERSION={pythonVersion}"
			" PYTHON_INCL_DIR={pythonIncludeDir}"
			" PYTHON_LIB_DIR={pythonLibDir}"
			" BLOSC_INCL_DIR={buildDir}/include"
			" BLOSC_LIB_DIR={buildDir}/lib"
			" NUMPY_INCL_DIR="
			" CONCURRENT_MALLOC_LIB="
			" GLFW_INCL_DIR="
			" LOG4CPLUS_INCL_DIR="
			" EPYDOC=",

		"mv {buildDir}/python/lib/python{pythonVersion}/pyopenvdb.so {buildDir}/python",
		"mv {buildDir}/python/include/python{pythonVersion}/pyopenvdb.h {buildDir}/include",

	],

	"platform:linux" : {

		"variables" : {

			"pythonIncludeDir" : "{buildDir}/include/python{pythonVersion}",
			"pythonLibDir" : "{buildDir}/lib",

		},

	},

	"platform:osx" : {

		"variables" : {

			"pythonIncludeDir" : "{buildDir}/lib/Python.framework/Headers",
			"pythonLibDir" : "{buildDir}/lib/Python.framework/Versions/{pythonVersion}",

		},

	},

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
			"copy {buildDir}\\lib\\python2.7\\pyopenvdb.pyd {buildDir}\\python\\pyopenvdb.pyd"

		],

	},

}
