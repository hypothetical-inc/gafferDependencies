{

	"downloads" : [

		"https://github.com/GafferHQ/resources/archive/0.54.2.0.tar.gz"

	],

	"url" : "https://www.gafferhq.org",

	"license" : None,

	"commands" : [

		"cp -r resources {buildDir}",

	],

	"manifest" : [

		"resources",

	],
	"platform:windows" : {

		"commands" : [

			"xcopy /s /e /h /y /i resources {buildDir}\\resources",

		],

	}

}
