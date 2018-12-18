{

	"downloads" : [

		"https://download.osgeo.org/libtiff/tiff-4.0.10.tar.gz",

	],

	"url" : "http://www.libtiff.org",

	"license" : "COPYRIGHT",

	"dependencies" : [ "LibJPEG-Turbo" ],

	"environment" : {

		# Needed to make sure we link against the libjpeg
		# in the Gaffer distribution and not the system
		# libjpeg.
		"CPPFLAGS" : "-I{buildDir}/include",
		"LDFLAGS" : "-L{buildDir}/lib",

	},

	"commands" : [

		"./configure --without-x --prefix={buildDir}",
		"make -j {jobs}",
		"make install"

	],

	"manifest" : [

		"include/tiff*",
		"lib/libtiff*{sharedLibraryExtension}*",

	],
	"platform:windows" : {

		"commands" : [

			"nmake /f makefile.vc",
			"copy libtiff\\*.h {buildDir}\\include",
			"copy libtiff\\libtiff.lib {buildDir}\\lib"

		],

	},

}
