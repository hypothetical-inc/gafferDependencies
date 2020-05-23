{

	"downloads" : [

		"https://github.com/lz4/lz4/archive/v1.9.2.tar.gz"

	],

	"url" : "http://www.lz4.org",
	"license" : "lib/LICENSE",

	"commands" : [

		"make install PREFIX={buildDir}",

	],

	"manifest" : [

		"lib/liblz4*{sharedLibraryExtension}*",

	],

	"platform:windows" : {

		"manifest" : [

			"visual\\VS2017\\bin\\x64_Release\\liblz4.dll",
			"visual\\VS2017\\bin\\x64_Release\\liblz4.lib",

		],

		"commands" : [

			# From the LZ4 appveyor script
			"msbuild visual\\VS2017\\lz4.sln /m /verbosity:minimal /property:PlatformToolset=v141 /t:Clean,Build /p:Platform=x64 /p:Configuration=Release",

		],

	},

}
