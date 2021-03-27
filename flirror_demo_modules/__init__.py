from flirror_demo_modules.modules.demo.foobar import demo_module

# To make your FlirrorModule availble, it must be exposed via one of the
# following variables: FLIRROR_MODULE or FLIRROR_MODULES.

invalid_module = "abc"

FLIRROR_MODULES = [demo_module, invalid_module]
# FLIRROR_MODULE = demo_module
