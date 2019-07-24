{

	"downloads" : [

		"https://github.com/openexr/openexr/releases/download/v2.3.0/openexr-2.3.0.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"./configure --prefix={buildDir}",
		"make -j {jobs}",
		"make install",

	],

	"platform:windows" : {

		"variables" : {
			"cmakeGenerator" : "\"Visual Studio 15 2017 Win64\"",
		},

		"downloads" : [

			"https://github.com/openexr/openexr/archive/v2.3.0.zip"

		],


		"commands" : [
			"mkdir gafferBuild",
			"cd gafferBuild && cmake"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -G {cmakeGenerator}"
				" -D CMAKE_PREFIX_PATH={buildDir}"
				" -D OPENEXR_PACKAGE_PREFIX={buildDir}"
				# " -D OPENEXR_NAMESPACE_VERSIONING=OFF"
				" -D OPENEXR_BUILD_TESTS=OFF"
				" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install",
			"rename {buildDir}\\lib\\Half-2_3.lib Half.lib",	# Packages expect Half to not have version suffix
			"if not exist {buildDir}\\python mkdir {buildDir}\\python",
			"copy {buildDir}\\lib\\python2.7\\site-packages\\iex.pyd {buildDir}\\python\\iex.pyd",
			"copy {buildDir}\\lib\\python2.7\\site-packages\\imath.pyd {buildDir}\\python\\imath.pyd",
		]
	},

}
