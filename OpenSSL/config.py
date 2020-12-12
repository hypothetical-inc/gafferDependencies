{

	"downloads" : [

		"https://www.openssl.org/source/openssl-1.1.1h.tar.gz",

	],

	"url" : "https://www.openssl.org",

	"license" : "LICENSE",

	"commands" : [

		"./config --prefix={buildDir} -fPIC",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		# The "lib" prefix is correct for all platforms

		"lib/libssl*{sharedLibraryExtension}*",
		"lib/libcrypto*{sharedLibraryExtension}*",

	],

	"platform:osx" : {

		"environment" : {

			"KERNEL_BITS" : "64",

		},

	},

	"platform:windows" : {

		"commands" : [

			"perl Configure VC-WIN64A --prefix={buildDir} --openssldir={buildDir}",
			"nmake",
			"nmake install",

		],

	},

}
