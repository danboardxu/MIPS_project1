#生成simulation
# 有立即数补"00"
# startAddress 为pc值

#J #target  instr_index

from disassembly import *

def instr1_J_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress):
    immediate = rs + rt + rd + shiftAmts + functionCodes + "00"
    startAddress[0] = int(immediate,base=2)

#JR rs
def instr1_JR_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress):
    immediate = rs + "00"
    startAddress[0] = int(immediate,base=2)

#BEQ rs=rt? banch
def instr1_BEQ_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress):
    offset = rd + shiftAmts + functionCodes + "00"
    if reg[int(rs,base=2)] == reg[int(rt,base=2)]:
        startAddress[0]  += int(offset,base= 2) + 4
    else:
         startAddress[0] += 4

#BLTZ if rs<0 then banch
def instr1_BLTZ_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress):
    offset = rd + shiftAmts + functionCodes + "00"
    if reg[int(rs, base=2)] < 0 :
        startAddress[0] += int(offset, base=2) + 4
    else:
        startAddress[0] += 4

#BGTZ if rs>0 then banch
def instr1_BGTZ_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    offset = rd + shiftAmts + functionCodes + "00"
    if reg[int(rs, base=2)] > 0:
        startAddress[0] += int(offset, base=2) + 4
    else:
        startAddress[0] += 4

#ADD rd = rs + rt
def instr1_ADD_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    reg[int(rd,base=2)] = reg[int(rs,base=2)] + reg[int(rt,base=2)]
    startAddress[0] += 4

# ADD I  rt = rs + immediate
def instr2_ADD_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    immediate = rd + shiftAmts + functionCodes
    reg[int(rt,base=2)] = int(immediate,base=2) + reg[int(rs,base=2)]
    startAddress[0] += 4

#SUB rd = rs - rt
def instr1_SUB_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    reg[int(rd, base=2)] = reg[int(rs, base=2)] - reg[int(rt, base=2)]
    startAddress[0] += 4

#SUB I rt = rs - imm
def instr2_SUB_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    immediate = rd + shiftAmts + functionCodes
    reg[int(rt,base=2)] =  int(immediate,base=2) - reg[int(rs,base=2)]
    startAddress[0] += 4

#BREAK
def instr1_BREAK_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    startAddress[0] += 4

#SW rt->mem[base+offset]
def instr1_SW_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    offset = rd + shiftAmts + functionCodes
    memory[int((reg[int(rs,base=2)] + int(offset,base=2)) /4)- int(dataAddress/4) ] = reg[int(rt,base=2)]

    startAddress[0] += 4

#LW rt <- memory[base+offset]
def instr1_LW_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    offset = rd + shiftAmts + functionCodes
    reg[int(rt, 2)] = memory[int((reg[int(rs,base=2)] + int(offset,base=2))/4) - int(dataAddress/4)]
    startAddress[0] += 4

#SLL rd <- rt<<sa 逻辑左移
def instr1_SLL_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    # 掩码 防止溢出
    mask = (2**32)-1
    reg[int(rd,2)] = (reg[int(rt,base=2)] << int(shiftAmts,base=2)) & mask
    startAddress[0] += 4

#SRL rd <- rt>>sa 逻辑
def instr1_SRL_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    reg[int(rd,2)] = (reg[int(rt,base=2)] >> int(shiftAmts[i],base=2))
    startAddress[0] += 4

#SRA rd <- rt>>sa 算术
def instr1_SRA_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    reg[int(rd,2)] = (reg[int(rt,base=2)] >> int(shiftAmts[i],base=2))
    startAddress[0] += 4

#NOP
def instr1_NOP_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    startAddress[0] += 4

#MUL rd<- rs * rt
def instr1_MUL_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    reg[int(rd, base=2)] = reg[int(rs, base=2)] * reg[int(rt, base=2)]
    startAddress[0] += 4

#MUL I rt<-rs * imm
def instr2_MUL_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    immediate = rd + shiftAmts + functionCodes
    reg[int(rt,base=2)] = reg[int(rs,base=2)] * int(immediate,base=2)
    startAddress[0] += 4

