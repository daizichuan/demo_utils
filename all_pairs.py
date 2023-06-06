from allpairspy import AllPairs

'''
正交实验法生成多个测试用例
'''
parameters = [
    ["X品牌", "Y品牌"],
    ["Windows10", "Windows11", "macOS", "Ubuntu"],
    ["有线网络", "无线网络"],
    ["按天", "按周", "按月", "按年"],
    [6, 10, 15, 30, 60]
]

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i + 1, pairs))