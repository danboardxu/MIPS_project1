#生成disassembly文件

#指令分解为 6    5   5   5   5   6
# category 1 : J JR BEQ BLTZ | ADD SUB | BREAK |SW LW |SLL SRL SRA NOP
#   op rs rt rd shamt funnc
#   6   5  5  5   5    6
# category 2 : ADD SUB| MUL | AND XOR | SLT
# : Imm opcode rs rt rd  0   functionn | imm function rs rt immediate
#   1    5     5   5  5 000000  6      |  1   5       5   5   16
# category 1

#分解指令 对于相应的category进行处理
def instr_divide(Instruction,category,opcode,rs,rt,rd,shiftAmts,functionCodes):
    category.append(Instruction[0])
    opcode.append(Instruction[1:6])
    rs.append(Instruction[6:11])
    rt.append(Instruction[11:16])
    rd.append(Instruction[16:21])
    shiftAmts.append(Instruction[21:26])
    functionCodes.append(Instruction[26:])

# category 2
# def Instr2_divide(Instruction,imm,opcode,rs,rt,rd,functionCodes,Immediate):
#     if(Instruction[0]==0):
#         imm.append(Instruction[0])
#         opcode.append(Instruction[1:6])
#         rs.append(Instruction[6:11])
#         rt.append(Instruction[11:16])
#         rd.append(Instruction[16:21])
#         functionCodes(Instruction[26:])
#     elif(Instruction[0]==1):
#         imm.append(Instruction[0])
#         functionCodes.append(Instruction[1:6])
#         rs.append(Instruction[6:11])
#         rt.append(Instruction[11:16])
#         Immediate.append(Instruction[17:])

def Regname(reg):
    if int(reg,base=2) >=0  and int(reg,base=2) <=31:
        regisname = 'R' +str(int(reg,base=2))
    return regisname

#指令集 Category 1 disassembly
# J    #target   op(6) target(26)  左移两位
def instr1_J_dis(rs,rt,rd,shiftAmts,functionCodes):
    InstrDis = '#' + str(int(rs+rt+rd+shiftAmts+functionCodes,base=2) << 2)
    return InstrDis

#JR   rs  op(6) rs(5) 0(10) hint (5) JR(6)
def instr1_JR_dis(rs,rt,rd,shiftAmts,functionCodes):
    InstrDis = Regname(rs)
    return InstrDis

#BEQ  rs rt offset||00 op(6) rs(5) offset(16)
def instr1_BEQ_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    offset = rd + shiftAmts + functionCodes + "00"
    InstrDis = rsname +', ' + rtname +', '+ '#' + str(int(offset,base=2))
    return InstrDis

#BLTZ rs,offset   regimm(6) rs(5) bltz(00000) offset(16)
def instr1_BLTZ_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    offset = rd + shiftAmts + functionCodes + "00"
    InstrDis = rsname +', '+'#'+str(int(offset,base=2))
    return InstrDis

#BGTZ rs,offset = BLTZ
def instr1_BGTZ_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    offset = rd + shiftAmts + functionCodes + "00"
    InstrDis = rsname +', '+'#'+str(int(offset,base=2))
    return InstrDis

#ADD rd,rs,rt 6 rs(5) rt(5) rd(5) 0(5) 10000
def instr1_ADD_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    rdname = Regname(rd)
    InstrDis = rdname + ', ' + rsname + ', ' + rtname
    return InstrDis

#ADD category rs + immediate
def instr2_ADD_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    immediate = rd + shiftAmts + functionCodes
    InstrDis = rtname + ', ' + rsname + ', '+'#' + str(int(immediate, base=2))
    return InstrDis

#SUB rd,rs,rt
def instr1_SUB_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    rdname = Regname(rd)
    InstrDis = rdname + ', ' + rsname + ', ' + rtname
    return InstrDis
#SUBI
def instr2_SUB_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    immediate = rd + shiftAmts + functionCodes
    InstrDis = rtname + ', ' + rsname + ', '+'#' + str(int(immediate, base=2))
    return InstrDis

#BREAK
def instr1_BREAK_dis(rs,rt,rd,shiftAmts,functionCodes):
    return ""

