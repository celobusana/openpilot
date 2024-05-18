# RUN UI
`poetry shell`
`tools/replay/replay "ROUTE"`
`poetry run scons -j$(nproc) && LIBGL_ALWAYS_SOFTWARE=1 selfdrive/ui/ui`