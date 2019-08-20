{

	"downloads" : [

		"https://github.com/openexr/openexr/archive/v2.3.0.tar.gz"

	],

	"license" : "LICENSE",

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"DYLD_FALLBACK_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"./configure --prefix={buildDir} --with-boost-include-dir={buildDir}/include --without-numpy",
		"make -j {jobs}",
		"make install",

		"mkdir -p {buildDir}/python",
		"mv {buildDir}/lib/python*/site-packages/iexmodule.so {buildDir}/python",
		"mv {buildDir}/lib/python*/site-packages/imathmodule.so {buildDir}/python",

	],

	"platform:windows" : {

		"commands" : [
			"echo PyIlmBase on Windows is built as part of OpenEXR",
		]
	},

}
