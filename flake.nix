{
  description = "my manimation";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    systems.url = "github:nix-systems/default";
  };

  outputs = { self, nixpkgs, systems, ... } @ inputs:
    let
      inherit (nixpkgs) lib;
      eachSystem = lib.genAttrs (import systems);
      pkgsFor = eachSystem (system:
        import nixpkgs {
          system = system;
        }
      );
    in
    {
      devShells = eachSystem (system: with pkgsFor.${system}; {
        default = mkShell {
          packages = [ 
            fish 
            python3
            ( python3Packages.manim )
            # python3.withPackages (ps: with ps; [
            #   manimgl
            # ])
          ];
        };
      });
    };
}