#AND rd<- rt & rs
def instr1_AND_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    reg[int(rd, base=2)] = reg[int(rs, base=2)] & reg[int(rt, base=2)]
    startAddress[0] += 4

# AND rt<- rs & imm
def instr2_AND_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    immediate = rd + shiftAmts + functionCodes
    reg[int(rt,base=2)] = reg[int(rs,base=2)] &  int(immediate,base=2)
    startAddress[0] += 4

# NOR rd<- ~(rs | rt)
def instr1_NOR_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    reg[int(rd,base=2)] = ~(reg[int(rs,base=2)] | reg[reg(int(rt,base=2))] )
    startAddress[0] += 4

# NOR rt<- ~(rs | imm)
def instr2_NOR_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    immediate = rd + shiftAmts + functionCodes
    reg[int(rt,base=2)] = ~(reg[int(rs,base=2)] |  int(immediate,base=2) )
    startAddress[0] += 4

#SLT rd <-( rs < rt)
def instr1_SLT_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    immediate = rd + shiftAmts + functionCodes
    if reg[int(rs,base=2)] < reg[int(rt,base=2)] :
        reg[int(rd,base=2)] = 1
    else:
        reg[int(rd, base=2)] = 0
    startAddress[0] += 4

#SLT rt <-( rs <imm)
def instr2_SLT_sim(rs, rt, rd, shiftAmts, functionCodes, reg, memory, dataAddress, startAddress):
    immediate = rd + shiftAmts + functionCodes
    if reg[int(rd,base=2)] <  int(immediate,base=2) :
        reg[int(rt,base=2)] = 1
    else:
        reg[int(rt, base=2)] = 0
    startAddress[0] += 4

# #字典序映射
# mapsim = {
#     'J': instr1_J_sim,
#     'JR':instr1_JR_sim,
#     'BEQ':instr1_BEQ_sim,
#     'BLTZ':instr1_BLTZ_sim,
#     'BGTZ': instr1_BGTZ_sim,
#     'ADD':{instr1_ADD_sim,instr2_ADD_sim},
#     'SUB':{instr1_SUB_sim,instr2_SUB_sim},
#     'BREAK':instr1_BREAK_sim,
#     'SW':instr1_SW_sim,
#     'LW':instr1_LW_sim,
#     'SLL':instr1_SLL_sim,
#     'SRL':instr1_SRL_sim,
#     'SRA':instr1_SLL_sim,
#     'NOP':instr1_NOP_sim,
#     'MUL':instr2_MUL_sim,
#     'AND':instr2_AND_sim,
#     'NOR':instr2_NOR_sim,
#     'SLT':instr2_SLT_sim,
# }
def judgeinstrution2(category,opcode,rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress):
    if category + opcode == '000010' :
        return instr1_J_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    elif category + opcode == '000100':
        return instr1_BEQ_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    elif category + opcode == '000001':
        return instr1_BLTZ_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    elif category + opcode == '000111':
        return instr1_BGTZ_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    elif category + opcode == '101011':
        return instr1_SW_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    elif category + opcode == '100011':
        return instr1_LW_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    elif category + opcode == '011100' and functionCodes == '000010':
        return instr1_MUL_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    #判断sp
    elif category + opcode == '000000' :
        if functionCodes == '001000':
            return instr1_JR_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '100000':
            return instr1_ADD_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '100010':
            return instr1_SUB_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '001101':

            return instr1_BREAK_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '000000' and rs == '00000' and rt != '00000' and rd != '00000' and shiftAmts !='00000':
            return instr1_SLL_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '000010':
            return instr1_SRL_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '000011':
            return instr1_SRA_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '000000' and rs == '00000' and rt == '00000' and rd == '00000' and shiftAmts =='00000':
            return instr1_NOP_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '100100':
            return instr1_AND_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '100111':
            return instr1_NOR_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        elif functionCodes == '101010':
            return instr1_SLT_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    elif category == '1':
        if opcode == '10000':
            return instr2_ADD_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        if opcode == '10001':
            return instr2_SUB_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        if opcode == '00001':
            return instr2_MUL_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        if opcode == '10010':
            return instr2_AND_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        if opcode == '10011':
            return instr2_NOR_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
        if opcode == '10101':
            return instr2_SLT_sim(rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)

