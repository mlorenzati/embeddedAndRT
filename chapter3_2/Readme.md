# RPI Pico version of FreeRTOS demo
This project imports [raspberry pi version](https://github.com/raspberrypi/FreeRTOS-Kernel) of FreeRTOS
If you want to build a similar rpi FreeRTOS you can copy this structure

- You need the FreeRTOS-Kernel as a Submodule
- You need to include pico_sdk_import.cmake and FreeRTOS_Kernel_import.cmake

To setup your board just modify the board election on Parent CMakeists.txt

# Setup
Make sure you have installed updated required compiler for C and ASM and linker, on mac do not use brew tap ArmMbed/homebrew-formulae && brew install arm-none-eabi-gcc 
instead use brew install --cask gcc-arm-embedded

# build
```
mkdir build
cd build
cmake ..
make -j 4
```

For more information check [https://github.com/raspberrypi/pico-examples/tree/master/freertos](Raspberry pico examples FreeRtos)

