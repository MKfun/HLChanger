from .parser import parser

parser.add_argument("input", type=str, help="Input file")
parser.add_argument("--skybox", type=str, help="Modify skybox (all for all)")
parser.add_argument("--background", type=None, help="Modify background (no need to specify the value)")
parser.add_argument("--addon", type=bool, help="Set to True for script to modify valve_addon directory instead of valve")
parser.add_argument("--output", type=str, help="Where to save the addon (not ignored only when --addon is set to True)")

args = parser.parse_args()
