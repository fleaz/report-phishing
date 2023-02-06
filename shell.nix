{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    black
    python3
    python3Packages.jinja2
    python3Packages.pyyaml
  ];

}