#生成simulation.txt
def outputsimulation(dataAddress,startAddress,category,opcode,rs,rt,rd,shiftAmts,functionCodes
                     ,reg,memory,cyclenum,outputsim):
    instructioninfo = judgeinstrutionName1(category,opcode,rs,rt,rd,shiftAmts,functionCodes)
    breakflag = False
    if category + opcode == '000000' and functionCodes == '001101': #寻找break并标记
        breakflag = True

    outputsim.write("--------------------" + '\n')

    if category + opcode != '000000' or functionCodes != '001101':#非BREAK
        outputsim.write("Cycle:" + str(cyclenum[0]+ 1 ) + '\t' + str(startAddress[0]) + '\t'+ str(instructioninfo) + '\n' )
    elif category + opcode == '000000' and functionCodes == '001101': #BREAK
        outputsim.write("Cycle:" + str(cyclenum[0]+ 1 ) + '\t' + str(startAddress[0]) + '\t'+ 'BREAK' + '\n')

    judgeinstrution2(category,opcode,rs,rt,rd,shiftAmts,functionCodes,reg,memory,dataAddress,startAddress)
    outputsim.write('Registers'+'\n')
    #print(reg)
    #print(memory)
    outputsim.write('R00:' + '\t' + str(reg[0]) + '\t' + str(reg[1]) + '\t' + str(reg[2]) + '\t' + str(reg[3]) + '\t' + str(reg[4])
                    + '\t' + str(reg[5]) + '\t' + str(reg[6]) + '\t' + str(reg[7]) + '\n' + '\t'
                    + '\t' + str(reg[8]) + '\t' + str(reg[9]) + '\t' + str(reg[10]) + '\t' + str(reg[11]) + '\t' + str(reg[12])
                    + '\t' + str(reg[13]) + '\t' + str(reg[14]) + '\t' + str(reg[15]) + '\n')
    outputsim.write('R16:' + '\t' + str(reg[16]) + '\t' + str(reg[17]) + '\t' + str(reg[18]) + '\t' + str(reg[19]) + '\t' + str(reg[20])
                    + '\t' + str(reg[21]) + '\t' + str(reg[22]) + '\t' + str(reg[23]) + '\n'+ '\t'
                    + '\t' + str(reg[24]) + '\t' + str(reg[25]) + '\t' + str(reg[26]) + '\t' + str(reg[27]) + '\t' + str(reg[28])
                    + '\t' + str(reg[29]) + '\t' + str(reg[30]) + '\t' + str(reg[31]) + '\n')
    outputsim.write('\n')
    outputsim.write('Data' + '\n')
    outputsim.write(str(dataAddress) + ':\t' + str(memory[0]) +'\t' + str(memory[1]) + '\t' + str(memory[2]) + '\t' + str(memory[3]) + '\t' + str(memory[4])
                    + '\t' + str(memory[5]) + '\t' + str(memory[6]) + '\t' + str(memory[7]) + '\n')
    outputsim.write(str(dataAddress+32) + ':\t' + str(memory[8]) + '\t' + str(memory[9]) + '\t' + str(memory[10]) + '\t' + str(memory[11]) + '\t' + str(memory[12])
                    + '\t' + str(memory[13]) + '\t' + str(memory[14]) + '\t' + str(memory[15]) + '\n')
    outputsim.write(str(dataAddress+64) + ':\t' +str(memory[16]) + '\t' + str(memory[17]) + '\t' + str(memory[18]) + '\t' + str(memory[19]) + '\t' + str(memory[20])
                    + '\t' + str(memory[21]) + '\t' + str(memory[22]) + '\t' + str(memory[23]) + '\n')
    outputsim.write('\n')
    cyclenum[0] = cyclenum[0] + 1
    return breakflag