#SW rt,offset(base) 101011 base(5) rt(5) offset(16)
def instr1_SW_dis(rs,rt,rd,shiftAmts,functionCodes):
    rtname = Regname(rt)
    basename = Regname(rs)
    offset = rd +shiftAmts + functionCodes
    Instrdis = rtname + ', ' + str(int(offset,base=2)) + '('+ basename + ')'
    return Instrdis

# LW
def instr1_LW_dis(rs,rt,rd,shiftAmts,functionCodes):
    rtname = Regname(rt)
    basename = Regname(rs)
    offset = rd +shiftAmts + functionCodes
    Instrdis = rtname + ', ' + str(int(offset,base=2)) + '('+ basename + ')'
    return Instrdis

#SLL rd,rt,sa 000000 0(5) rt(5) rd(5) sa(5) 000000
def instr1_SLL_dis(rs,rt,rd,shiftAmts,functionCodes):
    sa = str(int(shiftAmts,base=2))
    rdname = Regname(rd)
    rtname = Regname(rt)
    InstrDis = rdname + ', ' + rtname + ', ' + '#' + sa
    return InstrDis
#SRL
def instr1_SRL_dis(rs,rt,rd,shiftAmts,functionCodes):
    sa = str(int(shiftAmts,base=2))
    rdname = Regname(rd)
    rtname = Regname(rt)
    InstrDis = rdname + ', ' + rtname + ', ' + '#' + sa
    return InstrDis
#SRA
def instr1_SRA_dis(rs,rt,rd,shiftAmts,functionCodes):
    sa = str(int(shiftAmts,base=2))
    rdname = Regname(rd)
    rtname = Regname(rt)
    InstrDis = rdname + ', ' + rtname + ', ' + '#' + sa
    return InstrDis
#NOP
def instr1_NOP_dis(rs,rt,rd,shiftAmts,functionCodes):
    return ""

# rd<-rs * rt
def instr1_MUL_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    rdname = Regname(rd)
    InstrDis = rdname + ', ' + rsname + ', ' + rtname
    return InstrDis

#MUL rs*immediate
def instr2_MUL_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    immediate = rd + shiftAmts +functionCodes
    InstrDis = rtname + ', ' + rsname + ', '+'#' + str(int(immediate, base=2))
    return InstrDis

def instr1_AND_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    rdname = Regname(rd)
    InstrDis = rdname + ', ' + rsname + ', ' + rtname
    return InstrDis

#AND rt rs immediate rt<- rs + immediate
def instr2_AND_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    immediate = rd + shiftAmts + functionCodes
    InstrDis = rtname + ', ' + rsname + ', '+'#' + str(int(immediate, base=2))
    return InstrDis

def instr1_NOR_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    rdname = Regname(rd)
    InstrDis = rdname + ', ' + rsname + ', ' + rtname
    return InstrDis

#NOR
def instr2_NOR_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    immediate = rd + shiftAmts + functionCodes
    InstrDis = rtname + ', ' + rsname + ', '+'#' + str(int(immediate, base=2))
    return InstrDis

def instr1_SLT_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    rdname = Regname(rd)
    InstrDis = rdname + ', ' + rsname + ', '+ rtname
    return InstrDis

#SLT
def instr2_SLT_dis(rs,rt,rd,shiftAmts,functionCodes):
    rsname = Regname(rs)
    rtname = Regname(rt)
    immediate = rd + shiftAmts + functionCodes
    InstrDis = rtname + ', ' + rsname + ', '+'#' + str(int(immediate, base=2))
    return InstrDis

def check_category(category):
    flag = 0
    if(category=='0'):
        flag = 0 #代表category1
    else:
        flag = 1 #代表category2
    return int(flag)

# mapsim = {
#     'J': instr1_J_dis,
#     'JR':instr1_JR_dis,
#     'BEQ':instr1_BEQ_dis,
#     'BLTZ':instr1_BLTZ_dis,
#     'BGTZ': instr1_BGTZ_dis,
#     'ADD':{instr1_ADD_dis,instr2_ADD_dis},
#     'SUB':{instr1_SUB_dis,instr2_SUB_dis},
#     'BREAK':instr1_BREAK_dis,
#     'SW':instr1_SW_dis,
#     'LW':instr1_LW_dis,
#     'SLL':instr1_SLL_dis,
#     'SRL':instr1_SRL_dis,
#     'SRA':instr1_SLL_dis,
#     'NOP':instr1_NOP_dis,
#     'MUL':instr2_MUL_dis,
#     'AND':instr2_AND_dis,
#     'NOR':instr2_NOR_dis,
#     'SLT':instr2_SLT_dis,
# }

