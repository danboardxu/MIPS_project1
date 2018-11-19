# 传入文件

from simulation import *

from disassembly import *

def Load(filename):
    Instruction = []
    try:
        with open(filename + '.txt', 'r') as file:
            for instr in file:
                Instruction.append(instr.strip())
            return Instruction
    except Exception as e:
        print("打开文件出错，重新输入:",e)
    finally:
        pass
            #   print(instructions)




def main():
    InputName = input("请输入sample文件名称(放在同一目录下 如sample.txt 输入sample):\n")
    Instruction = Load(InputName)
    startAddress = [64] # 起始地址
    dataAddress = [] # 数据地址
    category = [] # Category 判断 R-R还是R-M
    opcode = [] #操作码
    rs = []  # 源寄存器
    rt = []  # 源寄存器
    rd = []  # 目的寄存器
    shiftAmts = []  # 移位
    functionCodes = []  # 功能码
    Immediate = [] #
    reg = [0] * 32 # 32个寄存器
    memory = [0] * 60 # 内存地址  60个
    cyclenum = [0]

    outputdis = open('disassembly.txt', 'w')
    outputsim = open('simulation.txt', 'w')


#指令解析
    for instruct in Instruction:
        instr_divide(instruct,category,opcode,rs,rt,rd,shiftAmts,functionCodes)

    for instruct in Instruction:
       # print(instruct)
        i = int((startAddress[0] / 4) - 16)
        # print(i)
        if Instructiondiassembly(instruct,startAddress,category[i],opcode[i],rs[i],rt[i],rd[i],
                         shiftAmts[i],functionCodes[i],i,outputdis):
            break
        startAddress[0] += 4


    #数据部分处理
    dataAddress = startAddress[0] + 4  # 数据部分开始地址
    breakIndex = int((dataAddress - 64) / 4)  # 数据开始行数
    dataInstructions = Instruction[breakIndex:]  # 切分Instruction
    i = 0
    for data in dataInstructions:
        bits = 32
        startAddress[0] += 4
        j = int((startAddress[0] / 4) - 16)
        if category[j] == '0':  # 正数
            outputdis.write(data + '\t' + '\t' + str(startAddress[0]) + '\t' + '\t' + str(int(data, base=2)) + '\n')
            memory[i] = int(data, base=2)

        else:  # 负数取反+1
            outputdis.write(data + '\t' + '\t' + str(startAddress[0]) + '\t' + '\t' + str(int(data, base=2) - (1 << bits)) + '\n')
            memory[i] = int(data, base=2) - (1 << bits)
        i = i + 1


    startAddress[0]= 64#重新设置初始地址

    isFinish = False
    while isFinish != True:
        i = int((startAddress[0] / 4) - 16)
        isFinish = outputsimulation(dataAddress,startAddress,category[i],opcode[i],rs[i],rt[i],rd[i],shiftAmts[i],functionCodes[i],reg,memory,cyclenum,outputsim)
        if isFinish==True:
            break


if __name__ == '__main__':
    main()

