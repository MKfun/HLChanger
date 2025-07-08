from .parser import parser

parser.add_argument("input", type=str, help="Input file")
parser.add_argument("--skybox", type=str, help="Modify skybox (all for all)")
parser.add_argument("--background", type=None, help="Modify background (no need to specify the value)")
parser.add_argument("--sfx", type=str, help="Modify sfx (this argument is incompatible with any other positional argument)")

args = parser.parse_args()

if args.sfx and (args.skybox or args.hud or args.background):
    raise Exception("sfx is not compatible with any other positional argument!")
