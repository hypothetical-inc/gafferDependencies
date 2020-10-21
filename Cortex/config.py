{

	"downloads" : [

		"https://github.com/ImageEngine/cortex/archive/10.0.0-a79.tar.gz"

	],

	"url" : "https://github.com/ImageEngine/cortex",

	"license" : "LICENSE",

	"dependencies" : [
		"Python", "OpenImageIO", "OpenEXR", "Boost", "OpenShadingLanguage",
		"Blosc", "FreeType", "GLEW", "Appleseed", "TBB", "OpenVDB", "USD", "Six"
	],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"requiredEnvironment" : [ "ARNOLD_ROOT", "RMAN_ROOT" ],

	"commands" : [

		"scons install installDoc"
			" -j {jobs}"
			" CXX=`which g++`"
			" CXXSTD={c++Standard}"
			" INSTALL_PREFIX={buildDir}"
			" INSTALL_DOC_DIR={buildDir}/doc/cortex"
			" INSTALL_RMANPROCEDURAL_NAME={buildDir}/renderMan/procedurals/iePython"
			" INSTALL_RMANDISPLAY_NAME={buildDir}/renderMan/displayDrivers/ieDisplay"
			" INSTALL_PYTHON_DIR={buildDir}/python"
			" INSTALL_ARNOLDOUTPUTDRIVER_NAME={buildDir}/arnold/plugins/ieOutputDriver.so"
			" INSTALL_IECORE_OPS=''"
			" PYTHON_CONFIG={buildDir}/bin/python{pythonMajorVersion}-config"
			" PYTHON={buildDir}/bin/python"
			" BOOST_INCLUDE_PATH={buildDir}/include/boost"
			" LIBPATH={buildDir}/lib"
			" BOOST_LIB_SUFFIX=''"
			" OPENEXR_INCLUDE_PATH={buildDir}/include"
			" OIIO_INCLUDE_PATH={buildDir}/include"
			" OSL_INCLUDE_PATH={buildDir}/include"
			" BLOSC_INCLUDE_PATH={buildDir}/include"
			" FREETYPE_INCLUDE_PATH={buildDir}/include/freetype2"
			" WITH_GL=1"
			" GLEW_INCLUDE_PATH={buildDir}/include/GL"
			" RMAN_ROOT=$RMAN_ROOT"
			" NUKE_ROOT="
			" ARNOLD_ROOT=$ARNOLD_ROOT"
			" APPLESEED_ROOT={buildDir}/appleseed"
			" APPLESEED_INCLUDE_PATH={buildDir}/appleseed/include"
			" APPLESEED_LIB_PATH={buildDir}/appleseed/lib"
			" ENV_VARS_TO_IMPORT=LD_LIBRARY_PATH"
			" OPTIONS=''"
			" SAVE_OPTIONS=gaffer.options",

		# Symlink for RenderMan, which uses a different convention to 3Delight.
		"ln -s -f ieDisplay{sharedLibraryExtension} {buildDir}/renderMan/displayDrivers/d_ieDisplay.so"

	],

	"manifest" : [

		"include/IECore*",
		"lib/{libraryPrefix}IECore*{sharedLibraryExtension}",
		"lib/{libraryPrefix}IECore*.lib",
		"python/IECore*",
		"renderMan",
		"arnold",
		"appleseedDisplays",
		"glsl/IECoreGL",
		"glsl/*.frag",
		"glsl/*.vert",
		"doc/cortex/html",

	],

    "platform:windows" : {

		"enabled" : False,

		"commands" : [

			"scons install installDoc --debug=findlibs"
				" -j 8"
				" INSTALL_PREFIX={buildDir}"
				" INSTALL_DOC_DIR={buildDir}\\doc\\cortex"
				" INSTALL_RMANPROCEDURAL_NAME={buildDir}\\renderMan\\procedurals\\iePython"
				" INSTALL_RMANDISPLAY_NAME={buildDir}\\renderMan\\displayDrivers\\ieDisplay"
				" INSTALL_PYTHON_DIR={buildDir}\\python"
				" INSTALL_ARNOLDOUTPUTDRIVER_NAME={buildDir}\\arnold\\plugins\\ieOutputDriver.dll"
				" BUILD_TYPE=RELWITHDEBINFO"
				" PYTHON={buildDir}\\bin\\python.exe"
				" PYTHON_INCLUDE_PATH={buildDir}\\include"
				" PYTHON_LINK_FLAGS="
				" BOOST_INCLUDE_PATH={buildDir}\\include\\boost-1_68"
				" BOOST_LIB_PATH={buildDir}\\lib"
				" BOOST_LIB_SUFFIX=-vc141-mt-x64-1_68"
				" OPENEXR_INCLUDE_PATH={buildDir}\\include"
				" OPENEXR_LIB_SUFFIX="
				" OIIO_INCLUDE_PATH={buildDir}\\include\\OpenImageIO"
				" OIIO_LIB_PATH={buildDir}\\lib"
				" OSL_INCLUDE_PATH={buildDir}\\include"
				" BLOSC_INCLUDE_PATH={buildDir}\\include"
				" FREETYPE_INCLUDE_PATH={buildDir}\\include\\freetype2"
				" FREETYPE_LIB_PATH={buildDir}\\lib"
				" WITH_GL=1"
				" GLEW_INCLUDE_PATH={buildDir}\\include"
				" GLEW_LIB_SUFFIX=32"
				" TBB_INCLUDE_PATH={buildDir}\\include"
				" APPLESEED_ROOT={buildDir}\\appleseed"
				" APPLESEED_INCLUDE_PATH={buildDir}\\appleseed\\include"
				" APPLESEED_LIB_PATH={buildDir}\\appleseed\\lib"
				" ARNOLD_ROOT=%ARNOLD_ROOT%"
				" RMAN_ROOT=%RMAN_ROOT"
				" USD_INCLUDE_PATH={buildDir}\\include"
				" USD_LIB_PATH={buildDir}\\lib"
				" PYTHONPATH={buildDir}\\python"
				" OPTIONS="
				" WARNINGS_AS_ERRORS=0"
				" SAVE_OPTIONS=cortex.options"
			
		]

	},

}
