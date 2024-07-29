from cx_Freeze import setup, Executable

# Define your application's executable
executables = [Executable("qr_code_generator.py", base="Win32GUI")]

# Setup configuration
setup(
    name="QR Code Generator",
    version="1.0",
    description="QR Code Generator Application",
    executables=executables
)
