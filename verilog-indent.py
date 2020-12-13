import sys
import re

filename = sys.argv[1]
indent = 0

with open(filename) as f:
    lines = f.readlines()

with open(filename, 'w') as f:
    for line in lines:
        replaced = re.sub('^\x20+', '', line)   # 元ファイルのインデントを削除
        indent_space = ''

        if('end ' in replaced or 'end\n' in replaced or 'endmodule' in replaced or ');' in replaced):
            indent -= 1
        if(indent < 0):
            indent = 0

        for i in range(indent):
            indent_space += '  '

        replaced = indent_space + replaced  # インデントを追加

        f.write(replaced)
        # print(replaced, end="")

        if ('module' in replaced or 'begin' in replaced or ');' in replaced):
            indent += 1
