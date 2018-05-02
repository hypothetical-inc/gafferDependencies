{

	"downloads" : [

		"http://releases.llvm.org/7.1.0/llvm-7.1.0.src.tar.xz",
		"http://releases.llvm.org/7.1.0/cfe-7.1.0.src.tar.xz"

	],

	"url" : "https://llvm.org",

	"license" : "LICENSE.TXT",

	"commands" : [

		"mv ../cfe* tools/clang",
		"mkdir build",
		"cd build &&"
			" cmake"
			" -G {cmakeGenerator}"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
			" -D LLVM_ENABLE_RTTI=ON"
			" ..",
		"cd build && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}"

	],

	"platform:windows" : {

		"commands" : [

			"move ..\\cfe* tools\\clang",
			"mkdir build",
			"cd build &&"
				" cmake"
				" -G {cmakeGenerator}"
				" -D CMAKE_INSTALL_PREFIX={buildDir}"
				" -D CMAKE_BUILD_TYPE={cmakeBuildType}"
				" -D BUILD_SHARED_LIBS=OFF"
				" -D LLVM_REQUIRES_RTTI=ON"
				" -D LLVM_TARGETS_TO_BUILD=\"X86\""
				" ..",
			"cd build && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}"

		],

	}

}
