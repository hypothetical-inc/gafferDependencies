{

	"downloads" : [

		"https://github.com/OpenImageIO/oiio/archive/Release-2.2.11.1.tar.gz"

	],

	"url" : "http://www.openimageio.org",

	"license" : "LICENSE.md",

	"dependencies" : [ "Boost", "Python", "PyBind11", "OpenEXR", "LibTIFF", "LibPNG", "LibJPEG-Turbo", "OpenColorIO", "LibRaw", "PugiXML" ],

	"environment" : {

		"PATH" : "{buildDir}/bin:$PATH",
		"LD_LIBRARY_PATH" : "{buildDir}/lib:$LD_LIBRARY_PATH",

	},

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_CXX_STANDARD={c++Standard}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D USE_FFMPEG=NO"
			" -D USE_PYTHON=YES"
			" -D USE_EXTERNAL_PUGIXML=YES"
			" -D OIIO_BUILD_TESTS=NO"
			" {pythonArguments}"
			# These next two disable `iv`. This fails to
			# build on Mac due to OpenGL deprecations, and
			# we've never packaged it anyway.
			" -D USE_OPENGL=NO"
			" -D USE_QT=NO"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",

	],

	"variant:Python:2" : {

		"variables" : {

			"pythonArguments" : "-D PYTHON_VERSION=2",

		},

	},

	"variant:Python:3" : {

			"variables" : {

			"pythonArguments" : "-D PYTHON_VERSION=3",

		},

	},

	"manifest" : [

		"bin/maketx{executableExtension}",
		"bin/oiiotool{executableExtension}",

		"include/OpenImageIO",
		"lib/{libraryPrefix}OpenImageIO*{sharedLibraryExtension}*",
		"lib/{libraryPrefix}OpenImageIO*.lib",

		"doc/openimageio.pdf",

	],
	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild &&"
				" cmake"
			 	" -G {cmakeGenerator}"
				" -D CMAKE_CXX_STANDARD={c++Standard}"
			 	" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
			 	" -D CMAKE_INSTALL_PREFIX={buildDirFwd}"
			 	" -D CMAKE_PREFIX_PATH={buildDirFwd}"
			 	" -D USE_FFMPEG=OFF"
			 	" -D USE_QT=OFF"
			 	" -D USE_PYTHON=OFF"
			 	" -D BUILDSTATIC=OFF"
				" -D BOOST_ROOT={buildDirFwd}"
			 	" -D OPENEXR_INCLUDE_PATH={buildDirFwd}/include"
			 	" -D OPENEXR_IMATH_LIBRARY={buildDirFwd}/lib/Imath.lib"
			 	" -D OPENEXR_ILMIMF_LIBRARY={buildDirFwd}/lib/IlmImf.lib"
				" -D OPENEXR_IEX_LIBRARY={buildDirFwd}/lib/Iex.lib"
				" -D OPENEXR_ILMTHREAD_LIBRARY={buildDirFwd}/lib/IlmThread.lib"
				" -D ZLIB_INCLUDE_DIR={buildDirFwd}/include"
				" -D ZLIB_LIBRARY={buildDirFwd}/lib/zlib.lib"
				" -D PNG_PNG_INCLUDE_DIR={buildDirFwd}/include"
				" -D PNG_LIBRARY={buildDirFwd}/lib/libpng16.lib"
				" -D JPEG_INCLUDE_DIR={buildDirFwd}/include"
				" -D JPEG_LIBRARY={buildDirFwd}/lib/jpeg.lib"
				" -D TIFF_INCLUDE_DIR={buildDirFwd}/include"
				" -D TIFF_LIBRARY={buildDirFwd}/lib/libtiff.lib"
				" -D PYTHON_INCLUDE_DIR={pythonIncludeDir}"
				" -D PYTHON_LIBRARY={pythonLibDir}/python{pythonMajorVersion}{pythonMinorVersion}.lib"
				" -D OCIO_LIBRARY_PATH={buildDirFwd}/lib/OpenColorIO.lib"
			 	" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",
			"copy {buildDir}\\bin\\{libraryPrefix}OpenImageIO*{sharedLibraryExtension}* {buildDir}\\lib\\",
		]

	}

}
