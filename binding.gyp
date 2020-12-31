{
  'variables': {
    'halide_dir': '<(module_root_dir)/Halide'
  },
  "targets": [
    {
      "target_name": "civalg",
      "sources": [
        "src/civalg.cpp",
        "src/Color.cpp",
        "src/util.cpp"
      ],
      "include_dirs": [
        "include",
        "Halide/include",
        # "<!(node -e \"require('nan')\")",
        '<!@(node -p "require(\'node-addon-api\').include")',
      ],
      "cflags!": [
        '-fno-exceptions',
        '-fno-rtti'
      ],
       "cflags_cc!": [
        '-fno-exceptions',
        '-fno-rtti'
      ],
      'xcode_settings': {
        'CLANG_CXX_LANGUAGE_STANDARD': 'c++17',
        'MACOSX_DEPLOYMENT_TARGET': '10.9',
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'GCC_ENABLE_CPP_RTTI': 'YES',
        'OTHER_CPLUSPLUSFLAGS': [
          '-fexceptions',
          '-Wall',
          '-mmacosx-version-min=10.15',
          '-O3'
        ],
        "OTHER_LDFLAGS": [
          '-Wl,-rpath,\'@loader_path/../../Halide/lib\''
        ],
        'link_settings': {
          'library_dirs': ['<(halide_dir)/lib'],
          'libraries': [
            'libHalide.dylib'
          ],
        }
      },
      'conditions':[
        ['OS == "win"', {}],
        ['OS == "linux"', {
          'link_settings': {
            'library_dirs': ['<(halide_dir)/lib'],
            'libraries': [
            'libHalide.dylib'
            ],
          },
        }]
      ]
      
    }
  ]
}