{

	"downloads" : [

		"https://github.com/OpenImageIO/oiio/archive/Release-1.8.12.tar.gz"

	],

	"url" : "http://www.openimageio.org",

	"license" : "LICENSE",

	"dependencies" : [ "Boost", "Python", "OpenEXR", "LibTIFF", "LibPNG", "LibJPEG-Turbo", "OpenColorIO" ],

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D USE_FFMPEG=NO"
			" -D USE_PYTHON=NO"
			# These next two disable `iv`. This fails to
			# build on Mac due to OpenGL deprecations, and
			# we've never packaged it anyway.
			" -D USE_OPENGL=NO"
			" -D USE_QT=NO"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",
		"cp {buildDir}/share/doc/OpenImageIO/openimageio.pdf {buildDir}/doc",
		
	],

	"manifest" : [

		"bin/maketx{executableExtension}",
		"bin/oiiotool{executableExtension}",

		"include/OpenImageIO",
		"lib/{libraryPrefix}OpenImageIO*{sharedLibraryExtension}*",

		"doc/openimageio.pdf",

	],
	"platform:windows" : {

		"commands" : [

			"mkdir gafferBuild",
			"cd gafferBuild &&"
				" cmake"
			 	" -G {cmakeGenerator}"
			 	" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
			 	" -D CMAKE_INSTALL_PREFIX={buildDir}"
			 	" -D CMAKE_PREFIX_PATH={buildDir}"
			 	" -D USE_FFMPEG=OFF"
			 	" -D USE_QT=OFF"
			 	" -D USE_PYTHON=OFF"
			 	" -D BUILDSTATIC=OFF"
				" -D BOOST_ROOT={buildDir}"
			 	" -D OPENEXR_INCLUDE_PATH={buildDir}\\include"
			 	" -D OPENEXR_IMATH_LIBRARY={buildDir}\\lib\\Imath.lib"
			 	" -D OPENEXR_ILMIMF_LIBRARY={buildDir}\\lib\\IlmImf.lib"
				" -D OPENEXR_IEX_LIBRARY={buildDir}\\lib\\Iex.lib"
				" -D OPENEXR_ILMTHREAD_LIBRARY={buildDir}\\lib\\IlmThread.lib"
				" -D ZLIB_INCLUDE_DIR={buildDir}\\include"
				" -D ZLIB_LIBRARY={buildDir}\\lib\\zlib.lib"
				" -D PNG_PNG_INCLUDE_DIR={buildDir}\\include"
				" -D PNG_LIBRARY={buildDir}\\lib\\libpng16.lib"
				" -D JPEG_INCLUDE_DIR={buildDir}\\include"
				" -D JPEG_LIBRARY={buildDir}\\lib\\jpeg.lib"
				" -D TIFF_INCLUDE_DIR={buildDir}\\include"
				" -D TIFF_LIBRARY={buildDir}\\lib\\libtiff.lib"
				" -D PYTHON_INCLUDE_DIR={pythonIncludeDir}"
				" -D PYTHON_LIBRARY={pythonLibDir}\\python{pythonMajorVersion}{pythonMinorVersion}.lib"
				" -D OCIO_LIBRARY_PATH={buildDir}\\lib\\OpenColorIO.lib"
			 	" ..",
			"cd gafferBuild && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",
			"copy {buildDir}\\bin\\{libraryPrefix}OpenImageIO*{sharedLibraryExtension}* {buildDir}\\lib\\",
		]

	}

}
