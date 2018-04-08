{

	"downloads" : [

		"https://www.autodesk.com/content/dam/autodesk/www/Company/files/PySide2-Maya-2018_6.tgz"

	],

	"license" : "LICENSE.LGPLv21",

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",

	},

	"commands" : [

		"python setup.py --ignore-git --no-examples --jobs {jobs} --osx-use-libc++ install"


	],

	"platform:linux" : {

		"environment" : {

			"LD_LIBRARY_PATH" : "{buildDir}/lib",

		},

	},

	"platform:osx" : {

		"environment" : {

			"DYLD_FRAMEWORK_PATH" : "{buildDir}/lib",

		},

	},

	"platform:windows" : {

		"environment" : {

			"PATH" : "{buildDir}\\bin;{buildDir}\\lib;%PATH%",
			"VERSION" : "",	# PySide will pull in VERSION from the environment if it exists and cause a failure because the --ignore-git conflicts with VERSION

		},

		"commands" : [
			"python setup.py install"
				" --ignore-git"
				" --qmake=%BUILD_DIR%\\bin\\qmake.exe"
				" --openssl=%BUILD_DIR%\\lib"
				" --cmake=\"C:\\Program Files\\CMake\\bin\\cmake.exe\""
				" --jobs {jobs}"
				" --no-examples",
				# PySide2 installs to unusual directory structure, clean that up to be more in line with Gaffer
				"if not exist {buildDir}\\python\\PySide2 mkdir {buildDir}\\python\\PySide2",
				"copy {buildDir}\\lib\\site-packages\\PySide2\\release\\__init__.* {buildDir}\\python\\PySide2",
				"copy {buildDir}\\lib\\site-packages\\PySide2\\release\\_utils.* {buildDir}\\python\\PySide2",
				"copy {buildDir}\\lib\\site-packages\\PySide2\\release\\pyside*.* {buildDir}\\python\\PySide2",
				"copy {buildDir}\\lib\\site-packages\\PySide2\\release\\Qt*.* {buildDir}\\python\\PySide2",
				"copy {buildDir}\\lib\\site-packages\\PySide2\\release\\shiboken*.* {buildDir}\\python\\PySide2",
				"copy {buildDir}\\lib\\site-packages\\PySide2\\release\\__init__.* {buildDir}\\python\\PySide2",
				"xcopy /s /e /h /y /i {buildDir}\\lib\\site-packages\\PySide2\\release\\plugins {buildDir}\\python\\PySide2\\plugins",
				"xcopy /s /e /h /y /i {buildDir}\\lib\\site-packages\\PySide2\\include {buildDir}\\include\\PySide2",
				"xcopy /s /e /h /y /i {buildDir}\\lib\\site-packages\\PySide2\\translations {buildDir}\\python\\PySide2\\translations",
				"xcopy /s /e /h /y /i {buildDir}\\lib\\site-packages\\PySide2\\typesystems {buildDir}\\python\\PySide2\\typesystems",
				"rmdir /s /q {buildDir}\\lib\\site-packages\\PySide2",
		]
	},

}
