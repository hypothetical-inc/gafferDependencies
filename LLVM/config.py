{

	"downloads" : [

		"https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/llvm-10.0.1.src.tar.xz",
		"https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/clang-10.0.1.src.tar.xz"

	],

	"url" : "https://llvm.org",

	"license" : "LICENSE.TXT",

	"commands" : [

		"mv ../clang* tools/clang",
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

			"move ..\\clang* tools\\clang",
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
			"cd build && cmake --build . --config {cmakeBuildType} --target install -- -j {jobs}",

		],

	}

}
