cmake_minimum_required(VERSION 3.13)

# ---- Set target board ----
# Options: pico, pico2, pico_w, pico2_w, etc.
set(PICO_BOARD pico2)
set(PICO_PLATFORM rp2350)

# ---- Import Pico SDK ----
include(pico_sdk_import.cmake)

# ---- Project ----
project(hello_freertos_one_core C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# ---- Init SDK ----
pico_sdk_init()

# ---- FreeRTOS ----
set(FREERTOS_KERNEL_PATH ${CMAKE_CURRENT_LIST_DIR}/FreeRTOS-Kernel)
include(FreeRTOS_Kernel_import.cmake)

# ---- Executable ----
add_executable(hello_freertos_one_core
    hello_freertos.c
)

# ---- Include dirs ----
target_include_directories(hello_freertos_one_core PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/..
    ${CMAKE_CURRENT_LIST_DIR}/.
    )

# ---- Link Libraries ----
target_link_libraries(hello_freertos_one_core PRIVATE
    pico_async_context_freertos
    FreeRTOS-Kernel-Heap4
    pico_stdlib
    )

# ---- Enable I/O ----
pico_enable_stdio_usb(hello_freertos_one_core 1)
pico_enable_stdio_uart(hello_freertos_one_core 0)

# ---- Create UF2, bin, etc. ----
pico_add_extra_outputs(hello_freertos_one_core)