##字符与操作符一一对应
def judgeinstrutionName1(category,opcode,rs,rt,rd,shiftAmts,functionCodes):
    if category + opcode == '000010':
        return str('J' + '\t' + str(instr1_J_dis(rs,rt,rd,shiftAmts,functionCodes)) + '\n')
    elif category + opcode == '000100':
        return str('BEQ' + '\t' + str(instr1_BEQ_dis(rs,rt,rd,shiftAmts,functionCodes)) + '\n')
    elif category + opcode == '000001':
        return str('BLTZ' + '\t' + str(instr1_BLTZ_dis(rs,rt,rd,shiftAmts,functionCodes)) + '\n')
    elif category + opcode == '000111':
        return str('BGTZ' + '\t' + str(instr1_BGTZ_dis(rs,rt,rd,shiftAmts,functionCodes)) + '\n')
    elif category + opcode == '101011':
        return str('SW' + '\t' + str(instr1_SW_dis(rs,rt,rd,shiftAmts,functionCodes)) + '\n')
    elif category + opcode == '100011':
        return str('LW' + '\t' + str(instr1_LW_dis(rs,rt,rd,shiftAmts,functionCodes)) + '\n')
    elif category + opcode == '011100' and functionCodes == '000010':
        return str('MUL' + '\t' + str(instr1_MUL_dis(rs,rt,rd,shiftAmts,functionCodes)) + '\n')
    #判断sp
    elif category + opcode == '000000' :
        if functionCodes == '001000':
            return str('JR' + '\t' +str(instr1_JR_dis(rs,rt,rd,shiftAmts,functionCodes))+'\n')
        elif functionCodes == '100000':
            return str('ADD' + '\t' + str(instr1_ADD_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '100010':
            return str('SUB' + '\t' + str(instr1_SUB_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '001101':
            return str('BREAK' + '\t' + str(instr1_BREAK_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '000000' and rs == '00000' and rt != '00000' and rd != '00000' and shiftAmts !='00000':
            return str('SLL' + '\t' + str(instr1_SLL_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '000010':
            return str('SRL' + '\t' + str(instr1_SRL_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '000011':
            return str('SRA' + '\t' + str(instr1_SRA_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '000000' and rs == '00000' and rt == '00000' and rd == '00000' and shiftAmts =='00000':
            return str('NOP' + '\t' + str(instr1_NOP_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '100100':
            return str('AND' + '\t' + str(instr1_AND_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '100111':
            return str('NOR' + '\t' + str(instr1_NOR_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        elif functionCodes == '101010':
            return str('SLT' + '\t' + str(instr1_SLT_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
    elif category == '1':
        if opcode == '10000':
            return str('ADD' + '\t' + str(instr2_ADD_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        if opcode == '10001':
            return str('SUB' + '\t' + str(instr2_SUB_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        if opcode == '00001':
            return str('MUL' + '\t' + str(instr2_MUL_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        if opcode == '10010':
            return str('AND' + '\t' + str(instr2_AND_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        if opcode == '10011':
            return str('NOR' + '\t' + str(instr2_NOR_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')
        if opcode == '10101':
            return str('SLT' + '\t' + str(instr2_SLT_dis(rs, rt, rd, shiftAmts, functionCodes)) + '\n')


def Instructiondiassembly(Instruction,startAddress,category,opcode,rs,rt,rd,shiftAmts,functionCodes
                     ,i,outputdis):
    instructioncode =category + opcode + ' ' + rs + ' ' + rt + ' ' + rd +' ' + shiftAmts +' '+functionCodes + ' '
    instructioninfo = judgeinstrutionName1(category,opcode,rs,rt,rd,shiftAmts,functionCodes)

    if category + opcode != '000000' or functionCodes != '001101':
        outputdis.write(str(instructioncode) + '\t' + str(startAddress[0]) + '\t' + str(instructioninfo))
    elif category + opcode == '000000' and functionCodes == '001101':
        outputdis.write(str(instructioncode) + '\t' + str(startAddress[0]) + '\t' +'BREAK' + '\n')
        return True

# def Datadiassembly(Instruction,category,startAddress,memory,outputdis):













