pkgname = "xh"
pkgver = "0.25.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=rustls,http3",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "oniguruma-devel",
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Tool for sending HTTP requests"
license = "MIT"
url = "https://github.com/ducaale/xh"
source = f"{url}/archive/8a575d3cf1131bb0fd645d672617a539a4ef8091.tar.gz"
sha256 = "3d542862dcc8e74e9bd4d1224c56d32fd70c6172af2630c5a9535640faf3b6e4"
tool_flags = {"RUSTFLAGS": ["--cfg=reqwest_unstable"]}



def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/xh")
    self.install_link("usr/bin/xhs", "xh")
    self.install_license("LICENSE")
    self.install_man("doc/xh.1")
    self.install_completion("completions/_xh", "zsh")
    self.install_completion("completions/xh.bash", "bash")
    self.install_completion("completions/xh.fish", "fish")
    self.install_completion("completions/xh.nu", "nushell")
