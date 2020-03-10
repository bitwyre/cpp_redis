from conans import ConanFile, CMake


class cpp_redisConan(ConanFile):
    name = "cpp_redis"
    version = "4.3.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of cpp_redis here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "use_pic": [True, False]
    }
    default_options = {"shared": False, "use_pic": False}
    generators = "cmake"
    exports_sources = "*"
    no_copy_source = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_EXAMPLES'] = False
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.definitions['BUILD_TESTS'] = False
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.use_pic
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cpp_redis", "tacopie"]
        if self.settings.os == "Windows":
            self.cpp_info.libs += ["ws2_32"]
        else:
            self.cpp_info.cxxflags = ["-pthread"]
