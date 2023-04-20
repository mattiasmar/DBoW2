from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, copy
from conan.tools.files.symlinks import absolute_to_relative_symlinks
import os

class dbow2Recipe(ConanFile):
    name = "dbow2"
    version = "1.0"


    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    #def source(self):
    #    get(self, "https://github.com/dorian3d/DBoW2/archive/refs/heads/master.zip",
    #              strip_root=True)
        
    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        self.options["opencv"].with_ffmpeg=False
        self.options["opencv"].with_gtk=False
        
    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        print("CMakeToolchain! BUILD_demo-False")
        tc.variables["BUILD_demo"] = False
        print("tc.variables=",tc.variables)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        copy(self, pattern="*.h", src=os.path.join(self.source_folder, "include"), dst=os.path.join(self.package_folder, "include"))
        copy(self, pattern="*.a", src=self.build_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False) 
        absolute_to_relative_symlinks(self, self.package_folder)
        
        cmake = CMake(self)
        cmake.install()
        
    def requirements(self):
        self.requires("libwebp/1.3.0",force=True)
        self.requires("opencv/4.5.5",force=True)
        self.requires("boost/1.76.0")
        
    def package_info(self):
        self.cpp_info.libs = ["dbow2"]

    